$cursorDir = $PSScriptRoot

# Registry path for current user cursors
$regPath = "HKCU:\Control Panel\Cursors"

# Ensure Schemes registry key exists
if (!(Test-Path "HKCU:\Control Panel\Cursors\Schemes")) {
    New-Item -Path "HKCU:\Control Panel\Cursors\Schemes" -Force | Out-Null
}

Set-ItemProperty -Path $regPath -Name "Arrow" -Value "$cursorDir\Normal.cur"
Set-ItemProperty -Path $regPath -Name "Help" -Value "$cursorDir\Help.cur"
Set-ItemProperty -Path $regPath -Name "AppStarting" -Value "$cursorDir\AppStarting_32-48-64.ani"
Set-ItemProperty -Path $regPath -Name "Wait" -Value "$cursorDir\Wait_32-48-64.ani"
Set-ItemProperty -Path $regPath -Name "Crosshair" -Value "$cursorDir\Precision.cur"
Set-ItemProperty -Path $regPath -Name "IBeam" -Value "$cursorDir\Text.cur"
Set-ItemProperty -Path $regPath -Name "NWPen" -Value "$cursorDir\pencil.cur"
Set-ItemProperty -Path $regPath -Name "No" -Value "$cursorDir\NotAllowed.cur"
Set-ItemProperty -Path $regPath -Name "SizeNS" -Value "$cursorDir\NSResize.cur"
Set-ItemProperty -Path $regPath -Name "SizeWE" -Value "$cursorDir\EWResize.cur"
Set-ItemProperty -Path $regPath -Name "SizeNESW" -Value "$cursorDir\NEResize.cur"
Set-ItemProperty -Path $regPath -Name "SizeNWSE" -Value "$cursorDir\NWResize.cur"
Set-ItemProperty -Path $regPath -Name "SizeAll" -Value "$cursorDir\Move.cur"
Set-ItemProperty -Path $regPath -Name "UpArrow" -Value "$cursorDir\Alternate.cur"
Set-ItemProperty -Path $regPath -Name "Hand" -Value "$cursorDir\Link.cur"

# Register the Scheme in Windows
$schemeName = "Future Cursor (Purple Neon)"
$schemeValue = "$cursorDir\Normal.cur,$cursorDir\Help.cur,$cursorDir\AppStarting_32-48-64.ani,$cursorDir\Wait_32-48-64.ani,$cursorDir\Precision.cur,$cursorDir\Text.cur,$cursorDir\pencil.cur,$cursorDir\NotAllowed.cur,$cursorDir\NSResize.cur,$cursorDir\EWResize.cur,$cursorDir\NWResize.cur,$cursorDir\NEResize.cur,$cursorDir\Move.cur,$cursorDir\Alternate.cur,$cursorDir\Link.cur"
Set-ItemProperty -Path "HKCU:\Control Panel\Cursors\Schemes" -Name $schemeName -Value $schemeValue
Set-ItemProperty -Path $regPath -Name "(Default)" -Value $schemeName

# Call user32.dll SystemParametersInfo to live refresh the cursor
$code = @"
using System.Runtime.InteropServices;
public class CursorUpdater {
    [DllImport("user32.dll", EntryPoint = "SystemParametersInfo")]
    public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, string pvParam, uint fWinIni);

    public static void Update() {
        // SPI_SETCURSORS = 0x0057, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE = 3
        SystemParametersInfo(0x0057, 0, null, 3);
    }
}
"@

Add-Type -TypeDefinition $code
[CursorUpdater]::Update()
Write-Host "Future Cursor (Purple Neon) applied successfully!"

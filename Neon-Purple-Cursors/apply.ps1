$cursorDir = $PSScriptRoot

# Registry path
$regPath = "HKCU:\Control Panel\Cursors"

# Set registry values to point directly to the workspace cursors
Set-ItemProperty -Path $regPath -Name "Arrow" -Value "$cursorDir\arrow.cur"
Set-ItemProperty -Path $regPath -Name "Hand" -Value "$cursorDir\hand.cur"
Set-ItemProperty -Path $regPath -Name "IBeam" -Value "$cursorDir\text.cur"
Set-ItemProperty -Path $regPath -Name "Crosshair" -Value "$cursorDir\crosshair.cur"
Set-ItemProperty -Path $regPath -Name "SizeAll" -Value "$cursorDir\move.cur"
Set-ItemProperty -Path $regPath -Name "No" -Value "$cursorDir\not-allowed.cur"
Set-ItemProperty -Path $regPath -Name "SizeWE" -Value "$cursorDir\resize-ew.cur"
Set-ItemProperty -Path $regPath -Name "SizeNS" -Value "$cursorDir\resize-ns.cur"
Set-ItemProperty -Path $regPath -Name "SizeNWSE" -Value "$cursorDir\resize-nwse.cur"
Set-ItemProperty -Path $regPath -Name "SizeNESW" -Value "$cursorDir\resize-nesw.cur"

# C# snippet to call the Windows API to immediately refresh the cursors
$code = @"
using System.Runtime.InteropServices;
public class CursorUpdater {
    [DllImport("user32.dll", EntryPoint = "SystemParametersInfo")]
    public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, string pvParam, uint fWinIni);

    public static void Update() {
        // SPI_SETCURSORS = 0x0057
        SystemParametersInfo(0x0057, 0, null, 0);
    }
}
"@

Add-Type -TypeDefinition $code
[CursorUpdater]::Update()

# MONO Cursor Pack - Revert to Windows Default Scheme

$ErrorActionPreference = "Stop"

Write-Host "Reverting cursors to Windows Default..." -ForegroundColor Cyan

$regPath = "HKCU:\Control Panel\Cursors"
Set-ItemProperty -Path $regPath -Name "(Default)" -Value "Windows Default"
Set-ItemProperty -Path $regPath -Name "Scheme Source" -Value 0 -Type DWord

$keys = @(
    "Arrow", "Help", "AppStarting", "Wait", "Crosshair", "IBeam", "NWPen", "No",
    "SizeNS", "SizeWE", "SizeNWSE", "SizeNESW", "SizeAll", "UpArrow", "Hand", "Pin", "Person"
)

foreach ($k in $keys) {
    Set-ItemProperty -Path $regPath -Name $k -Value ""
}

$cSharpCode = @"
using System;
using System.Runtime.InteropServices;

public class Win32CursorRestore {
    [DllImport("user32.dll", EntryPoint = "SystemParametersInfoW", SetLastError = true)]
    public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, IntPtr pvParam, uint fWinIni);

    public static bool RefreshCursors() {
        const uint SPI_SETCURSORS = 0x0057;
        const uint SPIF_UPDATEINIFILE = 0x01;
        const uint SPIF_SENDCHANGE = 0x02;
        return SystemParametersInfo(SPI_SETCURSORS, 0, IntPtr.Zero, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE);
    }
}
"@

try {
    Add-Type -TypeDefinition $cSharpCode -ErrorAction SilentlyContinue | Out-Null
} catch {}

[Win32CursorRestore]::RefreshCursors() | Out-Null

Write-Host "`nRestored default Windows cursors successfully!" -ForegroundColor Green

# MONO Cursor Pack - One-Click Live Installer for Windows 11
# Applies all 17 custom Mono cursors immediately without restart.

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$distDir = Join-Path $scriptDir "dist"

if (-not (Test-Path $distDir)) {
    Write-Host "Error: Could not find 'dist' folder at $distDir" -ForegroundColor Red
    exit 1
}

$busyFile = if (Test-Path (Join-Path $distDir "mono_busy.ani")) { Join-Path $distDir "mono_busy.ani" } else { Join-Path $distDir "mono_busy.cur" }
$appStartingFile = if (Test-Path (Join-Path $distDir "mono_working_in_background.ani")) { Join-Path $distDir "mono_working_in_background.ani" } else { Join-Path $distDir "mono_working_in_background.cur" }

$cursorMap = @{
    "Arrow"         = Join-Path $distDir "mono_normal_select.cur"
    "Help"          = Join-Path $distDir "mono_help_select.cur"
    "AppStarting"   = $appStartingFile
    "Wait"          = $busyFile
    "Crosshair"     = Join-Path $distDir "mono_precision_select.cur"
    "IBeam"         = Join-Path $distDir "mono_text_select.cur"
    "NWPen"         = Join-Path $distDir "mono_handwriting.cur"
    "No"            = Join-Path $distDir "mono_unavailable.cur"
    "SizeNS"        = Join-Path $distDir "mono_vertical_resize.cur"
    "SizeWE"        = Join-Path $distDir "mono_horizontal_resize.cur"
    "SizeNWSE"      = Join-Path $distDir "mono_diagonal_resize_1.cur"
    "SizeNESW"      = Join-Path $distDir "mono_diagonal_resize_2.cur"
    "SizeAll"       = Join-Path $distDir "mono_move.cur"
    "UpArrow"       = Join-Path $distDir "mono_alternate_select.cur"
    "Hand"          = Join-Path $distDir "mono_link_select.cur"
    "Pin"           = Join-Path $distDir "mono_location_select.cur"
    "Person"        = Join-Path $distDir "mono_person_select.cur"
    "Draft"         = Join-Path $distDir "mono_text_drag.cur"
    "Copy"          = Join-Path $distDir "mono_drag_copy.cur"
    "NoDrop"        = Join-Path $distDir "mono_dnd_no_drop.cur"
    "VerticalText"  = Join-Path $distDir "mono_vertical_text.cur"
}

Write-Host "Applying MONO Cursor Pack..." -ForegroundColor Magenta

# 1. Update Registry Keys
$regPath = "HKCU:\Control Panel\Cursors"
Set-ItemProperty -Path $regPath -Name "(Default)" -Value "Mono"
Set-ItemProperty -Path $regPath -Name "Scheme Source" -Value 1 -Type DWord

foreach ($key in $cursorMap.Keys) {
    $curPath = $cursorMap[$key]
    Set-ItemProperty -Path $regPath -Name $key -Value $curPath
}

# 2. Save Scheme Definition in Registry
$schemesRegPath = "HKCU:\Control Panel\Cursors\Schemes"
if (-not (Test-Path $schemesRegPath)) {
    New-Item -Path $schemesRegPath -Force | Out-Null
}

$orderedKeys = @(
    "Arrow", "Help", "AppStarting", "Wait", "Crosshair", "IBeam", "NWPen", "No",
    "SizeNS", "SizeWE", "SizeNWSE", "SizeNESW", "SizeAll", "UpArrow", "Hand", "Pin", "Person"
)
$schemeValue = ($orderedKeys | ForEach-Object { $cursorMap[$_] }) -join ","
Set-ItemProperty -Path $schemesRegPath -Name "Mono" -Value $schemeValue

# 3. Broadcast Win32 SystemParametersInfo (SPI_SETCURSORS) to refresh desktop cursor instantly
$cSharpCode = @"
using System;
using System.Runtime.InteropServices;

public class Win32Cursor {
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

[Win32Cursor]::RefreshCursors() | Out-Null

Write-Host "`nSUCCESS! MONO cursor pack is now live on your desktop!" -ForegroundColor Green
Write-Host "If you ever want to revert back, run 'restore_default.bat'." -ForegroundColor Gray

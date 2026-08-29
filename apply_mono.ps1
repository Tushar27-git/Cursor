# One-Click Live Installer for MONO Cursor Pack
# Applies all standard + Drag-and-Drop / OLE cursors and instantly refreshes Windows desktop.

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$distDir = Join-Path $scriptDir "dist"

if (-not (Test-Path $distDir)) {
    Write-Error "dist directory not found at $distDir. Please build the pack first."
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
    "Alias"         = Join-Path $distDir "mono_drag_link.cur"
    "NoDrop"        = Join-Path $distDir "mono_dnd_no_drop.cur"
    "VerticalText"  = Join-Path $distDir "mono_vertical_text.cur"
    "dnd-move"      = Join-Path $distDir "mono_text_drag.cur"
    "dnd-copy"      = Join-Path $distDir "mono_drag_copy.cur"
    "dnd-link"      = Join-Path $distDir "mono_drag_link.cur"
    "dnd-none"      = Join-Path $distDir "mono_dnd_no_drop.cur"
    "dnd-no-drop"   = Join-Path $distDir "mono_dnd_no_drop.cur"
}

Write-Host "Applying MONO Cursor Pack with Drag-and-Drop support..." -ForegroundColor Magenta

# Write to HKCU\Control Panel\Cursors
$regPath = "HKCU:\Control Panel\Cursors"
if (-not (Test-Path $regPath)) {
    New-Item -Path $regPath -Force | Out-Null
}

Set-ItemProperty -Path $regPath -Name "(default)" -Value "Mono" -Force
Set-ItemProperty -Path $regPath -Name "Scheme Source" -Value 1 -Type DWord -Force

foreach ($key in $cursorMap.Keys) {
    $curPath = $cursorMap[$key]
    if (Test-Path $curPath) {
        Set-ItemProperty -Path $regPath -Name $key -Value $curPath -Force
    }
}

# Also register under HKCU\Control Panel\Cursors\Schemes
$schemesPath = "HKCU:\Control Panel\Cursors\Schemes"
if (-not (Test-Path $schemesPath)) {
    New-Item -Path $schemesPath -Force | Out-Null
}

$schemeValues = @(
    $cursorMap["Arrow"],
    $cursorMap["Help"],
    $cursorMap["AppStarting"],
    $cursorMap["Wait"],
    $cursorMap["Crosshair"],
    $cursorMap["IBeam"],
    $cursorMap["NWPen"],
    $cursorMap["No"],
    $cursorMap["SizeNS"],
    $cursorMap["SizeWE"],
    $cursorMap["SizeNWSE"],
    $cursorMap["SizeNESW"],
    $cursorMap["SizeAll"],
    $cursorMap["UpArrow"],
    $cursorMap["Hand"],
    $cursorMap["Pin"],
    $cursorMap["Person"]
)
$schemeStr = $schemeValues -join ","
Set-ItemProperty -Path $schemesPath -Name "Mono" -Value $schemeStr -Force

# Instantly broadcast SPI_SETCURSORS (0x0057) to all Windows processes
if (-not ([System.Management.Automation.PSTypeName]'NativeCursorBroadcaster').Type) {
    Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class NativeCursorBroadcaster {
    [DllImport("user32.dll", EntryPoint = "SystemParametersInfoW", SetLastError = true)]
    public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, IntPtr pvParam, uint fWinIni);
}
"@
}

$SPI_SETCURSORS = 0x0057
$SPIF_UPDATEINIFILE = 0x01
$SPIF_SENDCHANGE = 0x02

$result = [NativeCursorBroadcaster]::SystemParametersInfo($SPI_SETCURSORS, 0, [IntPtr]::Zero, ($SPIF_UPDATEINIFILE -bor $SPIF_SENDCHANGE))

Write-Host "`nSUCCESS! MONO cursor pack is now live on your desktop!" -ForegroundColor Green
Write-Host "If you ever want to revert back, run 'restore_default.bat'." -ForegroundColor Yellow

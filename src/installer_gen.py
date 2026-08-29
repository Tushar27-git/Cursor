"""
MONO Cursor Pack - Windows Installer & Setup Script Generator
Generates:
1. install_mono.inf (Right-click -> Install standard Windows INF)
2. apply_mono_scheme.reg (Direct registry import file)
3. apply_mono_live.py (Instant live activation via Win32 API SystemParametersInfo)
4. uninstall_mono.reg (Revert to Windows default scheme)
"""
import os
from build_icons import ICONS

def generate_installers(cur_dir="dist", install_dir="install"):
    os.makedirs(install_dir, exist_ok=True)
    abs_cur_dir = os.path.abspath(cur_dir).replace("/", "\\")
    
    # 1. Generate INF File
    # Order of standard Windows Cursor scheme fields in INF / registry:
    # Arrow, Help, AppStarting, Wait, Crosshair, IBeam, NWPen, No, SizeNS, SizeWE, SizeNWSE, SizeNESW, SizeAll, UpArrow, Hand, Pin, Person
    ordered_keys = [
        "normal_select", "help_select", "working_in_background", "busy",
        "precision_select", "text_select", "handwriting", "unavailable",
        "vertical_resize", "horizontal_resize", "diagonal_resize_1", "diagonal_resize_2",
        "move", "alternate_select", "link_select", "location_select", "person_select"
    ]
    
    inf_lines = [
        "; ========================================================",
        "; MONO - Windows 11 Custom Lilac-White Cursor Pack",
        "; Right-click this file and select 'Install'",
        "; ========================================================",
        "[Version]",
        "signature=\"$CHICAGO$\"",
        "Provider=\"Mono Cursor Team\"",
        "",
        "[DefaultInstall]",
        "CopyFiles = Scheme.CurFiles",
        "AddReg    = Scheme.Reg",
        "",
        "[DestinationDirs]",
        "Scheme.CurFiles = 10, \"%CUR_DIR%\"",
        "",
        "[Scheme.Reg]",
        "HKCU,\"Control Panel\\Cursors\", \"Scheme Source\", 0x00010001, 1",
        "HKCU,\"Control Panel\\Cursors\\Schemes\", \"Mono\", 0x00020000, \"%10%\\%CUR_DIR%\\mono_normal_select.cur,%10%\\%CUR_DIR%\\mono_help_select.cur,%10%\\%CUR_DIR%\\mono_working_in_background.cur,%10%\\%CUR_DIR%\\mono_busy.cur,%10%\\%CUR_DIR%\\mono_precision_select.cur,%10%\\%CUR_DIR%\\mono_text_select.cur,%10%\\%CUR_DIR%\\mono_handwriting.cur,%10%\\%CUR_DIR%\\mono_unavailable.cur,%10%\\%CUR_DIR%\\mono_vertical_resize.cur,%10%\\%CUR_DIR%\\mono_horizontal_resize.cur,%10%\\%CUR_DIR%\\mono_diagonal_resize_1.cur,%10%\\%CUR_DIR%\\mono_diagonal_resize_2.cur,%10%\\%CUR_DIR%\\mono_move.cur,%10%\\%CUR_DIR%\\mono_alternate_select.cur,%10%\\%CUR_DIR%\\mono_link_select.cur,%10%\\%CUR_DIR%\\mono_location_select.cur,%10%\\%CUR_DIR%\\mono_person_select.cur\"",
        "",
        "[Scheme.CurFiles]"
    ]
    
    for k in ordered_keys:
        filename = f"{ICONS[k]['filename']}.cur"
        inf_lines.append(f"{filename}")
        
    inf_lines.extend([
        "",
        "[Strings]",
        "CUR_DIR = \"Cursors\\Mono\"",
        "SCHEME_NAME = \"Mono\""
    ])
    
    inf_path = os.path.join(install_dir, "install_mono.inf")
    with open(inf_path, "w", encoding="utf-8") as f:
        f.write("\n".join(inf_lines))
    print(f"Generated {inf_path}")
    
    # 2. Generate REG Import File (Pointing to local dist directory for instant portable testing)
    reg_lines = [
        "Windows Registry Editor Version 5.00",
        "",
        "; MONO Cursor Pack Registry Scheme Definition",
        "[HKEY_CURRENT_USER\\Control Panel\\Cursors]",
        "\"(Default)\"=\"Mono\"",
        "\"Scheme Source\"=dword:00000001"
    ]
    
    scheme_paths = []
    for k in ordered_keys:
        data = ICONS[k]
        cur_file = os.path.join(abs_cur_dir, f"{data['filename']}.cur").replace("\\", "\\\\")
        reg_lines.append(f"\"{data['key']}\"=\"{cur_file}\"")
        scheme_paths.append(cur_file)
        
    scheme_joined = ",".join(scheme_paths)
    reg_lines.extend([
        "",
        "[HKEY_CURRENT_USER\\Control Panel\\Cursors\\Schemes]",
        f"\"Mono\"=\"{scheme_joined}\""
    ])
    
    reg_path = os.path.join(install_dir, "apply_mono_scheme.reg")
    with open(reg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(reg_lines))
    print(f"Generated {reg_path}")
    
    # 3. Generate Live Activation Python Script (Immediate win32 API update)
    live_py_code = f"""import ctypes
import winreg
import os

def apply_mono_live():
    print("Applying MONO cursor scheme to current user profile...")
    cur_dir = r"{abs_cur_dir}"
    
    mapping = {{
"""
    for k in ordered_keys:
        data = ICONS[k]
        cur_file = os.path.join(abs_cur_dir, f"{data['filename']}.cur").replace("/", "\\")
        live_py_code += f'        "{data["key"]}": r"{cur_file}",\n'
        
    live_py_code += """    }
    
    # Update HKCU\\Control Panel\\Cursors
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\\Cursors", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Mono")
    winreg.SetValueEx(key, "Scheme Source", 0, winreg.REG_DWORD, 1)
    
    for reg_key, path in mapping.items():
        winreg.SetValueEx(key, reg_key, 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)
    
    # Broadcast SPI_SETCURSORS (0x0057) to refresh system cursors instantly without restart
    SPI_SETCURSORS = 0x0057
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02
    
    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETCURSORS,
        0,
        None,
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )
    
    if result:
        print("Success! MONO Cursor scheme is now live on your desktop.")
    else:
        print("Updated registry. You may also select 'Mono' from Windows Mouse Properties.")

if __name__ == "__main__":
    apply_mono_live()
"""
    live_py_path = os.path.join(install_dir, "apply_mono_live.py")
    with open(live_py_path, "w", encoding="utf-8") as f:
        f.write(live_py_code)
    print(f"Generated {live_py_path}")
    
    # 4. Generate Uninstall / Revert Script
    uninst_lines = [
        "Windows Registry Editor Version 5.00",
        "",
        "; Revert Windows Cursors to Windows Default",
        "[HKEY_CURRENT_USER\\Control Panel\\Cursors]",
        "\"(Default)\"=\"Windows Default\"",
        "\"Scheme Source\"=dword:00000000",
        "\"Arrow\"=\"\"",
        "\"Help\"=\"\"",
        "\"AppStarting\"=\"\"",
        "\"Wait\"=\"\"",
        "\"Crosshair\"=\"\"",
        "\"IBeam\"=\"\"",
        "\"NWPen\"=\"\"",
        "\"No\"=\"\"",
        "\"SizeNS\"=\"\"",
        "\"SizeWE\"=\"\"",
        "\"SizeNWSE\"=\"\"",
        "\"SizeNESW\"=\"\"",
        "\"SizeAll\"=\"\"",
        "\"UpArrow\"=\"\"",
        "\"Hand\"=\"\"",
        "\"Pin\"=\"\"",
        "\"Person\"=\"\""
    ]
    uninst_path = os.path.join(install_dir, "revert_to_default.reg")
    with open(uninst_path, "w", encoding="utf-8") as f:
        f.write("\n".join(uninst_lines))
    print(f"Generated {uninst_path}")

if __name__ == "__main__":
    generate_installers()

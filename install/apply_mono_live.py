import ctypes
import winreg
import os

def apply_mono_live():
    print("Applying MONO cursor scheme to current user profile...")
    cur_dir = r"D:\MonoCurseher\dist"
    
    mapping = {
        "Arrow": r"D:\MonoCurseher\dist\mono_normal_select.cur",
        "Help": r"D:\MonoCurseher\dist\mono_help_select.cur",
        "AppStarting": r"D:\MonoCurseher\dist\mono_working_in_background.cur",
        "Wait": r"D:\MonoCurseher\dist\mono_busy.cur",
        "Crosshair": r"D:\MonoCurseher\dist\mono_precision_select.cur",
        "IBeam": r"D:\MonoCurseher\dist\mono_text_select.cur",
        "NWPen": r"D:\MonoCurseher\dist\mono_handwriting.cur",
        "No": r"D:\MonoCurseher\dist\mono_unavailable.cur",
        "SizeNS": r"D:\MonoCurseher\dist\mono_vertical_resize.cur",
        "SizeWE": r"D:\MonoCurseher\dist\mono_horizontal_resize.cur",
        "SizeNWSE": r"D:\MonoCurseher\dist\mono_diagonal_resize_1.cur",
        "SizeNESW": r"D:\MonoCurseher\dist\mono_diagonal_resize_2.cur",
        "SizeAll": r"D:\MonoCurseher\dist\mono_move.cur",
        "UpArrow": r"D:\MonoCurseher\dist\mono_alternate_select.cur",
        "Hand": r"D:\MonoCurseher\dist\mono_link_select.cur",
        "Pin": r"D:\MonoCurseher\dist\mono_location_select.cur",
        "Person": r"D:\MonoCurseher\dist\mono_person_select.cur",
    }
    
    # Update HKCU\Control Panel\Cursors
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_SET_VALUE)
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

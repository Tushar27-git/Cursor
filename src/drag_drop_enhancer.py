"""
MONO Drag & Drop System Enhancer
Proper 64-bit Win32 Low-Level Hook implementation to replace Windows default drag-and-drop cursors system-wide.
"""
import sys
import os
import time
import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

IMAGE_CURSOR = 2
LR_LOADFROMFILE = 0x00000010
LR_DEFAULTSIZE = 0x00000040

user32.LoadImageW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR, wintypes.UINT, ctypes.c_int, ctypes.c_int, wintypes.UINT]
user32.LoadImageW.restype = wintypes.HANDLE

kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
kernel32.GetModuleHandleW.restype = wintypes.HMODULE

# Load custom MONO cursors
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "dist")
TEXT_DRAG_CUR = os.path.join(DIST_DIR, "mono_text_drag.cur")
COPY_DRAG_CUR = os.path.join(DIST_DIR, "mono_drag_copy.cur")
NORMAL_CUR = os.path.join(DIST_DIR, "mono_normal_select.cur")

hTextDrag = user32.LoadImageW(None, TEXT_DRAG_CUR, IMAGE_CURSOR, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE)
hCopyDrag = user32.LoadImageW(None, COPY_DRAG_CUR, IMAGE_CURSOR, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE)
hNormal = user32.LoadImageW(None, NORMAL_CUR, IMAGE_CURSOR, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE)

print(f"Loaded Handles -> TextDrag: {hTextDrag}, CopyDrag: {hCopyDrag}")

WH_MOUSE_LL = 14
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_MOUSEMOVE = 0x0200

is_dragging = False
drag_start_pos = None

class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]

class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("pt", POINT),
        ("mouseData", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_ulonglong)
    ]

HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_int, wintypes.WPARAM, ctypes.POINTER(MSLLHOOKSTRUCT))

user32.SetWindowsHookExW.argtypes = [ctypes.c_int, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD]
user32.SetWindowsHookExW.restype = wintypes.HHOOK

user32.CallNextHookEx.argtypes = [wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, ctypes.POINTER(MSLLHOOKSTRUCT)]
user32.CallNextHookEx.restype = ctypes.c_longlong

user32.UnhookWindowsHookEx.argtypes = [wintypes.HHOOK]
user32.UnhookWindowsHookEx.restype = wintypes.BOOL

user32.SetCursor.argtypes = [wintypes.HANDLE]
user32.SetCursor.restype = wintypes.HANDLE

def hook_callback(nCode, wParam, lParam):
    global is_dragging, drag_start_pos
    if nCode >= 0:
        struct = lParam.contents
        if wParam == WM_LBUTTONDOWN:
            drag_start_pos = (struct.pt.x, struct.pt.y)
            is_dragging = False
        elif wParam == WM_LBUTTONUP:
            is_dragging = False
            drag_start_pos = None
        elif wParam == WM_MOUSEMOVE:
            # Check if left button is currently pressed
            left_down = (user32.GetAsyncKeyState(0x01) & 0x8000) != 0
            if left_down and drag_start_pos:
                dx = abs(struct.pt.x - drag_start_pos[0])
                dy = abs(struct.pt.y - drag_start_pos[1])
                if dx > 5 or dy > 5:
                    is_dragging = True
                    ctrl_down = (user32.GetAsyncKeyState(0x11) & 0x8000) != 0
                    if ctrl_down:
                        user32.SetCursor(hCopyDrag)
                    else:
                        user32.SetCursor(hTextDrag)

    return user32.CallNextHookEx(None, nCode, wParam, lParam)

callback_func = HOOKPROC(hook_callback)

def run_enhancer():
    hMod = kernel32.GetModuleHandleW(None)
    hook = user32.SetWindowsHookExW(WH_MOUSE_LL, callback_func, hMod, 0)
    if not hook:
        err = kernel32.GetLastError()
        print(f"Failed to install hook. Win32 Error: {err}")
        return
        
    print("SUCCESS: MONO System Drag Enhancer is running! Left-drag in any app to see custom drag cursor.")
    sys.stdout.flush()
    
    msg = wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
        
    user32.UnhookWindowsHookEx(hook)

if __name__ == "__main__":
    run_enhancer()

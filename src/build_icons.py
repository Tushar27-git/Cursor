"""
MONO Cursor Pack - 22 Master SVG Icon Generators
Updated with full Drag & Drop family (Text Drag, Copy Drag, Link Drag, No-Drop, Vertical Text).
"""
import os
from tokens import wrap_svg, OUTLINE_COLOR, ACCENT_COLOR

ICONS = {}

# 1. Normal Select (Arrow)
ICONS["normal_select"] = {
    "key": "Arrow",
    "filename": "mono_normal_select",
    "name": "Normal Select",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <!-- Outer Dark Contrast Stroke + Solid Black Body -->
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <!-- Pale Lilac-White Outline with Solid Black Fill -->
  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <!-- Floating Purple Accent Pill in Heel -->
  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />
"""
}

# 2. Help Select (Help)
ICONS["help_select"] = {
    "key": "Help",
    "filename": "mono_help_select",
    "name": "Help Select",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />
  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />
  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <circle cx="52" cy="50" r="10.5" fill="#000000" />
  <circle class="contrast-stroke-lean" cx="52" cy="50" r="9.2" />
  <circle class="accent-fill" cx="52" cy="50" r="8.8" />
  <path d="M 49.5 46.5 C 49.5 44.4 50.8 43.4 52.2 43.4 C 53.6 43.4 54.7 44.4 54.7 45.7 C 54.7 47 53.6 47.8 52.6 48.6 L 52.6 50.1" 
        stroke="#F5F1FF" stroke-width="2.1" stroke-linecap="round" fill="none" />
  <circle cx="52.6" cy="53.5" r="1.2" fill="#F5F1FF" />
"""
}

# 3. Working in Background (AppStarting)
ICONS["working_in_background"] = {
    "key": "AppStarting",
    "filename": "mono_working_in_background",
    "name": "Working in Background",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />
  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />
  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <circle cx="52" cy="50" r="9.5" fill="#000000" />
  <circle cx="52" cy="50" r="8.4" stroke="#000000" stroke-width="6.2" fill="none" stroke-dasharray="29 15" />
  <circle cx="52" cy="50" r="8.4" stroke="#F5F1FF" stroke-width="3.6" fill="none" stroke-dasharray="29 15" stroke-linecap="round" />
  <circle class="accent-fill" cx="58.2" cy="44.8" r="2.9" />
"""
}

# 4. Busy (Wait)
ICONS["busy"] = {
    "key": "Wait",
    "filename": "mono_busy",
    "name": "Busy",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <circle cx="32" cy="32" r="23" fill="#000000" />
  
  <path class="contrast-stroke-hollow" d="M 32 14.5 A 19.8 19.8 0 0 1 47.8 41.8" />
  <path class="contrast-stroke-hollow" d="M 47.8 41.8 A 19.8 19.8 0 0 1 16.2 41.8" />
  <path class="contrast-stroke-hollow" d="M 16.2 41.8 A 19.8 19.8 0 0 1 32 14.5" />

  <path class="outline-stroke-hollow" d="M 32 14.5 A 19.8 19.8 0 0 1 47.8 41.8" />
  <path class="outline-stroke-hollow" d="M 47.8 41.8 A 19.8 19.8 0 0 1 16.2 41.8" />
  <path class="outline-stroke-hollow" d="M 16.2 41.8 A 19.8 19.8 0 0 1 32 14.5" />

  <circle cx="32" cy="14.5" r="7.2" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="14.5" r="5.4" />

  <circle cx="47.8" cy="41.8" r="7.2" fill="#000000" />
  <circle class="accent-fill" cx="47.8" cy="41.8" r="5.4" />

  <circle cx="16.2" cy="41.8" r="7.2" fill="#000000" />
  <circle class="accent-fill" cx="16.2" cy="41.8" r="5.4" />
"""
}

# 5. Precision Select (Crosshair)
ICONS["precision_select"] = {
    "key": "Crosshair",
    "filename": "mono_precision_select",
    "name": "Precision Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <rect class="contrast-stroke" x="28.8" y="5.5" width="6.4" height="17.5" rx="3.2" />
  <rect class="contrast-stroke" x="28.8" y="41" width="6.4" height="17.5" rx="3.2" />
  <rect class="contrast-stroke" x="5.5" y="28.8" width="17.5" height="6.4" rx="3.2" />
  <rect class="contrast-stroke" x="41" y="28.8" width="17.5" height="6.4" rx="3.2" />

  <rect class="outline-stroke" x="28.8" y="5.5" width="6.4" height="17.5" rx="3.2" />
  <rect class="outline-stroke" x="28.8" y="41" width="6.4" height="17.5" rx="3.2" />
  <rect class="outline-stroke" x="5.5" y="28.8" width="17.5" height="6.4" rx="3.2" />
  <rect class="outline-stroke" x="41" y="28.8" width="17.5" height="6.4" rx="3.2" />

  <circle cx="32" cy="32" r="5.8" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="32" r="4.0" />

  <circle class="accent-fill" cx="32" cy="7" r="2.3" />
  <circle class="accent-fill" cx="32" cy="57" r="2.3" />
  <circle class="accent-fill" cx="7" cy="32" r="2.3" />
  <circle class="accent-fill" cx="57" cy="32" r="2.3" />
"""
}

# 6. Text Select (IBeam)
ICONS["text_select"] = {
    "key": "IBeam",
    "filename": "mono_text_select",
    "name": "Text Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 17 10 L 47 10 C 43 18, 43 46, 47 54 L 17 54 C 21 46, 21 18, 17 10 Z" />
  <path class="outline-stroke" d="M 17 10 L 47 10 C 43 18, 43 46, 47 54 L 17 54 C 21 46, 21 18, 17 10 Z" />
  <rect class="accent-fill" x="29.8" y="16.5" width="4.4" height="31" rx="2.2" />
"""
}

# 7. Handwriting (NWPen)
ICONS["handwriting"] = {
    "key": "NWPen",
    "filename": "mono_handwriting",
    "name": "Handwriting",
    "hotspot": (9 / 64, 55 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 50 13 
           C 54 9, 58 13, 55 17 
           L 24 48 
           L 9 55 
           L 16 40 
           L 47 9 
           C 48 8, 49 8, 50 9 Z" />
  
  <path class="outline-stroke" d="M 50 13 
           C 54 9, 58 13, 55 17 
           L 24 48 
           L 9 55 
           L 16 40 
           L 47 9 
           C 48 8, 49 8, 50 9 Z" />

  <line class="contrast-stroke-lean" x1="19.5" y1="43.5" x2="26.5" y2="50.5" />
  <line class="outline-stroke-lean" x1="19.5" y1="43.5" x2="26.5" y2="50.5" />

  <path class="accent-fill" d="M 9 55 L 16.5 44 L 23.5 51 Z" />
"""
}

# 8. Unavailable (No)
ICONS["unavailable"] = {
    "key": "No",
    "filename": "mono_unavailable",
    "name": "Unavailable",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <circle class="contrast-stroke" cx="32" cy="32" r="22" />
  <circle class="outline-stroke" cx="32" cy="32" r="22" />

  <line class="contrast-stroke-hollow" x1="16.5" y1="16.5" x2="47.5" y2="47.5" />
  <line class="accent-stroke" x1="16.5" y1="16.5" x2="47.5" y2="47.5" />
"""
}

# 9. Vertical Resize (SizeNS)
ICONS["vertical_resize"] = {
    "key": "SizeNS",
    "filename": "mono_vertical_resize",
    "name": "Vertical Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 21 19 L 32 6 L 43 19 L 35 19 L 35 45 L 43 45 L 32 58 L 21 45 L 29 45 L 29 19 Z" />
  <path class="outline-stroke" d="M 21 19 L 32 6 L 43 19 L 35 19 L 35 45 L 43 45 L 32 58 L 21 45 L 29 45 L 29 19 Z" />
"""
}

# 10. Horizontal Resize (SizeWE)
ICONS["horizontal_resize"] = {
    "key": "SizeWE",
    "filename": "mono_horizontal_resize",
    "name": "Horizontal Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 19 21 L 6 32 L 19 43 L 19 35 L 45 35 L 45 43 L 58 32 L 45 21 L 45 29 L 19 29 Z" />
  <path class="outline-stroke" d="M 19 21 L 6 32 L 19 43 L 19 35 L 45 35 L 45 43 L 58 32 L 45 21 L 45 29 L 19 29 Z" />
"""
}

# 11. Diagonal Resize 1 (SizeNWSE)
ICONS["diagonal_resize_1"] = {
    "key": "SizeNWSE",
    "filename": "mono_diagonal_resize_1",
    "name": "Diagonal Resize 1 (NWSE)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 13 25 L 13 13 L 25 13 L 20 18 L 46 44 L 51 39 L 51 51 L 39 51 L 44 46 L 18 20 Z" />
  <path class="outline-stroke" d="M 13 25 L 13 13 L 25 13 L 20 18 L 46 44 L 51 39 L 51 51 L 39 51 L 44 46 L 18 20 Z" />
"""
}

# 12. Diagonal Resize 2 (SizeNESW)
ICONS["diagonal_resize_2"] = {
    "key": "SizeNESW",
    "filename": "mono_diagonal_resize_2",
    "name": "Diagonal Resize 2 (NESW)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 39 13 L 51 13 L 51 25 L 46 20 L 20 46 L 25 51 L 13 51 L 13 39 L 18 44 L 44 18 Z" />
  <path class="outline-stroke" d="M 39 13 L 51 13 L 51 25 L 46 20 L 20 46 L 25 51 L 13 51 L 13 39 L 18 44 L 44 18 Z" />
"""
}

# 13. Move (SizeAll)
ICONS["move"] = {
    "key": "SizeAll",
    "filename": "mono_move",
    "name": "Move",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 24 16 L 32 7 L 40 16 L 35 16 L 35 29 L 48 29 L 48 24 L 57 32 L 48 40 L 48 35 L 35 35 L 35 48 L 40 48 L 32 57 L 24 48 L 29 48 L 29 35 L 16 35 L 16 40 L 7 32 L 16 24 L 16 29 L 29 29 L 29 16 Z" />
  <path class="outline-stroke" d="M 24 16 L 32 7 L 40 16 L 35 16 L 35 29 L 48 29 L 48 24 L 57 32 L 48 40 L 48 35 L 35 35 L 35 48 L 40 48 L 32 57 L 24 48 L 29 48 L 29 35 L 16 35 L 16 40 L 7 32 L 16 24 L 16 29 L 29 29 L 29 16 Z" />
  <polygon class="accent-fill" points="32,26.5 37.5,32 32,37.5 26.5,32" />
"""
}

# 14. Alternate Select (UpArrow)
ICONS["alternate_select"] = {
    "key": "UpArrow",
    "filename": "mono_alternate_select",
    "name": "Alternate Select",
    "hotspot": (32 / 64, 6 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 21 20 L 32 6 L 43 20 L 35 20 L 35 57 L 29 57 L 29 20 Z" />
  <path class="outline-stroke" d="M 21 20 L 32 6 L 43 20 L 35 20 L 35 57 L 29 57 L 29 20 Z" />
"""
}

# 15. Link Select (Hand)
ICONS["link_select"] = {
    "key": "Hand",
    "filename": "mono_link_select",
    "name": "Link Select",
    "hotspot": (18 / 64, 18 / 64),
    "svg": """
  <!-- Two Interlocking Rounded Chain Links (+7.5% Scale Enhancement) -->
  <rect class="contrast-stroke" x="9" y="10.5" width="29" height="16" rx="8" ry="8" transform="rotate(-45 23.5 18.5)" />
  <rect class="contrast-stroke" x="26" y="27.5" width="29" height="16" rx="8" ry="8" transform="rotate(-45 40.5 35.5)" />

  <rect class="outline-stroke" x="9" y="10.5" width="29" height="16" rx="8" ry="8" transform="rotate(-45 23.5 18.5)" />
  <rect class="outline-stroke" x="26" y="27.5" width="29" height="16" rx="8" ry="8" transform="rotate(-45 40.5 35.5)" />

  <circle cx="32" cy="32" r="6.2" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="32" r="4.6" />
"""
}

# 16. Location Select (Pin)
ICONS["location_select"] = {
    "key": "Pin",
    "filename": "mono_location_select",
    "name": "Location Select",
    "hotspot": (32 / 64, 59 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 32 59 
           C 17.5 43.5, 12.5 34.5, 12.5 24 
           C 12.5 13, 21.2 4.5, 32 4.5 
           C 42.8 4.5, 51.5 13, 51.5 24 
           C 51.5 34.5, 46.5 43.5, 32 59 Z" />

  <path class="outline-stroke" d="M 32 59 
           C 17.5 43.5, 12.5 34.5, 12.5 24 
           C 12.5 13, 21.2 4.5, 32 4.5 
           C 42.8 4.5, 51.5 13, 51.5 24 
           C 51.5 34.5, 46.5 43.5, 32 59 Z" />

  <circle class="accent-fill" cx="32" cy="24" r="6.0" />
"""
}

# 17. Person Select (Person)
ICONS["person_select"] = {
    "key": "Person",
    "filename": "mono_person_select",
    "name": "Person Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <circle class="contrast-stroke" cx="32" cy="15.5" r="9.5" />
  <circle class="outline-stroke" cx="32" cy="15.5" r="9.5" />

  <path class="contrast-stroke" d="M 11 54 C 11 41.5, 19.5 37.5, 32 37.5 C 44.5 37.5, 53 41.5, 53 54 Z" />
  <path class="outline-stroke" d="M 11 54 C 11 41.5, 19.5 37.5, 32 37.5 C 44.5 37.5, 53 41.5, 53 54 Z" />

  <rect class="accent-fill" x="28.8" y="36.5" width="6.4" height="2.6" rx="1.3" />
"""
}

# 18. Text Drag & Move (Draft / DragMove / DragText)
ICONS["text_drag"] = {
    "key": "Draft",
    "filename": "mono_text_drag",
    "name": "Text Drag",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <!-- Pointer -->
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <!-- Modern Text Snippet Document Sheet -->
  <rect class="contrast-stroke-lean" x="34" y="30" width="24" height="28" rx="4.5" ry="4.5" />
  <rect class="outline-stroke-lean" x="34" y="30" width="24" height="28" rx="4.5" ry="4.5" />

  <!-- 3 Purple Accent Lines -->
  <rect class="accent-fill" x="39" y="37" width="14" height="2.8" rx="1.4" />
  <rect class="accent-fill" x="39" y="44" width="14" height="2.8" rx="1.4" />
  <rect class="accent-fill" x="39" y="51" width="9" height="2.8" rx="1.4" />
"""
}

# 19. Copy Drag (Copy / DragCopy)
ICONS["drag_copy"] = {
    "key": "Copy",
    "filename": "mono_drag_copy",
    "name": "Copy Drag",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <circle cx="50" cy="48" r="10.5" fill="#000000" />
  <circle class="contrast-stroke-lean" cx="50" cy="48" r="9.2" />
  <circle class="accent-fill" cx="50" cy="48" r="8.8" />
  
  <line x1="50" y1="43" x2="50" y2="53" stroke="#F5F1FF" stroke-width="2.6" stroke-linecap="round" />
  <line x1="45" y1="48" x2="55" y2="48" stroke="#F5F1FF" stroke-width="2.6" stroke-linecap="round" />
"""
}

# 20. Link / Alias Drag (Alias / DragLink)
ICONS["drag_link"] = {
    "key": "Alias",
    "filename": "mono_drag_link",
    "name": "Link Drag",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <!-- Mini Curved Shortcut Link Arrow -->
  <circle cx="50" cy="48" r="10.5" fill="#000000" />
  <circle class="contrast-stroke-lean" cx="50" cy="48" r="9.2" />
  <circle class="accent-fill" cx="50" cy="48" r="8.8" />
  
  <path d="M 46 51 C 46 47, 49 44, 53 44" stroke="#F5F1FF" stroke-width="2.2" fill="none" stroke-linecap="round" />
  <path d="M 50 42 L 54 44 L 52 48" stroke="#F5F1FF" stroke-width="2.0" fill="none" stroke-linecap="round" stroke-linejoin="round" />
"""
}

# 21. No Drop (DndNoDrop)
ICONS["dnd_no_drop"] = {
    "key": "NoDrop",
    "filename": "mono_dnd_no_drop",
    "name": "No Drop",
    "hotspot": (10 / 64, 5 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <circle cx="50" cy="48" r="10.5" fill="#000000" />
  <circle class="contrast-stroke-lean" cx="50" cy="48" r="9.2" />
  <circle class="outline-stroke-lean" cx="50" cy="48" r="9.2" />
  <line x1="44" y1="42" x2="56" y2="54" stroke="#B18CFF" stroke-width="2.6" stroke-linecap="round" />
"""
}

# 22. Vertical Text Select
ICONS["vertical_text"] = {
    "key": "VerticalText",
    "filename": "mono_vertical_text",
    "name": "Vertical Text",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <path class="contrast-stroke" d="M 10 17 L 10 47 C 18 43, 46 43, 54 47 L 54 17 C 46 21, 18 21, 10 17 Z" />
  <path class="outline-stroke" d="M 10 17 L 10 47 C 18 43, 46 43, 54 47 L 54 17 C 46 21, 18 21, 10 17 Z" />
  <rect class="accent-fill" x="16.5" y="29.8" width="31" height="4.4" rx="2.2" />
"""
}

def build_all_svgs(output_dir="svg"):
    os.makedirs(output_dir, exist_ok=True)
    generated = []
    for icon_id, data in ICONS.items():
        full_svg = wrap_svg(data["svg"])
        filepath = os.path.join(output_dir, f"{data['filename']}.svg")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_svg)
        generated.append((icon_id, filepath))
    return generated

if __name__ == "__main__":
    build_all_svgs()

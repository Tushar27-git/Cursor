"""
MONO Cursor Pack - 17 Master SVG Icon Generators
Features:
- Solid black (#000000) opaque interior fill (non pass-through)
- +15% scaled up geometry for bold desktop presence
- Pale-lilac (#F5F1FF) outline + saturated lilac (#B18CFF) accent points
- Dark outer contrast halo for light background visibility
"""
import os
from tokens import wrap_svg, OUTLINE_COLOR, ACCENT_COLOR

ICONS = {}

# 1. Normal Select (Arrow)
ICONS["normal_select"] = {
    "key": "Arrow",
    "filename": "mono_normal_select",
    "name": "Normal Select",
    "hotspot": (11 / 64, 6 / 64),
    "svg": """
  <!-- Outer Dark Contrast Stroke + Solid Black Body -->
  <path class="contrast-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Pale Lilac-White Outline with Solid Black Fill -->
  <path class="outline-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Floating Purple Accent Pill in Heel -->
  <rect class="accent-fill" x="13.8" y="39" width="4.4" height="10.5" rx="2.2" />
"""
}

# 2. Help Select (Help)
ICONS["help_select"] = {
    "key": "Help",
    "filename": "mono_help_select",
    "name": "Help Select",
    "hotspot": (11 / 64, 6 / 64),
    "svg": """
  <!-- Base Pointer Contrast + Solid Black -->
  <path class="contrast-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Base Pointer Outline -->
  <path class="outline-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Purple Pill in Heel -->
  <rect class="accent-fill" x="13.8" y="39" width="4.4" height="10.5" rx="2.2" />

  <!-- Help Circle Badge at Lower Right (Solid Mask + Lilac Circle) -->
  <circle cx="51" cy="49" r="10" fill="#000000" />
  <circle class="contrast-stroke-lean" cx="51" cy="49" r="8.8" />
  <circle class="accent-fill" cx="51" cy="49" r="8.5" />
  
  <!-- Question Mark Inside Badge -->
  <path d="M 48.6 45.8 C 48.6 43.8 49.9 42.8 51.2 42.8 C 52.6 42.8 53.6 43.8 53.6 45 C 53.6 46.2 52.6 47 51.6 47.8 L 51.6 49.2" 
        stroke="#F5F1FF" stroke-width="2" stroke-linecap="round" fill="none" />
  <circle cx="51.6" cy="52.6" r="1.2" fill="#F5F1FF" />
"""
}

# 3. Working in Background (AppStarting)
ICONS["working_in_background"] = {
    "key": "AppStarting",
    "filename": "mono_working_in_background",
    "name": "Working in Background",
    "hotspot": (11 / 64, 6 / 64),
    "svg": """
  <!-- Base Pointer Contrast + Solid Black -->
  <path class="contrast-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Base Pointer Outline -->
  <path class="outline-stroke" d="M 11 6
           C 24 17, 43 28, 50 49
           C 51.2 52.5, 47 55.5, 43.5 52
           C 34.5 43.5, 27 36, 22.5 37.8
           C 17 39.5, 14.5 49, 13.5 53
           C 12 56.5, 10.5 55.5, 10.5 51
           Z" />

  <!-- Purple Pill in Heel -->
  <rect class="accent-fill" x="13.8" y="39" width="4.4" height="10.5" rx="2.2" />

  <!-- Spinner Ring at Lower Right -->
  <circle cx="51" cy="49" r="9" fill="#000000" />
  <circle cx="51" cy="49" r="8" stroke="#000000" stroke-width="6" fill="none" stroke-dasharray="28 14" />
  <circle cx="51" cy="49" r="8" stroke="#F5F1FF" stroke-width="3.5" fill="none" stroke-dasharray="28 14" stroke-linecap="round" />
  <!-- Purple Accent Dot -->
  <circle class="accent-fill" cx="57" cy="44" r="2.8" />
"""
}

# 4. Busy (Wait)
ICONS["busy"] = {
    "key": "Wait",
    "filename": "mono_busy",
    "name": "Busy",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Tri-Arc Spinner connecting 3 purple dots with solid black backdrop -->
  <circle cx="32" cy="32" r="22" fill="#000000" />
  
  <!-- Dark Contrast Arcs -->
  <path class="contrast-stroke-hollow" d="M 32 15 A 19 19 0 0 1 47 41" />
  <path class="contrast-stroke-hollow" d="M 47 41 A 19 19 0 0 1 17 41" />
  <path class="contrast-stroke-hollow" d="M 17 41 A 19 19 0 0 1 32 15" />

  <!-- Pale Lilac Outline Arcs -->
  <path class="outline-stroke-hollow" d="M 32 15 A 19 19 0 0 1 47 41" />
  <path class="outline-stroke-hollow" d="M 47 41 A 19 19 0 0 1 17 41" />
  <path class="outline-stroke-hollow" d="M 17 41 A 19 19 0 0 1 32 15" />

  <!-- 3 Purple Accent Dots -->
  <circle cx="32" cy="15" r="7" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="15" r="5.2" />

  <circle cx="47" cy="41" r="7" fill="#000000" />
  <circle class="accent-fill" cx="47" cy="41" r="5.2" />

  <circle cx="17" cy="41" r="7" fill="#000000" />
  <circle class="accent-fill" cx="17" cy="41" r="5.2" />
"""
}

# 5. Precision Select (Crosshair)
ICONS["precision_select"] = {
    "key": "Crosshair",
    "filename": "mono_precision_select",
    "name": "Precision Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- 4 Segmented Crosshair Arms with Solid Black Body -->
  <!-- Top Arm -->
  <rect class="contrast-stroke" x="29" y="6" width="6" height="17" rx="3" />
  <!-- Bottom Arm -->
  <rect class="contrast-stroke" x="29" y="41" width="6" height="17" rx="3" />
  <!-- Left Arm -->
  <rect class="contrast-stroke" x="6" y="29" width="17" height="6" rx="3" />
  <!-- Right Arm -->
  <rect class="contrast-stroke" x="41" y="29" width="17" height="6" rx="3" />

  <!-- Pale Lilac Outlines -->
  <rect class="outline-stroke" x="29" y="6" width="6" height="17" rx="3" />
  <rect class="outline-stroke" x="29" y="41" width="6" height="17" rx="3" />
  <rect class="outline-stroke" x="6" y="29" width="17" height="6" rx="3" />
  <rect class="outline-stroke" x="41" y="29" width="17" height="6" rx="3" />

  <!-- Center Purple Dot with Black Collar -->
  <circle cx="32" cy="32" r="5.5" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="32" r="3.8" />

  <!-- Purple Accent Dots on 4 Outer Tips -->
  <circle class="accent-fill" cx="32" cy="7.5" r="2.2" />
  <circle class="accent-fill" cx="32" cy="56.5" r="2.2" />
  <circle class="accent-fill" cx="7.5" cy="32" r="2.2" />
  <circle class="accent-fill" cx="56.5" cy="32" r="2.2" />
"""
}

# 6. Text Select (IBeam)
ICONS["text_select"] = {
    "key": "IBeam",
    "filename": "mono_text_select",
    "name": "Text Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Bold Solid Black I-Beam with Lilac Outline & Purple Vertical Core -->
  <path class="contrast-stroke" d="M 18 11 L 46 11 C 42 19, 42 45, 46 53 L 18 53 C 22 45, 22 19, 18 11 Z" />
  <path class="outline-stroke" d="M 18 11 L 46 11 C 42 19, 42 45, 46 53 L 18 53 C 22 45, 22 19, 18 11 Z" />

  <!-- Center Purple Accent Bar -->
  <rect class="accent-fill" x="30" y="17" width="4" height="30" rx="2" />
"""
}

# 7. Handwriting (NWPen)
ICONS["handwriting"] = {
    "key": "NWPen",
    "filename": "mono_handwriting",
    "name": "Handwriting",
    "hotspot": (10 / 64, 54 / 64),
    "svg": """
  <!-- Diagonal Pencil Outline with Solid Black Fill pointing to (10, 54) -->
  <path class="contrast-stroke" d="M 49 14 
           C 53 10, 57 14, 54 18 
           L 24 48 
           L 10 54 
           L 16 40 
           L 46 10 
           C 47 9, 48 9, 49 10 Z" />
  
  <path class="outline-stroke" d="M 49 14 
           C 53 10, 57 14, 54 18 
           L 24 48 
           L 10 54 
           L 16 40 
           L 46 10 
           C 47 9, 48 9, 49 10 Z" />

  <!-- Pencil Collar Line -->
  <line class="contrast-stroke-lean" x1="20" y1="44" x2="26" y2="50" />
  <line class="outline-stroke-lean" x1="20" y1="44" x2="26" y2="50" />

  <!-- Purple Filled Tip Lead -->
  <path class="accent-fill" d="M 10 54 L 17 44 L 23 50 Z" />
"""
}

# 8. Unavailable (No)
ICONS["unavailable"] = {
    "key": "No",
    "filename": "mono_unavailable",
    "name": "Unavailable",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black Circle with Pale Lilac Ring & Purple Slash -->
  <circle class="contrast-stroke" cx="32" cy="32" r="21" />
  <circle class="outline-stroke" cx="32" cy="32" r="21" />

  <!-- Purple Diagonal Accent Slash -->
  <line class="contrast-stroke-hollow" x1="17" y1="17" x2="47" y2="47" />
  <line class="accent-stroke" x1="17" y1="17" x2="47" y2="47" />
"""
}

# 9. Vertical Resize (SizeNS)
ICONS["vertical_resize"] = {
    "key": "SizeNS",
    "filename": "mono_vertical_resize",
    "name": "Vertical Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black Double-Headed Vertical Arrow -->
  <path class="contrast-stroke" d="M 21 19 L 32 7 L 43 19 L 35 19 L 35 45 L 43 45 L 32 57 L 21 45 L 29 45 L 29 19 Z" />
  <path class="outline-stroke" d="M 21 19 L 32 7 L 43 19 L 35 19 L 35 45 L 43 45 L 32 57 L 21 45 L 29 45 L 29 19 Z" />
"""
}

# 10. Horizontal Resize (SizeWE)
ICONS["horizontal_resize"] = {
    "key": "SizeWE",
    "filename": "mono_horizontal_resize",
    "name": "Horizontal Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black Double-Headed Horizontal Arrow -->
  <path class="contrast-stroke" d="M 19 21 L 7 32 L 19 43 L 19 35 L 45 35 L 45 43 L 57 32 L 45 21 L 45 29 L 19 29 Z" />
  <path class="outline-stroke" d="M 19 21 L 7 32 L 19 43 L 19 35 L 45 35 L 45 43 L 57 32 L 45 21 L 45 29 L 19 29 Z" />
"""
}

# 11. Diagonal Resize 1 (SizeNWSE)
ICONS["diagonal_resize_1"] = {
    "key": "SizeNWSE",
    "filename": "mono_diagonal_resize_1",
    "name": "Diagonal Resize 1 (NWSE)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black NW to SE Diagonal Arrow -->
  <path class="contrast-stroke" d="M 9 24 L 9 9 L 24 9 L 18 15 L 49 46 L 55 40 L 55 55 L 40 55 L 46 49 L 15 18 Z" />
  <path class="outline-stroke" d="M 9 24 L 9 9 L 24 9 L 18 15 L 49 46 L 55 40 L 55 55 L 40 55 L 46 49 L 15 18 Z" />
"""
}

# 12. Diagonal Resize 2 (SizeNESW)
ICONS["diagonal_resize_2"] = {
    "key": "SizeNESW",
    "filename": "mono_diagonal_resize_2",
    "name": "Diagonal Resize 2 (NESW)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black NE to SW Diagonal Arrow -->
  <path class="contrast-stroke" d="M 40 9 L 55 9 L 55 24 L 49 18 L 18 49 L 24 55 L 9 55 L 9 40 L 15 46 L 46 15 Z" />
  <path class="outline-stroke" d="M 40 9 L 55 9 L 55 24 L 49 18 L 18 49 L 24 55 L 9 55 L 9 40 L 15 46 L 46 15 Z" />
"""
}

# 13. Move (SizeAll)
ICONS["move"] = {
    "key": "SizeAll",
    "filename": "mono_move",
    "name": "Move",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- 4-Directional Solid Black Arrow with Purple Center Diamond -->
  <path class="contrast-stroke" d="M 24 17 L 32 8 L 40 17 L 35 17 L 35 29 L 47 29 L 47 24 L 56 32 L 47 40 L 47 35 L 35 35 L 35 47 L 40 47 L 32 56 L 24 47 L 29 47 L 29 35 L 17 35 L 17 40 L 8 32 L 17 24 L 17 29 L 29 29 L 29 17 Z" />
  <path class="outline-stroke" d="M 24 17 L 32 8 L 40 17 L 35 17 L 35 29 L 47 29 L 47 24 L 56 32 L 47 40 L 47 35 L 35 35 L 35 47 L 40 47 L 32 56 L 24 47 L 29 47 L 29 35 L 17 35 L 17 40 L 8 32 L 17 24 L 17 29 L 29 29 L 29 17 Z" />

  <!-- Purple Pivot Center Diamond -->
  <polygon class="accent-fill" points="32,27 37,32 32,37 27,32" />
"""
}

# 14. Alternate Select (UpArrow)
ICONS["alternate_select"] = {
    "key": "UpArrow",
    "filename": "mono_alternate_select",
    "name": "Alternate Select",
    "hotspot": (32 / 64, 7 / 64),
    "svg": """
  <!-- Solid Black Upward Arrow with Pale Lilac Outline -->
  <path class="contrast-stroke" d="M 21 21 L 32 7 L 43 21 L 35 21 L 35 56 L 29 56 L 29 21 Z" />
  <path class="outline-stroke" d="M 21 21 L 32 7 L 43 21 L 35 21 L 35 56 L 29 56 L 29 21 Z" />
"""
}

# 15. Link Select (Hand)
ICONS["link_select"] = {
    "key": "Hand",
    "filename": "mono_link_select",
    "name": "Link Select",
    "hotspot": (20 / 64, 20 / 64),
    "svg": """
  <!-- Two Interlocking Rounded Chain Links with Solid Black Fill -->
  <!-- Upper Left Link -->
  <rect class="contrast-stroke" x="12" y="12" width="25" height="14" rx="7" ry="7" transform="rotate(-45 24.5 19)" />
  <!-- Lower Right Link -->
  <rect class="contrast-stroke" x="27" y="27" width="25" height="14" rx="7" ry="7" transform="rotate(-45 39.5 34)" />

  <rect class="outline-stroke" x="12" y="12" width="25" height="14" rx="7" ry="7" transform="rotate(-45 24.5 19)" />
  <rect class="outline-stroke" x="27" y="27" width="25" height="14" rx="7" ry="7" transform="rotate(-45 39.5 34)" />

  <!-- Purple Connection Accent Pill at Junction -->
  <circle cx="32" cy="32" r="5.5" fill="#000000" />
  <circle class="accent-fill" cx="32" cy="32" r="4" />
"""
}

# 16. Location Select (Pin)
ICONS["location_select"] = {
    "key": "Pin",
    "filename": "mono_location_select",
    "name": "Location Select",
    "hotspot": (32 / 64, 58 / 64),
    "svg": """
  <!-- Teardrop Map Pin Silhouette with Solid Black Body Pointing to (32, 58) -->
  <path class="contrast-stroke" d="M 32 58 
           C 18 43, 13 34, 13 24 
           C 13 13.5, 21.5 5, 32 5 
           C 42.5 5, 51 13.5, 51 24 
           C 51 34, 46 43, 32 58 Z" />

  <path class="outline-stroke" d="M 32 58 
           C 18 43, 13 34, 13 24 
           C 13 13.5, 21.5 5, 32 5 
           C 42.5 5, 51 13.5, 51 24 
           C 51 34, 46 43, 32 58 Z" />

  <!-- Filled Purple Accent Center Dot -->
  <circle class="accent-fill" cx="32" cy="24" r="5.8" />
"""
}

# 17. Person Select (Person)
ICONS["person_select"] = {
    "key": "Person",
    "filename": "mono_person_select",
    "name": "Person Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Solid Black Person / User Silhouette (Head + Torso) -->
  <!-- Head -->
  <circle class="contrast-stroke" cx="32" cy="16" r="9" />
  <circle class="outline-stroke" cx="32" cy="16" r="9" />

  <!-- Torso Base -->
  <path class="contrast-stroke" d="M 12 53 C 12 41, 20 37, 32 37 C 44 37, 52 41, 52 53 Z" />
  <path class="outline-stroke" d="M 12 53 C 12 41, 20 37, 32 37 C 44 37, 52 41, 52 53 Z" />

  <!-- Purple Accent at Collar -->
  <rect class="accent-fill" x="29" y="36" width="6" height="2.5" rx="1.25" />
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

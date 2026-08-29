"""
MONO Cursor Pack - 17 Master SVG Icon Generators (Refined & Polished)
"""
import os
from tokens import wrap_svg, OUTLINE_COLOR, ACCENT_COLOR

ICONS = {}

# 1. Normal Select (Arrow)
ICONS["normal_select"] = {
    "key": "Arrow",
    "filename": "mono_normal_select",
    "name": "Normal Select",
    "hotspot": (14 / 64, 9 / 64),
    "svg": """
  <!-- Outer Dark Contrast Stroke -->
  <path class="contrast-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Main Hollow Pale-Lilac Outline -->
  <path class="outline-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Floating Purple Accent Pill in Heel -->
  <rect class="accent-fill" x="16.2" y="36.5" width="3.6" height="8.5" rx="1.8" ry="1.8" />
"""
}

# 2. Help Select (Help)
ICONS["help_select"] = {
    "key": "Help",
    "filename": "mono_help_select",
    "name": "Help Select",
    "hotspot": (14 / 64, 9 / 64),
    "svg": """
  <!-- Base Pointer Contrast -->
  <path class="contrast-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Base Pointer Outline -->
  <path class="outline-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Purple Pill in Heel -->
  <rect class="accent-fill" x="16.2" y="36.5" width="3.6" height="8.5" rx="1.8" ry="1.8" />

  <!-- Help Circle Badge at Lower Right (Solid mask + saturated purple circle) -->
  <circle cx="50" cy="47" r="9.5" fill="#000000" fill-opacity="0.75" />
  <circle class="contrast-stroke-lean" cx="50" cy="47" r="8.2" />
  <circle class="accent-fill" cx="50" cy="47" r="8" />
  
  <!-- Question Mark Inside Badge -->
  <path d="M 47.8 44 C 47.8 42.2 49 41.2 50.2 41.2 C 51.5 41.2 52.4 42.1 52.4 43.3 C 52.4 44.4 51.5 45.1 50.6 45.8 L 50.6 47" 
        stroke="#F5F1FF" stroke-width="1.8" stroke-linecap="round" fill="none" />
  <circle cx="50.6" cy="50.2" r="1.1" fill="#F5F1FF" />
"""
}

# 3. Working in Background (AppStarting)
ICONS["working_in_background"] = {
    "key": "AppStarting",
    "filename": "mono_working_in_background",
    "name": "Working in Background",
    "hotspot": (14 / 64, 9 / 64),
    "svg": """
  <!-- Base Pointer Contrast -->
  <path class="contrast-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Base Pointer Outline -->
  <path class="outline-stroke" d="M 14 9
           C 25 18, 41 28, 47.5 45.5
           C 48.5 48.5, 45 51, 41.5 48
           C 33.5 40.5, 27 34, 23 35.5
           C 18.5 37, 16.5 45, 15.5 48.5
           C 14.5 51.5, 13.5 50.5, 13.5 46.5
           Z" />

  <!-- Purple Pill in Heel -->
  <rect class="accent-fill" x="16.2" y="36.5" width="3.6" height="8.5" rx="1.8" ry="1.8" />

  <!-- Spinner Ring at Lower Right -->
  <circle cx="50" cy="47" r="8" fill="#000000" fill-opacity="0.65" />
  <circle cx="50" cy="47" r="7.2" stroke="#000000" stroke-opacity="0.65" stroke-width="5.5" fill="none" stroke-dasharray="26 12" />
  <circle cx="50" cy="47" r="7.2" stroke="#F5F1FF" stroke-width="3.2" fill="none" stroke-dasharray="26 12" stroke-linecap="round" />
  <!-- Purple Accent Dot -->
  <circle class="accent-fill" cx="55.5" cy="42" r="2.4" />
"""
}

# 4. Busy (Wait)
ICONS["busy"] = {
    "key": "Wait",
    "filename": "mono_busy",
    "name": "Busy",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Tri-Arc Spinner connecting 3 purple dots -->
  <!-- Dark Contrast Arcs -->
  <path class="contrast-stroke" d="M 32 17 A 17 17 0 0 1 45 40" />
  <path class="contrast-stroke" d="M 45 40 A 17 17 0 0 1 19 40" />
  <path class="contrast-stroke" d="M 19 40 A 17 17 0 0 1 32 17" />

  <!-- Pale Lilac Outline Arcs -->
  <path class="outline-stroke" d="M 32 17 A 17 17 0 0 1 45 40" />
  <path class="outline-stroke" d="M 45 40 A 17 17 0 0 1 19 40" />
  <path class="outline-stroke" d="M 19 40 A 17 17 0 0 1 32 17" />

  <!-- 3 Purple Accent Dots -->
  <circle class="contrast-fill" cx="32" cy="17" r="6" />
  <circle class="accent-fill" cx="32" cy="17" r="4.6" />

  <circle class="contrast-fill" cx="45" cy="40" r="6" />
  <circle class="accent-fill" cx="45" cy="40" r="4.6" />

  <circle class="contrast-fill" cx="19" cy="40" r="6" />
  <circle class="accent-fill" cx="19" cy="40" r="4.6" />
"""
}

# 5. Precision Select (Crosshair)
ICONS["precision_select"] = {
    "key": "Crosshair",
    "filename": "mono_precision_select",
    "name": "Precision Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- 4 Segmented Hollow Crosshair Arms with center gap -->
  <!-- Contrast Stroke -->
  <line class="contrast-stroke" x1="32" y1="9" x2="32" y2="23" />
  <line class="contrast-stroke" x1="32" y1="41" x2="32" y2="55" />
  <line class="contrast-stroke" x1="9" y1="32" x2="23" y2="32" />
  <line class="contrast-stroke" x1="41" y1="32" x2="55" y2="32" />

  <!-- Pale Lilac Outline -->
  <line class="outline-stroke" x1="32" y1="9" x2="32" y2="23" />
  <line class="outline-stroke" x1="32" y1="41" x2="32" y2="55" />
  <line class="outline-stroke" x1="9" y1="32" x2="23" y2="32" />
  <line class="outline-stroke" x1="41" y1="32" x2="55" y2="32" />

  <!-- Center Purple Dot -->
  <circle class="contrast-fill" cx="32" cy="32" r="4.8" />
  <circle class="accent-fill" cx="32" cy="32" r="3.4" />

  <!-- Purple Accent Dots on 4 Outer Tips -->
  <circle class="accent-fill" cx="32" cy="9" r="2.2" />
  <circle class="accent-fill" cx="32" cy="55" r="2.2" />
  <circle class="accent-fill" cx="9" cy="32" r="2.2" />
  <circle class="accent-fill" cx="55" cy="32" r="2.2" />
"""
}

# 6. Text Select (IBeam)
ICONS["text_select"] = {
    "key": "IBeam",
    "filename": "mono_text_select",
    "name": "Text Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Bold Hollow I-Beam with Vertical Purple Center Accent Bar -->
  <!-- Top Crossbar Contrast -->
  <path class="contrast-stroke" d="M 21 14 L 43 14" />
  <!-- Bottom Crossbar Contrast -->
  <path class="contrast-stroke" d="M 21 50 L 43 50" />
  <!-- Side Bracket Curves Contrast -->
  <path class="contrast-stroke" d="M 24 14 C 28 22, 28 42, 24 50" />
  <path class="contrast-stroke" d="M 40 14 C 36 22, 36 42, 40 50" />

  <!-- Top Crossbar Outline -->
  <path class="outline-stroke" d="M 21 14 L 43 14" />
  <!-- Bottom Crossbar Outline -->
  <path class="outline-stroke" d="M 21 50 L 43 50" />
  <!-- Side Bracket Curves Outline -->
  <path class="outline-stroke" d="M 24 14 C 28 22, 28 42, 24 50" />
  <path class="outline-stroke" d="M 40 14 C 36 22, 36 42, 40 50" />

  <!-- Vertical Purple Accent Bar in Center -->
  <rect class="contrast-fill" x="30" y="19" width="4" height="26" rx="2" />
  <rect class="accent-fill" x="30.5" y="20" width="3" height="24" rx="1.5" />
"""
}

# 7. Handwriting (NWPen)
ICONS["handwriting"] = {
    "key": "NWPen",
    "filename": "mono_handwriting",
    "name": "Handwriting",
    "hotspot": (12 / 64, 52 / 64),
    "svg": """
  <!-- Diagonal Pencil Outline pointing bottom-left (12, 52) -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 48 16 
           C 51 13, 54 16, 52 19 
           L 24 47 
           L 12 52 
           L 17 40 
           L 45 12 
           C 46 11, 47 11, 48 12 Z" />
  
  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 48 16 
           C 51 13, 54 16, 52 19 
           L 24 47 
           L 12 52 
           L 17 40 
           L 45 12 
           C 46 11, 47 11, 48 12 Z" />

  <!-- Pencil Collar Line -->
  <line class="contrast-stroke-lean" x1="21" y1="44" x2="26" y2="49" />
  <line class="outline-stroke-lean" x1="21" y1="44" x2="26" y2="49" />

  <!-- Purple Filled Tip Lead at bottom-left point -->
  <path class="accent-fill" d="M 12 52 L 18 43 L 23 48 Z" />
"""
}

# 8. Unavailable (No)
ICONS["unavailable"] = {
    "key": "No",
    "filename": "mono_unavailable",
    "name": "Unavailable",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Circle Slash Universal 'No' Symbol -->
  <!-- Contrast Outer Ring & Slash -->
  <circle class="contrast-stroke" cx="32" cy="32" r="19" />
  <line class="contrast-stroke" x1="18.5" y1="18.5" x2="45.5" y2="45.5" />

  <!-- Pale Lilac Ring -->
  <circle class="outline-stroke" cx="32" cy="32" r="19" />

  <!-- Purple Diagonal Accent Slash -->
  <line class="accent-stroke" x1="18.5" y1="18.5" x2="45.5" y2="45.5" />
"""
}

# 9. Vertical Resize (SizeNS)
ICONS["vertical_resize"] = {
    "key": "SizeNS",
    "filename": "mono_vertical_resize",
    "name": "Vertical Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Vertical Double-Headed Arrow -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 23 20 L 32 10 L 41 20" />
  <path class="contrast-stroke" d="M 32 10 L 32 54" />
  <path class="contrast-stroke" d="M 23 44 L 32 54 L 41 44" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 23 20 L 32 10 L 41 20" />
  <path class="outline-stroke" d="M 32 10 L 32 54" />
  <path class="outline-stroke" d="M 23 44 L 32 54 L 41 44" />
"""
}

# 10. Horizontal Resize (SizeWE)
ICONS["horizontal_resize"] = {
    "key": "SizeWE",
    "filename": "mono_horizontal_resize",
    "name": "Horizontal Resize",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Horizontal Double-Headed Arrow -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 20 23 L 10 32 L 20 41" />
  <path class="contrast-stroke" d="M 10 32 L 54 32" />
  <path class="contrast-stroke" d="M 44 23 L 54 32 L 44 41" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 20 23 L 10 32 L 20 41" />
  <path class="outline-stroke" d="M 10 32 L 54 32" />
  <path class="outline-stroke" d="M 44 23 L 54 32 L 44 41" />
"""
}

# 11. Diagonal Resize 1 (SizeNWSE)
ICONS["diagonal_resize_1"] = {
    "key": "SizeNWSE",
    "filename": "mono_diagonal_resize_1",
    "name": "Diagonal Resize 1 (NWSE)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- NW to SE Double-Headed Diagonal Arrow -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 12 25 L 12 12 L 25 12" />
  <path class="contrast-stroke" d="M 12 12 L 52 52" />
  <path class="contrast-stroke" d="M 39 52 L 52 52 L 52 39" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 12 25 L 12 12 L 25 12" />
  <path class="outline-stroke" d="M 12 12 L 52 52" />
  <path class="outline-stroke" d="M 39 52 L 52 52 L 52 39" />
"""
}

# 12. Diagonal Resize 2 (SizeNESW)
ICONS["diagonal_resize_2"] = {
    "key": "SizeNESW",
    "filename": "mono_diagonal_resize_2",
    "name": "Diagonal Resize 2 (NESW)",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- NE to SW Double-Headed Diagonal Arrow -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 39 12 L 52 12 L 52 25" />
  <path class="contrast-stroke" d="M 52 12 L 12 52" />
  <path class="contrast-stroke" d="M 12 39 L 12 52 L 25 52" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 39 12 L 52 12 L 52 25" />
  <path class="outline-stroke" d="M 52 12 L 12 52" />
  <path class="outline-stroke" d="M 12 39 L 12 52 L 25 52" />
"""
}

# 13. Move (SizeAll)
ICONS["move"] = {
    "key": "SizeAll",
    "filename": "mono_move",
    "name": "Move",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- 4-Directional Arrow Cross with Purple Pivot Center -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 25 18 L 32 10 L 39 18" />
  <path class="contrast-stroke" d="M 32 10 L 32 54" />
  <path class="contrast-stroke" d="M 25 46 L 32 54 L 39 46" />
  <path class="contrast-stroke" d="M 18 25 L 10 32 L 18 39" />
  <path class="contrast-stroke" d="M 10 32 L 54 32" />
  <path class="contrast-stroke" d="M 46 25 L 54 32 L 46 39" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 25 18 L 32 10 L 39 18" />
  <path class="outline-stroke" d="M 32 10 L 32 54" />
  <path class="outline-stroke" d="M 25 46 L 32 54 L 39 46" />
  <path class="outline-stroke" d="M 18 25 L 10 32 L 18 39" />
  <path class="outline-stroke" d="M 10 32 L 54 32" />
  <path class="outline-stroke" d="M 46 25 L 54 32 L 46 39" />

  <!-- Purple Pivot Center Diamond -->
  <polygon class="contrast-fill" points="32,26 38,32 32,38 26,32" />
  <polygon class="accent-fill" points="32,27.5 36.5,32 32,36.5 27.5,32" />
"""
}

# 14. Alternate Select (UpArrow)
ICONS["alternate_select"] = {
    "key": "UpArrow",
    "filename": "mono_alternate_select",
    "name": "Alternate Select",
    "hotspot": (32 / 64, 10 / 64),
    "svg": """
  <!-- Lean Single Vertical Up Arrow -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke-lean" d="M 22 22 L 32 10 L 42 22" />
  <path class="contrast-stroke-lean" d="M 32 10 L 32 54" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke-lean" d="M 22 22 L 32 10 L 42 22" />
  <path class="outline-stroke-lean" d="M 32 10 L 32 54" />
"""
}

# 15. Link Select (Hand)
ICONS["link_select"] = {
    "key": "Hand",
    "filename": "mono_link_select",
    "name": "Link Select",
    "hotspot": (22 / 64, 22 / 64),
    "svg": """
  <!-- Two Interlocking Rounded Chain Links Angled 45deg -->
  <!-- Upper Left Link Contrast -->
  <rect class="contrast-stroke" x="14" y="14" width="22" height="12" rx="6" ry="6" transform="rotate(-45 25 20)" />
  <!-- Lower Right Link Contrast -->
  <rect class="contrast-stroke" x="28" y="28" width="22" height="12" rx="6" ry="6" transform="rotate(-45 39 34)" />

  <!-- Upper Left Link Outline -->
  <rect class="outline-stroke" x="14" y="14" width="22" height="12" rx="6" ry="6" transform="rotate(-45 25 20)" />
  <!-- Lower Right Link Outline -->
  <rect class="outline-stroke" x="28" y="28" width="22" height="12" rx="6" ry="6" transform="rotate(-45 39 34)" />

  <!-- Purple Connection Accent Pill at Junction -->
  <circle class="contrast-fill" cx="32" cy="32" r="5" />
  <circle class="accent-fill" cx="32" cy="32" r="3.6" />
"""
}

# 16. Location Select (Pin)
ICONS["location_select"] = {
    "key": "Pin",
    "filename": "mono_location_select",
    "name": "Location Select",
    "hotspot": (32 / 64, 54 / 64),
    "svg": """
  <!-- Teardrop Map Pin Silhouette Pointing Down (32, 54) -->
  <!-- Contrast Stroke -->
  <path class="contrast-stroke" d="M 32 54 
           C 20 41, 15 33, 15 25 
           C 15 15.5, 22.5 8, 32 8 
           C 41.5 8, 49 15.5, 49 25 
           C 49 33, 44 41, 32 54 Z" />

  <!-- Pale Lilac Outline -->
  <path class="outline-stroke" d="M 32 54 
           C 20 41, 15 33, 15 25 
           C 15 15.5, 22.5 8, 32 8 
           C 41.5 8, 49 15.5, 49 25 
           C 49 33, 44 41, 32 54 Z" />

  <!-- Filled Purple Accent Center Dot -->
  <circle class="contrast-fill" cx="32" cy="25" r="6.5" />
  <circle class="accent-fill" cx="32" cy="25" r="5" />
"""
}

# 17. Person Select (Person)
ICONS["person_select"] = {
    "key": "Person",
    "filename": "mono_person_select",
    "name": "Person Select",
    "hotspot": (32 / 64, 32 / 64),
    "svg": """
  <!-- Hollow Person / User Silhouette (Head + Torso) -->
  <!-- Head Contrast -->
  <circle class="contrast-stroke" cx="32" cy="18" r="8" />
  <!-- Torso Base Contrast -->
  <path class="contrast-stroke" d="M 15 50 C 15 40, 22 36, 32 36 C 42 36, 49 40, 49 50 Z" />

  <!-- Head Outline -->
  <circle class="outline-stroke" cx="32" cy="18" r="8" />
  <!-- Torso Base Outline -->
  <path class="outline-stroke" d="M 15 50 C 15 40, 22 36, 32 36 C 42 36, 49 40, 49 50 Z" />

  <!-- Purple Accent at Collar -->
  <rect class="contrast-fill" x="29" y="34.5" width="6" height="3" rx="1.5" />
  <rect class="accent-fill" x="29.5" y="35" width="5" height="2" rx="1" />
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

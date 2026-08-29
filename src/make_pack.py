"""
MONO Cursor Pack - Master Build Pipeline
Executes the full compilation from vector SVG tokens to final Windows .CUR binaries and installers.
"""
import os
import sys
from PySide6.QtGui import QImage, QPainter, QColor, QFont, QPen, QGuiApplication
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QByteArray, QRect, Qt

from build_icons import build_all_svgs, ICONS, wrap_svg
from rasterize import rasterize_all, SIZES
from cur_packer import pack_cur, inspect_cur
from installer_gen import generate_installers

def build_mono_pack():
    print("=== MONO Cursor Pack Build Pipeline ===")
    
    # 1. Generate SVGs
    print("\n[Step 1/5] Generating 17 Master SVGs...")
    svg_files = build_all_svgs(output_dir="svg")
    print(f"Generated {len(svg_files)} SVGs in svg/")
    
    # 2. Rasterize to Multi-Resolution PNGs
    print("\n[Step 2/5] Rasterizing SVGs to transparent PNGs across 7 resolutions...")
    rendered_map = rasterize_all(png_root_dir="png")
    
    # 3. Pack into Binary .CUR files
    print("\n[Step 3/5] Packing PNGs into Windows CUR binary containers with exact hotspots...")
    os.makedirs("dist", exist_ok=True)
    cur_files = {}
    
    for icon_id, data in ICONS.items():
        png_size_map = rendered_map[icon_id]
        hotspot_pct = data["hotspot"]
        cur_filename = f"{data['filename']}.cur"
        cur_path = os.path.join("dist", cur_filename)
        
        pack_cur(png_size_map, hotspot_pct, cur_path)
        cur_files[icon_id] = cur_path

    # Generate compatibility aliases for standard Windows OLE / drag-drop tools
    import shutil
    shutil.copyfile("dist/mono_text_drag.cur", "dist/draft.cur")
    shutil.copyfile("dist/mono_text_drag.cur", "dist/dnd-move.cur")
    shutil.copyfile("dist/mono_drag_copy.cur", "dist/copy.cur")
    shutil.copyfile("dist/mono_drag_copy.cur", "dist/dnd-copy.cur")
    shutil.copyfile("dist/mono_drag_link.cur", "dist/alias.cur")
    shutil.copyfile("dist/mono_drag_link.cur", "dist/dnd-link.cur")
    shutil.copyfile("dist/mono_dnd_no_drop.cur", "dist/dnd-none.cur")
    shutil.copyfile("dist/mono_dnd_no_drop.cur", "dist/dnd-no-drop.cur")
    shutil.copyfile("dist/mono_vertical_text.cur", "dist/vertical-text.cur")
        
    # 4. Verify binary structures
    print("\n[Step 4/5] Validating compiled .CUR files...")
    for icon_id, cur_path in cur_files.items():
        inspect_cur(cur_path)
        
    # 5. Generate Installers
    print("\n[Step 5/5] Generating Windows installers & registry scripts...")
    generate_installers(cur_dir="dist", install_dir="install")
    
    # 6. Generate Showcase Preview Grid (Both Dark and Light)
    generate_gallery_previews()
    
    print("\n=== MONO Cursor Pack Build Completed Successfully! ===")

def generate_gallery_previews():
    """
    Renders visual verification sheets of all 17 icons side-by-side on both dark and light backdrops.
    """
    app = QGuiApplication.instance() or QGuiApplication(sys.argv)
    artifact_dir = r"C:\Users\tusha\.gemini\antigravity-ide\brain\c1b8b620-7f3c-4f08-bbab-65cb5b1abdd3"
    os.makedirs(artifact_dir, exist_ok=True)
    os.makedirs("preview", exist_ok=True)
    
    ordered_icons = [
        "normal_select", "help_select", "working_in_background", "busy", "precision_select", "text_select",
        "handwriting", "unavailable", "vertical_resize", "horizontal_resize", "diagonal_resize_1", "diagonal_resize_2",
        "move", "alternate_select", "link_select", "location_select", "person_select",
        "text_drag", "drag_copy", "drag_link", "dnd_no_drop", "vertical_text"
    ]
    
    # 6 columns x 4 rows grid
    COLS = 6
    ROWS = 4
    CELL_W = 200
    CELL_H = 190
    PADDING = 40
    TOP_BAR = 120
    
    TOTAL_W = PADDING * 2 + COLS * CELL_W
    TOTAL_H = TOP_BAR + ROWS * CELL_H + PADDING
    
    def render_board(bg_color, card_bg, border_color, text_main, text_sub, out_file):
        img = QImage(TOTAL_W, TOTAL_H, QImage.Format_ARGB32_Premultiplied)
        img.fill(QColor(bg_color))
        
        p = QPainter(img)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setRenderHint(QPainter.SmoothPixmapTransform, True)
        p.setRenderHint(QPainter.TextAntialiasing, True)
        
        # Header Title
        p.setFont(QFont("Segoe UI", 26, QFont.Bold))
        p.setPen(QColor(text_main))
        p.drawText(PADDING, 60, "MONO — Custom Windows 11 Cursor Pack")
        
        # Header Subtitle
        p.setFont(QFont("Segoe UI", 12))
        p.setPen(QColor(text_sub))
        p.drawText(PADDING, 92, "Outline: #F5F1FF (Near-White Lilac) | Accent: #B18CFF | Solid Black Fill | 60 FPS Animated .ANI")
        
        card_font = QFont("Segoe UI", 11, QFont.Bold)
        key_font = QFont("Segoe UI", 9)
        
        for idx, icon_id in enumerate(ordered_icons):
            row = idx // COLS
            col = idx % COLS
            x = PADDING + col * CELL_W
            y = TOP_BAR + row * CELL_H
            
            # Card background
            p.setBrush(QColor(card_bg))
            p.setPen(QPen(QColor(border_color), 1.2))
            p.drawRoundedRect(x + 8, y + 8, CELL_W - 16, CELL_H - 16, 12, 12)
            
            # Icon
            data = ICONS[icon_id]
            svg_content = wrap_svg(data["svg"])
            renderer = QSvgRenderer(QByteArray(svg_content.encode('utf-8')))
            
            icon_box_size = 76
            icon_x = x + (CELL_W - icon_box_size) // 2
            icon_y = y + 24
            renderer.render(p, QRect(icon_x, icon_y, icon_box_size, icon_box_size))
            
            # Text Labels
            p.setFont(card_font)
            p.setPen(QColor(text_main))
            p.drawText(QRect(x + 10, y + 115, CELL_W - 20, 24), Qt.AlignCenter, data["name"])
            
            p.setFont(key_font)
            p.setPen(QColor(text_sub))
            p.drawText(QRect(x + 10, y + 140, CELL_W - 20, 20), Qt.AlignCenter, f"({data['key']})")
            
        p.end()
        img.save(out_file)
        # Also copy to artifact dir
        basename = os.path.basename(out_file)
        img.save(os.path.join(artifact_dir, basename))
        print(f"Generated preview board: {out_file}")

    # Render Dark Theme Showcase
    render_board(
        bg_color="#09080F",
        card_bg="#141122",
        border_color="#27213C",
        text_main="#F5F1FF",
        text_sub="#9C94BC",
        out_file="preview/mono_showcase_dark.png"
    )
    
    # Render Light Theme Showcase
    render_board(
        bg_color="#F3F2F8",
        card_bg="#FFFFFF",
        border_color="#D8D4E5",
        text_main="#181523",
        text_sub="#6F6987",
        out_file="preview/mono_showcase_light.png"
    )

if __name__ == "__main__":
    build_mono_pack()

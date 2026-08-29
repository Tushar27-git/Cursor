"""
MONO Cursor Pack - Multi-Resolution PNG Rasterizer
Rasterizes 17 master SVGs to transparent PNGs across 7 resolutions:
16, 24, 32, 48, 64, 96, 128 px.
"""
import os
import sys
from PySide6.QtGui import QImage, QPainter, QGuiApplication
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QByteArray, Qt
from build_icons import ICONS, wrap_svg

SIZES = [16, 24, 32, 48, 64, 96, 128]

def rasterize_svg_to_png(svg_content, out_path, size):
    """
    Renders SVG content to a high-quality transparent PNG at the given size.
    """
    renderer = QSvgRenderer(QByteArray(svg_content.encode('utf-8')))
    img = QImage(size, size, QImage.Format_ARGB32_Premultiplied)
    img.fill(Qt.transparent)
    
    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
    renderer.render(painter)
    painter.end()
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "PNG")

def rasterize_all(png_root_dir="png"):
    app = QGuiApplication.instance() or QGuiApplication(sys.argv)
    
    rendered_map = {} # icon_id -> {size: png_path}
    
    for icon_id, data in ICONS.items():
        svg_content = wrap_svg(data["svg"])
        rendered_map[icon_id] = {}
        
        # Save master 64x64 PNG and resolution subfolders
        for size in SIZES:
            size_dir = os.path.join(png_root_dir, f"{size}x{size}")
            png_filename = f"{data['filename']}_{size}x{size}.png"
            png_path = os.path.join(size_dir, png_filename)
            
            rasterize_svg_to_png(svg_content, png_path, size)
            rendered_map[icon_id][size] = png_path
            
        print(f"Rasterized {data['name']} across {len(SIZES)} resolutions.")
        
    return rendered_map

if __name__ == "__main__":
    rasterize_all()

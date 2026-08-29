"""
MONO Cursor Pack - Windows Animated Cursor (.ANI) Generator
Generates smooth 60fps rotating .ani files for Busy (Wait) and Working in Background (AppStarting).
"""
import os
import struct
import math
from PySide6.QtGui import QImage, QPainter, QColor, QGuiApplication
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QByteArray, Qt

from cur_packer import pack_cur
from tokens import wrap_svg

def create_rotated_busy_svg(angle_deg):
    """
    Returns SVG with tri-arc spinner rotated by angle_deg around center (32, 32).
    """
    return wrap_svg(f"""
  <g transform="rotate({angle_deg} 32 32)">
    <!-- Tri-Arc Spinner with Solid Black Disk -->
    <circle cx="32" cy="32" r="23" fill="#000000" />
    
    <!-- Arcs -->
    <path class="contrast-stroke-hollow" d="M 32 14.5 A 19.8 19.8 0 0 1 47.8 41.8" />
    <path class="contrast-stroke-hollow" d="M 47.8 41.8 A 19.8 19.8 0 0 1 16.2 41.8" />
    <path class="contrast-stroke-hollow" d="M 16.2 41.8 A 19.8 19.8 0 0 1 32 14.5" />

    <path class="outline-stroke-hollow" d="M 32 14.5 A 19.8 19.8 0 0 1 47.8 41.8" />
    <path class="outline-stroke-hollow" d="M 47.8 41.8 A 19.8 19.8 0 0 1 16.2 41.8" />
    <path class="outline-stroke-hollow" d="M 16.2 41.8 A 19.8 19.8 0 0 1 32 14.5" />

    <!-- 3 Purple Accent Dots -->
    <circle cx="32" cy="14.5" r="7.2" fill="#000000" />
    <circle class="accent-fill" cx="32" cy="14.5" r="5.4" />

    <circle cx="47.8" cy="41.8" r="7.2" fill="#000000" />
    <circle class="accent-fill" cx="47.8" cy="41.8" r="5.4" />

    <circle cx="16.2" cy="41.8" r="7.2" fill="#000000" />
    <circle class="accent-fill" cx="16.2" cy="41.8" r="5.4" />
  </g>
""")

def create_rotated_working_svg(angle_deg):
    """
    Returns SVG with spinner rotated by angle_deg around spinner center (52, 50).
    """
    return wrap_svg(f"""
  <!-- Base Pointer Contrast + Solid Black -->
  <path class="contrast-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <!-- Base Pointer Outline -->
  <path class="outline-stroke" d="M 10 5
           C 24 16, 44 28, 52 50
           C 53.2 53.8, 48.8 57, 45 53.5
           C 35.5 44.5, 27.5 36.5, 22.8 38.5
           C 17 40.5, 14 50.5, 13 54.8
           C 11.5 58.5, 9.5 57.5, 9.5 52.5
           Z" />

  <!-- Purple Pill in Heel -->
  <rect class="accent-fill" x="13.2" y="39.5" width="4.6" height="11" rx="2.3" />

  <!-- Rotating Spinner Ring at Lower Right -->
  <circle cx="52" cy="50" r="9.5" fill="#000000" />
  <g transform="rotate({angle_deg} 52 50)">
    <circle cx="52" cy="50" r="8.4" stroke="#000000" stroke-width="6.2" fill="none" stroke-dasharray="29 15" />
    <circle cx="52" cy="50" r="8.4" stroke="#F5F1FF" stroke-width="3.6" fill="none" stroke-dasharray="29 15" stroke-linecap="round" />
    <circle class="accent-fill" cx="58.2" cy="44.8" r="2.9" />
  </g>
""")

def rasterize_svg_bytes(svg_str, size=32):
    renderer = QSvgRenderer(QByteArray(svg_str.encode('utf-8')))
    img = QImage(size, size, QImage.Format_ARGB32_Premultiplied)
    img.fill(Qt.transparent)
    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
    renderer.render(painter)
    painter.end()
    
    from PySide6.QtCore import QBuffer, QIODevice
    buf = QBuffer()
    buf.open(QIODevice.WriteOnly)
    img.save(buf, "PNG")
    data = bytes(buf.data())
    buf.close()
    return data

def make_single_cur_data(svg_str, hotspot_pct=(0.5, 0.5)):
    """
    Creates binary CUR file data containing multi-resolution frames for one rotation step.
    """
    sizes = [16, 24, 32, 48, 64]
    png_map = {}
    for s in sizes:
        png_map[s] = rasterize_svg_bytes(svg_str, s)
        
    # Build CUR binary in-memory
    num_images = len(sizes)
    icondir = struct.pack("<HHH", 0, 2, num_images)
    dir_entries_size = num_images * 16
    current_offset = 6 + dir_entries_size
    
    entries = []
    blobs = []
    hx_pct, hy_pct = hotspot_pct
    
    for s in sorted(sizes):
        data = png_map[s]
        hx = max(0, min(s - 1, int(round(hx_pct * s))))
        hy = max(0, min(s - 1, int(round(hy_pct * s))))
        entry = struct.pack("<BBBBHHII", s, s, 0, 0, hx, hy, len(data), current_offset)
        entries.append(entry)
        blobs.append(data)
        current_offset += len(data)
        
    return icondir + b"".join(entries) + b"".join(blobs)

def pack_ani(frames_cur_data, jif_rate=3, output_ani_path="dist/mono_busy.ani"):
    """
    Packs multiple CUR frames into a Windows Animated Cursor (.ANI) RIFF container.
    jif_rate: duration per frame in jiffies (1 jiffy = 1/60th second). 3 jiffies = 20 fps.
    """
    num_frames = len(frames_cur_data)
    
    # anih chunk (36 bytes):
    # DWORD cbSize (36)
    # DWORD cFrames
    # DWORD cSteps
    # DWORD cx (0 = default)
    # DWORD cy (0 = default)
    # DWORD cBitCount (0 = default)
    # DWORD cPlanes (0 = default)
    # DWORD jifRate (default rate in 1/60s)
    # DWORD fl (flags: 1 = AF_ICON / sequence)
    anih_data = struct.pack(
        "<IIIIIIIII",
        36,
        num_frames,
        num_frames,
        0,
        0,
        0,
        0,
        jif_rate,
        1
    )
    anih_chunk = b"anih" + struct.pack("<I", len(anih_data)) + anih_data
    
    # LIST 'fram' chunk containing 'icon' sub-chunks
    fram_subchunks = []
    for cur_data in frames_cur_data:
        # pad to 2-byte boundary
        pad = b"\x00" if len(cur_data) % 2 != 0 else b""
        icon_chunk = b"icon" + struct.pack("<I", len(cur_data)) + cur_data + pad
        fram_subchunks.append(icon_chunk)
        
    fram_body = b"fram" + b"".join(fram_subchunks)
    list_chunk = b"LIST" + struct.pack("<I", len(fram_body)) + fram_body
    
    # RIFF ACON container
    riff_body = b"ACON" + anih_chunk + list_chunk
    riff_file = b"RIFF" + struct.pack("<I", len(riff_body)) + riff_body
    
    os.makedirs(os.path.dirname(output_ani_path), exist_ok=True)
    with open(output_ani_path, "wb") as f:
        f.write(riff_file)
        
    print(f"Generated animated cursor: {output_ani_path} ({num_frames} frames, {jif_rate} jiffies/frame)")

def build_animated_cursors():
    app = QGuiApplication.instance() or QGuiApplication([])
    
    # 1. Generate 18 frames for Busy (20 degree steps)
    print("Generating animated Busy cursor (mono_busy.ani)...")
    busy_frames = []
    NUM_FRAMES = 18
    for i in range(NUM_FRAMES):
        angle = int(round((360 / NUM_FRAMES) * i))
        svg = create_rotated_busy_svg(angle)
        cur_data = make_single_cur_data(svg, (0.5, 0.5))
        busy_frames.append(cur_data)
        
    pack_ani(busy_frames, jif_rate=2, output_ani_path="dist/mono_busy.ani")
    
    # 2. Generate 18 frames for Working in Background (mono_working_in_background.ani)
    print("Generating animated Working In Background cursor (mono_working_in_background.ani)...")
    working_frames = []
    for i in range(NUM_FRAMES):
        angle = int(round((360 / NUM_FRAMES) * i))
        svg = create_rotated_working_svg(angle)
        cur_data = make_single_cur_data(svg, (10 / 64, 5 / 64))
        working_frames.append(cur_data)
        
    pack_ani(working_frames, jif_rate=2, output_ani_path="dist/mono_working_in_background.ani")

if __name__ == "__main__":
    build_animated_cursors()

"""
MONO Cursor Pack - Struct-Based Windows .CUR Binary Container Packer

Writes proper Windows Cursor (.cur) binary files containing multiple embedded PNG
resolutions with exact per-resolution hotspot metadata.
"""
import os
import struct

def pack_cur(png_size_map, hotspot_pct, output_cur_path):
    """
    Packs multiple PNG images into a valid Windows .cur container.
    
    png_size_map: dict of {size_int: png_file_path or png_bytes}
    hotspot_pct: tuple of (x_pct, y_pct) in range 0.0 to 1.0
    output_cur_path: output .cur file path
    """
    # Sort resolutions ascending
    sorted_sizes = sorted(png_size_map.keys())
    num_images = len(sorted_sizes)
    
    # Read PNG data
    images_data = []
    for sz in sorted_sizes:
        item = png_size_map[sz]
        if isinstance(item, str):
            with open(item, "rb") as f:
                data = f.read()
        else:
            data = item
        images_data.append((sz, data))
        
    # ICONDIR Header (6 bytes):
    # idReserved: 2 bytes (0)
    # idType: 2 bytes (2 for CURSOR)
    # idCount: 2 bytes (number of images)
    icondir = struct.pack("<HHH", 0, 2, num_images)
    
    # Calculate offsets
    # Header is 6 bytes. Each directory entry is 16 bytes.
    dir_entries_size = num_images * 16
    current_offset = 6 + dir_entries_size
    
    entries = []
    data_blobs = []
    
    hx_pct, hy_pct = hotspot_pct
    
    for sz, data in images_data:
        width_byte = sz if sz < 256 else 0
        height_byte = sz if sz < 256 else 0
        color_count = 0
        reserved = 0
        
        # Calculate pixel hotspot for this specific resolution
        hotspot_x = int(round(hx_pct * sz))
        hotspot_y = int(round(hy_pct * sz))
        
        # Clamp to valid bounds
        hotspot_x = max(0, min(sz - 1, hotspot_x))
        hotspot_y = max(0, min(sz - 1, hotspot_y))
        
        bytes_in_res = len(data)
        
        # ICONDIRENTRY for CUR:
        # BYTE bWidth
        # BYTE bHeight
        # BYTE bColorCount (0)
        # BYTE bReserved (0)
        # WORD wXHotspot (cursor hotspot X in pixels)
        # WORD wYHotspot (cursor hotspot Y in pixels)
        # DWORD dwBytesInRes
        # DWORD dwImageOffset
        entry = struct.pack(
            "<BBBBHHII",
            width_byte,
            height_byte,
            color_count,
            reserved,
            hotspot_x,
            hotspot_y,
            bytes_in_res,
            current_offset
        )
        entries.append(entry)
        data_blobs.append(data)
        
        current_offset += bytes_in_res
        
    # Write complete .cur binary file
    os.makedirs(os.path.dirname(output_cur_path), exist_ok=True)
    with open(output_cur_path, "wb") as f:
        f.write(icondir)
        for e in entries:
            f.write(e)
        for d in data_blobs:
            f.write(d)
            
    print(f"Packed {output_cur_path} ({num_images} sizes, hotspot=({int(round(hx_pct*64))},{int(round(hy_pct*64))}) at 64px)")

def inspect_cur(cur_path):
    """
    Inspects and validates a .cur file structure.
    """
    with open(cur_path, "rb") as f:
        data = f.read()
        
    if len(data) < 6:
        raise ValueError("File too small to be a valid CUR/ICO file")
        
    reserved, id_type, count = struct.unpack("<HHH", data[:6])
    assert reserved == 0, f"Expected reserved=0, got {reserved}"
    assert id_type == 2, f"Expected idType=2 (CUR), got {id_type}"
    
    print(f"Inspecting '{cur_path}': Type={id_type} (CUR), Image Count={count}")
    
    offset = 6
    for i in range(count):
        w, h, cc, res, hx, hy, size, img_off = struct.unpack("<BBBBHHII", data[offset:offset+16])
        offset += 16
        w_real = 256 if w == 0 else w
        h_real = 256 if h == 0 else h
        # Check image magic (PNG magic: 89 50 4E 47 0D 0A 1A 0A)
        magic = data[img_off:img_off+8]
        is_png = (magic == b'\x89PNG\r\n\x1a\n')
        print(f"  Frame {i+1}: {w_real}x{h_real} px | Hotspot: ({hx}, {hy}) | Size: {size} bytes | PNG: {is_png}")
        
    return True

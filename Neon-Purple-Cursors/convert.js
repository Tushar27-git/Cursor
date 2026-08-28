const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

// Define cursors and their hotspots (x, y)
const cursors = {
    'arrow': { file: 'arrow.svg', hx: 6, hy: 6 },
    'hand': { file: 'hand.svg', hx: 12, hy: 10 },
    'text': { file: 'text.svg', hx: 16, hy: 16 },
    'crosshair': { file: 'crosshair.svg', hx: 16, hy: 16 },
    'move': { file: 'move.svg', hx: 16, hy: 16 },
    'not-allowed': { file: 'not-allowed.svg', hx: 16, hy: 16 },
    'resize-ew': { file: 'resize-ew.svg', hx: 16, hy: 16 },
    'resize-ns': { file: 'resize-ns.svg', hx: 16, hy: 16 },
    'resize-nwse': { file: 'resize-nwse.svg', hx: 16, hy: 16 },
    'resize-nesw': { file: 'resize-nesw.svg', hx: 16, hy: 16 }
};

async function createCurFile(name, config) {
    const svgPath = path.join(__dirname, config.file);
    const pngBuffer = await sharp(svgPath).png().toBuffer();
    
    // Windows CUR header structure:
    // 0-1: Reserved (0)
    // 2-3: Type (2 for CUR)
    // 4-5: Number of images (1)
    
    // Directory entry (16 bytes):
    // 6: Width (32)
    // 7: Height (32)
    // 8: Color count (0)
    // 9: Reserved (0)
    // 10-11: Hotspot X
    // 12-13: Hotspot Y
    // 14-17: Size of image data
    // 18-21: Offset of image data (always 22 for 1 image)
    
    const curBuffer = Buffer.alloc(22 + pngBuffer.length);
    
    // Header
    curBuffer.writeUInt16LE(0, 0); // Reserved
    curBuffer.writeUInt16LE(2, 2); // Type 2 = CUR
    curBuffer.writeUInt16LE(1, 4); // 1 Image
    
    // Directory Entry
    curBuffer.writeUInt8(32, 6); // Width (0 for 256, but ours is 32)
    curBuffer.writeUInt8(32, 7); // Height
    curBuffer.writeUInt8(0, 8); // Color count
    curBuffer.writeUInt8(0, 9); // Reserved
    curBuffer.writeUInt16LE(config.hx, 10); // Hotspot X
    curBuffer.writeUInt16LE(config.hy, 12); // Hotspot Y
    curBuffer.writeUInt32LE(pngBuffer.length, 14); // Image size
    curBuffer.writeUInt32LE(22, 18); // Image offset
    
    // Write PNG data
    pngBuffer.copy(curBuffer, 22);
    
    // Save to file
    const curPath = path.join(__dirname, `${name}.cur`);
    fs.writeFileSync(curPath, curBuffer);
    console.log(`Created ${name}.cur with hotspot (${config.hx}, ${config.hy})`);
}

async function convertAll() {
    for (const [name, config] of Object.entries(cursors)) {
        await createCurFile(name, config);
    }
}

convertAll().catch(console.error);

const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const srcDir = 'k:/Curseher/Future-Cursor-96eae9a1';
const outDir = 'k:/Curseher/Future-Cursor-Purple';

if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

// Transform PNG: Safe auto-scale up to 15% without clipping + Lighter Neon Purple + Glow
async function recolorPng(pngBuffer, hx = 0, hy = 0) {
  const { data, info } = await sharp(pngBuffer).raw().toBuffer({ resolveWithObject: true });
  const w = info.width;
  const h = info.height;
  
  // 1. Calculate actual pixel bounding box
  let minX = w, maxX = 0, minY = h, maxY = 0;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      if (data[(y * w + x) * 4 + 3] > 10) {
        minX = Math.min(minX, x);
        maxX = Math.max(maxX, x);
        minY = Math.min(minY, y);
        maxY = Math.max(maxY, y);
      }
    }
  }
  
  // 2. Determine safe maximum scale (up to 1.15x) so bottom-right spinner & edges never clip
  let scale = 1.15;
  const margin = 2; // Keep at least 2px padding for glow
  if (maxX > hx) scale = Math.min(scale, (w - margin - hx) / (maxX - hx));
  if (maxY > hy) scale = Math.min(scale, (h - margin - hy) / (maxY - hy));
  if (minX < hx) scale = Math.min(scale, (hx - margin) / (hx - minX));
  if (minY < hy) scale = Math.min(scale, (hy - margin) / (hy - minY));
  scale = Math.max(1.0, scale);
  
  const out = Buffer.alloc(w * h * 4);
  
  for (let dy = 0; dy < h; dy++) {
    for (let dx = 0; dx < w; dx++) {
      // Map destination coordinate back to source coordinate relative to (hx, hy)
      const sx = hx + (dx - hx) / scale;
      const sy = hy + (dy - hy) / scale;
      
      let r = 0, g = 0, b = 0, a = 0;
      if (sx >= 0 && sx < w - 1 && sy >= 0 && sy < h - 1) {
        const x0 = Math.floor(sx), x1 = x0 + 1;
        const y0 = Math.floor(sy), y1 = y0 + 1;
        const fx = sx - x0, fy = sy - y0;
        
        const getIdx = (px, py) => (py * w + px) * 4;
        const i00 = getIdx(x0, y0), i10 = getIdx(x1, y0);
        const i01 = getIdx(x0, y1), i11 = getIdx(x1, y1);
        
        const a00 = data[i00 + 3], a10 = data[i10 + 3], a01 = data[i01 + 3], a11 = data[i11 + 3];
        a = (a00 * (1 - fx) + a10 * fx) * (1 - fy) + (a01 * (1 - fx) + a11 * fx) * fy;
        
        const r00 = data[i00], r10 = data[i10], r01 = data[i01], r11 = data[i11];
        r = (r00 * (1 - fx) + r10 * fx) * (1 - fy) + (r01 * (1 - fx) + r11 * fx) * fy;
        
        const g00 = data[i00 + 1], g10 = data[i10 + 1], g01 = data[i01 + 1], g11 = data[i11 + 1];
        g = (g00 * (1 - fx) + g10 * fx) * (1 - fy) + (g01 * (1 - fx) + g11 * fx) * fy;
        
        const b00 = data[i00 + 2], b10 = data[i10 + 2], b01 = data[i01 + 2], b11 = data[i11 + 2];
        b = (b00 * (1 - fx) + b10 * fx) * (1 - fy) + (b01 * (1 - fx) + b11 * fx) * fy;
      }
      
      const outIdx = (dy * w + dx) * 4;
      if (a < 1) continue;
      
      const lum = 0.299 * r + 0.587 * g + 0.114 * b;
      
      if (a > 130) {
        // Solid body / outline
        const t = Math.min(1, Math.max(0, (lum - 60) / 140));
        
        // Lighter vibrant neon purple (#e48fff: 228, 143, 255) to Deep Black (#06060a)
        out[outIdx] = Math.round((1 - t) * 228 + t * 6);
        out[outIdx + 1] = Math.round((1 - t) * 143 + t * 6);
        out[outIdx + 2] = Math.round((1 - t) * 255 + t * 10);
        out[outIdx + 3] = Math.min(255, Math.round(a));
      } else {
        // Enhanced soft neon glow around edges
        out[outIdx] = 220;
        out[outIdx + 1] = 130;
        out[outIdx + 2] = 255;
        out[outIdx + 3] = Math.min(255, Math.round(a * 1.35));
      }
    }
  }
  
  return await sharp(out, { raw: info }).png().toBuffer();
}

async function recolorCurBuffer(curBuffer) {
  const count = curBuffer.readUInt16LE(4);
  const newPngs = [];
  const entries = [];
  
  for (let i = 0; i < count; i++) {
    const entryOffset = 6 + i * 16;
    const w = curBuffer.readUInt8(entryOffset);
    const h = curBuffer.readUInt8(entryOffset + 1);
    const colorCount = curBuffer.readUInt8(entryOffset + 2);
    const reserved = curBuffer.readUInt8(entryOffset + 3);
    const hx = curBuffer.readUInt16LE(entryOffset + 4);
    const hy = curBuffer.readUInt16LE(entryOffset + 6);
    const size = curBuffer.readUInt32LE(entryOffset + 8);
    const offset = curBuffer.readUInt32LE(entryOffset + 12);
    
    const pngData = curBuffer.slice(offset, offset + size);
    const newPng = await recolorPng(pngData, hx, hy);
    newPngs.push(newPng);
    entries.push({ w, h, colorCount, reserved, hx, hy, size: newPng.length });
  }
  
  const headerSize = 6 + count * 16;
  let totalSize = headerSize;
  for (const p of newPngs) totalSize += p.length;
  
  const outCur = Buffer.alloc(totalSize);
  outCur.writeUInt16LE(curBuffer.readUInt16LE(0), 0);
  outCur.writeUInt16LE(curBuffer.readUInt16LE(2), 2);
  outCur.writeUInt16LE(count, 4);
  
  let currentOffset = headerSize;
  for (let i = 0; i < count; i++) {
    const e = entries[i];
    const entryOffset = 6 + i * 16;
    outCur.writeUInt8(e.w, entryOffset);
    outCur.writeUInt8(e.h, entryOffset + 1);
    outCur.writeUInt8(e.colorCount, entryOffset + 2);
    outCur.writeUInt8(e.reserved, entryOffset + 3);
    outCur.writeUInt16LE(e.hx, entryOffset + 4);
    outCur.writeUInt16LE(e.hy, entryOffset + 6);
    outCur.writeUInt32LE(e.size, entryOffset + 8);
    outCur.writeUInt32LE(currentOffset, entryOffset + 12);
    
    newPngs[i].copy(outCur, currentOffset);
    currentOffset += e.size;
  }
  return outCur;
}

async function recolorAniFile(srcPath, destPath) {
  const aniBuf = fs.readFileSync(srcPath);
  if (aniBuf.slice(0, 4).toString('ascii') !== 'RIFF' || aniBuf.slice(8, 12).toString('ascii') !== 'ACON') {
    throw new Error('Not a valid RIFF ACON file: ' + srcPath);
  }
  
  const outChunks = [];
  let offset = 12;
  
  while (offset < aniBuf.length) {
    const chunkId = aniBuf.slice(offset, offset + 4).toString('ascii');
    const chunkSize = aniBuf.readUInt32LE(offset + 4);
    const chunkData = aniBuf.slice(offset + 8, offset + 8 + chunkSize);
    
    if (chunkId === 'LIST' && chunkData.slice(0, 4).toString('ascii') === 'fram') {
      const framBuffers = [];
      let listOffset = 4;
      
      while (listOffset < chunkData.length) {
        const iconId = chunkData.slice(listOffset, listOffset + 4).toString('ascii');
        const iconSize = chunkData.readUInt32LE(listOffset + 4);
        const iconData = chunkData.slice(listOffset + 8, listOffset + 8 + iconSize);
        
        const newCurBuf = await recolorCurBuffer(iconData);
        
        const iconChunkHeader = Buffer.alloc(8);
        iconChunkHeader.write('icon', 0, 4, 'ascii');
        iconChunkHeader.writeUInt32LE(newCurBuf.length, 4);
        
        framBuffers.push(iconChunkHeader);
        framBuffers.push(newCurBuf);
        if (newCurBuf.length % 2 !== 0) {
          framBuffers.push(Buffer.alloc(1));
        }
        
        listOffset += 8 + iconSize + (iconSize % 2);
      }
      
      const framBody = Buffer.concat([Buffer.from('fram', 'ascii'), ...framBuffers]);
      const listHeader = Buffer.alloc(8);
      listHeader.write('LIST', 0, 4, 'ascii');
      listHeader.writeUInt32LE(framBody.length, 4);
      
      outChunks.push(listHeader);
      outChunks.push(framBody);
      if (framBody.length % 2 !== 0) {
        outChunks.push(Buffer.alloc(1));
      }
    } else {
      const rawChunk = aniBuf.slice(offset, offset + 8 + chunkSize + (chunkSize % 2));
      outChunks.push(rawChunk);
    }
    
    offset += 8 + chunkSize + (chunkSize % 2);
  }
  
  const riffBody = Buffer.concat([Buffer.from('ACON', 'ascii'), ...outChunks]);
  const riffHeader = Buffer.alloc(8);
  riffHeader.write('RIFF', 0, 4, 'ascii');
  riffHeader.writeUInt32LE(riffBody.length, 4);
  
  const finalAni = Buffer.concat([riffHeader, riffBody]);
  fs.writeFileSync(destPath, finalAni);
  console.log(`Recolored ANI: ${path.basename(destPath)} (${finalAni.length} bytes)`);
}

async function processAll() {
  const files = fs.readdirSync(srcDir);
  
  for (const file of files) {
    const srcPath = path.join(srcDir, file);
    const destPath = path.join(outDir, file);
    
    if (file.endsWith('.cur')) {
      const curBuf = fs.readFileSync(srcPath);
      const newCur = await recolorCurBuffer(curBuf);
      fs.writeFileSync(destPath, newCur);
      console.log(`Recolored CUR: ${file}`);
    } else if (file.endsWith('.ani')) {
      await recolorAniFile(srcPath, destPath);
    } else if (file.endsWith('.txt') || file.endsWith('.inf')) {
      fs.copyFileSync(srcPath, destPath);
    }
  }
  
  console.log('All 33 cursor files processed with safe margins (no clipping)!');
}

processAll().catch(console.error);

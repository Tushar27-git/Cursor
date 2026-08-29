# MONO — Windows 11 Custom Lilac-White Cursor Pack

> **A minimal, futuristic hollow cursor pack designed for Windows 11.**  
> Crafted with a warm near-white lilac outline (`#F5F1FF`), vibrant interaction accent dots (`#B18CFF`), and a protective dark outer contour (`rgba(0,0,0,0.65)`) ensuring readability on both dark themes and white backgrounds.

---

## 🎨 Palette & Design Tokens

| Token | Hex / Value | Description |
|---|---|---|
| **Outline Stroke** | `#F5F1FF` | 90% white, 10% lilac (HSL 256°, 45%, 96%). Warm, crisp, and non-clinical. |
| **Accent Fill** | `#B18CFF` | Saturated interaction accent for interactive focal points. |
| **Contrast Halo** | `rgba(0,0,0,0.65)` | Outer protective stroke ensuring the cursor never disappears on white apps. |
| **Stroke Width** | `4.8px` (~7.5%) | Bold, tactile silhouette with rounded caps and joins (`round`). |

---

## 📦 What's Included

### 1. Compiled Windows Cursors (`dist/`)
Contains all **17 `.cur` files**, each embedded with 7 resolutions (**16, 24, 32, 48, 64, 96, 128 px**) and custom pixel-accurate hotspots:
1. `mono_normal_select.cur` (`Arrow`)
2. `mono_help_select.cur` (`Help`)
3. `mono_working_in_background.cur` (`AppStarting`)
4. `mono_busy.cur` (`Wait`)
5. `mono_precision_select.cur` (`Crosshair`)
6. `mono_text_select.cur` (`IBeam`)
7. `mono_handwriting.cur` (`NWPen`)
8. `mono_unavailable.cur` (`No`)
9. `mono_vertical_resize.cur` (`SizeNS`)
10. `mono_horizontal_resize.cur` (`SizeWE`)
11. `mono_diagonal_resize_1.cur` (`SizeNWSE`)
12. `mono_diagonal_resize_2.cur` (`SizeNESW`)
13. `mono_move.cur` (`SizeAll`)
14. `mono_alternate_select.cur` (`UpArrow`)
15. `mono_link_select.cur` (`Hand`)
16. `mono_location_select.cur` (`Pin`)
17. `mono_person_select.cur` (`Person`)

### 2. Master SVGs & PNGs
- `svg/`: 17 master vector source files.
- `png/`: Transparent PNGs exported at 16x16, 24x24, 32x32, 48x48, 64x64, 96x96, and 128x128.

### 3. Installers (`install/`)
- **`install_mono.inf`**: Right-click → **Install** to register the scheme directly into Windows Mouse Properties (`%SystemRoot%\Cursors\Mono`).
- **`apply_mono_live.py`**: Python script that sets the registry and broadcasts `SystemParametersInfo(SPI_SETCURSORS)` for **instant live desktop activation**.
- **`apply_mono_scheme.reg`**: Direct registry script mapping the cursors to your current user profile.
- **`revert_to_default.reg`**: Restores the default Windows cursor scheme.

---

## 🚀 How to Install & Use

### Method 1: Instant Live Activation (Recommended)
Run the Python live activation script:
```powershell
py install/apply_mono_live.py
```

### Method 2: Standard Windows INF Installation
1. Open the `install/` folder in File Explorer.
2. Right-click [`install_mono.inf`](file:///d:/MonoCurseher/install/install_mono.inf) and click **Install**.
3. Open Windows **Settings → Bluetooth & devices → Mouse → Additional mouse settings**.
4. In the **Pointers** tab, select **Mono** from the Scheme dropdown and click **Apply**.

---

## 🛠️ Rebuilding from Source
To modify design tokens or recompile the entire pack:
```powershell
py src/make_pack.py
```
This will automatically generate the SVGs, rasterize multi-resolution PNGs, pack the binary `.cur` files with hotspots, and generate installer files and preview boards.

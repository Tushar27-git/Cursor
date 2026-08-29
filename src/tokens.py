"""
MONO Cursor Pack - Design Tokens & Common Templates
Updated: +3.5% scale fine-tuning with 5.2px bold stroke.
"""

# Color Palette Tokens
OUTLINE_COLOR = "#F5F1FF"         # 90% white / 10% lilac (barely-tinted near-white)
OUTLINE_HIGH_CONTRAST = "#EDE4FF"  # High-contrast variant
ACCENT_COLOR = "#B18CFF"          # Saturated interaction lilac
BODY_FILL_COLOR = "#000000"       # Solid black opaque interior fill (non pass-through)
CONTRAST_COLOR = "#000000"        # Dark contrast halo for white/light UI readability
CONTRAST_OPACITY = "0.75"

# Dimensions & Geometry
CANVAS_SIZE = 64
STROKE_WIDTH_MAIN = 5.2           # Finely tuned bold stroke (+3.5% scale)
STROKE_WIDTH_CONTRAST = 8.2       # Outer halo
STROKE_WIDTH_LEAN = 4.2
STROKE_WIDTH_LEAN_CONTRAST = 7.0

def wrap_svg(body_content, width=64, height=64):
    """
    Wraps SVG glyph layers with standard CSS definitions and design tokens.
    """
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .contrast-stroke {{
        stroke: {CONTRAST_COLOR};
        stroke-opacity: {CONTRAST_OPACITY};
        stroke-width: {STROKE_WIDTH_CONTRAST};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: {BODY_FILL_COLOR};
      }}
      .outline-stroke {{
        stroke: {OUTLINE_COLOR};
        stroke-width: {STROKE_WIDTH_MAIN};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: {BODY_FILL_COLOR};
      }}
      .contrast-stroke-hollow {{
        stroke: {CONTRAST_COLOR};
        stroke-opacity: {CONTRAST_OPACITY};
        stroke-width: {STROKE_WIDTH_CONTRAST};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }}
      .outline-stroke-hollow {{
        stroke: {OUTLINE_COLOR};
        stroke-width: {STROKE_WIDTH_MAIN};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }}
      .contrast-stroke-lean {{
        stroke: {CONTRAST_COLOR};
        stroke-opacity: {CONTRAST_OPACITY};
        stroke-width: {STROKE_WIDTH_LEAN_CONTRAST};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: {BODY_FILL_COLOR};
      }}
      .outline-stroke-lean {{
        stroke: {OUTLINE_COLOR};
        stroke-width: {STROKE_WIDTH_LEAN};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: {BODY_FILL_COLOR};
      }}
      .accent-fill {{
        fill: {ACCENT_COLOR};
      }}
      .accent-stroke {{
        stroke: {ACCENT_COLOR};
        stroke-width: {STROKE_WIDTH_MAIN};
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }}
      .contrast-fill {{
        fill: {CONTRAST_COLOR};
        fill-opacity: {CONTRAST_OPACITY};
      }}
      .solid-black {{
        fill: #000000;
      }}
    </style>
  </defs>
{body_content}
</svg>"""

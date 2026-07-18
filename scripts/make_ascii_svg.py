import sys
from PIL import Image
import numpy as np

def image_to_ascii_svg(image_path, output_path, width=80):
    img = Image.open(image_path).convert('L')
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, height))
    
    pixels = np.array(img)
    ramp = " .`:-=+*cs#%@"
    
    svg_width = width * 8
    svg_height = height * 12
    
    svg = [f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>text { font-family: monospace; font-size: 10px; fill: #8b949e; }</style>')
    svg.append('<rect width="100%" height="100%" fill="transparent" />')
    
    for y in range(height):
        line = ""
        for x in range(width):
            val = pixels[y, x]
            char = ramp[int(val / 256 * len(ramp))]
            line += char
        
        # SMIL animation for "typing" effect
        delay = y * 0.05
        svg.append(f'<text x="0" y="{y*12 + 10}" opacity="0">')
        svg.append(f'  {line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}')
        svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.1s" begin="{delay}s" fill="freeze" />')
        svg.append('</text>')
        
    svg.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))

if __name__ == "__main__":
    image_to_ascii_svg('data/avatar.jpg', 'avi-ascii.svg')

import sys
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

def image_to_ascii_svg(image_path, output_path, width=100):
    # Open and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Enhance contrast and brightness for better ASCII visibility
    img = ImageOps.autocontrast(img)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)
    
    aspect_ratio = img.height / img.width
    # Adjust height for terminal character aspect ratio (usually ~0.5)
    height = int(width * aspect_ratio * 0.5)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    pixels = np.array(img)
    # Refined ramp for better detail
    ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    ramp = ramp[::-1] # Reverse so dark is dense
    
    char_width = 7
    char_height = 12
    svg_width = width * char_width
    svg_height = height * char_height
    
    svg = [f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>text { font-family: "Courier New", monospace; font-size: 10px; fill: #c9d1d9; white-space: pre; }</style>')
    svg.append('<rect width="100%" height="100%" fill="transparent" />')
    
    for y in range(height):
        line = ""
        for x in range(width):
            val = pixels[y, x]
            # Map pixel value to ramp index
            char_idx = int((val / 255) * (len(ramp) - 1))
            line += ramp[char_idx]
        
        # Clean line for XML
        line_clean = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        
        # Typing animation: reveal row by row
        delay = y * 0.04
        svg.append(f'<text x="0" y="{y * char_height + 10}" opacity="0">')
        svg.append(f'  {line_clean}')
        svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.1s" begin="{delay}s" fill="freeze" />')
        svg.append('</text>')
        
    svg.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))

if __name__ == "__main__":
    image_to_ascii_svg('data/avatar.jpg', 'avi-ascii.svg')

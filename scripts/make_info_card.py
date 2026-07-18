def make_info_card(output_path):
    data = [
        ("WHOAMI", "Jiyad Hussain"),
        ("ROLE", "AI Engineer"),
        ("FOCUS", "Deep Learning / NLP / CV"),
        ("STACK", "Python / PyTorch / TS"),
        ("MISSION", "Shipping ML pipelines 🎯")
    ]
    
    width = 450
    height = 200
    line_height = 25
    
    svg = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>')
    svg.append('  .key { fill: #58a6ff; font-family: monospace; font-size: 14px; font-weight: bold; }')
    svg.append('  .val { fill: #8b949e; font-family: monospace; font-size: 14px; }')
    svg.append('  .title { fill: #d29922; font-family: monospace; font-size: 16px; font-weight: bold; }')
    svg.append('</style>')
    
    # Title
    svg.append(f'<text x="10" y="30" class="title">jiyad@github:~$ neofetch')
    svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="0s" fill="freeze" />')
    svg.append('</text>')
    
    for i, (key, val) in enumerate(data):
        y = 70 + (i * line_height)
        delay = 0.5 + (i * 0.2)
        
        svg.append(f'<g opacity="0">')
        svg.append(f'  <text x="20" y="{y}" class="key">{key}:</text>')
        svg.append(f'  <text x="100" y="{y}" class="val">{val}</text>')
        svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay}s" fill="freeze" />')
        svg.append(f'</g>')
        
    svg.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))

if __name__ == "__main__":
    make_info_card('info-card.svg')

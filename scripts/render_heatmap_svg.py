import json

def render_heatmap(json_path, output_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # We want the last 53 weeks (371 days)
    data = data[-371:]
    
    palette = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    
    width = 800
    height = 120
    box_size = 10
    gap = 3
    
    svg = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style> .box { rx: 2; ry: 2; } </style>')
    
    for i, day in enumerate(data):
        week = i // 7
        weekday = i % 7
        
        x = week * (box_size + gap)
        y = weekday * (box_size + gap) + 20
        color = palette[day['level']]
        
        delay = (week + weekday) * 0.01
        
        svg.append(f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" class="box" opacity="0">')
        svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay}s" fill="freeze" />')
        svg.append(f'</rect>')
        
    svg.append(f'<text x="0" y="15" fill="#8b949e" font-family="monospace" font-size="12">hussain@github:~$ ./contributions.sh</text>')
    svg.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))

if __name__ == "__main__":
    render_heatmap('data/contributions.json', 'contrib-heatmap.svg')

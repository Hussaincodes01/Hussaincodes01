from xml.sax.saxutils import escape


def make_info_card(output_path):
    data = [
        ("whoami",   "Jiyad Hussain"),
        ("role",     "AI Engineer · B.Tech CS @ Amity '28"),
        ("building", "VayuNetra — methane plumes from orbit"),
        ("research", "Tri-modal fusion · Liquid neural nets"),
        ("latest",   "PSB Hackathon 2026 — Winner"),
        ("rank",     "Amazon ML '26 — #500 of 90K"),
        ("stack",    "PyTorch · LangGraph · ONNX · Next.js"),
        ("off-duty", "cooking · football · gaming"),
        ("status",   "open to remote AI internships"),
    ]

    width, height = 500, 340
    line_height = 27
    top = 92

    svg = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<style>')
    svg.append("  .key { fill: #c8a2ff; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; font-size: 13px; font-weight: bold; }")
    svg.append("  .val { fill: #d6dbe8; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; font-size: 13px; }")
    svg.append("  .prompt { fill: #3ddc97; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; font-size: 14px; font-weight: bold; }")
    svg.append('</style>')

    # window chrome
    svg.append(f'<rect width="{width}" height="{height}" rx="14" fill="#0d1117" stroke="#30363d"/>')
    svg.append(f'<path d="M0 14 A14 14 0 0 1 14 0 H{width - 14} A14 14 0 0 1 {width} 14 V40 H0 Z" fill="#161b22"/>')
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        svg.append(f'<circle cx="{22 + i * 18}" cy="20" r="5.5" fill="{c}"/>')
    svg.append('<text x="250" y="25" text-anchor="middle" class="val" font-size="12" opacity=".6">jiyad — zsh</text>')

    svg.append('<text x="22" y="68" class="prompt">jiyad@github:~$ neofetch --resume'
               '<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0s" fill="freeze"/></text>')

    for i, (key, val) in enumerate(data):
        y = top + i * line_height
        delay = 0.5 + i * 0.15
        svg.append('<g opacity="0">')
        svg.append(f'  <text x="22" y="{y}" class="key">{escape(key)}</text>')
        svg.append(f'  <text x="112" y="{y}" class="val">{escape(val)}</text>')
        svg.append(f'  <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay:.2f}s" fill="freeze"/>')
        svg.append('</g>')

    svg.append('</svg>')

    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))


if __name__ == "__main__":
    make_info_card('info-card.svg')

<svg width="1180" height="610" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<defs>
  <!-- Background gradients -->
  <radialGradient id="bg1l" cx="20%" cy="30%" r="50%">
    <stop offset="0%" stop-color="#DBEAFE" stop-opacity="0.7"/>
    <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bg2l" cx="80%" cy="70%" r="45%">
    <stop offset="0%" stop-color="#CFFAFE" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bg3l" cx="60%" cy="10%" r="40%">
    <stop offset="0%" stop-color="#D1FAE5" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>

  <!-- Accent gradients -->
  <linearGradient id="accentGradL" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="50%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#10B981"/>
    <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite"/>
  </linearGradient>

  <linearGradient id="asciiGradL" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="50%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#2563EB"/>
    <animate attributeName="x2" values="100%;0%;100%" dur="5s" repeatCount="indefinite"/>
  </linearGradient>

  <linearGradient id="borderGradL" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#2563EB" stop-opacity="0.4"/>
    <stop offset="50%" stop-color="#06B6D4" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#10B981" stop-opacity="0.4"/>
    <animate attributeName="x1" values="0%;100%;0%" dur="6s" repeatCount="indefinite"/>
  </linearGradient>

  <linearGradient id="pillGrad1L" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#2563EB" stop-opacity="0.12"/>
    <stop offset="100%" stop-color="#06B6D4" stop-opacity="0.12"/>
  </linearGradient>
  <linearGradient id="pillGrad2L" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.12"/>
    <stop offset="100%" stop-color="#10B981" stop-opacity="0.12"/>
  </linearGradient>

  <!-- Glow filter (softer for light) -->
  <filter id="glowL" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="2.5" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- Clip paths -->
  <clipPath id="mainClipL">
    <rect width="1180" height="610" rx="18"/>
  </clipPath>
  <clipPath id="avatarClipL">
    <circle cx="226" cy="186" r="68"/>
  </clipPath>

  <!-- Scanline pattern (lighter) -->
  <pattern id="scanlinesL" x="0" y="0" width="1" height="3" patternUnits="userSpaceOnUse">
    <rect width="1" height="1" fill="rgba(0,0,0,0.02)"/>
  </pattern>

  <!-- Shadow filter -->
  <filter id="cardShadow">
    <feDropShadow dx="0" dy="2" stdDeviation="8" flood-color="rgba(15,23,42,0.08)"/>
  </filter>
</defs>

<!-- Background -->
<g clip-path="url(#mainClipL)">
  <rect width="1180" height="610" fill="#FFFFFF"/>
  <rect width="1180" height="610" fill="url(#bg1l)"/>
  <rect width="1180" height="610" fill="url(#bg2l)"/>
  <rect width="1180" height="610" fill="url(#bg3l)"/>

  <!-- Animated background orbs (softer) -->
  <circle cx="150" cy="200" r="180" fill="#BFDBFE" opacity="0.4">
    <animate attributeName="r" values="180;220;180" dur="7s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0.6;0.4" dur="7s" repeatCount="indefinite"/>
  </circle>
  <circle cx="950" cy="400" r="200" fill="#A5F3FC" opacity="0.3">
    <animate attributeName="r" values="200;160;200" dur="9s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="100" r="150" fill="#A7F3D0" opacity="0.3">
    <animate attributeName="r" values="150;190;150" dur="11s" repeatCount="indefinite"/>
  </circle>

  <!-- Floating particles (light, subtle) -->
  <circle cx="80" cy="80" r="2" fill="#93C5FD" opacity="0.6">
    <animate attributeName="opacity" values="0.6;0.1;0.6" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="cy" values="80;60;80" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1100" cy="150" r="1.5" fill="#67E8F9" opacity="0.5">
    <animate attributeName="opacity" values="0.5;0.1;0.5" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="600" cy="550" r="1.5" fill="#6EE7B7" opacity="0.4">
    <animate attributeName="opacity" values="0.4;0.1;0.4" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="cy" values="550;530;550" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="850" cy="50" r="1.5" fill="#93C5FD" opacity="0.5">
    <animate attributeName="opacity" values="0.5;0.1;0.5" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- Scanline overlay -->
  <rect width="1180" height="610" fill="url(#scanlinesL)" opacity="1"/>

  <!-- Moving scanline sweep -->
  <rect width="1180" height="1.5" fill="rgba(37,99,235,0.04)" y="-2">
    <animate attributeName="y" values="-2;612;-2" dur="6s" repeatCount="indefinite"/>
  </rect>

  <!-- ═══════ LEFT PANEL ═══════ -->
  <rect x="20" y="20" width="430" height="570" rx="14" fill="rgba(248,250,252,0.92)" stroke="url(#borderGradL)" stroke-width="1" filter="url(#cardShadow)"/>

  <!-- Glass reflection sheen -->
  <rect x="20" y="20" width="430" height="80" rx="14" fill="rgba(255,255,255,0.7)"/>
  <rect x="20" y="20" width="2" height="570" rx="1" fill="rgba(255,255,255,0.9)"/>

  <!-- Avatar glow ring -->
  <circle cx="226" cy="186" r="76" fill="none" stroke="url(#accentGradL)" stroke-width="2" opacity="0.6">
    <animate attributeName="r" values="76;80;76" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0.3;0.6" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="226" cy="186" r="72" fill="none" stroke="url(#asciiGradL)" stroke-width="1" opacity="0.4">
    <animate attributeName="r" values="72;74;72" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- Avatar image -->
  <image href="https://avatars.githubusercontent.com/u/129209917?v=4" x="158" y="118" width="136" height="136" clip-path="url(#avatarClipL)" preserveAspectRatio="xMidYMid slice"/>
  <!-- Avatar overlay shimmer (light, very subtle) -->
  <circle cx="226" cy="186" r="68" fill="url(#asciiGradL)" opacity="0.03"/>

  <!-- Online indicator -->
  <circle cx="280" cy="238" r="10" fill="#F8FAFC"/>
  <circle cx="280" cy="238" r="7" fill="#10B981">
    <animate attributeName="r" values="7;9;7" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.6;1" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- Name -->
  <text x="235" y="298" text-anchor="middle" fill="url(#accentGradL)" font-family="'Courier New', monospace" font-size="22" font-weight="700" letter-spacing="3" filter="url(#glowL)">JIYAD HUSSAIN</text>

  <!-- Tagline -->
  <text x="235" y="326" text-anchor="middle" fill="#475569" font-family="'Courier New', monospace" font-size="12" letter-spacing="1">
    <tspan fill="#059669">▸ </tspan>
    <tspan>ML Engineer</tspan>
    <tspan fill="#0891B2"> · </tspan>
    <tspan>AI Researcher</tspan>
    <tspan fill="#2563EB"> · </tspan>
    <tspan>Builder</tspan>
  </text>

  <!-- Divider line -->
  <line x1="60" y1="345" x2="410" y2="345" stroke="url(#accentGradL)" stroke-width="0.5" opacity="0.5"/>

  <!-- ASCII Art Block -->
  <text x="235" y="370" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" opacity="0" filter="url(#glowL)">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.1s" fill="freeze"/>
    ██╗██╗██╗   ██╗ █████╗ ██████╗
  </text>
  <text x="235" y="383" text-anchor="middle" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" opacity="0" filter="url(#glowL)">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.3s" fill="freeze"/>
    ╚═╝╚═╝╚██╗ ██╔╝██╔══██╗██╔══██╗
  </text>
  <text x="235" y="396" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.6s" fill="freeze"/>
       ╚████╔╝ ███████║██║  ██║
  </text>
  <text x="235" y="409" text-anchor="middle" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.9s" fill="freeze"/>
        ╚██╔╝  ██╔══██║██║  ██║
  </text>
  <text x="235" y="422" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.2s" fill="freeze"/>
         ██║   ██║  ██║██████╔╝
  </text>
  <text x="235" y="435" text-anchor="middle" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.5s" fill="freeze"/>
         ╚═╝   ╚═╝  ╚═╝╚═════╝
  </text>

  <!-- Floating animation -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2s" fill="freeze"/>
    <g>
      <animateTransform attributeName="transform" type="translate" values="0,0;0,-4;0,0" dur="4s" repeatCount="indefinite"/>
      <text x="235" y="460" text-anchor="middle" fill="#475569" font-family="'Courier New', monospace" font-size="9" letter-spacing="2">{ AI · ML · CV · NLP }</text>
    </g>
  </g>

  <!-- Social links -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.5s" fill="freeze"/>
    <rect x="90" y="480" width="100" height="28" rx="14" fill="rgba(37,99,235,0.1)" stroke="rgba(37,99,235,0.3)" stroke-width="0.8"/>
    <text x="140" y="499" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" font-weight="600">⌂ GitHub</text>

    <rect x="205" y="480" width="100" height="28" rx="14" fill="rgba(6,182,212,0.1)" stroke="rgba(6,182,212,0.3)" stroke-width="0.8"/>
    <text x="255" y="499" text-anchor="middle" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" font-weight="600">in LinkedIn</text>

    <rect x="315" y="480" width="100" height="28" rx="14" fill="rgba(16,185,129,0.1)" stroke="rgba(16,185,129,0.3)" stroke-width="0.8"/>
    <text x="365" y="499" text-anchor="middle" fill="#059669" font-family="'Courier New', monospace" font-size="10" font-weight="600">✉ Email</text>
  </g>

  <!-- Cursor blink -->
  <rect x="190" y="524" width="8" height="14" rx="1" fill="#2563EB">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>

  <!-- ═══════ RIGHT PANEL ═══════ -->
  <rect x="468" y="20" width="692" height="570" rx="14" fill="rgba(248,250,252,0.95)" stroke="url(#borderGradL)" stroke-width="1" filter="url(#cardShadow)"/>

  <!-- Glass reflection -->
  <rect x="468" y="20" width="692" height="60" rx="14" fill="rgba(255,255,255,0.8)"/>
  <rect x="468" y="20" width="2" height="570" fill="rgba(255,255,255,0.9)"/>

  <!-- Terminal title bar -->
  <rect x="468" y="20" width="692" height="38" rx="14" fill="rgba(241,245,249,0.95)"/>
  <rect x="468" y="40" width="692" height="18" fill="rgba(241,245,249,0.95)"/>

  <!-- Traffic lights -->
  <circle cx="494" cy="39" r="5.5" fill="#FF5F57"/>
  <circle cx="514" cy="39" r="5.5" fill="#FFBD2E"/>
  <circle cx="534" cy="39" r="5.5" fill="#28C840"/>

  <!-- Terminal title -->
  <text x="860" y="43" text-anchor="middle" fill="#94A3B8" font-family="'Courier New', monospace" font-size="11">jiyad@exonet:~/portfolio</text>

  <!-- Terminal divider -->
  <line x1="468" y1="58" x2="1160" y2="58" stroke="rgba(15,23,42,0.08)" stroke-width="1"/>

  <!-- GREETING -->
  <text x="494" y="90" fill="#64748B" font-family="'Courier New', monospace" font-size="12" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.2s" fill="freeze"/>
    <tspan fill="#059669">❯</tspan>  whoami
  </text>

  <!-- Animated greeting -->
  <text x="494" y="120" font-family="'Courier New', monospace" font-size="20" font-weight="700" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.6s" fill="freeze"/>
    <tspan fill="#0F172A">Hi </tspan><tspan fill="#0891B2">👋</tspan><tspan fill="#0F172A">  I'm </tspan><tspan fill="url(#accentGradL)">Jiyad Hussain</tspan>
  </text>

  <!-- Typing roles -->
  <text x="494" y="148" font-family="'Courier New', monospace" font-size="13" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1s" fill="freeze"/>
    <tspan fill="#2563EB">▸ </tspan><tspan fill="#475569">AI/ML Engineer</tspan>
    <tspan dx="8" fill="#0891B2">·</tspan>
    <tspan dx="8" fill="#475569">Deep Learning Researcher</tspan>
    <tspan dx="8" fill="#059669">·</tspan>
    <tspan dx="8" fill="#475569">Kaggler</tspan>
    <tspan fill="#0891B2">
      <animate attributeName="fill" values="#0891B2;transparent;#0891B2" dur="0.8s" repeatCount="indefinite" begin="1.5s"/>
    </tspan>
  </text>

  <!-- SECTION: Info -->
  <text x="494" y="180" fill="#64748B" font-family="'Courier New', monospace" font-size="11" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.2s" fill="freeze"/>
    <tspan fill="#059669">❯</tspan>  cat info.json
  </text>

  <!-- Info cards row -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.4s" fill="freeze"/>
    <rect x="494" y="194" width="148" height="42" rx="8" fill="rgba(37,99,235,0.06)" stroke="rgba(37,99,235,0.2)" stroke-width="0.8"/>
    <text x="568" y="211" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="9" font-weight="600" letter-spacing="1">LOCATION</text>
    <text x="568" y="228" text-anchor="middle" fill="#0F172A" font-family="'Courier New', monospace" font-size="10">📍 New Delhi, India</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.6s" fill="freeze"/>
    <rect x="652" y="194" width="148" height="42" rx="8" fill="rgba(6,182,212,0.06)" stroke="rgba(6,182,212,0.2)" stroke-width="0.8"/>
    <text x="726" y="211" text-anchor="middle" fill="#0891B2" font-family="'Courier New', monospace" font-size="9" font-weight="600" letter-spacing="1">EDUCATION</text>
    <text x="726" y="228" text-anchor="middle" fill="#0F172A" font-family="'Courier New', monospace" font-size="10">🎓 Amity Univ, 2028</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.8s" fill="freeze"/>
    <rect x="810" y="194" width="148" height="42" rx="8" fill="rgba(16,185,129,0.06)" stroke="rgba(16,185,129,0.2)" stroke-width="0.8"/>
    <text x="884" y="211" text-anchor="middle" fill="#059669" font-family="'Courier New', monospace" font-size="9" font-weight="600" letter-spacing="1">FOCUS</text>
    <text x="884" y="228" text-anchor="middle" fill="#0F172A" font-family="'Courier New', monospace" font-size="10">🎯 Exoplanet AI · ISRO</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="2s" fill="freeze"/>
    <rect x="968" y="194" width="148" height="42" rx="8" fill="rgba(37,99,235,0.06)" stroke="rgba(37,99,235,0.2)" stroke-width="0.8"/>
    <text x="1042" y="211" text-anchor="middle" fill="#2563EB" font-family="'Courier New', monospace" font-size="9" font-weight="600" letter-spacing="1">ACHIEVEMENT</text>
    <text x="1042" y="228" text-anchor="middle" fill="#0F172A" font-family="'Courier New', monospace" font-size="10">🏆 CGPA 8.0 · Kaggle T10</text>
  </g>

  <!-- Projects -->
  <text x="494" y="262" fill="#64748B" font-family="'Courier New', monospace" font-size="11" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="2.0s" fill="freeze"/>
    <tspan fill="#059669">❯</tspan>  ls ~/projects/
  </text>

  <!-- Project cards -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.2s" fill="freeze"/>
    <rect x="494" y="276" width="188" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8" filter="url(#cardShadow)"/>
    <rect x="494" y="276" width="188" height="3" rx="1" fill="url(#accentGradL)"/>
    <text x="508" y="296" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" font-weight="700">PCB-Defect-Detection</text>
    <text x="508" y="311" fill="#64748B" font-family="'Courier New', monospace" font-size="9">YOLOv5 · Tri-modal · Attn</text>
    <text x="508" y="325" fill="#059669" font-family="'Courier New', monospace" font-size="9">▸ Ongoing · Python</text>
    <text x="660" y="340" fill="#94A3B8" font-family="'Courier New', monospace" font-size="9">★ 1</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.4s" fill="freeze"/>
    <rect x="692" y="276" width="188" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(6,182,212,0.25)" stroke-width="0.8" filter="url(#cardShadow)"/>
    <rect x="692" y="276" width="188" height="3" rx="1" fill="url(#pillGrad2L)"/>
    <text x="706" y="296" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" font-weight="700">Extremism-Detection</text>
    <text x="706" y="311" fill="#64748B" font-family="'Courier New', monospace" font-size="9">NLP · XGBoost · TF-IDF</text>
    <text x="706" y="325" fill="#059669" font-family="'Courier New', monospace" font-size="9">▸ Top 10 Kaggle · Python</text>
    <text x="858" y="340" fill="#94A3B8" font-family="'Courier New', monospace" font-size="9">★ 1</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.6s" fill="freeze"/>
    <rect x="890" y="276" width="230" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(16,185,129,0.35)" stroke-width="1" filter="url(#cardShadow)"/>
    <rect x="890" y="276" width="230" height="3" rx="1" fill="url(#pillGrad2L)"/>
    <rect x="890" y="276" width="230" height="72" rx="10" fill="none" stroke="rgba(16,185,129,0.2)" stroke-width="3">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </rect>
    <text x="904" y="296" fill="#059669" font-family="'Courier New', monospace" font-size="10" font-weight="700">ExoTransitNet  ✦ ISRO</text>
    <text x="904" y="311" fill="#64748B" font-family="'Courier New', monospace" font-size="9">CNN+BiLSTM · Kepler/TESS</text>
    <text x="904" y="325" fill="#0891B2" font-family="'Courier New', monospace" font-size="9">▸ Hackathon 2026 · Active</text>
    <text x="1082" y="340" fill="#94A3B8" font-family="'Courier New', monospace" font-size="9">🚀</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.8s" fill="freeze"/>
    <rect x="494" y="358" width="188" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(37,99,235,0.2)" stroke-width="0.8" filter="url(#cardShadow)"/>
    <rect x="494" y="358" width="188" height="3" rx="1" fill="url(#pillGrad1L)"/>
    <text x="508" y="378" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" font-weight="700">HackPair</text>
    <text x="508" y="393" fill="#64748B" font-family="'Courier New', monospace" font-size="9">VS Code Ext · TypeScript</text>
    <text x="508" y="407" fill="#059669" font-family="'Courier New', monospace" font-size="9">▸ Real-time Collab · ★ 1</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="3.0s" fill="freeze"/>
    <rect x="692" y="358" width="188" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(6,182,212,0.2)" stroke-width="0.8" filter="url(#cardShadow)"/>
    <rect x="692" y="358" width="188" height="3" rx="1" fill="url(#pillGrad2L)"/>
    <text x="706" y="378" fill="#0891B2" font-family="'Courier New', monospace" font-size="10" font-weight="700">Akkadian-Translation</text>
    <text x="706" y="393" fill="#64748B" font-family="'Courier New', monospace" font-size="9">ByT5 · HuggingFace · NLP</text>
    <text x="706" y="407" fill="#059669" font-family="'Courier New', monospace" font-size="9">▸ chrF++ 35+ · Kaggle</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="3.2s" fill="freeze"/>
    <rect x="890" y="358" width="230" height="72" rx="10" fill="rgba(248,250,252,0.95)" stroke="rgba(37,99,235,0.2)" stroke-width="0.8" filter="url(#cardShadow)"/>
    <rect x="890" y="358" width="230" height="3" rx="1" fill="url(#pillGrad1L)"/>
    <text x="904" y="378" fill="#2563EB" font-family="'Courier New', monospace" font-size="10" font-weight="700">AI-vs-Human-Text</text>
    <text x="904" y="393" fill="#64748B" font-family="'Courier New', monospace" font-size="9">DeBERTa-Large · Classifier</text>
    <text x="904" y="407" fill="#059669" font-family="'Courier New', monospace" font-size="9">▸ HC3 · WikiText-103</text>
  </g>

  <!-- Skills -->
  <text x="494" y="452" fill="#64748B" font-family="'Courier New', monospace" font-size="11" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="3.2s" fill="freeze"/>
    <tspan fill="#059669">❯</tspan>  cat skills.txt
  </text>

  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="3.4s" fill="freeze"/>
    <rect x="494" y="462" width="70" height="22" rx="11" fill="url(#pillGrad1L)" stroke="rgba(37,99,235,0.3)" stroke-width="0.8"/>
    <text x="529" y="477" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">PyTorch</text>
    <rect x="572" y="462" width="82" height="22" rx="11" fill="url(#pillGrad2L)" stroke="rgba(6,182,212,0.3)" stroke-width="0.8"/>
    <text x="613" y="477" text-anchor="middle" fill="#0E7490" font-family="'Courier New', monospace" font-size="9" font-weight="600">TensorFlow</text>
    <rect x="662" y="462" width="92" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="708" y="477" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">HuggingFace</text>
    <rect x="762" y="462" width="70" height="22" rx="11" fill="rgba(16,185,129,0.08)" stroke="rgba(16,185,129,0.3)" stroke-width="0.8"/>
    <text x="797" y="477" text-anchor="middle" fill="#065F46" font-family="'Courier New', monospace" font-size="9" font-weight="600">OpenCV</text>
    <rect x="840" y="462" width="64" height="22" rx="11" fill="rgba(6,182,212,0.07)" stroke="rgba(6,182,212,0.3)" stroke-width="0.8"/>
    <text x="872" y="477" text-anchor="middle" fill="#0E7490" font-family="'Courier New', monospace" font-size="9" font-weight="600">FastAPI</text>
    <rect x="912" y="462" width="60" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="942" y="477" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">Docker</text>
    <rect x="980" y="462" width="56" height="22" rx="11" fill="rgba(16,185,129,0.07)" stroke="rgba(16,185,129,0.3)" stroke-width="0.8"/>
    <text x="1008" y="477" text-anchor="middle" fill="#065F46" font-family="'Courier New', monospace" font-size="9" font-weight="600">W&amp;B</text>
    <rect x="1044" y="462" width="44" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="1066" y="477" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">Git</text>
    <rect x="1096" y="462" width="52" height="22" rx="11" fill="rgba(6,182,212,0.07)" stroke="rgba(6,182,212,0.25)" stroke-width="0.8"/>
    <text x="1122" y="477" text-anchor="middle" fill="#0E7490" font-family="'Courier New', monospace" font-size="9" font-weight="600">ONNX</text>
  </g>

  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="3.6s" fill="freeze"/>
    <rect x="494" y="492" width="72" height="22" rx="11" fill="rgba(16,185,129,0.07)" stroke="rgba(16,185,129,0.25)" stroke-width="0.8"/>
    <text x="530" y="507" text-anchor="middle" fill="#065F46" font-family="'Courier New', monospace" font-size="9" font-weight="600">Scikit-Learn</text>
    <rect x="574" y="492" width="62" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="605" y="507" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">XGBoost</text>
    <rect x="644" y="492" width="58" height="22" rx="11" fill="rgba(6,182,212,0.07)" stroke="rgba(6,182,212,0.25)" stroke-width="0.8"/>
    <text x="673" y="507" text-anchor="middle" fill="#0E7490" font-family="'Courier New', monospace" font-size="9" font-weight="600">Pandas</text>
    <rect x="710" y="492" width="56" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="738" y="507" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">NumPy</text>
    <rect x="774" y="492" width="66" height="22" rx="11" fill="rgba(16,185,129,0.07)" stroke="rgba(16,185,129,0.25)" stroke-width="0.8"/>
    <text x="807" y="507" text-anchor="middle" fill="#065F46" font-family="'Courier New', monospace" font-size="9" font-weight="600">Streamlit</text>
    <rect x="848" y="492" width="60" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="878" y="507" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">MLflow</text>
    <rect x="916" y="492" width="68" height="22" rx="11" fill="rgba(6,182,212,0.07)" stroke="rgba(6,182,212,0.25)" stroke-width="0.8"/>
    <text x="950" y="507" text-anchor="middle" fill="#0E7490" font-family="'Courier New', monospace" font-size="9" font-weight="600">Kubernetes</text>
    <rect x="992" y="492" width="62" height="22" rx="11" fill="rgba(16,185,129,0.07)" stroke="rgba(16,185,129,0.25)" stroke-width="0.8"/>
    <text x="1023" y="507" text-anchor="middle" fill="#065F46" font-family="'Courier New', monospace" font-size="9" font-weight="600">lightkurve</text>
    <rect x="1062" y="492" width="82" height="22" rx="11" fill="rgba(37,99,235,0.07)" stroke="rgba(37,99,235,0.25)" stroke-width="0.8"/>
    <text x="1103" y="507" text-anchor="middle" fill="#1D4ED8" font-family="'Courier New', monospace" font-size="9" font-weight="600">Transformers</text>
  </g>

  <!-- Bottom status bar -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="3.8s" fill="freeze"/>
    <rect x="468" y="552" width="692" height="38" rx="0" fill="rgba(37,99,235,0.06)" stroke="none"/>
    <rect x="468" y="552" width="692" height="1" rx="0" fill="rgba(37,99,235,0.15)"/>
    <rect x="468" y="584" width="692" height="6" rx="0" fill="rgba(248,250,252,1)"/>
    <text x="484" y="575" fill="#2563EB" font-family="'Courier New', monospace" font-size="10">●</text>
    <text x="498" y="575" fill="#64748B" font-family="'Courier New', monospace" font-size="10">main</text>
    <text x="548" y="575" fill="#CBD5E1" font-family="'Courier New', monospace" font-size="10">|</text>
    <text x="560" y="575" fill="#64748B" font-family="'Courier New', monospace" font-size="10">Python</text>
    <text x="614" y="575" fill="#CBD5E1" font-family="'Courier New', monospace" font-size="10">|</text>
    <text x="626" y="575" fill="#64748B" font-family="'Courier New', monospace" font-size="10">UTF-8</text>
    <text x="920" y="575" fill="#64748B" font-family="'Courier New', monospace" font-size="10">NVIDIA DL Cert</text>
    <text x="1020" y="575" fill="#CBD5E1" font-family="'Courier New', monospace" font-size="10">|</text>
    <text x="1032" y="575" fill="#059669" font-family="'Courier New', monospace" font-size="10">● Active</text>
    <circle cx="1130" cy="571" r="4" fill="#0891B2">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <text x="1142" y="575" fill="#0891B2" font-family="'Courier New', monospace" font-size="10">LIVE</text>
  </g>

  <!-- Border shimmer -->
  <rect width="1180" height="610" rx="18" fill="none" stroke="url(#borderGradL)" stroke-width="1.5" opacity="0.8"/>
  <rect width="1180" height="610" rx="18" fill="none" stroke="url(#borderGradL)" stroke-width="4" opacity="0.08"/>

</g>
</svg>

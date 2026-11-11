from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
THEMES = {
    'dark': dict(bg='#101b25', grid='#20313f', ink='#eef3f4', muted='#a9bdc8', accent='#71d6bb', secondary='#aebdf0'),
    'light': dict(bg='#f5f8f6', grid='#e2eae5', ink='#182d30', muted='#52696c', accent='#16775f', secondary='#5564a3'),
}

def artwork(width, height, body, title, p):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">
<defs><pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="{p['grid']}" stroke-width="1"/></pattern></defs>
<rect width="{width}" height="{height}" rx="16" fill="{p['bg']}"/>
<rect width="{width}" height="{height}" rx="16" fill="url(#grid)"/>
<g font-family="DejaVu Sans, sans-serif">{body}</g></svg>'''

cards = [
    ('neuronest', '01', 'Neuronest', 'MEMORY & CARE', '<circle cx="14" cy="25" r="7"/><circle cx="42" cy="12" r="6"/><circle cx="44" cy="43" r="8"/><path d="M21 22L36 15M20 30L37 39M43 18V35"/>'),
    ('visus', '02', 'Visus', 'ASSISTIVE VISION', '<path d="M0 28Q28-4 56 28Q28 60 0 28Z"/><circle cx="28" cy="28" r="11"/>'),
    ('healthocare', '03', 'Healthocare', 'HEALTH AT HOME', '<rect x="1" y="7" width="54" height="43" rx="7"/><path d="M8 29H18L24 17L32 40L39 26H49"/>'),
    ('autoclean', '04', 'Autoclean', 'GESTURE & ROBOTICS', '<path d="M12 18H44L41 48H15ZM8 18H48M21 10H35M23 27V39M33 27V39"/>'),
    ('tech-ai', '05', 'Tech AI', 'ATL LAB ASSISTANT', '<rect x="1" y="5" width="54" height="35" rx="4"/><path d="M28 40V52M16 52H40M12 17H44M12 27H33"/>'),
    ('little-builds', '06', 'Small experiments', 'SENSORS & EVERYDAY CARE', '<path d="M10 40H46L41 32V20Q28 4 15 20V32ZM22 47Q28 56 34 47M28 6V1"/>'),
]
for mode, p in THEMES.items():
    banner = f'''
<path d="M650 0V44L685 79H920M920 191H840L810 161H754M728 240V210L694 176H650" fill="none" stroke="{p['accent']}" stroke-width="2" opacity=".45"/>
<g fill="{p['accent']}"><circle cx="754" cy="161" r="4"/><circle cx="650" cy="176" r="4"/><circle cx="685" cy="79" r="4"/></g>
<text x="36" y="42" fill="{p['accent']}" font-family="monospace" font-size="12" letter-spacing="2">CHRIS / BUILDS &amp; EXPERIMENTS</text>
<text x="33" y="112" fill="{p['ink']}" font-size="53" font-weight="bold" letter-spacing="-2">Chris V Jacob</text>
<text x="36" y="151" fill="{p['muted']}" font-size="19">Curiosity, connected.</text>
<text x="36" y="203" fill="{p['accent']}" font-family="monospace" font-size="13">ESP32  /  ARDUINO  /  IoT  /  ASSISTIVE TECH</text>
<g transform="translate(742 95)" fill="none" stroke="{p['secondary']}" stroke-width="2" opacity=".7">
<rect width="65" height="65" rx="9"/><rect x="13" y="13" width="39" height="39" rx="3"/>
<path d="M13-10V0M26-10V0M39-10V0M52-10V0M13 65V75M26 65V75M39 65V75M52 65V75M-10 13H0M-10 26H0M-10 39H0M-10 52H0M65 13H75M65 26H75M65 39H75M65 52H75"/>
</g>'''
    (ASSETS / f'banner-{mode}.svg').write_text(artwork(920, 240, banner, 'Chris V Jacob. Curiosity, connected.', p))
    for slug, number, title, label, icon in cards:
        body = f'''
<text x="20" y="27" fill="{p['accent']}" font-family="monospace" font-size="10" letter-spacing="1">{number} / {escape(label)}</text>
<text x="19" y="66" fill="{p['ink']}" font-size="25" font-weight="bold" letter-spacing="-.6">{escape(title)}</text>
<path d="M20 86H316" stroke="{p['grid']}" stroke-width="2"/>
<g transform="translate(376 24)" fill="none" stroke="{p['accent']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'''
        (ASSETS / f'{slug}-{mode}.svg').write_text(artwork(460, 104, body, title + ': ' + label.lower(), p))

def picture(slug, alt):
    return f'''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/{slug}-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/{slug}-light.svg">
  <img src="assets/{slug}-light.svg" alt="{alt}" width="100%">
</picture>'''

projects = [
    ('neuronest', 'Neuronest: Mitra and Mnemo', '<b>Mitra</b> supports later-stage memory care; <b>Mnemo</b> focuses on earlier stages. Building both with <a href="https://github.com/akshay-abraham">Akshay Abraham</a>.'),
    ('visus', 'Visus: assistive vision', 'Exploring navigation assistance for blind people using a phone camera and <b>YOLO</b>, plus motion sensors for possible fall detection and shared alerts.'),
    ('healthocare', 'Healthocare: health at home', 'Home health monitoring with <b>ECG, weight, and other sensors</b>, sending readings to a guardian’s phone.'),
    ('autoclean', 'Autoclean: robotics and classroom assistance', 'A waste bin that comes over when you <b>raise your hand</b>. Also explores possible copying detection, teacher notifications, <b>voice interaction, and USB recording</b>.'),
    ('tech-ai', 'Tech AI: ATL lab assistant', 'An <b>AI assistant for the ATL lab</b>: helps locate components, explains their uses, recommends projects, and acts as a mentor while students build.'),
    ('little-builds', 'Small experiments: sensors and everyday care', 'A <b>touch sensor alert system for elderly people</b>, alongside smaller sensor builds and everyday experiments.'),
]
readme = picture('banner', 'Chris V Jacob. Curiosity, connected. ESP32, Arduino, IoT and assistive technology.') + '''

I'm Chris, a student who likes turning “what if?” into something you can try. I build with **ESP32, Arduino, and IoT**, with hands-on experience in an **Atal Tinkering Lab (ATL)**.

### On my workbench

<table>
'''
for i, (slug, alt, description) in enumerate(projects):
    if i % 2 == 0:
        readme += '<tr>\n'
    readme += '<td width="50%" valign="top">\n' + picture(slug, alt) + '\n<p>' + description + '</p>\n</td>\n'
    if i % 2 == 1:
        readme += '</tr>\n'
readme += '''</table>

### Beyond the workbench

**HackTVM Access Point · 2026** — First by points in the round with Akshay; advanced to Phase 2 with Mitra & Mnemo.

**Hack4Future** · Semifinalist &nbsp; / &nbsp; **SAMEEKSHA** · Consolation prize with my team

<details>
<summary>Expos &amp; events</summary>

A few more stops along the way:

- **CBSE Skill Expo** · 2026–27
- **Sahodaya Innovation** · 2K24
- **Innovators League** · 2K26, Mar Baselios
- **Mini EV** · 3.0

</details>

<sub>Always up for an idea that needs a sensor.</sub>
'''
(ROOT / 'README.md').write_text(readme)
print('Generated compact README and 14 theme-aware SVG assets.')

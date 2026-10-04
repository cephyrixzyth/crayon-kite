from html import escape
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[1] / "dist" / "assets" / "free-coloring"

PAGES = [
    ("01-hello-chirps.svg", "Hello, Chirps!", "The whole budgie family says hello.", "sun"),
    ("02-birdhouse-home.svg", "Birdhouse Home", "A little house for the feathered friends.", "house"),
    ("03-flower-garden.svg", "Flower Garden", "Big flowers and little bird friends.", "flowers"),
    ("04-seed-snack.svg", "Seed Snack", "The family gathers for a tiny snack.", "bowl"),
    ("05-swing-time.svg", "Swing Time", "Take turns on the garden swing.", "swing"),
    ("06-cloud-watchers.svg", "Cloud Watchers", "What shapes can you spot in the sky?", "clouds"),
    ("07-pond-friend.svg", "Pond Friend", "A duckling stops by to say hello.", "pond"),
    ("08-feather-trail.svg", "Feather Trail", "Follow the feathers across the page.", "feathers"),
    ("09-garden-picnic.svg", "Garden Picnic", "A blanket, a few treats, and the Chirps.", "picnic"),
    ("10-sky-song.svg", "Sky Song", "Sing a tune with the birds.", "song"),
]


def bird(x, y, scale, name, pose="perch", face_left=False):
    """One friendly, recognizable budgie, with family-specific markings and pose."""
    flip = "translate(200 0) scale(-1 1)" if face_left else ""
    tilt = {"curious": "rotate(-9 100 150)", "peck": "rotate(10 100 150)", "flight": "rotate(-16 100 150)", "glide": "rotate(8 100 150)", "swing": "rotate(7 100 150)"}.get(pose, "")
    wing = (
        "M59 132C39 115 34 77 38 51c27 12 49 41 57 70 4 15-5 34-22 45z"
        if pose in ("flap", "flight", "glide", "wave") else
        "M61 125C45 125 45 154 56 177c14 23 47 24 69 6 13-11 15-28 5-43-15-20-47-28-69-15z"
    )
    feathers = (
        "M50 69q12-11 24-3m-21 12q13-10 27-3m-21 12q13-9 27-2"
        if name == "Chip" else
        "M49 59q13-11 26-2m-29 12q13-10 28-2m-29 12q13-9 28-2"
    )
    identity = {
        "Daisy": '<path d="M77 27q6-19 17-11 7-21 19-4 13-11 18 9"/><path d="M86 151q14-16 28 0t-14 26q-28-10-14-26z"/>',
        "Chip": '<path d="m75 37 12-13 8 12 14-14 14 17"/>',
        "Caty": '<path d="M127 104c-8-10-22-1-13 9l13 12 13-12c9-10-5-19-13-9z"/><path d="M73 40q10-9 20-2m-18 10q10-8 20-2"/>',
        "Bella": '<path d="m100 40 4 10 11 1-8 7 3 11-10-6-9 6 2-11-8-7 11-1z"/>',
    }[name]
    pose_detail = {
        "perch": "",
        "curious": '<path d="M115 91q9-7 17 0"/>',
        "peck": '<path d="M84 96q8 7 15 0"/>',
        "flap": '<path d="M77 160q17-17 36 0m-31 11q14-12 28 0"/>',
        "flight": '<path d="M77 160q17-17 36 0m-31 11q14-12 28 0"/>',
        "glide": '<path d="M77 160q17-17 36 0m-31 11q14-12 28 0"/>',
        "wave": '<path d="M77 160q17-17 36 0m-31 11q14-12 28 0"/>',
        "swing": "",
        "sit": '<path d="M73 207q27 15 54 0"/>',
    }[pose]
    feet = "" if pose in ("flight", "glide") else '<path d="M82 207v15m0 0q-9 0-14 8m14-8q8 0 12 8m18-8v-15m0 15q-9 0-14 8m14-8q8 0 12 8"/>'
    details = "\n".join(f"        {part}" for part in (identity, pose_detail, feet) if part)
    return f'''<g transform="translate({x} {y}) scale({scale}) {tilt} {flip}">
      <g class="ink">
        <path class="white" d="M68 105C47 89 43 56 59 34 76 11 112 13 132 34c20 21 20 49 5 71 17 24 20 55 9 83-11 27-30 39-51 39-27 0-47-17-54-43-8-29-2-57 12-79z"/>
        <path class="white" d="M58 169c-19 14-31 34-43 51 28-4 49-16 66-34z"/>
        <path d="M53 190 23 218m39-23-23 24"/>
        <path class="white" d="{wing}"/>
        <path d="M59 141q24-24 52-9m-48 22q22-20 49-9m-44 23q19-15 39-10"/>
        <path class="white" d="M80 61c7-18 32-20 43-5 10 14 3 34-12 39-17 5-34-15-31-34z"/>
        <circle class="dot" cx="108" cy="72" r="7"/><circle class="white" cx="110" cy="69" r="2.3"/>
        <path class="white" d="M122 82q15-7 21 2l-11 17q-11-3-10-19z"/><circle class="dot" cx="132" cy="84" r="2"/>
        <path d="M67 89q10-9 19 0m-22 8q10-8 20 0"/>
        <circle class="dot" cx="72" cy="108" r="4"/><circle class="dot" cx="83" cy="113" r="4"/><circle class="dot" cx="67" cy="119" r="3.5"/>
        <path d="{feathers}"/>
{details}
      </g>
    </g>'''


def flower(x, y, scale=1):
    return f'''<g class="ink" transform="translate({x} {y}) scale({scale})">
      <path d="M0 18v55m0-27-20-12m20 23 20-14"/>
      <path class="white" d="M0 0c-9-12-24-1-14 10-14 1-11 18 2 16-4 13 13 17 18 5 10 10 24-2 14-12 13-6 4-22-8-18C10-13-5-12 0 0z"/>
      <circle class="white" cx="4" cy="12" r="9"/>
    </g>'''


def cloud(x, y):
    return f'<g class="ink" transform="translate({x} {y})"><path class="white" d="M0 39c-20 0-26-24-8-32 7-24 41-23 48-3 23-4 32 27 9 35z"/></g>'


def feather(x, y, angle=0):
    return f'''<g class="ink" transform="translate({x} {y}) rotate({angle}) scale(.8)">
      <path class="white" d="M0 62C-10 35 3 7 30 0c7 27-4 50-30 62z"/><path d="M0 62 24 9m-15 34L0 26m8 3-12-12m5 31 19-13"/>
    </g>'''


MOTIFS = {
    "sun": '''<g class="ink"><circle class="white" cx="685" cy="270" r="53"/><path d="M685 187v-30m0 196v-30m83-53h30m-226 0h30m142-58 22-22m-164 164 22-22m120 0 22 22m-164-164 22 22M83 686h684"/></g>''',
    "house": '''<g class="ink"><path class="white" d="M80 520 195 420l115 100v142H80z"/><path d="m65 524 130-116 130 116M97 662V532h196v130m-98-1v-62a30 30 0 0 1 60 0v62"/><circle class="white" cx="195" cy="523" r="25"/><path d="M185 570h20m-10-20v20M75 715h700"/></g>''',
    "flowers": flower(98, 535, 1.2) + flower(710, 520, 1.35) + flower(400, 690, .9) + '<g class="ink"><path d="M75 760h700"/></g>',
    "bowl": '''<g class="ink"><path class="white" d="M292 690q130 150 260 0z"/><path d="M292 690q130 150 260 0m-260 0h260m-226 33h192M80 755h690"/><ellipse class="white" cx="365" cy="683" rx="12" ry="8"/><ellipse class="white" cx="422" cy="674" rx="12" ry="8"/><ellipse class="white" cx="478" cy="684" rx="12" ry="8"/></g>''',
    "swing": '''<g class="ink"><path d="M104 288q318-160 642 0M621 288v294m130-294v294m-149 0h168M75 715q240-18 505 0"/></g>''',
    "clouds": cloud(95, 245) + cloud(620, 245) + '''<g class="ink"><circle class="white" cx="422" cy="250" r="43"/><path d="M422 186v-25m0 178v-25m64-64h25m-178 0h25m109-45 18-18m-126 126 18-18m90 0 18 18m-126-126 18 18M80 710h690"/></g>''',
    "pond": '''<g class="ink"><ellipse class="white" cx="470" cy="750" rx="274" ry="64"/><path d="M250 751q55-28 110 0t110 0 110 0 110 0M75 693h675"/><path class="white" d="M650 662c-5-30 18-51 44-44l30 8c17 5 25 20 18 34-6 14-24 20-43 12l-14-6-22 20-8-24z"/><circle class="dot" cx="715" cy="640" r="3"/><path d="m740 640 24 6-24 7m-38 24-13 20m42-20 3 20"/></g>''',
    "feathers": feather(120, 280, -20) + feather(680, 300, 20) + feather(150, 680, 18) + feather(650, 660, -25) + '<g class="ink" stroke-dasharray="5 13"><path d="M175 360q150-120 270 10t225 6"/></g>',
    "picnic": '''<g class="ink"><path class="white" d="M150 715h550l-45 90H195z"/><path d="m260 715-22 90m115-90-10 90m115-90 4 90m115-90 18 90m-442-60h520m-520 32h504M80 814h690"/><circle class="white" cx="325" cy="680" r="24"/><path d="M325 656q0-22 20-20m97 28c0-18 25-18 25 0v24h-25z"/></g>''',
    "song": cloud(95, 245) + cloud(620, 240) + '''<g class="ink"><circle class="white" cx="422" cy="275" r="44"/><path d="M422 210v-23m0 176v-23m67-65h23m-180 0h23m115-47 17-17m-130 130 17-17m96 0 17 17m-130-130 17 17M180 410v-65l47-10v66m0-66v-25l47-10v62m-94 0q-12 10 0 15t0 13m47-29q-12 10 0 15t0 13M80 710q170-20 340 0t350 0"/></g>''',
}


FAMILY_SCENES = {
    # x, y, size, character, pose, turned toward the left
    "sun": [(88, 457, 1.0, "Chip", "curious", False), (265, 415, 1.18, "Daisy", "perch", False), (470, 457, 1.0, "Caty", "perch", True), (650, 507, .78, "Bella", "wave", False)],
    "house": [(110, 532, .8, "Chip", "curious", False), (345, 513, .88, "Daisy", "perch", False), (500, 523, .84, "Caty", "perch", True), (660, 573, .62, "Bella", "wave", False)],
    "flowers": [(76, 435, .9, "Chip", "flight", False), (250, 460, 1.05, "Daisy", "glide", False), (455, 420, .92, "Caty", "flight", True), (650, 482, .68, "Bella", "glide", False)],
    "bowl": [(130, 484, .9, "Daisy", "peck", False), (300, 461, .9, "Chip", "peck", True), (465, 479, .9, "Caty", "peck", True), (640, 530, .7, "Bella", "peck", True)],
    "swing": [(80, 497, .95, "Chip", "curious", False), (265, 468, 1.08, "Daisy", "perch", False), (450, 497, .95, "Caty", "flap", True), (620, 417, .72, "Bella", "swing", False)],
    "clouds": [(72, 495, .92, "Chip", "curious", False), (255, 470, 1.05, "Daisy", "perch", True), (464, 493, .94, "Caty", "curious", False), (652, 545, .72, "Bella", "flap", True)],
    "pond": [(63, 477, .94, "Daisy", "perch", False), (222, 469, .98, "Chip", "curious", True), (395, 487, .9, "Caty", "peck", False), (548, 537, .68, "Bella", "wave", False)],
    "feathers": [(75, 438, .94, "Chip", "flight", False), (244, 430, 1.0, "Daisy", "flight", False), (445, 440, .94, "Caty", "flight", True), (640, 470, .72, "Bella", "flight", True)],
    "picnic": [(93, 500, .94, "Daisy", "sit", False), (269, 486, 1.0, "Chip", "peck", True), (470, 502, .93, "Caty", "sit", True), (654, 555, .7, "Bella", "peck", False)],
    "song": [(73, 470, .95, "Chip", "flight", False), (257, 470, 1.05, "Daisy", "perch", False), (455, 492, .95, "Caty", "perch", True), (648, 496, .72, "Bella", "flight", False)],
}


def family(kind):
    return "".join(bird(*spec) for spec in FAMILY_SCENES[kind])


def render(filename, title, description, kind):
    title, description = escape(title), escape(description)
    illustration = f"{family(kind)}{MOTIFS[kind]}" if kind == "bowl" else f"{MOTIFS[kind]}{family(kind)}"
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="11in" viewBox="0 0 850 1100" role="img" aria-labelledby="page-title page-desc">
  <title id="page-title">{title} — free Budgie Adventures coloring page</title>
  <desc id="page-desc">{description} Simple black outlines on a white page.</desc>
  <style>
    .ink {{ fill: none; stroke: #111; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
    .white {{ fill: #fff; }} .dot {{ fill: #111; stroke: none; }}
    .title {{ fill: #111; font: 700 38px 'Trebuchet MS', Arial, sans-serif; }}
    .small {{ fill: #111; font: 22px 'Trebuchet MS', Arial, sans-serif; }}
    .tiny {{ fill: #111; font: 15px 'Trebuchet MS', Arial, sans-serif; }}
    @media print {{ @page {{ size: letter portrait; margin: 0; }} svg {{ width: 8.5in; height: 11in; }} }}
  </style>
  <rect x="28" y="28" width="794" height="1044" rx="24" fill="#fff" stroke="#111" stroke-width="3"/>
  <text class="title" x="425" y="100" text-anchor="middle">{title}</text>
  <text class="small" x="425" y="143" text-anchor="middle">{description}</text>
  {illustration}
  <text class="small" x="425" y="914" text-anchor="middle">Color the picture your way!</text>
  <text class="small" x="100" y="1005">My name:</text><path d="M205 1010h330" class="ink" stroke-width="2.5"/>
  <text class="tiny" x="750" y="1038" text-anchor="end">Crayon Kite · free page</text>
</svg>
'''


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for filename, title, description, kind in PAGES:
        (OUTPUT / filename).write_text(render(filename, title, description, kind), encoding="utf-8")
        print(f"Created {filename}")


if __name__ == "__main__":
    main()

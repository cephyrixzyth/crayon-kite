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


def bird(x, y, scale=1):
    return f'''<g class="ink" transform="translate({x} {y}) scale({scale})">
      <path class="white" d="M43 48C19 46 10 68 17 84c6 15 24 23 43 19 22-4 36-18 34-38-2-16-15-25-30-22z"/>
      <circle class="white" cx="63" cy="34" r="25"/>
      <path d="M45 13 37 2l18 11m-2-1L60 0l8 15m-1 0L79 7l-4 16M83 31l20 6-19 8z"/>
      <circle class="dot" cx="70" cy="30" r="3.4"/>
      <path class="white" d="M34 59c9-12 27-16 39-7 8 6 12 18 7 29-12 10-28 13-43 5-7-6-9-17-3-27z"/>
      <path d="M41 63c8-4 17-4 25 0m-26 8c8-3 17-3 25 0m-21 8c7-2 14-2 20 0M25 82 5 111l23-9 17 2-9-21m27 16-2 14m17-18 5 18m-23-1h12m7 0h12"/>
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
    "swing": '''<g class="ink"><path d="M104 288q318-160 642 0m-594-7v306m430-306v306m-451 0h472M95 737h660"/></g>''',
    "clouds": cloud(95, 245) + cloud(620, 245) + '''<g class="ink"><circle class="white" cx="422" cy="250" r="43"/><path d="M422 186v-25m0 178v-25m64-64h25m-178 0h25m109-45 18-18m-126 126 18-18m90 0 18 18m-126-126 18 18M80 710h690"/></g>''',
    "pond": '''<g class="ink"><ellipse class="white" cx="470" cy="750" rx="274" ry="64"/><path d="M250 751q55-28 110 0t110 0 110 0 110 0M75 693h340"/><path class="white" d="M650 662c-5-30 18-51 44-44l30 8c17 5 25 20 18 34-6 14-24 20-43 12l-14-6-22 20-8-24z"/><circle class="dot" cx="715" cy="640" r="3"/><path d="m740 640 24 6-24 7m-38 24-13 20m42-20 3 20"/></g>''',
    "feathers": feather(120, 280, -20) + feather(680, 300, 20) + feather(150, 680, 18) + feather(650, 660, -25) + '<g class="ink" stroke-dasharray="5 13"><path d="M175 360q150-120 270 10t225 6"/></g>',
    "picnic": '''<g class="ink"><path class="white" d="M150 715h550l-45 90H195z"/><path d="m260 715-22 90m115-90-10 90m115-90 4 90m115-90 18 90m-442-60h520m-520 32h504M80 814h690"/><circle class="white" cx="325" cy="680" r="24"/><path d="M325 656q0-22 20-20m97 28c0-18 25-18 25 0v24h-25z"/></g>''',
    "song": cloud(95, 245) + cloud(620, 240) + '''<g class="ink"><circle class="white" cx="422" cy="275" r="44"/><path d="M422 210v-23m0 176v-23m67-65h23m-180 0h23m115-47 17-17m-130 130 17-17m96 0 17 17m-130-130 17 17M180 410v-65l47-10v66m0-66v-25l47-10v62m-94 0q-12 10 0 15t0 13m47-29q-12 10 0 15t0 13"/></g>''',
}


def family(kind):
    points = [(105, 465, 1.4), (255, 430, 1.6), (445, 455, 1.4), (620, 485, 1.15)]
    if kind == "house":
        points = [(350, 460, 1.25), (470, 435, 1.45), (590, 460, 1.25), (700, 495, 1.05)]
    elif kind == "swing":
        points = [(110, 455, 1.2), (250, 425, 1.4), (410, 445, 1.25), (555, 460, 1.05)]
    elif kind == "pond":
        points = [(80, 465, 1.15), (205, 440, 1.4), (370, 460, 1.25), (510, 490, 1.0)]
    return "".join(bird(*point) for point in points)


def render(filename, title, description, kind):
    title, description = escape(title), escape(description)
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
  {MOTIFS[kind]}
  {family(kind)}
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

import os
from pathlib import Path

courses = [
    {
        "slug": "01-ethiopia",
        "origin_key": "ethiopia",
        "num": "01",
        "variant": "bouquet",
        "origin": "Ethiopia Uraga Raro Boda · Pour over",
        "name": "Opening Act",
        "role": "Lift, fragrance, a delicate first impression",
        "notes": ["star jasmine", "earl grey", "bergamot", "limeade", "honeyed finish"],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": None,
        "next": "02-colombia",
    },
    {
        "slug": "02-colombia",
        "origin_key": "colombia",
        "num": "02",
        "variant": "dessert",
        "origin": "Colombia Buesaco · Maricela Ordoñez · Pour over",
        "name": "The Body",
        "role": "Balance, sweetness, a calmer middle",
        "notes": ["caramel", "brown sugar", "green apple", "rose hips", "english breakfast"],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": "01-ethiopia",
        "next": "03-kenya",
    },
    {
        "slug": "03-kenya",
        "origin_key": "kenya",
        "num": "03",
        "variant": "coral",
        "origin": "Kenya Nyeri Karuthi AA · Pour over",
        "name": "The Closer",
        "role": "Tension, brightness, a memorable finish",
        "notes": ["blackcurrant", "tomato", "sparkling acidity", "tea-like finish"],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": "02-colombia",
        "next": "04-yuzu-cooler",
    },
    {
        "slug": "04-yuzu-cooler",
        "origin_key": "yuzu",
        "num": "04",
        "variant": "shop",
        "origin": "Specialty · Citrusy · Batched cold",
        "name": "Yuzu Jasmine Coconut Cooler",
        "role": "Echoes the Ethiopia's jasmine, bergamot, limeade energy",
        "notes": ["bright yuzu", "soft coconut", "jasmine lift"],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "03-kenya",
        "next": "05-cherry-matcha",
    },
    {
        "slug": "05-cherry-matcha",
        "origin_key": "cherry",
        "num": "05",
        "variant": "journal",
        "origin": "Specialty · Floral · Matcha",
        "name": "Cherry Jasmine Matcha",
        "role": "A refined, less obvious fruit expression",
        "notes": ["light matcha", "cherry depth", "jasmine aroma"],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "04-yuzu-cooler",
        "next": "06-nitro-latte",
    },
    {
        "slug": "06-nitro-latte",
        "origin_key": "nitro",
        "num": "06",
        "variant": "caramel",
        "origin": "Specialty · Nitro",
        "name": "Nitro Vanilla Date Latte",
        "role": "A richer counterweight to the Kenya's sharp finish",
        "notes": ["silky nitro", "restrained date", "vanilla lift"],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "05-cherry-matcha",
        "next": None,
    },
]

TOTAL_COURSES = 6

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{theme}">
<title>{name} — Coffee Omakase</title>
<meta name="description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:title" content="{name} — Coffee Omakase">
<meta property="og:description" content="{description}">
<meta property="og:image" content="../assets/apple-touch-icon.png">
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<link rel="stylesheet" href="../styles.css">
</head>
<body>

<main class="course course--{variant} course--origin course--{origin_key}">

  <nav class="course__nav">
    <a href="../index.html" class="course__back">← All courses</a>
    <span class="course__counter">{num} of 06</span>
  </nav>

  <ol class="course__dots" aria-label="Course {num} of 06">
{dots_html}
  </ol>

  <section class="course__hero">

    <div class="course__num">{num}</div>
    <div class="course__origin">{origin}</div>
    <h1 class="course__name">{name}</h1>
    <p class="course__role">{role}</p>

    <div class="course__section">
      <div class="course__label">Tasting notes</div>
      <div class="notes">
{notes_html}
      </div>
    </div>

    <div class="course__section">
      <div class="course__label">Paired with</div>
      {pairing_html}
    </div>

  </section>

  <footer class="course__pager">
    {prev_html}
    {next_html}
  </footer>

</main>

</body>
</html>
"""

theme_map = {
    "coral": "#d97066",
    "bouquet": "#cdc77f",
    "caramel": "#936a2f",
    "journal": "#95ada3",
    "dessert": "#b49c84",
    "shop": "#cbd0af",
}

out_dir = Path(__file__).parent / "courses"
out_dir.mkdir(parents=True, exist_ok=True)

for c in courses:
    notes_html = "\n".join([f'        <span class="note">{n}</span>' for n in c["notes"]])
    description = f'{c["role"]}. Tasting notes: {", ".join(c["notes"])}.'

    dots_lines = []
    position = int(c["num"])
    for i in range(1, TOTAL_COURSES + 1):
        if i < position:
            dots_lines.append('    <li class="course__dots-item course__dots-item--past"></li>')
        elif i == position:
            dots_lines.append('    <li class="course__dots-item course__dots-item--current" aria-current="step"></li>')
        else:
            dots_lines.append('    <li class="course__dots-item"></li>')
    dots_html = "\n".join(dots_lines)

    if c["pairing"]:
        pairing_html = f'<div class="pairing">{c["pairing"]}</div>'
    elif c.get("pairing_status") == "tbd":
        pairing_html = '<div class="pairing pairing__none">Pastry pairing · forthcoming</div>'
    elif c.get("pairing_status") == "coming":
        pairing_html = '<div class="pairing pairing__none">Pastry pairing · forthcoming</div>'
    else:
        pairing_html = '<div class="pairing pairing__none">Served on its own</div>'

    if c["prev"]:
        prev_html = f'<a href="{c["prev"]}.html" class="pager-link">← previous</a>'
    else:
        prev_html = '<span class="pager-link pager-link--disabled">← previous</span>'

    if c["next"]:
        next_html = f'<a href="{c["next"]}.html" class="pager-link">next course →</a>'
    else:
        next_html = '<a href="../index.html" class="pager-link">back to menu →</a>'

    html = template.format(
        theme=theme_map[c["variant"]],
        variant=c["variant"],
        origin_key=c["origin_key"],
        name=c["name"],
        num=c["num"],
        origin=c["origin"],
        role=c["role"],
        description=description,
        notes_html=notes_html,
        dots_html=dots_html,
        pairing_html=pairing_html,
        prev_html=prev_html,
        next_html=next_html,
    )

    (out_dir / f'{c["slug"]}.html').write_text(html)
    print(f'Generated {c["slug"]}.html')

print("\nAll courses generated.")

import os
from pathlib import Path

courses = [
    {
        "slug": "01-ethiopia",
        "num": "01",
        "variant": "bouquet",
        "origin_slug": "ethiopia",
        "origin": "Ethiopia Uraga Raro Boda · Pour over",
        "name": "Opening Act",
        "role": "Lift, fragrance, a delicate first impression",
        "notes": ["star jasmine", "earl grey", "bergamot", "limeade", "honeyed finish"],
        "brew_specs": [
            ("Dose", "18 g"),
            ("Ratio", "1:16"),
            ("Temp", "94°C / 201°F"),
            ("Grind", "Medium-fine"),
            ("Method", "V60, ~2:45 total"),
        ],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": None,
        "next": "02-colombia",
    },
    {
        "slug": "02-colombia",
        "num": "02",
        "variant": "dessert",
        "origin_slug": "colombia",
        "origin": "Colombia Buesaco · Maricela Ordoñez · Pour over",
        "name": "The Body",
        "role": "Balance, sweetness, a calmer middle",
        "notes": ["caramel", "brown sugar", "green apple", "rose hips", "english breakfast"],
        "brew_specs": [
            ("Dose", "18 g"),
            ("Ratio", "1:16"),
            ("Temp", "93°C / 199°F"),
            ("Grind", "Medium"),
            ("Method", "V60, ~3:00 total"),
        ],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": "01-ethiopia",
        "next": "03-kenya",
    },
    {
        "slug": "03-kenya",
        "num": "03",
        "variant": "coral",
        "origin_slug": "kenya",
        "origin": "Kenya Nyeri Karuthi AA · Pour over",
        "name": "The Closer",
        "role": "Tension, brightness, a memorable finish",
        "notes": ["blackcurrant", "tomato", "sparkling acidity", "tea-like finish"],
        "brew_specs": [
            ("Dose", "18 g"),
            ("Ratio", "1:16.5"),
            ("Temp", "96°C / 205°F"),
            ("Grind", "Medium-fine"),
            ("Method", "Kalita Wave, ~3:15 total"),
        ],
        "pairing": None,
        "pairing_status": "tbd",
        "prev": "02-colombia",
        "next": "04-yuzu-cooler",
    },
    {
        "slug": "04-yuzu-cooler",
        "num": "04",
        "variant": "shop",
        "origin_slug": "yuzu",
        "origin": "Specialty · Citrusy · Batched cold",
        "name": "Yuzu Jasmine Coconut Cooler",
        "role": "Echoes the Ethiopia's jasmine, bergamot, limeade energy",
        "notes": ["bright yuzu", "soft coconut", "jasmine lift"],
        "brew_specs": [
            ("Base", "Cold brew concentrate, 1:8"),
            ("Steep", "14 hr, ambient"),
            ("Grind", "Coarse"),
            ("Build", "Yuzu + coconut cream, jasmine tincture"),
            ("Serve", "Shaken over ice"),
        ],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "03-kenya",
        "next": "05-cherry-matcha",
    },
    {
        "slug": "05-cherry-matcha",
        "num": "05",
        "variant": "journal",
        "origin_slug": "cherry",
        "origin": "Specialty · Floral · Matcha",
        "name": "Cherry Jasmine Matcha",
        "role": "A refined, less obvious fruit expression",
        "notes": ["light matcha", "cherry depth", "jasmine aroma"],
        "brew_specs": [
            ("Matcha", "3 g ceremonial grade"),
            ("Water", "60 ml at 75°C / 167°F"),
            ("Whisk", "Chasen, M-pattern"),
            ("Build", "Cherry reduction + jasmine milk"),
            ("Serve", "Layered over ice"),
        ],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "04-yuzu-cooler",
        "next": "06-nitro-latte",
    },
    {
        "slug": "06-nitro-latte",
        "num": "06",
        "variant": "caramel",
        "origin_slug": "nitro",
        "origin": "Specialty · Nitro",
        "name": "Nitro Vanilla Date Latte",
        "role": "A richer counterweight to the Kenya's sharp finish",
        "notes": ["silky nitro", "restrained date", "vanilla lift"],
        "brew_specs": [
            ("Dose", "18 g espresso"),
            ("Ratio", "1:2 (36 g out)"),
            ("Grind", "Fine"),
            ("Build", "Date syrup + vanilla + whole milk"),
            ("Charge", "N₂O, iSi Gourmet Whip"),
        ],
        "pairing": None,
        "pairing_status": "coming",
        "prev": "05-cherry-matcha",
        "next": None,
    },
]

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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="../styles.css">
</head>
<body>

<main class="course course--{variant} course--origin course--{origin_slug}">

  <nav class="course__nav">
    <a href="../index.html" class="course__back">← All courses</a>
    <span class="course__counter">{num} of 06</span>
  </nav>

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
      <div class="course__label">Brew specs</div>
      <dl class="brew-specs">
{brew_specs_html}
      </dl>
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

<script>
(function() {{
  if (!window.matchMedia('(max-width: 767px)').matches) return;
  var prevHref = null, nextHref = null;
  document.querySelectorAll('.course__pager a.pager-link').forEach(function(a) {{
    if (a.textContent.trim().charAt(0) === '\u2190') prevHref = a.getAttribute('href');
    else nextHref = a.getAttribute('href');
  }});
  if (!prevHref && !nextHref) return;
  var startX = 0, startY = 0;
  document.addEventListener('touchstart', function(e) {{
    var t = e.changedTouches[0];
    startX = t.screenX;
    startY = t.screenY;
  }}, {{ passive: true }});
  document.addEventListener('touchend', function(e) {{
    var t = e.changedTouches[0];
    var dx = t.screenX - startX, dy = t.screenY - startY;
    if (Math.abs(dx) < 60 || Math.abs(dy) > Math.abs(dx)) return;
    if (dx < 0 && nextHref) window.location.href = nextHref;
    else if (dx > 0 && prevHref) window.location.href = prevHref;
  }}, {{ passive: true }});
}})();
</script>
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
    brew_specs_html = "\n".join(
        [f'        <dt>{label}</dt><dd>{value}</dd>' for label, value in c["brew_specs"]]
    )
    description = f'{c["role"]}. Tasting notes: {", ".join(c["notes"])}.'

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
        origin_slug=c["origin_slug"],
        name=c["name"],
        num=c["num"],
        origin=c["origin"],
        role=c["role"],
        description=description,
        notes_html=notes_html,
        brew_specs_html=brew_specs_html,
        pairing_html=pairing_html,
        prev_html=prev_html,
        next_html=next_html,
    )

    (out_dir / f'{c["slug"]}.html').write_text(html)
    print(f'Generated {c["slug"]}.html')

print("\nAll courses generated.")

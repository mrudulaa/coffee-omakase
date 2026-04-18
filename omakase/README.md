# Coffee Omakase — Site

A mobile-first course-by-course site for the coffee omakase. Static HTML, no build step.

## Structure

```
omakase/
├── index.html                    # Gallery grid (home)
├── styles.css                    # Shared styles
├── courses/
│   ├── 01-kenya.html
│   ├── 02-ethiopia.html
│   ├── 03-guatemala.html
│   ├── 04-coconut-cooler.html
│   ├── 05-citrus-tonic.html
│   └── 06-nitro-latte.html
├── generate.py                   # Regenerates all course pages
├── vercel.json
└── README.md
```

## Editing content

To change tasting notes, pairings, origins, or course names: open `generate.py`, edit the `courses` list at the top, then run:

```bash
python3 generate.py
```

This regenerates all six course pages. Edit once, propagate everywhere.

Minor tweaks to a single page can be made directly in the `courses/*.html` file, but the next `generate.py` run will overwrite them.

### Adding pastry pairings

All six courses currently show "Pastry pairing · forthcoming". To add a pairing, find the course in `generate.py` and replace `"pairing": None` with `"pairing": "Your pastry name here"`. Then run `python3 generate.py`.

## Editing colors or fonts

All design tokens live at the top of `styles.css` inside `:root`. Change a color variable and it updates everywhere.

## Deploying

### Vercel (easiest)

**Option A — drag and drop:**
1. Go to [vercel.com/new](https://vercel.com/new)
2. Drag this folder onto the page
3. Done. You get a free URL like `omakase-xyz.vercel.app`

**Option B — via GitHub:**
1. Push this folder to a GitHub repo
2. Import the repo on Vercel
3. Every push auto-deploys

### Netlify

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the folder
3. Done

### Custom domain

Both Vercel and Netlify let you add a custom domain in settings for free. Point your domain's DNS at their servers.

## Sharing with guests

Once deployed, share the URL. The site works on any phone, no app needed. You can generate a QR code at [qr-code-generator.com](https://www.qr-code-generator.com/) and print it on a physical card at each seat.

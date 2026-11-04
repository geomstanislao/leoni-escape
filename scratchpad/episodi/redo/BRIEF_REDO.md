# Redraw brief: richer art for existing cards ("Leoni di Laguna – Escape")

SD = /tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad

The user finds the card illustrations "troppo semplici" (too simple, empty backgrounds, sketch-like). You redraw the ILLUSTRATION of a list of existing cards, much richer, keeping everything else identical.

## Inputs
- Source cards: a JSON file (card number string → full card HTML 238×333 px) given in your task. Read each card you must redraw.
- STYLE REFERENCE (approved trial, match this level of richness): `SD/episodi/ep1_redo/trial.json` (cards 2, 5, 10, 52) and its build script in `SD/episodi/ep1_redo/`. Read it first and reuse its techniques/helpers.
- House rules: `SD/episodi/BRIEF.md` (character looks — Leo's wings small rounded feathered GOLDEN YELLOW #f4c64e, never bat wings; Becco grey seagull with white captain hat; Nico red hoodie, Sofia braid + round glasses + yellow cardigan, Toni chubby with straw gondolier hat and striped shirt). Template `SD/escA/common.py`, characters `SD/escD/lib.py`, `SD/escD/gen.py`, `SD/ep2a/lib.py`, `SD/ep3a/lib3.py`, `SD/ep3b/lib3.py`.

## Rules
- Keep IDENTICAL: type band, number, title, strip, text, layout, the illustration box size (same viewBox width/height), and the card's whole HTML outside the illustration SVG. Simplest: replace only the illustration `<svg>…</svg>` element inside the card HTML string.
- Keep the same scene and the same story content. PUZZLE CONTENT MUST STAY EXACTLY THE SAME: same objects, same counts (feathers, horses, torches, signs, branches…), same distinguishing features, same painted/white-sign numbers, same gold hidden-number circles (same numbers, on the same objects, drawn as gold circles with the digit). No other digits or gold circles anywhere. Details must never hide or confuse puzzle elements.
- Richer means: full backgrounds (gradient sky, clouds, hills, trees, reeds, water with ripples/reflections, stone/wood textures), light and shadow with gradients, cast shadows, highlights, depth layers, small props, shaded characters with expressive faces. Flat cartoon style, outlines #3b2416, readable at small size.
- SVG ids unique: prefix every id with the prefix given in your task + card number + `_`. No `/>` self-closing tags, no scripts, no external images.
- Render to check (Playwright: `require('playwright')`, `chromium.launch()`, `page.setContent`, screenshot, then look with Read). Render every card at least once and fix problems.

## Output
The JSON file named in your task: {card number string: full new card HTML} for exactly the cards in your list. Work only in your own work folder. Reply with one short line per card where you had to make a judgement call.

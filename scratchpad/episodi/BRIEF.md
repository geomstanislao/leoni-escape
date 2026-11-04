# Drawing brief – card art for one episode of "Leoni di Laguna – Escape"

SD = /tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad

You draw the card FRONTS for one episode. Output: ONE JSON file `SD/episodi/<ep>_cards.json` = an object mapping the card number as a string ("1", "142", …) to that card's complete HTML (one outer `<div>` of exactly 238×333 px, the same card template as the existing deck). Nothing else.

## Inputs
- The episode script: `SD/episodi/spec.json` → key `<ep>` → `cards` (each: n, typ, title, text, art, optional strip, hidden, H). Texts are FINAL Italian: copy them exactly. `**n**` in text = a bold dark-red card reference (the template's fmt_text already handles it).
- The card template: `SD/escA/common.py` — use `card_front(typ, num, title, H, svgs, text=..., strip=...)` and its helpers (`svg`, `hid` for gold hidden-number circles, `tx`, `rgrad_def`, etc.). Read it first. The colours per type (LUOGO, OGGETTO ROSSO, OGGETTO BLU, PERSONAGGIO, INDIZIO, ENIGMA, COMBINAZIONE, RISPOSTA, SBAGLIATO, SPECIALE) come from the template: `typ` values are exactly those strings.
- Character drawing code: `SD/escD/lib.py` and `SD/escD/gen.py` (Nico, Sofia, Toni, Leo, Becco, horses, boats, etc.), plus `SD/ep2a/lib.py`, `SD/ep3a/lib3.py`, `SD/ep3b/lib3.py` (Tito, Elena, Papà, Nonna, Roman and lagoon scenery from the comic). Copy what you need into your own folder `SD/episodi/<ep>_work/` and import from there. NEVER edit files outside your folder.
- Look at one existing deck file for the finished look: `SD/escape/project/Carte4_Fronte.dc.html`.

## Character rules (must match the rest of the series)
- Nico: spiky brown hair, red hoodie, jeans, beige backpack with orange oar keychain. Sofia: brown hair with long braid, round glasses, yellow cardigan, grey skirt. Toni: chubby, big straw gondolier hat with red ribbon, striped white-blue shirt.
- Leo: golden lion cub, small ROUNDED FEATHERED wings GOLDEN YELLOW like his body (#f4c64e, feather lines #d99a2b), thin glowing gold halo. Never bat wings.
- Becco: grey seagull, white chest, orange beak/legs, white captain's hat with navy band, small X scar on the chest.

## Drawing rules
- Follow each card's `art` brief. Keep illustrations simple, flat, readable at small size; outlines #3b2416, round joins.
- `hidden`: draw exactly those numbers as gold circles with `hid()` ON the named object, and NO other gold circles or stray digits anywhere.
- Answer numbers that the brief calls "white signs" / painted numerals / written boards are drawn as plain text on white boards or painted on objects — NEVER as gold circles.
- Puzzle cards (typ ENIGMA and the LUOGO cards with hidden numbers) must be crystal clear: counts exact, differences big. These matter most.
- SVG ids must be unique inside your file: prefix every id with `<ep>c<n>_` (e.g. `ep3c9_g1`).
- Close every element explicitly (no self-closing `/>`), quote attributes, no emoji, no external images, no scripts.
- Text must fit: if a card's text is long, lower the illustration height H (default 120, minimum ~85). Use the template's own text size.

## Done
Write the JSON with a small Python build script in your folder. Then check: every card in the spec for your episode is present; `'/>'` does not occur in any card HTML; each card's hidden gold circles = exactly its `hidden` list. Do not publish, open a browser, render or screenshot. Reply with one line per card that needed a judgement call, nothing else.

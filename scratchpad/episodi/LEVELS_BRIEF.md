# Brief: level versions (Bambini / Famiglia / Adulti) of existing escape episodes

SD = /tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad

The game "Leoni di Laguna – Escape" (Italian, real history of the Veneti and Venice) has episodes. Each episode can exist at 3 levels with THE SAME STORY AND THE SAME CARD ART, but different texts/puzzles/hints/diary tiles:
- **k = Bambini (6–9 years)**: short simple sentences, easy vocabulary, more help written directly on the cards (e.g. the puzzle card tells exactly what to count or which two numbers to add), arithmetic small (sums/subtractions they can do; if the base puzzle needs hard maths, either put the needed partial result in the text or cut that step). You MAY drop a hard branch of cards (list them in `drop`) and reroute with `rules` so the episode stays winnable and shorter. Diary tiles: 1 short sentence each.
- **f = Famiglia (10–14)**: the base level of episodes ep1–ep10.
- **a = Adulti**: more real history in card texts and in diary tiles (2–3 sentences, dates, names, sources like chroniclers), clues less explicit (the notebook gives facts, not the method). Puzzles may be a bit harder but MUST keep the same answer numbers (the answer cards' art shows those numbers), unless you add a twist that is fully consistent like the ep1a example.

## Inputs
- Existing patch examples (read them!): `SD/episodi/levels.py` → dict `P` (ep1k, ep1a, ep2k, ep2a, ep3k, ep3a).
- Episode scripts: `SD/episodi/spec.json` (ep2–ep5), `SD/episodi/spec2.json` (ep6–ep10), `SD/episodi/spec3.json` (a1–a3, these are ADULT base episodes: for them you write k and f versions). Each card: n, typ, title, text, req, next, disc, keep, tess, final, hidden, art. Plus hints and tessere.
- Card art cannot change. A card's picture shows what its `art` field says. Never write text that contradicts the picture (numbers shown, objects, counts).

## Patch format (one JSON object per version)
{
 "base": "ep4", "level": "k" | "a" | "f", "title": ..., "place": ..., "intro": ...,
 "drop": [card numbers removed] (optional),
 "text": {"n": "new card text", ...}   (only cards you change; `**12**` = bold red card reference, same as base texts),
 "title_over": {"n": "NEW TITLE"} (optional),
 "rules": {"req": {"n": [...]}, "next": {"n": [...] or null}, "disc": {...}, "keep": {...}} (optional overrides; null deletes),
 "wrong_add": [n] (optional: extra cards that are wrong answers),
 "clone": {"newN": [srcN, typ or null, title or null, strip or null, text]} (optional: new card number reusing another card's art),
 "final": n (only if the final card changes),
 "tess": {"n": "key"} (which card unlocks which diary tile; every key in tessere must be unlocked by exactly one card that is on the winning path),
 "tessere": {"key": ["Title", "Text"]},
 "hints": [ {"done":[n...], "t":"step title", "h":["aiuto 1","aiuto 2","soluzione"]}, ... ] (full list for this version, in play order; `done` = the card(s) whose taking completes that step),
 "test_path": [winning sequence: card numbers to type, and "C<red>+<blue>" for combinations] — start with 2,3,4 (card 1 is given automatically), take every card in order like a player would.
}
Engine rules you must respect: a card can be taken only if all its `req` cards were taken before; combining red R + blue B takes card R+B (it must exist with req [R,B]); `wrong` cards cost a feather. Keep `req`s consistent after any `drop`.

## Texts
- Italian, correct and natural. Cards have little space: Bambini ≤ ~35 words per card, Adulti ≤ ~60 words (illustration may be shrunk automatically if text is long, but keep it reasonable).
- FACTS: use only facts already in the specs/tessere, or very well-established facts (dates, names) you are sure of. For each new fact you add in Adulti, list it in your final reply so it can be verified. No invented quotes attributed to real people.
- Keep Leo, Becco, Nico, Sofia, Toni and their tone.

## Output
Write each version to `SD/episodi/levels_extra/<id>.json` where id = base + level letter (e.g. `ep4k.json`, `ep4a.json`, `a1k.json`, `a1f.json`). Then validate it yourself with: `python3 SD/episodi/check_level.py SD/episodi/levels_extra/<id>.json` (it simulates the test_path and checks links) and fix until it prints OK. Reply with: the ids written, and the list of new historical facts used in Adulti versions.

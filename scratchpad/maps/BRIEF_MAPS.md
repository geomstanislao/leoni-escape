# Brief: 4 illustrated historical maps for "Leoni di Laguna – Escape"

SD = /tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad
Work only in `SD/maps/`. No network: there is NO geographic data available — draw coastlines yourself from your own knowledge as lat/lon point lists, then project them in code.

## Output
`SD/maps/maps.json` = list of 4 objects, in this order:
{ "id": "veneti"|"laguna"|"terra"|"mar", "title": "...", "svg": "<svg ...>...</svg>" }
Each SVG: viewBox "0 0 800 560", one self-contained element, no `/>` self-closing tags (always `<path ...></path>`), no scripts, no external images or fonts (use font-family "Georgia, serif"). All ids prefixed `mp_<mapid>_`.

Every place marker must be a group `<g class="pl" data-k="<key>">…</g>` (dot + label) using exactly the keys listed below, so the game can highlight the current episode's place. Put a soft dot of radius ~5 with dark outline; label next to it, readable at 800 px wide and still OK at 400 px.

## Style
Illustrated old-map look, matching a cartoon game: parchment background (#f3e3bf with subtle vignette/gradient), sea #9cc7d3 with fine wave lines, land #e7d3a1 with a darker coast outline (#7a5a3e) and a soft inner shadow, small hand-drawn mountain icons for the Alps/Apennines/Dinaric Alps where relevant, rivers as thin blue lines (#5f9fb5), a compass rose, a decorative title cartouche, a small scale note "mappa illustrata, non in scala esatta". Territories as translucent fills/hatching with a legend box. Keep it clean: no clutter over labels.

## Projection
Equirectangular with x = (lon − lon0) · cos(latc) · k, y = (lat0 − lat) · k, fit to the frame per map (bounds below). Write coastlines with enough points to be recognisable (the Adriatic, Istria, the Po delta, the Venetian lagoon barrier islands, Greece and the Peloponnese, Crete, Cyprus, the Bosphorus, the Nile delta). Better recognisable shapes than many points.

## Maps and markers (key: name — lat, lon — label text)

### 1. veneti — "I Veneti antichi (circa VI secolo a.C.)"  bounds lat 44.7–46.6, lon 10.6–13.6
Area of the ancient Veneti shaded (between the Adige/Lake Garda area to the west, the Alps to the north, the Tagliamento/Isonzo to the east, the Adriatic and the Po to the south). Rivers: Po, Adige, Brenta, Piave, Tagliamento (approximate). Label "Mare Adriatico", "Alpi". Markers:
este — 45.228, 11.657 — "Este (Ateste) · santuario di Reitia"
padova — 45.406, 11.876 — "Padova (Patavium)"
vicenza — 45.548, 11.546 — "Vicenza"
treviso — 45.667, 12.245 — "Treviso"
oderzo — 45.781, 12.492 — "Oderzo (Opitergium)"
altino — 45.553, 12.397 — "Altino"
adria — 45.055, 12.056 — "Adria"
concordia — 45.755, 12.845 — "Concordia"
belluno — 46.140, 12.217 — "Belluno"
Legend: "Area abitata dai Veneti antichi" (shading), "Città dei Veneti" (dot).

### 2. laguna — "Venezia e la sua laguna"  bounds lat 45.18–45.65, lon 12.15–12.75
Draw the lagoon (water inside), the barrier islands Lido and Pellestrina with the three port mouths (Lido, Malamocco, Chioggia), the mainland edge, small island shapes for Venezia (with the S of the Canal Grande hinted), Giudecca, Murano, Burano, Torcello, the Lido, Chioggia. Markers:
venezia — 45.438, 12.336 — "Venezia (Rialto)"
rialto — 45.438, 12.336 — (no extra dot; put this key on the same group as venezia: use data-k="venezia rialto")
murano — 45.458, 12.353 — "Murano"
burano — 45.485, 12.417 — "Burano"
torcello — 45.497, 12.418 — "Torcello"
altino — 45.553, 12.397 — "Altino"
eraclea — 45.600, 12.640 — "Eraclea (Cittanova)"
malamocco — 45.370, 12.338 — "Malamocco"
lido — 45.410, 12.372 — "Lido"
chioggia — 45.219, 12.279 — "Chioggia"
mestre — 45.490, 12.240 — "Mestre"
lazzaretto — 45.462, 12.383 — "Lazzaretto Nuovo"
giudecca — 45.425, 12.325 — "Giudecca · Redentore"
Also mark the Arsenale as a small symbol on the east side of Venezia, labelled "Arsenale" (key arsenale, same group structure). Legend: "Bocche di porto" (three small symbols on the mouths).

### 3. terra — "Lo Stato da Terra (verso il 1500)"  bounds lat 44.9–46.7, lon 9.4–13.9
Shade the Venetian mainland territory around 1500 (approximate border: west along the Adda river including Bergamo and Crema; north the Alps including Belluno/Feltre/Cadore; east Friuli up to roughly the Isonzo; south along the Adige/Po including the Polesine and Rovigo). Rivers: Po, Adda, Oglio, Adige, Brenta, Piave, Tagliamento, Isonzo. Lake Garda. Markers with year of joining:
venezia — 45.438, 12.336 — "Venezia"
treviso — 45.667, 12.245 — "Treviso (1339)"
padova — 45.406, 11.876 — "Padova (1405)"
vicenza — 45.548, 11.546 — "Vicenza (1404)"
verona — 45.438, 10.992 — "Verona (1405)"
brescia — 45.541, 10.211 — "Brescia (1426)"
bergamo — 45.698, 9.677 — "Bergamo (1428)"
crema — 45.364, 9.686 — "Crema (1449)"
udine — 46.064, 13.235 — "Udine · Friuli (1420)"
belluno — 46.140, 12.217 — "Belluno e Feltre (1404)"
rovigo — 45.070, 11.790 — "Rovigo · Polesine (1484)"
Legend: "Stato da Terra della Repubblica (circa 1500)".

### 4. mar — "Lo Stato da Mar e le rotte"  bounds lat 30.5–46.5, lon 12–35.5
Italy, the Balkans, Greece, Anatolia, the Levant coast, Egypt's coast with the Nile delta, Crete, Cyprus, Rhodes, Euboea, Corfu. Shade Venetian possessions; draw dashed galley routes Venezia → Corfù → Modone → Creta → Cipro / Alessandria, and Venezia → Costantinopoli. Markers (possession + years):
venezia — 45.438, 12.336 — "Venezia"
istria — 45.548, 13.730 — "Istria · Capodistria"
zara — 44.119, 15.231 — "Zara · Dalmazia"
spalato — 43.508, 16.440 — "Spalato"
cattaro — 42.424, 18.771 — "Cattaro (1420–1797)"
corfu — 39.624, 19.921 — "Corfù (1386–1797)"
lepanto — 38.392, 21.828 — "Lepanto (1571)"
modone — 36.817, 21.705 — "Modone e Corone (1207–1500)"
negroponte — 38.463, 23.594 — "Negroponte (1390–1470)"
creta — 35.339, 25.144 — "Creta · Candia (1211–1669)"
cipro — 35.125, 33.942 — "Cipro · Famagosta (1489–1571)"
costantinopoli — 41.008, 28.978 — "Costantinopoli"
alessandria — 31.200, 29.918 — "Alessandria d'Egitto"
acri — 32.927, 35.082 — "Acri · verso l'Asia (Marco Polo)"
Costantinopoli, Alessandria and Acri are trade destinations, NOT Venetian possessions: draw them with a different marker (ring) and say so in the legend: "Possedimenti veneziani" (filled red dot / red shading) vs "Porti delle rotte commerciali" (ring).

## Check
Render all 4 with Playwright (`require('playwright')`, `chromium.launch()`, `page.setContent`), look at each PNG with Read, and fix: shapes recognisable, labels not overlapping, markers on land/in the right place. Then write maps.json. Reply with a short list of judgement calls.

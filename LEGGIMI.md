# Sorgenti di Leoni di Laguna – Escape

Ramo `sorgenti`: tutto quello che serve per ricostruire l'app (ramo `main`).

Uso in una nuova sessione:
1. Copiare la cartella `scratchpad/` di questo ramo in
   `/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/`
   (gli script usano questo percorso fisso).
2. `cd .../scratchpad/episodi && python3 -I spec.py && python3 -I spec2.py && python3 -I spec3.py && python3 -I spec4.py && python3 levels.py`
3. `cd ../tv && python3 build2.py && node --check game2.js && node test3.js` (tutte le versioni devono arrivare a «win true»)
4. Copiare `scratchpad/pwa/index.html` in `index.html` del ramo `main`, aumentare il numero di `CACHE` in `sw.js`, commit e push.

Gara del mese: episodi in `episodi/spec4.py` (chiave `gAAMM`, `level='g'`, `month='AAAA-MM'`), carte in `episodi/gAAMM_cards.json`,
percorso di prova in `tv/test3.js`. Regole Firestore in `gara/firestore.rules`, configurazione in `gara/firebase.json`.

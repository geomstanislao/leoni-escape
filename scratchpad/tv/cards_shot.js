const { chromium } = require('playwright');const fs=require('fs');
const sd='/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/';
const pick=[['ep1a',[2,53,39,34]],['ep2a',[1,2,9,142]],['ep3a',[1,3,31,50]],['ep1k',[5,50,2,43]]];
(async()=>{const b=await chromium.launch();
for(const [ep,ns] of pick){const c=JSON.parse(fs.readFileSync(sd+ep+'_cards.json'));
 const html='<html><head><link href="https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet"></head><body style="margin:0;background:#333;display:flex;gap:10px;padding:10px;zoom:1.6">'+ns.map(n=>c[String(n)]).join('')+'</body></html>';
 const p=await b.newPage({viewport:{width:1620,height:560}});await p.setContent(html);await p.waitForTimeout(200);await p.screenshot({path:`cs_${ep}.png`});}
await b.close();})();

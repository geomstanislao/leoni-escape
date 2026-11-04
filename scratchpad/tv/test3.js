const { chromium } = require('playwright');
const P={
 ep1:[2,3,4,5,8,7,12,11,16,9,15,10,19,22,'C7+22',27,18,'C12+18',35,'C15+35',52,53,58,56,68,14,'C14+58',74,26,76,81,20,'C20+26',39,43],
 ep2:[2,3,4,7,11,12,9,22,'C12+22',6,24,5,46,18,142],
 ep3:[2,3,4,7,11,8,'C7+8',9,26,30,40,12,31,32,41,16,'C16+12',10,'C10+40'],
 ep4:[2,3,4,7,11,6,24,30,33,36,35,12,'C7+36',40,811],
 ep5:[2,3,4,11,12,5,8,'C5+8',23,34,40,'C12+40',60,61,74],
 ep6:[2,3,4,11,12,6,9,7,528,40,'C9+40',60,150],
 ep7:[2,3,4,7,11,5,8,14,6,20,'C20+8',30,1000],
 ep8:[2,3,4,11,12,5,7,30,40,16,'C16+7',10,'C12+10',50,24],
 ep9:[2,3,4,11,12,5,6,102,8,14,'C12+14',21,'C21+8'],
 ep10:[2,3,4,11,12,5,9,'C12+9',6,1100,30,40,7,8,'C7+8'],
 ep1k:[2,3,4,5,8,7,12,11,16,9,15,10,19,22,'C7+22',27,18,'C12+18',35,'C15+35',39,43],
 ep1a:[2,3,4,5,8,7,12,11,16,9,15,10,19,22,'C7+22',27,18,'C12+18',35,'C15+35',52,53,58,56,68,14,'C14+58',74,26,76,81,20,'C20+26',39,34],
 ep2k:[2,3,4,7,11,12,9,22,'C12+22',6,24,5,46],
 ep2a:[2,3,4,7,11,12,9,22,'C12+22',6,24,5,46,18,142],
 ep3k:[2,3,4,7,11,8,'C7+8',9,26,30,40,12,31,32,41,16,'C16+12',10,'C10+40'],
 ep3a:[2,3,4,7,11,8,'C7+8',9,26,30,40,12,31,32,41,16,'C16+12',10,'C10+40'],
 g2611:[2,3,4,11,12,7,13,20,38,16,'C16+7',40,14,'C12+14',50,1291],
 a1:[2,3,4,11,12,6,9,14,'C12+14',30,'C30+6',40,82,50,529],
 a2:[2,3,4,11,12,5,8,7,261,14,'C12+14',33,'C33+8',50,263],
 a3:[2,3,4,11,12,5,8,7,14,'C12+8',30,40,23,9,'C23+9',50,18]};
try{Object.assign(P,JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-claude/3a5afc48-e9b0-588f-bde5-1ee6b1274f62/scratchpad/episodi/levels_paths.json')));}catch(e){}
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/download/leoni-escape-tv.html');await p.waitForTimeout(300);
 await p.screenshot({path:'m_menu.png'});
 for(const ep of Object.keys(P)){
  const LVL={};for(const e of JSON.parse(await p.evaluate(()=>document.getElementById('game-data').textContent)).episodes)LVL[e.id]=e.level;
  await p.click('#tab_'+LVL[ep]);await p.click(`.epcard[data-ep="${ep}"]`);await p.click('#btnPlay');await p.waitForTimeout(150);
  await p.click('[data-act="close"]');
  let fail=null;
  for(const s of P[ep]){
   if(String(s).startsWith('C')){const [a,c]=s.slice(1).split('+');await p.click('#btnCombine');await p.click(`.thumb[data-n="${a}"]`);await p.click(`.thumb[data-n="${c}"]`);}
   else{for(const d of String(s))await p.click(`.key[data-k="${d}"]`);await p.click('.key[data-k="ok"]');}
   await p.waitForTimeout(60);
   if(!(await p.isVisible('#ovZoom'))){fail=s+': '+await p.textContent('#leotext');break;}
   if(await p.isVisible('[data-act="win"]')){await p.click('[data-act="win"]');break;}
   await p.click('[data-act="close"]');
  }
  const win=await p.isVisible('#ovWin'); const stats=win?await p.textContent('#winstats'):'';
  console.log(ep,'win',win,stats,fail||'');
  if(win) await p.click('#btnWinMenu');
 }
 await p.click('#btnDiary2');await p.waitForTimeout(200);console.log(await p.textContent('#dcount'));
 await p.screenshot({path:'m_diary.png'});
 console.log('errs',errs);await b.close();})();

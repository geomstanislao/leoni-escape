const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [,,f,out,keys]=process.argv;const d=JSON.parse(fs.readFileSync(f));const ks=keys?keys.split(','):Object.keys(d);
const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1000,height:400},deviceScaleFactor:2});
await pg.setContent('<body style="margin:8px;display:flex;flex-wrap:wrap;gap:8px;background:#ccc;align-items:flex-start">'+ks.map(k=>d[k]).join('')+'</body>');
await pg.waitForTimeout(400);
const ov=await pg.evaluate(()=>[...document.querySelectorAll('body>div')].map(c=>{const t=c.children[c.children.length-1];return t.scrollHeight>t.clientHeight+1?'OVERFLOW':'ok'}));
console.log(JSON.stringify(ks.map((k,i)=>k+':'+ov[i])));
await pg.screenshot({path:out,fullPage:true});await b.close()})()

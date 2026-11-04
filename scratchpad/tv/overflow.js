const { chromium } = require('playwright');const fs=require('fs');
const [file,list]=process.argv.slice(2);const c=JSON.parse(fs.readFileSync(file));const ns=list?list.split(','):[];
(async()=>{const b=await chromium.launch();const p=await b.newPage();const out={};
for(const n of ns){await p.setContent('<html><head><link href="https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet"></head><body>'+c[n]+'</body></html>');await p.waitForTimeout(80);
 const r=await p.evaluate(()=>{const ds=[...document.querySelectorAll('div')].filter(d=>d.style.flex&&d.style.flex.startsWith('1'));const d=ds[ds.length-1];return [d.scrollHeight,d.clientHeight];});
 if(r[0]>r[1]+1)out[n]=r;}
console.log(JSON.stringify(out));await b.close();})();

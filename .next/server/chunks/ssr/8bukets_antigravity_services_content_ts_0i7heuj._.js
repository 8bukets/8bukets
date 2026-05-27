module.exports=[64622,a=>{"use strict";var b=a.i(22734),c=a.i(14747),d=a.i(31359);async function e(a){console.log(`📝 [Content] Generating content: ${a.title}...`);let e=c.default.join(process.cwd(),"data",a.filename),f=`# ${a.title}

Generated on: ${new Date().toISOString()}

${a.content}`;return b.default.writeFileSync(e,f),(0,d.logAutonomousAction)(`[CONTENT] Generated ${a.filename}`,"info"),{filePath:e,size:f.length}}a.s(["generateContent",0,e])}];

//# sourceMappingURL=8bukets_antigravity_services_content_ts_0i7heuj._.js.map
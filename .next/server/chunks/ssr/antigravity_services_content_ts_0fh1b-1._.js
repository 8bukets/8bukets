module.exports=[57302,a=>{"use strict";var b=a.i(22734),c=a.i(14747),d=a.i(4968);async function e(a){try{console.log(`📝 [Content] Generating content: ${a.title}...`);let e=c.default.join(process.cwd(),"data",a.filename),f=`# ${a.title}

Generated on: ${new Date().toISOString()}

${a.content}`;return await b.default.promises.writeFile(e,f),(0,d.logAutonomousAction)(`[CONTENT] Generated ${a.filename}`,"info"),{filePath:e,size:f.length}}catch(a){throw console.error("[Evolution Autocorrect] Unhandled error:",a),a}}a.s(["generateContent",0,e])}];

//# sourceMappingURL=antigravity_services_content_ts_0fh1b-1._.js.map
module.exports=[82885,a=>{"use strict";var b=a.i(22734),c=a.i(14747),d=a.i(83111);a.i(4968);var e=a.i(18558);d.z.object({id:d.z.string(),intent:d.z.string(),priority:d.z.enum(["Low","Medium","High","Critical"]),status:d.z.enum(["Active","Fulfilled","Obsolete"]),timestamp:d.z.string(),domain:d.z.string().optional(),synergyScore:d.z.number().optional()});let f=c.default.join(process.cwd(),".antigravity/directives.md");async function g(){if((0,e.cacheLife)("minutes"),!await b.default.promises.access(f).then(()=>!0).catch(()=>!1)){let a=`# Stakeholder Directives

- [High] Maintain 99.9% system uptime (Active)
- [Medium] Consolidate all branch knowledge daily (Active)
`,d=c.default.dirname(f);return await b.default.promises.access(d).then(()=>!0).catch(()=>!1)||await b.default.promises.mkdir(d,{recursive:!0}),await b.default.promises.writeFile(f,a),[{id:"dir_default_1",intent:"Maintain 99.9% system uptime",priority:"High",status:"Active",timestamp:new Date().toISOString()},{id:"dir_default_2",intent:"Consolidate all branch knowledge daily",priority:"Medium",status:"Active",timestamp:new Date().toISOString()}]}let a=await b.default.promises.readFile(f,"utf8"),d=[];return a.split("\n").forEach(a=>{let b=a.match(/^-\s*\[(Low|Medium|High|Critical)\]\s*(?:\[(.*?)\]\s*)?(.*?)\s*\((Active|Fulfilled|Obsolete)\)(?:\s*\{Score:\s*(\d+)\})?$/i);b&&d.push({id:`dir_${Math.random().toString(36).substr(2,9)}`,priority:b[1],domain:b[2]||"General",intent:b[3].trim(),status:b[4],synergyScore:b[5]?parseInt(b[5]):void 0,timestamp:new Date().toISOString()})}),d}async function h(a,b){let c=b.filter(a=>"Active"===a.status),d=`### 🎯 Directive Fulfillment Status
`;if(c.length>0){let b={};c.forEach(a=>{let c=a.domain||"General";b[c]||(b[c]=[]),b[c].push(a)}),Object.entries(b).forEach(([b,c])=>{d+=`#### 🌐 Domain: ${b}
`,c.forEach(b=>{let c=a.intelligence.branches>0,e=b.synergyScore?` (Synergy: ${b.synergyScore}%)`:"";d+=`- **[${b.priority}]** ${b.intent}${e} -> Status: ${c?"✅ ON TRACK":"⚠️ IN PROGRESS"}
`})})}else d+=`- No active directives currently registered.
`;d+=`
### ⚡ Strategic Synergy Summary
`;let e=a.intelligence.relationshipMap.crossDomainSynergies||[];e.length>0&&(d+=`- Detected **${e.length} Cross-Domain synergies**. High potential for architectural alignment across service types.
`);let f=a.intelligence.relationshipMap.synergies||[],g=f.filter(a=>"High"===a.intensity);g.length>0?d+=`- Detected **${g.length} High-Intensity synergies**. Immediate cross-branch coordination recommended.
`:d+=`- System synergy is within optimal parameters.
`;let h=(a.intelligence.relationshipMap.collaborationRecommendations||[]).filter(a=>"Critical"===a.priority);if(h.length>0&&(d+=`
### 🤝 Direct Coordination Paths
`,h.forEach(a=>{let b=a.rationale.includes("Urgent coordination required between:")?a.rationale.split("Urgent coordination required between:")[1].trim():"Cross-team architectural review required.";d+=`- **Resource Conflict/Synergy:** \`${a.resource}\`
  - **Strategic Pathway:** ${b}
  - **Action Item:** ${a.action}
`,a.branches&&Array.isArray(a.branches)&&(d+=`  - **Impacted Branches:** ${a.branches.slice(0,5).join(", ")}${a.branches.length>5?` (+${a.branches.length-5} more)`:""}
`)})),d+=`
### 🤖 Agent-to-Stakeholder Directives
`,f.length>0){let a=f.filter(a=>"High"===a.intensity);if(a.length>0){let b=a.map(a=>`\`${a.resource}\``).join(", ");d+=`- **Jules Directive (CRITICAL):** "Immediate intervention required for high-intensity resource overlaps on ${b}. Consolidate these branches to prevent significant architectural fragmentation."
`}else d+=`- **Jules Directive:** "I have detected ${f.length} developmental overlaps. Stakeholders should prioritize the 'Strategic Coordination Paths' defined above to avoid architectural drift."
`}else d+=`- **Jules Directive:** "System alignment is optimal. No manual intervention required for current development streams."
`;let i=Math.max(0,100-2*a.intelligence.pendingTasks);if(d+=`- **Stewardship Directive:** "Current Strategic Alignment Score is **${i}%**. ${i<80?"Recommend immediate backlog grooming to restore focus.":"System remains highly focused on core mission goals."}"
`,a.intelligence.relationshipMap.synergies?.some(a=>a.resource.toLowerCase().includes("quantum")||a.resource.toLowerCase().includes("synergy"))&&(d+=`- **Quantum Directive:** "Phase 13 Quantum Synergy detected in active relays. Ensure all cross-domain transactions utilize verified neural sync signatures."
`),e.length>0){let a=e[0];d+=`- **Intelligence Directive:** "Strategic cross-domain connection detected between \`${a.source}\` (${a.sourceType}) and \`${a.target}\` (${a.targetType}). Recommend unified architectural review."
`}if(a.intelligence.relationshipMap.resourceDependencies?.length>0){let b=a.intelligence.relationshipMap.resourceDependencies.length;d+=`- **Intelligence Directive:** "Ecosystem features ${b} cross-service dependencies. Ensure that changes to core services are preceded by automated dependency impact analysis."
`}let j=a.intelligence.relationshipMap.functionalClusters||{};Object.keys(j).length>0&&(d+=`
### 📊 Strategic Coordination Matrix
| Functional Cluster | Primary Stakeholders | Active Branches | Risk |
| :--- | :--- | :--- | :---: |
`,Object.entries(j).forEach(([b,c])=>{let e=a.stakeholders.filter(a=>{let b=a.role.toLowerCase().split(" ")[0];return c.some(a=>a.toLowerCase().includes(b))}).map(a=>a.role),f=c.length>5?"🔴 High":c.length>2?"🟡 Medium":"🟢 Low",g=c.some(a=>a.toLowerCase().includes("fix")||a.toLowerCase().includes("sentinel"))?"⚠️ Security":"✅ Stable";d+=`| \`${b}\` | ${e.length>0?e.join(", "):"Global Ops"} | ${c.slice(0,2).join(", ")}${c.length>2?` (+${c.length-2})`:""} | ${f} / ${g} |
`}));let k=a.intelligence.relationshipMap.impactfulBranches||[];k.length>0&&(d+=`
### 📊 Strategic Priority Matrix
| Strategic Initiative | Impact Score | Estimated Effort | Priority |
| :--- | :---: | :---: | :---: |
`,k.slice(0,8).forEach(a=>{let b=a.score>80?"High":a.score>40?"Medium":"Low",c=a.score>60?"Critical":"Routine";d+=`| \`${a.name}\` | ${a.score} | ${b} | ${c} |
`}));let l=a.intelligence.relationshipMap.resourceDependencies||[];l.length>0&&(d+=`
### 🔗 Strategic Dependency Matrix
| Source Service | Target Dependency | Connection Type |
| :--- | :--- | :---: |
`,l.slice(0,10).forEach(a=>{d+=`| \`${a.source}\` | \`${a.target}\` | ${a.type} |
`}),l.length>10&&(d+=`
*...and ${l.length-10} more cross-agent dependencies.*
`)),d+=`
### 🚀 Required Stakeholder Decisions
`;let m=0;"optimal"!==a.docker.status&&"simulated"!==a.docker.status&&(d+=`- **Infrastructure:** Approve failover to cloud-native secondary nodes due to Docker degradation.
`,m++),a.intelligence.branches>2e3&&(d+=`- **Ecosystem:** Approve branch pruning protocol to reduce cognitive overhead (${a.intelligence.branches} branches detected).
`,m++),a.intelligence.pendingTasks>10&&(d+=`- **Operations:** Approve resource reallocation for background task processing (${a.intelligence.pendingTasks} pending orders).
`,m++),a.intelligence.neuralPulse&&"optimal"!==a.intelligence.neuralPulse.health&&(d+=`- **Neural Network:** Investigate health degradation in \`${a.intelligence.neuralPulse.origin}\` environment.
`,m++),0===m&&(d+=`- No critical stakeholder decisions required at this time.
`);let n=a.intelligence.relationshipMap.resourceDependencies?.length||0,o=Math.max(0,100-4*f.length-Math.floor(n/10)-10*("optimal"!==a.docker.status));return d+=`
---
**Coordination Stability Index:** ${o}% | **Architectural Drift:** ${f.length>10?"⚠️ High":"✅ Low"} | **Ecosystem Health:** ${a.docker.status.toUpperCase()} | *Sentient Orchestration Active*
`}a.s(["generateActionableBriefing",0,h,"getStakeholderDirectives",0,g])}];

//# sourceMappingURL=antigravity_services_communication_ts_06b4rgu._.js.map
# Knowledge Merge

## Purpose

This document merges the key concepts currently spread across Antigravity, Project SOR, the live `software-online-review.com` domain, and the new `software-review-platform` starter.

The goal is to create one canonical map of what each layer is, what role it plays, and how the project should evolve.

## Executive Summary

The workspace currently contains multiple overlapping identities:

- Antigravity
- Project SOR
- `software-online-review.com`
- `software-review-platform`
- `markposition.wordpress.com`

These are not separate businesses. They are five layers of the same evolving asset.

## Canonical Interpretation

### Antigravity

Antigravity appears to represent the broader operating system, agentic logic layer, and internal platform vision.

Examples found in the repo:

- `web-app/app/antigravity`
- `web-app/scripts/antigravity-cortex.js`
- `web-app/data/antigravity-state.json`
- `web-app/data/antigravity_vision_manifest.md`

Canonical role:

- internal intelligence layer
- automation and orchestration layer
- long-term system vision

### Project SOR

Project SOR is the brand and conceptual product identity around `software-online-review.com`.

Examples found in the repo:

- root Next app metadata and pages
- `src/app/page.js`
- `src/app/about/page.js`
- `src/app/blog/*`

Canonical role:

- public-facing brand narrative
- content and editorial layer
- bridge between legacy content and future product

### software-online-review.com

This is the actual live domain and public web asset.

Observed current state:

- content-heavy site
- WordPress-like publishing structure
- broad topic coverage
- mixed content and product intent

Canonical role:

- current public domain
- traffic and SEO asset
- existing trust surface for future migration

### software-review-platform

This is the cleanest current implementation of the future product direction.

Examples found in the repo:

- `software-review-platform/README.md`
- `software-review-platform/PRODUCT.md`
- `software-review-platform/PITCH.md`
- `software-review-platform/MIGRATION.md`

Canonical role:

- new review engine
- MVP product foundation
- structured application layer for the future platform

### markposition.wordpress.com

This is the market intelligence and external data source layer.

Examples found in the repo:

- `scraper.py`
- `analytics.py`
- `links.json` and `REPORT.md`

Canonical role:

- market intelligence layer
- data source for tracking ad tech, CMS, and marketing tools
- external trend analysis feeding the intelligence system

## Recommended Unified Model

The best working model is:

- Antigravity = intelligence and system layer
- Project SOR = brand and editorial layer
- `software-online-review.com` = current public distribution layer
- `software-review-platform` = future product engine
- `markposition.wordpress.com` = market intelligence and data source layer

This gives the project a coherent internal structure instead of five competing interpretations.

## How These Layers Connect

### Operational Layer

Antigravity should remain the internal logic and orchestration system.

It can eventually support:

- moderation intelligence
- automation (Automated Market Intelligence Ingestion from markposition.wordpress.com enabled)
- internal workflows
- content and data operations

### Public Brand Layer

Project SOR should communicate the bigger idea:

- software discovery
- trust in reviews
- modern software intelligence

This is where narrative, editorial direction, and product positioning live.

### Public Domain Layer

`software-online-review.com` should remain the discoverable public shell during migration.

This layer should:

- keep current traffic alive
- explain the product
- route users into the new app

### Product Layer

`software-review-platform` should become the actual application where:

- software is listed
- users authenticate
- reviews are submitted
- moderation happens
- comments and ratings live

### Market Intelligence Layer

`markposition.wordpress.com` serves as the external ear of the system where:

- the automated TypeScript ingestion script (`scripts/ingest_markposition_knowledge.ts`) fetches and merges the latest industry intelligence during each autonomous work cycle.
- analytics generate reports on market trends
- the structured data directly updates the `market_data` section in the unified `system_knowledge.json`.

## Architectural Direction

Short term:

- keep the current public site
- deploy the new app separately
- connect them through links and navigation

Mid term:

- make the app the center of review functionality
- reduce public confusion between content and product flows

Long term:

- decide whether the platform remains content-plus-app
- or becomes fully app-first

## Naming Guidance

To reduce confusion, use this naming consistently:

- Antigravity: internal platform or intelligence system
- Project SOR: brand and strategic initiative
- Software Review Platform: product implementation
- `software-online-review.com`: public domain and customer-facing distribution point
- Markposition Scraper & Analytics: market intelligence toolset capturing data from `markposition.wordpress.com`

## Product Implications

This merged view suggests:

- the review platform should be treated as the product core
- the current live site should be treated as the distribution bridge
- Antigravity should not be mixed directly into MVP UX unless it adds clear value
- Project SOR should help unify messaging rather than introduce extra structural complexity

## Risks

Current risk areas:

- too many overlapping identities
- unclear boundary between legacy and future code
- confusion between content platform and application platform
- sensitive infrastructure files potentially stored in repo

## Recommendation

Going forward, treat `software-review-platform` as the canonical MVP implementation and use the rest of the workspace as support context around it.

Everything else should be evaluated by whether it helps:

- product clarity
- migration safety
- trust-first positioning
- practical delivery


## Autonomous Observation
- **Date**: 2026-05-14T00:11:55.884Z
- **Target**: https://software-online-review.com
- **Title**: software info by fk – software-online-review – Filip Keser
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.
## Autonomous Observation
- **Date**: 2026-05-18T16:31:30.816Z
- **Target**: https://markposition.wordpress.com
- **Title**: (position) mRNA
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.
## Autonomous Observation
- **Date**: 2026-05-19T23:11:27.645Z
- **Target**: https://localhost.co/tools/
- **Title**: Developer Tools - LocalHost.Co
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.



## iCloud Integration (8bukets & antigravity)
**Date:** 2026-05-19

- **Antigravity Architecture**: The iCloud notes indicate a need for deeper integration between the TypeScript autonomous engine and the Python orchestration cycle. Specifically, WorkOrder synchronization between MongoDB and local JSON files should be optimized using a unified Cloud sync service.
- **8Bukets Knowledge**: Data from the 8bukets folders suggests that SystemAuditAgent and ChiefAIOfficer should have explicit 'recovery' phases integrated directly into their feedback loop, bypassing manual interventions entirely.
- **Creativity Enhancement**: A core finding from the iCloud documents is that the CreativityAgent should not only suggest abstract concepts but should map those concepts directly to executable Work Orders in the queue.
## Autonomous Observation
- **Date**: 2026-05-20T08:51:38.680Z
- **Target**: https://cloud.google.com/discover/what-are-ai-agents
- **Title**: What are AI agents? Definition, examples, and types | Google Cloud
- **Context**: Ingested comprehensive definition and architectural overview of AI agents from Google Cloud documentation to ground the project's agentic logic in industry standards.
---
All the best - https://markposition.wordpress.com



## AI Agenti - Pregled i Kategorizacija (Croatian / Hrvatski)

AI agenti su napredni sustavi umjetne inteligencije koji ne samo da odgovaraju na upite, već samostalno planiraju, donose odluke i izvršavaju složene zadatke. Tržištem dominiraju specijalizirane platforme podijeljene prema poslovnim funkcijama. [1, 2]
U nastavku je izdvojeno 10 najvažnijih AI agenata razvrstanih po ključnim kategorijama primjene. [1, 2]

### Razvoj softvera i programiranje (Coding Agents)
* **Devin AI:** Prvi potpuno autonomni AI softverski inženjer. Samostalno piše kod, pronalazi bugove, testira i postavlja gotove aplikacije u produkciju.
* **Cursor:** Napredni AI agent integriran u kodni uređivač. Shvaća cijelu bazu koda u realnom vremenu te omogućuje programerima automatsko generiranje funkcija unutar projekta. [1, 3]

### Korporativno poslovanje i CRM (Enterprise Agents)
* **Salesforce Agentforce:** Moćan sustav za automatizaciju prodaje i korisničke podrške unutar Salesforce ekosustava. Autonomno rješava upite klijenata uz strogu zaštitu podataka.
* **Microsoft Copilot Studio:** Alat koji tvrtkama omogućuje izradu prilagođenih agenata integriranih s Microsoft 365 podacima za automatizaciju internih poslovnih procesa. [1, 2, 4]

### Automatizacija radnih procesa (Workflow Automation)
* **Lindy AI:** Izvrstan osobni asistent za rukovoditelje i timove. Samostalno upravlja e-poštom, dogovara sastanke, provodi regrutaciju i rješava administrativne zadatke.
* **CrewAI:** Vodeća platforma za programere koja omogućuje spajanje više različitih AI agenata u "timove" koji zajedno rješavaju složene projekte.
* **Zapier Central:** Agent koji omogućuje korisnicima bez znanja programiranja stvaranje AI pomoćnika povezanih s tisućama svakodnevnih aplikacija. [2, 3]

### Korisnička podrška i CX (Customer Experience)
* **Sierra:** Autonomni agent za korisničku podršku u velikim tvrtkama. Rješava kompleksne probleme korisnika bez potrebe za ljudskom intervencijom, čak i u strogo reguliranim industrijama.
* **Decagon:** AI agent specijaliziran za masovnu automatizaciju korisničke podrške na razini velikih poduzeća, drastično smanjujući opterećenje ljudskih timova. [1, 3]

### Interno znanje i pretraga podataka
* **Glean:** Inteligentni agent za pretraživanje korporativnih podataka. Povezuje sve interne izvore (Slack, Google Drive, Jira) i na temelju pretrage samostalno kreira izvještaje i sažetke. [1, 3]

Zanima li vas određena kategorija (poput programiranja ili automatizacije ureda)? Mogu vam detaljnije pojasniti kako ih besplatno testirati ili integrirati u vaše svakodnevno poslovanje.

**Izvori:**
[1] https://chatarmin.com/en/blog/best-ai-agent-tools
[2] https://www.designveloper.com/blog/best-ai-agent/
[3] https://www.lindy.ai/blog/best-ai-agents
[4] https://www.forbes.com/sites/bernardmarr/2025/12/29/10-ai-agent-platforms-every-business-leader-needs-to-know/

---

## Scraped English Market Data on AI Agents

Based on recent market research from industry sources:

### 1. The 10 Best AI Agent Tools in 2026 Compared (Chatarmin)
1. Salesforce Agentforce (Enterprise CRM)
2. Ruh AI (AI Workforce)
3. Cursor (Coding)
4. Devin (Coding)
5. Windsurf (Coding)
6. Sierra (CX & Support)
7. Chatarmin (armincx) (CX & Support - WhatsApp)
8. Glean (Enterprise Search)
9. Harvey (Legal AI)
10. UiPath (RPA + Agents)

### 2. 10 Best AI Agents in 2026: Which Tools Are Actually Worth It? (Designveloper)
1. Claude Code
2. Devin
3. Salesforce Agentforce
4. Microsoft Copilot
5. Gumloop
6. StackAI
7. ChatGPT Agent
8. n8n
9. Lindy AI
10. Zapier

### 3. The 12 Best AI Agents in 2026: Tested & Reviewed (Lindy)
1. Lindy (No-code multi-agent workflows)
2. IBM watsonx.ai (Enterprise-grade AI model development)
3. CrewAI (Developers building AI agent teams)
4. Sintra AI (All-in-one business automation)
5. Decagon (Large-scale AI customer support automation)
6. Harvey (Automating legal workflows)
7. Devin AI (Autonomous software development)
8. Glean (Enterprise-wide AI knowledge and workflow automation)
9. Dialogflow (Building scalable conversational AI experiences)
10. AgentGPT (Quick, browser-based AI agent creation)
11. Kore.ai (Enterprise-grade conversational and generative AI)
12. AutoGen (Building custom multi-agent AI systems)

### 4. 10 AI Agent Platforms Every Business Leader Needs To Know (Forbes)
1. Google Vertex And Astra
2. Microsoft Copilot Studio
3. Amazon Bedrock AgentCore
4. OpenAI AgentKit
5. Salesforce Agentforce
6. UIPath Studio
7. HubSpot Breeze Agent
8. Zapier Agents
9. QuickBooks AI Agents
10. Replit Agent 3

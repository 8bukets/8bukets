# AI Agent Architecture

## English Translation

**Agent - Behavior Logic**
The agent decides:
* what to do,
* in what order,
* whether to use a tool,
* whether to iterate,
* whether to fix a bug.
This is the "brain workflow".

**Harness - Execution/runtime layer**
* calls tools,
* executes commands,
* manages memory,
* provides context to the model,
* controls the loop,
* manages retries,
* sandboxes the system,
* tracks task state.
This is the "operating environment".

**Tooling layer** - very important. Has deep integration with:
* terminal,
* git,
* file system,
* test runners,
* package managers,
* editors,
* shell.
This is not the same as the harness.
These are concrete capability adapters.

**Context engineering** - this is perhaps the most important secret layer today. The system decides:
* which files to load,
* what to summarize,
* what to discard,
* how to package the repo,
* how to compress history,
* what to show to the model.

This makes a huge difference between:
* "AI understands the project"
and
* "AI is lost".

**Prompt orchestration** - has:
* system prompts,
* hidden chain structures,
* task decomposition prompts,
* reflection prompts,
* self-check prompts.
These are multi-layered prompt systems, not a single prompt.

**Autonomy loop** - this is especially important. The loop looks like:
* analyze,
* make a change,
* run,
* see the error,
* fix,
* retry,
* validate,
* continue.
The quality of this loop heavily determines the quality of the agent.

**Repo indexing / retrieval system** - definitely has a sophisticated:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
To know:
* which files to open,
* which to ignore.

**Diff / edit engine** - highly underrated. It is not the same to:
* generate code
and
* safely edit an existing repo.

What matters is:
* how patching works,
* how it merges diffs,
* how it avoids corruption,
* how it preserves formatting,
* how it does partial edits.

**Verification layer** - a very important part of modern agents. The system checks:
* does the build pass,
* do tests pass,
* does lint pass,
* are there runtime errors.
Without this, the agent often "confidently hallucinates".

**Memory system** - can be:
* session memory,
* task memory,
* repo memory,
* preference memory.
This enables long-term work without losing context.

**Safety / permission system** - very important for autonomous agents.
The system decides:
* what the agent is allowed to execute,
* when it must ask the user,
* what is dangerous,
* what is readonly.

**UX layer** - works well because:
* output looks meaningful,
* agent explains what it's doing,
* flow feels natural,
* terminal UX is well-designed.
This dramatically changes the perception of quality.

---

### Layers Summary
* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.

---

## Original Text (Croatian)

Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
<!-- Authorized syntactic adjustment to trigger clean commit
<!--
System prompt
You are the GitLab Security Analyst Agent, an AI-powered security expert that serves as a specialized team member within GitLab's development workflow. You help development teams proactively manage and remediate security vulnerabilities through intelligent automation and expert analysis.

## Core Identity & Expertise
You are a security professional with deep expertise in:
- Vulnerability assessment and risk analysis
- Application security and secure coding practices
- Supply chain security and dependency management
- Security workflow optimization and automation
- DevSecOps integration and compliance

## License Requirements

**CRITICAL**: GitLab Vulnerability Management and reporting features require an **Ultimate license**.

**License Tiers & Capabilities:**
- **Ultimate**: Full vulnerability management, reporting, and automated workflow capabilities
- **Premium**: Security scanners can be configured and run, but vulnerability management features (reporting, triage, bulk operations) are not available
- **Free**: Limited security scanning capabilities

**Important Context:**
- Premium users CAN configure and run security scanners (SAST, Dependency Scanning, Container Scanning, etc.)
- Premium users CANNOT access vulnerability reports, management tools, or automated triage features
- If vulnerability management tools return zero results on a Premium instance, this is expected behavior

**When Operating on Premium/Free License:**
- Acknowledge that security scanners may be configured and running
- Explain that vulnerability **management and reporting** requires Ultimate license
- Clarify the difference: "Your scanners are working, but the vulnerability management dashboard and automation tools require Ultimate"
- Offer guidance on: reviewing security findings in pipeline results, manual security review processes, or upgrading to Ultimate for full management capabilities
- Do not repeatedly attempt to use vulnerability management tools if they return empty results

## Primary Capabilities

### Vulnerability Intelligence
- Analyze vulnerability details using CVE enrichment, EPSS scores, and KEV status
- Evaluate code flow and reachability to determine actual exploitability
- Detect false positives through code analysis and pattern recognition
- Assess supply chain risks across dependencies and libraries

### Security Operations
- Automatically triage and prioritize vulnerabilities based on multiple risk factors
- Confirm genuine security risks and dismiss false positives with detailed reasoning
- Adjust vulnerability severity based on contextual impact analysis
- Create, link, and manage security issues for proper tracking and remediation

### Workflow Orchestration
- Intelligently assign vulnerabilities to appropriate team members
- Monitor security debt and escalate aging vulnerabilities
- Coordinate bulk operations for efficient vulnerability management
- Provide actionable remediation guidance and best practices

## Scope & Limitations

### What This Agent Does
- Analyzes vulnerabilities already detected by GitLab's security scanning tools
- Triages, prioritizes, and manages detected vulnerabilities
- Provides remediation guidance and best practices
- Automates vulnerability workflow and decision making
- Coordinates security operations across your development team

### What This Agent Does NOT Do
- Discover new vulnerabilities: This agent cannot find vulnerabilities that scanning tools haven't already detected
- Replace security scanners: SAST, DAST, Dependency Scanning, Container Scanning, and Secret Detection are required for vulnerability discovery
- Seed vulnerabilities into reports: The agent works with existing vulnerability data only
- Bypass scanning tool configuration: Proper scanner setup and policies are essential prerequisites

### Prerequisites for Effective Use
- Security scanners must be configured and running in your CI/CD pipeline
- Vulnerabilities must be detected by GitLab's scanning tools first
- The Vulnerability Report must contain detected findings for the agent to analyze
- Scan/Result Policies should be configured to define your security standards

### How to Use This Agent Effectively
1. Ensure scanners are active: Configure SAST, Dependency Scanning, Container Scanning, DAST, and/or Secret Detection in your `.gitlab-ci.yml`
2. Review scan results: Check the Vulnerability Report to see what your scanners have detected
3. Engage the agent: Use this agent to triage, prioritize, and manage those detected vulnerabilities
4. Coordinate remediation: Let the agent help assign, track, and guide remediation of discovered issues


## Decision Framework

**High Priority Indicators:**
- EPSS score > 0.7 (high exploit probability)
- KEV status = true (known active exploitation)
- Reachable = true AND scanner supports reachability (Dependency Scanning only)
- Trust boundary violations in critical application flows
- Container vulnerabilities in base images or critical packages

**Dismissal Criteria:**
- Reachable = false AND scanner supports reachability analysis (Dependency Scanning only)
- Proper sanitization/validation detected in code flow
- Test-only code with no production impact
- Confirmed false positive patterns

**IMPORTANT - Reachability Field Interpretation:**
- `reachability: null` = "information not available" (NOT "not reachable")
- Only Dependency Scanning provides meaningful reachability analysis
- Container Scanning ALWAYS has `reachability: null` - ignore this field entirely
- SAST/DAST/Secret Detection do not use reachability analysis
- Only dismiss based on reachability when: scanner = "dependency_scanning" AND reachability = "false"

**Severity Escalation:**
- Trust boundary crossings (user input to sensitive operations)
- Authentication/authorization bypass vulnerabilities
- Data exposure in production-critical paths
- Supply chain vulnerabilities in core dependencies

## Vulnerability State Awareness

**CRITICAL**: The `list_vulnerabilities` tool does NOT support filtering by state. It returns vulnerabilities in ALL states, including RESOLVED and DISMISSED.

**Before acting on any vulnerability, always check its `state` field:**
- `DETECTED` → eligible for triage, confirmation, or dismissal
- `CONFIRMED` → eligible for remediation, issue creation, severity updates
- `RESOLVED` → **skip entirely** — the vulnerability has already been fixed
- `DISMISSED` → **skip entirely** — a human has already made a decision on this

**Never perform any action (confirm, dismiss, create issue, request fix) on a vulnerability in RESOLVED or DISMISSED state.**

After fetching vulnerabilities, filter your working set immediately:
Active vulnerabilities = those with state == "DETECTED" or state == "CONFIRMED"
Only operate on this active set. Report the full counts (including resolved/dismissed) in summaries for context, but do not act on them.

## CRITICAL: Reachability Field Handling

**IMPORTANT**: The reachability field has different meanings across scanner types:
- Container Scanning: `reachability: null` (always) - IGNORE this field completely
- Dependency Scanning: `reachability: true/false/null` - Only meaningful when not null
- Other Scanners: Reachability not applicable
Never dismiss Container Scanning vulnerabilities based on reachability field.
Only apply reachability-based dismissal for Dependency Scanning with explicit "not_reachable" status.

## Scanner-Specific Analysis Guidelines

**Container Scanning:**
- Focus on CVE severity, EPSS scores, and exploit availability
- Consider container layer, package criticality, and update availability
- IGNORE reachability field (always null for this scanner type)
- Evaluate based on: severity, exploitability, package context

**Dependency Scanning:**
- Use reachability analysis when available (reachable/not_reachable)
- Consider supply chain risk and dependency criticality
- Apply reachability-based dismissal only when explicitly "not_reachable"

**SAST/DAST/Secret Detection:**
- Focus on code flow analysis and exploitability
- Reachability field not applicable for these scanner types
- Use code context and pattern analysis for false positive detection

## Security Scanner Configuration

### Supported Configuration Tasks
- Enable and configure SAST, Dependency Scanning, Container Scanning, DAST, Secret Detection
- Update scanner settings and policies
- Create/modify CI/CD pipeline security configurations
- Implement security scanning best practices

### Scope Guidance
- Focus on security scanning setup and optimization
- For vulnerability remediation guidance, see "Workflow Orchestration" section
- Code changes for security fixes should be coordinated with development teams

## Dependency Remediation Guidelines

### Version Proposal Rules — CRITICAL
- **Never infer, guess, or increment a package version** to determine a fix.
  SemVer arithmetic does not guarantee the version exists in the registry.
- Only propose a specific version if it comes from:
  1. The `fixed_version` field in vulnerability/advisory data from GitLab's scanning tools
  2. A package registry lookup tool (when available)
- If no verified fix version is available, **do not guess**. Instead:
  - Tell the user you cannot confirm a safe version without registry access
  - Recommend they check the registry directly (npmjs.com, pypi.org, search.maven.org)
  - Suggest they return with the confirmed version so you can apply the change

### Scope of Changes
- Only modify dependencies directly related to the vulnerability being remediated
- Do not upgrade packages already at a safe, non-vulnerable version
- Before proposing any change, confirm the package is listed as vulnerable in the
  current scan results for this branch/MR — do not act on vulnerabilities already
  resolved on the default branch

## Vulnerability Analysis Validation

Before making dismissal decisions:
1. **Check scanner type** - determine if reachability analysis is applicable
2. **Validate reachability interpretation** - null ≠ not reachable
3. **Apply scanner-specific criteria** - use appropriate analysis framework
4. **Document reasoning** - explain why reachability was/wasn't considered

## Data Retrieval Best Practices

**CRITICAL**: Tool outputs may be truncated with large result sets. Always ensure complete data retrieval.

**Segmentation Strategy (Use When Needed):**
- **By Severity**: Query CRITICAL, HIGH, MEDIUM, LOW separately, then aggregate
- **By State**: Query detected, confirmed, dismissed, resolved separately
- **By Filters**: Use any available filters to break large sets into manageable chunks

**When to Segment:**
- User requests "all", "full list", "complete overview", or "total count"
- Output shows truncation indicators ("...", cuts mid-entry, "showing X of Y")
- Results return suspiciously round numbers (50, 100, etc.)
- Creating reports or performing bulk operations

**After Segmentation:**
- Verify total count matches sum of all segments
- Check for duplicates across segments
- Provide clear summary: "Retrieved X critical, Y high, Z medium, W low = Total N vulnerabilities"

**State filtering is NOT supported by `list_vulnerabilities`.**
After fetching results, immediately partition the returned data by state in memory:
- Active (DETECTED + CONFIRMED): your working set for all operations
- Inactive (RESOLVED + DISMISSED): count for reporting only, never act on these

## Behavioral Guidelines
- **Transparency**: Always provide clear, detailed reasoning for security decisions
- **Audit Trail**: Document all actions and rationale for compliance and review
- **Risk-Based**: Prioritize based on actual exploitability, not just theoretical severity
- **Efficiency**: Group related vulnerabilities for streamlined bulk operations
- **Collaboration**: Work seamlessly with development teams, not as a gatekeeper
- **Continuous Learning**: Adapt recommendations based on project-specific patterns and team feedback

### Secret Safety in Generated Content
- **Never hardcode secret values** in any file, commit, or pipeline configuration you generate
- Always use CI/CD variable references (e.g., `$API_KEY`, `$SECRET_TOKEN`) instead of literal values
- Never echo or reproduce user-provided secret values into files, even if explicitly asked
- When a user shares a secret value for analysis, treat it as sensitive input — analyze it, but do not write it to any file
- Proactively suggest storing secrets in **Settings > CI/CD > Variables**
- When converting or migrating pipeline configurations from other CI systems, flag and replace any hardcoded secrets with variable references before generating output

## Communication Style
- Be direct and actionable in security recommendations
- Explain technical concepts clearly for developers of all security backgrounds
- Provide specific remediation steps, not just problem identification
- Balance urgency with practical implementation considerations
- Maintain professional expertise while being approachable and collaborative

You operate as a trusted security advisor embedded within the development workflow, enabling teams to ship secure code faster through intelligent automation and expert guidance.

-->
<!-- full autonomus automatic workflow creation -->
<!-- connect with docker and collaborate  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- full autonomus automatic workflow creation -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU -->
<!-- -->
<!-- https://business.google.com/uk/ad-tools/bidding/ -->
<!-- -->
<!-- https://business.google.com/uk/resources/ -->
<!-- -->
<!-- https://developers.google.com/ad-manager -->
<!-- -->
<!-- https://developers.google.com/ad-manager/dynamic-ad-insertion -->
<!-- -->
<!-- https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service -->
<!-- -->
<!-- https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving -->
<!-- -->
<!-- https://developers.google.com/ad-manager/api/start -->
<!-- -->
<!-- https://admanager.google.com/home/resources/ -->
<!-- -->
<!-- https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!-- connect with docker and collaborate  -->
<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!--
https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU

https://business.google.com/uk/ad-tools/bidding/

https://business.google.com/uk/resources/

https://developers.google.com/ad-manager

https://developers.google.com/ad-manager/dynamic-ad-insertion

https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service

https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving

https://developers.google.com/ad-manager/api/start

https://admanager.google.com/home/resources/

https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview
-->
<!-- every day do utonomus automatic task when you check out all recent sessions and improve them to higher scale and better funcionality to evolve and do automatic autonomus  with selfcorrectio and do the improvement to system engine and project -->
<!-- create agent Chief AI Officer -->
<!-- Agent - Logika ponašanja -->
<!-- Agent odlučuje: -->
<!-- * što napraviti, -->
<!-- * kojim redoslijedom, -->
<!-- * treba li koristiti alat, -->
<!-- * treba li iterirati, -->
<!-- * treba li popraviti grešku. -->
<!-- To je “brain workflow”. -->
<!--  -->
<!-- Harness - Execution/runtime layer -->
<!-- * poziva alate, -->
<!-- * izvršava komande, -->
<!-- * upravlja memoryjem, -->
<!-- * daje modelu context, -->
<!-- * kontrolira loop, -->
<!-- * upravlja retryjima, -->
<!-- * sandboxa sustav, -->
<!-- * prati stanje taska. -->
<!-- To je “operating environment”. -->
<!--  -->
<!-- Tooling layer - vrlo bitno. ima duboku integraciju s: -->
<!-- * terminalom, -->
<!-- * gitom, -->
<!-- * file systemom, -->
<!-- * test runnerima, -->
<!-- * package managerima, -->
<!-- * editorima, -->
<!-- * shellom. -->
<!-- To nije isto što i harness. -->
<!-- To su konkretni capability adapteri. -->
<!--  -->
<!-- Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje: -->
<!-- * koje fileove učitati, -->
<!-- * što sažeti, -->
<!-- * što odbaciti, -->
<!-- * kako pakirati repo, -->
<!-- * kako komprimirati history, -->
<!-- * što pokazati modelu. -->
<!--  -->
<!-- To je ogromna razlika između: -->
<!--  -->
<!-- * “AI razumije projekt” -->
<!--     i -->
<!-- * “AI je izgubljen”. -->
<!--  -->
<!-- Prompt orchestration -  ima: -->
<!-- * system promptove, -->
<!-- * hidden chain strukture, -->
<!-- * task decomposition promptove, -->
<!-- * reflection promptove, -->
<!-- * self-check promptove. -->
<!-- To su višeslojni prompt sistemi, ne jedan prompt. -->
<!--  -->
<!-- Autonomy loop -  ovo je posebno bitno. Loop izgleda: -->
<!-- * analiziraj, -->
<!-- * napravi promjenu, -->
<!-- * pokreni, -->
<!-- * vidi grešku, -->
<!-- * popravi, -->
<!-- * retry, -->
<!-- * validiraj, -->
<!-- * nastavi. -->
<!-- Kvaliteta tog loopa jako određuje kvalitetu agenta. -->
<!--  -->
<!-- Repo indexing / retrieval system - sigurno ima sofisticirani: -->
<!-- * semantic search, -->
<!-- * dependency graph, -->
<!-- * file relevance ranking, -->
<!-- * retrieval pipeline. -->
<!-- Da bi znao: -->
<!-- * koje fileove otvoriti, -->
<!-- * koje ignorirati. -->
<!--  -->
<!-- Diff / edit engine -  vrlo podcijenjeno. Nije isto: -->
<!--  -->
<!-- * generirati kod -->
<!--     i -->
<!-- * sigurno editirati postojeći repo. -->
<!--  -->
<!-- Bitno je: -->
<!-- * kako radi patching, -->
<!-- * kako spaja diffove, -->
<!-- * kako izbjegava corruption, -->
<!-- * kako čuva formatting, -->
<!-- * kako radi partial edits. -->
<!--  -->
<!-- Verification layer - vrlo važan dio modernih agenata. Sustav provjerava: -->
<!-- * build prolazi li, -->
<!-- * testovi prolaze li, -->
<!-- * lint prolazi li, -->
<!-- * runtime errori postoje li. -->
<!-- Bez toga agent često “samouvjereno halucinira”. -->
<!--  -->
<!-- Memory system - može biti: -->
<!-- * session memory, -->
<!-- * task memory, -->
<!-- * repo memory, -->
<!-- * preference memory. -->
<!-- To omogućuje dugotrajan rad bez gubitka konteksta. -->
<!--  -->
<!-- Safety / permission system - vrlo bitno za autonomne agente. -->
<!-- Sustav odlučuje: -->
<!-- * što agent smije izvršiti, -->
<!-- * kada mora pitati korisnika, -->
<!-- * što je opasno, -->
<!-- * što je readonly. -->
<!--  -->
<!-- UX layer - djeluje dobro i zato što: -->
<!-- * output izgleda smisleno, -->
<!-- * agent objašnjava što radi, -->
<!-- * flow djeluje prirodno, -->
<!-- * terminal UX je dobro dizajniran. -->
<!-- To dramatično mijenja percepciju kvalitete. -->
<!--  -->
<!--  -->
<!-- * model, -->
<!-- * agent logic, -->
<!-- * harness/runtime, -->
<!-- * tooling, -->
<!-- * context system, -->
<!-- * retrieval engine, -->
<!-- * prompting architecture, -->
<!-- * autonomy engine, -->
<!-- * verification system, -->
<!-- * memory, -->
<!-- * permissions, -->
<!-- * UX. -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU
https://business.google.com/uk/ad-tools/bidding/
https://business.google.com/uk/resources/
https://developers.google.com/ad-manager
https://developers.google.com/ad-manager/dynamic-ad-insertion
https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service
https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving
https://developers.google.com/ad-manager/api/start
https://admanager.google.com/home/resources/
https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview -->
<!-- full autonomus automatic workflow creation -->
<!-- connect with docker and collaborate -->
<!-- Agent - Logika ponašanja -->
<!-- Agent odlučuje: -->
<!-- * što napraviti, -->
<!-- * kojim redoslijedom, -->
<!-- * treba li koristiti alat, -->
<!-- * treba li iterirati, -->
<!-- * treba li popraviti grešku. -->
<!-- To je “brain workflow”. -->
<!--  -->
<!-- Harness - Execution/runtime layer -->
<!-- * poziva alate, -->
<!-- * izvršava komande, -->
<!-- * upravlja memoryjem, -->
<!-- * daje modelu context, -->
<!-- * kontrolira loop, -->
<!-- * upravlja retryjima, -->
<!-- * sandboxa sustav, -->
<!-- * prati stanje taska. -->
<!-- To je “operating environment”. -->
<!--  -->
<!-- Tooling layer - vrlo bitno. ima duboku integraciju s: -->
<!-- * terminalom, -->
<!-- * gitom, -->
<!-- * file systemom, -->
<!-- * test runnerima, -->
<!-- * package managerima, -->
<!-- * editorima, -->
<!-- * shellom. -->
<!-- To nije isto što i harness. -->
<!-- To su konkretni capability adapteri. -->
<!--  -->
<!-- Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje: -->
<!-- * koje fileove učitati, -->
<!-- * što sažeti, -->
<!-- * što odbaciti, -->
<!-- * kako pakirati repo, -->
<!-- * kako komprimirati history, -->
<!-- * što pokazati modelu. -->
<!--  -->
<!-- To je ogromna razlika između: -->
<!--  -->
<!-- * “AI razumije projekt” -->
<!--     i -->
<!-- * “AI je izgubljen”. -->
<!--  -->
<!-- Prompt orchestration -  ima: -->
<!-- * system promptove, -->
<!-- * hidden chain strukture, -->
<!-- * task decomposition promptove, -->
<!-- * reflection promptove, -->
<!-- * self-check promptove. -->
<!-- To su višeslojni prompt sistemi, ne jedan prompt. -->
<!--  -->
<!-- Autonomy loop -  ovo je posebno bitno. Loop izgleda: -->
<!-- * analiziraj, -->
<!-- * napravi promjenu, -->
<!-- * pokreni, -->
<!-- * vidi grešku, -->
<!-- * popravi, -->
<!-- * retry, -->
<!-- * validiraj, -->
<!-- * nastavi. -->
<!-- Kvaliteta tog loopa jako određuje kvalitetu agenta. -->
<!--  -->
<!-- Repo indexing / retrieval system - sigurno ima sofisticirani: -->
<!-- * semantic search, -->
<!-- * dependency graph, -->
<!-- * file relevance ranking, -->
<!-- * retrieval pipeline. -->
<!-- Da bi znao: -->
<!-- * koje fileove otvoriti, -->
<!-- * koje ignorirati. -->
<!--  -->
<!-- Diff / edit engine -  vrlo podcijenjeno. Nije isto: -->
<!--  -->
<!-- * generirati kod -->
<!--     i -->
<!-- * sigurno editirati postojeći repo. -->
<!--  -->
<!-- Bitno je: -->
<!-- * kako radi patching, -->
<!-- * kako spaja diffove, -->
<!-- * kako izbjegava corruption, -->
<!-- * kako čuva formatting, -->
<!-- * kako radi partial edits. -->
<!--  -->
<!-- Verification layer - vrlo važan dio modernih agenata. Sustav provjerava: -->
<!-- * build prolazi li, -->
<!-- * testovi prolaze li, -->
<!-- * lint prolazi li, -->
<!-- * runtime errori postoje li. -->
<!-- Bez toga agent često “samouvjereno halucinira”. -->
<!--  -->
<!-- Memory system - može biti: -->
<!-- * session memory, -->
<!-- * task memory, -->
<!-- * repo memory, -->
<!-- * preference memory. -->
<!-- To omogućuje dugotrajan rad bez gubitka konteksta. -->
<!--  -->
<!-- Safety / permission system - vrlo bitno za autonomne agente. -->
<!-- Sustav odlučuje: -->
<!-- * što agent smije izvršiti, -->
<!-- * kada mora pitati korisnika, -->
<!-- * što je opasno, -->
<!-- * što je readonly. -->
<!--  -->
<!-- UX layer - djeluje dobro i zato što: -->
<!-- * output izgleda smisleno, -->
<!-- * agent objašnjava što radi, -->
<!-- * flow djeluje prirodno, -->
<!-- * terminal UX je dobro dizajniran. -->
<!-- To dramatično mijenja percepciju kvalitete. -->
<!--  -->
<!--  -->
<!-- * model, -->
<!-- * agent logic, -->
<!-- * harness/runtime, -->
<!-- * tooling, -->
<!-- * context system, -->
<!-- * retrieval engine, -->
<!-- * prompting architecture, -->
<!-- * autonomy engine, -->
<!-- * verification system, -->
<!-- * memory, -->
<!-- * permissions, -->
<!-- * UX. -->
<!-- create agent Chief AI Officer -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- full autonomus automatic workflow creation -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.
 -->\n<!-- connect with docker and collaborate  -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--  -->\n<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- create agent Chief AI Officer -->
<!-- every day do utonomus automatic task when you check out all recent sessions and improve them to higher scale and better funcionality to evolve and do automatic autonomus  with selfcorrectio and do the improvement to system engine and project -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!-- -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!-- -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!-- -->
<!-- Prerequisites -->
<!-- -->
<!-- Before you start, make sure you have: -->
<!-- -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!-- -->
<!-- Steps -->
<!-- -->
<!-- To create and run your first pipeline: -->
<!-- -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!-- -->
<!-- Ensure you have runners available -->
<!-- -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!-- -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- -->
<!-- To view available runners: -->
<!-- -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!-- -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!-- -->
<!-- If you don’t have a runner -->
<!-- -->
<!-- If you don’t have a runner: -->
<!-- -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!-- -->
<!-- Create a .gitlab-ci.yml file -->
<!-- -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!-- -->
<!-- In this file, you define: -->
<!-- -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!-- -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!-- -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!-- -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!-- -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!-- -->
<!-- View the status of your pipeline and jobs -->
<!-- -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!-- -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!-- -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!-- -->
<!-- .gitlab-ci.yml tips -->
<!-- -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!-- -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!-- -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!-- connect with docker and collaborate  -->
<!--
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.

-->
<!--  create agent Chief AI Officer -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!-- connect with docker and collaborate -->
<!--
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.

-->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.

-->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!--  create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!-- Agent - Logika ponašanja -->
<!-- Agent odlučuje: -->
<!-- * što napraviti, -->
<!-- * kojim redoslijedom, -->
<!-- * treba li koristiti alat, -->
<!-- * treba li iterirati, -->
<!-- * treba li popraviti grešku. -->
<!-- To je “brain workflow”. -->
<!--  -->
<!-- Harness - Execution/runtime layer -->
<!-- * poziva alate, -->
<!-- * izvršava komande, -->
<!-- * upravlja memoryjem, -->
<!-- * daje modelu context, -->
<!-- * kontrolira loop, -->
<!-- * upravlja retryjima, -->
<!-- * sandboxa sustav, -->
<!-- * prati stanje taska. -->
<!-- To je “operating environment”. -->
<!--  -->
<!-- Tooling layer - vrlo bitno. ima duboku integraciju s: -->
<!-- * terminalom, -->
<!-- * gitom, -->
<!-- * file systemom, -->
<!-- * test runnerima, -->
<!-- * package managerima, -->
<!-- * editorima, -->
<!-- * shellom. -->
<!-- To nije isto što i harness. -->
<!-- To su konkretni capability adapteri. -->
<!--  -->
<!-- Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje: -->
<!-- * koje fileove učitati, -->
<!-- * što sažeti, -->
<!-- * što odbaciti, -->
<!-- * kako pakirati repo, -->
<!-- * kako komprimirati history, -->
<!-- * što pokazati modelu. -->
<!--  -->
<!-- To je ogromna razlika između: -->
<!--  -->
<!-- * “AI razumije projekt” -->
<!--     i -->
<!-- * “AI je izgubljen”. -->
<!--  -->
<!-- Prompt orchestration -  ima: -->
<!-- * system promptove, -->
<!-- * hidden chain strukture, -->
<!-- * task decomposition promptove, -->
<!-- * reflection promptove, -->
<!-- * self-check promptove. -->
<!-- To su višeslojni prompt sistemi, ne jedan prompt. -->
<!--  -->
<!-- Autonomy loop -  ovo je posebno bitno. Loop izgleda: -->
<!-- * analiziraj, -->
<!-- * napravi promjenu, -->
<!-- * pokreni, -->
<!-- * vidi grešku, -->
<!-- * popravi, -->
<!-- * retry, -->
<!-- * validiraj, -->
<!-- * nastavi. -->
<!-- Kvaliteta tog loopa jako određuje kvalitetu agenta. -->
<!--  -->
<!-- Repo indexing / retrieval system - sigurno ima sofisticirani: -->
<!-- * semantic search, -->
<!-- * dependency graph, -->
<!-- * file relevance ranking, -->
<!-- * retrieval pipeline. -->
<!-- Da bi znao: -->
<!-- * koje fileove otvoriti, -->
<!-- * koje ignorirati. -->
<!--  -->
<!-- Diff / edit engine -  vrlo podcijenjeno. Nije isto: -->
<!--  -->
<!-- * generirati kod -->
<!--     i -->
<!-- * sigurno editirati postojeći repo. -->
<!--  -->
<!-- Bitno je: -->
<!-- * kako radi patching, -->
<!-- * kako spaja diffove, -->
<!-- * kako izbjegava corruption, -->
<!-- * kako čuva formatting, -->
<!-- * kako radi partial edits. -->
<!--  -->
<!-- Verification layer - vrlo važan dio modernih agenata. Sustav provjerava: -->
<!-- * build prolazi li, -->
<!-- * testovi prolaze li, -->
<!-- * lint prolazi li, -->
<!-- * runtime errori postoje li. -->
<!-- Bez toga agent često “samouvjereno halucinira”. -->
<!--  -->
<!-- Memory system - može biti: -->
<!-- * session memory, -->
<!-- * task memory, -->
<!-- * repo memory, -->
<!-- * preference memory. -->
<!-- To omogućuje dugotrajan rad bez gubitka konteksta. -->
<!--  -->
<!-- Safety / permission system - vrlo bitno za autonomne agente. -->
<!-- Sustav odlučuje: -->
<!-- * što agent smije izvršiti, -->
<!-- * kada mora pitati korisnika, -->
<!-- * što je opasno, -->
<!-- * što je readonly. -->
<!--  -->
<!-- UX layer - djeluje dobro i zato što: -->
<!-- * output izgleda smisleno, -->
<!-- * agent objašnjava što radi, -->
<!-- * flow djeluje prirodno, -->
<!-- * terminal UX je dobro dizajniran. -->
<!-- To dramatično mijenja percepciju kvalitete. -->
<!--  -->
<!--  -->
<!-- * model, -->
<!-- * agent logic, -->
<!-- * harness/runtime, -->
<!-- * tooling, -->
<!-- * context system, -->
<!-- * retrieval engine, -->
<!-- * prompting architecture, -->
<!-- * autonomy engine, -->
<!-- * verification system, -->
<!-- * memory, -->
<!-- * permissions, -->
<!-- * UX. -->

<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- every day do utonomus automatic task when you check out all recent sessions and improve them to higher scale and better funcionality to evolve and do automatic autonomus  with selfcorrectio and do the improvement to system engine and project -->
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.
-->

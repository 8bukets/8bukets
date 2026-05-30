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

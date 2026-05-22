# Antigravity Architecture Proposals

This document maps the 12-layer AI Agent Architecture model to the current state of the Antigravity system, and proposes actionable improvements to align the project closer to the ideal state.

## 1. Agent - Behavior Logic
**Current State:**
- `antigravity/jules.ts` handles the overarching workflow decisions (`executeWorkCycle`, branch scanning, task assignment).
- `antigravity/services/react.ts` acts on textual goals by selecting available tools (Reasoning and Acting).
- Python `agents/react_agent.py` also handles logic but is largely deprecated in favor of TS/Next.js organisms.

**Proposals:**
- Standardize on `jules.ts` and `services/react.ts` for all decision-making logic, ensuring all legacy python loops are completely removed.
- Refine the 'ReAct' protocol to support branching logic natively instead of linear reasoning-action loops.

## 2. Harness - Execution/runtime layer
**Current State:**
- The Node.js environment acts as the harness, running the autonomous loop in `jules.ts` (`run_parallel.ts` and `run_daily.ts`).
- `child_process.execSync` and asynchronous calls are used to interact with the system.
- `antigravity/core.ts` orchestrates DB fetching and validations.

**Proposals:**
- Build a dedicated `Sandbox/Execution` wrapper around commands to capture errors gracefully and implement a standard `retry` policy for flaky tools.
- Track task state globally in memory (`data/work_orders.json` and `.jules_memory.json`).

## 3. Tooling layer
**Current State:**
- Deeply integrated into `services/` and `actions/`.
- Terminal and Git interactions are somewhat scattered (`execSync` calls in `jules.ts` and scripts like `fix_git.sh`).

**Proposals:**
- Extract all file system, git, and shell commands into a dedicated adapter pattern (`services/capabilities/*.ts`) to decouple capability from business logic.
- Remove raw `execSync` usage (flagged as `SECURITY_PERF_VULNERABILITY` by `evolution.ts`) and use robust async wrappers across all capabilities.

## 4. Context engineering
**Current State:**
- Context relies heavily on `KNOWLEDGE_MERGE.md`, `system_knowledge.json`, and `ai_agents_knowledge.md`.
- `antigravity/services/knowledge_observer.ts` ingests docs.
- The ReAct prompt currently pulls state from the core system (`core.healthCheck()`).

**Proposals:**
- Implement dynamic context compression: Avoid dumping huge log files into prompts.
- Build a context packager that only includes relevant file chunks based on the active task domain (Security, Performance, Frontend).

## 5. Prompt orchestration
**Current State:**
- Multi-layered prompts are beginning to take shape via ReAct (`services/react.ts`) and the Cognitive Evolution engine (`evolution.ts`).

**Proposals:**
- Separate Prompt Engineering into a distinct `prompts/` directory.
- Formalize hidden chains for task decomposition, reflections, and self-checks before finalizing code.

## 6. Autonomy loop
**Current State:**
- Defined in `jules.ts` (`executeWorkCycle`) and triggered via `scripts/execute_creation_cycle.ts` / Jenkins / `.github/workflows`.
- Follows: Analyze -> Make Change -> Run -> Validate.

**Proposals:**
- Enhance the 'Error/Fix/Retry' feedback loop. Currently, if an autonomous step fails, it often just logs an error. The system should intercept the error, self-correct, and retry.

## 7. Repo indexing / retrieval system
**Current State:**
- Partially handled by `KnowledgeObserver` and `jules.ts` branch scanning. No advanced semantic search yet.

**Proposals:**
- Implement a lightweight semantic search (e.g., using local embeddings or Supabase pgvector) to rank file relevance before attaching them to the context window.

## 8. Diff / edit engine
**Current State:**
- Agent directly writes to files or generates `.ts` files via `singularity.ts`.

**Proposals:**
- Build a strict Patching Engine (`services/edit_engine.ts`) that safely edits files using diffs, avoids corruption, preserves formatting, and handles AST-level partial edits instead of overwriting files completely.

## 9. Verification layer
**Current State:**
- Vitest handles testing (`npm test`).
- Continuous PR validation triggers via GitHub actions. Explorer (`explorer.ts`) checks system health.

**Proposals:**
- Integrate pre-commit and pre-push automated verification directly into the autonomy loop. The agent must verify its own build/lint/tests before committing (no "confident hallucinations").

## 10. Memory system
**Current State:**
- `.jules_memory.json` tracks pending autonomous tasks.
- `data/knowledge/system_knowledge.json` tracks project context.

**Proposals:**
- Formalize a 4-tier memory system:
  - Session Memory (current run),
  - Task Memory (`work_orders.json`),
  - Repo Memory (`system_knowledge`),
  - Preference Memory (User preferences/rules).

## 11. Safety / permission system
**Current State:**
- Zero-Secret Integrity and Tier-13 Root Access Keys (`SYSTEM_AUTH_TOKEN`, `ADMIN_AUTH_TOKEN`).
- Docker Network isolation (`app-network`).

**Proposals:**
- Add an explicit permission matrix for the agent (what is read-only, what requires manual approval).
- Introduce a "Dry Run" mode for the autonomy loop.

## 12. UX layer
**Current State:**
- Web Dashboard (`http://localhost:3000`) and terminal output logging.

**Proposals:**
- Enhance terminal UX with clearer progress bars and natural language explanations of what the agent is doing at each step.

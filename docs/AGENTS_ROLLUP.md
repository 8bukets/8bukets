# AI Ecosystem Rollup: 12-Layer Architecture Mapping

This document categorizes all active Antigravity components, Gemini CLI remote subagents, and Python agents into the 12-Layer AI Agent Architecture model.

## 1. Agent Logic (Behavior & Decision)
* **`antigravity/jules.ts`**: Core workflow orchestration (Analyze -> Route -> Act).
* **`.gemini/agents/chief_ai_officer.md` (CAIO)**: Global strategic planning and goal generation.
* **`.gemini/agents/duo_planner_agent.md`**: Multi-agent task breakdown and reasoning.
* **`antigravity/services/react.ts`**: Immediate reasoning loops for specific tasks.

## 2. Harness (Execution & Runtime)
* **`antigravity/run_parallel.ts` & `antigravity/run_daily.ts`**: The parallel runtime environments executing system crons.
* **`antigravity/core.ts`**: Fundamental validations and DB connection handler.

## 3. Tooling (Capabilities & Integrations)
* **`antigravity/services/git_provider.ts`**: Terminal/Git integrations.
* **`antigravity/services/docker.ts`**: Sandbox management and capability adapter for fleets.
* **`agents/sync_agent.py`**: Database sync integrations (psycopg2).
* **`agents/notification_agent.py`**: External webhook integration (Slack/Discord).

## 4. Context Engineering
* **`antigravity/services/knowledge.ts` & `antigravity/services/knowledge_observer.ts`**: Gathers docs, formats them, and decides what is relevant.
* **`.gemini/agents/resource_optimizer_agent.md`**: Summarizes system logs to create compressed state context for other models.

## 5. Prompt Orchestration
* **`.gemini/agents/` Directory YAMLs**: Hosts complex, hidden prompt chains for distinct personas (e.g. `gitlab_security_agent.md`, `backup_agent_prompt.md`).

## 6. Autonomy Loop
* **`scripts/execute_creation_cycle.ts`**: The continuous cycle (run -> evaluate -> evolve -> loop).

## 7. Retrieval System (Indexing)
* **Semantic Search missing, handled implicitly by `grep` flows.**
* **`antigravity/services/persistence.ts`**: Stores and retrieves past session states from Supabase.

## 8. Diff / Edit Engine
* **`antigravity/singularity.ts`**: Generates and scaffolds code cleanly.

## 9. Verification Layer
* **`antigravity/services/explorer.ts`**: Checks system and cloud simulation health before runs.
* **`.github/workflows/`**: Validates builds before they merge into the primary ecosystem.

## 10. Memory System
* **`.jules_memory.json`**: Task memory.
* **`data/knowledge/system_knowledge.json`**: Repo/context memory.
* **`data/work_orders.json`**: Action queue and preference memory.
* **`.gemini/agents/backup_agent_prompt.md`**: Explicit guardian of state memory.

## 11. Safety & Permissions
* **`antigravity/services/cognitive_security.ts`**: Active vulnerability scanning.
* **`.gemini/agents/gitlab_security_agent.md`**: CI/CD compliance enforcer.

## 12. UX Layer
* **Terminal output in `jules.ts`**: Emoji-rich, well-designed step logging for CLI operators.
* **Web Dashboards (Next.js)**: Output visualization layers (e.g. `http://localhost:3000`).

---
*Rollup successfully generated mapping available components to the 12 key capabilities.*

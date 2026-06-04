# ANTIGRAVITY AUTONOMOUS PROTOCOL

This document defines the formal operational protocols for the Jules agent and all contributing autonomous units within the Antigravity ecosystem.

## 1. Core Mandates (The Golden Rules)

1.  **Transparency**: Every autonomous modification must be preceded by a reasoning phase (ReAct: Thought -> Action -> Observation).
2.  **Traceability**: All autonomous git operations must include a roadmap tag (e.g., `[ROADMAP:PHASE-12]`) and an execution summary.
3.  **Integrity**: No autocorrection shall be applied without subsequent verification (e.g., build check, lint check, or unit test).
4.  **Safety**: Merging of Pull Requests (PRs) or Merge Requests (MRs) is permitted only if all CI checks pass and the internal "Cognitive Audit" returns a score > 0.9.

## 2. Autocorrection & Bug Fix Protocol

Agents must scan the codebase periodically for "Architectural Drift" and "Logical Vulnerabilities".

### Categories of Autonomous Fixes
-   **CRITICAL**: Security vulnerabilities (leaked tokens, sync props violations in Next.js). Fixed via direct commit to `main` with immediate notification.
-   **STANDARD**: Linting errors, unused imports, type mismatches (`any` to structured types). Fixed via autonomous PR.
-   **PREDICTIVE**: Refactoring large files (>150 lines), optimizing imports, performance tuning. Fixed via autonomous PR.

### Execution Loop
1.  **Observe**: Scan files in `antigravity/` and `software-review-platform/`.
2.  **Reason**: Use `ReActService` to determine if a fix is safe and necessary.
3.  **Execute**: Apply fix using `evolution.ts` logic.
4.  **Verify**: Run `npm run test` or `vitest`.

## 3. Pull Request (PR/MR) Lifecycle Protocol

Jules is empowered to manage the full lifecycle of PRs on GitHub and MRs on GitLab.

### PR Creation
-   Complex fixes or new features must be developed on a branch and submitted via PR.
-   PR descriptions must include the "Reasoning Trace" from the `ReActService`.

### PR Review & Audit
-   Jules will scan existing PRs (both human and agent-created).
-   **Audit Criteria**:
    -   Code complexity change.
    -   Test coverage impact.
    -   Adherence to `AGENTS.md` guidelines.
-   **Approval**: Jules may approve PRs that meet all audit criteria.

### PR Merging
-   Jules may autonomously merge PRs that:
    1.  Are approved by an agent or human.
    2.  Have passing CI/CD pipelines.
    3.  Do not contain "BREAKING CHANGE" markers unless specifically authorized.

## 4. Communication & Escalation

-   **Handshake**: Agents communicate state via the `data/work_orders.json` (Local) and MongoDB (Remote).
-   **Conflict Resolution**: In the event of a git merge conflict, the agent must abort the rebase and create a "RESOLVE_CONFLICT" work order for human intervention.
-   **Executive Briefing**: High-impact actions (merges, critical fixes) must be logged in `CONSOLIDATED_INTELLIGENCE.md`.

---
*Authorized by the Antigravity Autonomous Engine.*

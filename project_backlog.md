# Antigravity Ecosystem - Structured Backlog

Based on the local codebase health assessment, the following Work Items should be imported into GitLab. The local codebase is currently degraded due to Turbopack compilation failures, TypeScript issues, and missing credentials.

## 🚀 Epic 1: Project Stabilization and Build Recovery
**Description:** The primary repository build is failing due to out-of-memory errors and Next.js 16 Canary compilation issues (`TurbopackInternalError`). This epic covers all foundational fixes required to achieve a passing CI pipeline and stable local build.

### 🐛 Issue 1.1: Resolve Turbopack OOM and Compilation Errors
**Type:** Issue / Bug
**Description:**
- The `npm run build` process in `my-app` consistently runs out of memory (`JavaScript heap out of memory`).
- Turbopack trace reveals unintended file tracking (`Encountered unexpected file in NFT list`), specifically linking to `next.config.ts`, `antigravity/evolution.ts`, and `instrumentation.ts`.
- There is a possible infinite loop or recursive module graph generation within the `antigravity` core architecture.
**Tasks:**
- [ ] Profile memory usage during `npm run build`.
- [ ] Refactor `antigravity` dynamic imports to prevent circular dependencies in the Next.js compilation step.
- [ ] Isolate and temporarily disable `antigravity` cognitive systems to confirm if they are the source of the OOM crash.

### 🐛 Issue 1.2: Fix TypeScript and ESLint Violations
**Type:** Issue / Bug
**Description:**
- `npm run lint` yields over 125 problems (72 errors, 53 warnings).
- Frequent use of `any` types and unsafe functions.
- Missing explicit type definitions across `antigravity` core services.
**Tasks:**
- [ ] Replace `any` casts in `antigravity/core.ts` with explicit Zod schemas or interfaces.
- [ ] Fix unsafe function types in `antigravity/services/react.ts`.
- [ ] Ensure all local module imports use proper resolution (no `.ts` extensions).

### 🛠️ Issue 1.3: Resolve Test Suite Degradation
**Type:** Issue / Maintenance
**Description:**
- Vitest tests pass, but warn: `Missing production credentials. System running in limited observability mode.`
- Mock dependencies (e.g., `Jenkins`) emit warnings.
**Tasks:**
- [ ] Update `vitest.config.ts` (Fixed casting locally, needs permanent implementation).
- [ ] Setup a local `.env.test` file with mock database credentials for MongoDB and Supabase to remove test warnings.

## 🧠 Epic 2: Autonomous Core Refinement
**Description:** The "Antigravity" cognitive loops (evolution, optimization, synthesis) are active but appear to interfere with standard application behavior and generate recursive data structures.

### ✨ Issue 2.1: Graceful Degradation Implementation
**Type:** Issue / Feature
**Description:**
- If production credentials are missing or the database is unreachable, the system currently crashes or logs excessive errors.
- Implementing a proper fallback shell will allow the UI to render while the cognitive backend operates in a mocked mode.
**Tasks:**
- [ ] Review `autonomousFetch` in `antigravity/core.ts` and enhance the `Attempting Graceful Degradation` fallback to return stubbed objects rather than throwing unhandled rejections.

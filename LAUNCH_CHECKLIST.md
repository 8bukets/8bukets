# Launch Readiness Checklist

Living document, updated by the `daily-launch-prep` skill on each scheduled
run (see `.claude/skills/daily-launch-prep/SKILL.md`). Newest entries at the
top of each section. Move items between Open / In Progress / Done rather than
deleting history.

## Reliability

### Open
- Investigate the remaining 220 Dependabot alerts (8 critical, 116 high, 83
  moderate, 13 low) flagged on `main` — triage critical/high first, prefer
  non-breaking upgrades, flag anything needing a major bump instead of
  bumping blindly. (Surfaced 2026-09-14, not yet triaged.)

### Done
- 2026-09-14: Removed `.github/workflows/test_testservice.yml` (dead
  workflow referencing nonexistent `antigravity/services/testservice.*`).
- 2026-09-14: Removed the equivalent broken `test-testservice` job from
  `.gitlab-ci.yml` (this one had no path filter, so it failed every
  pipeline run, not just sat dormant).
- 2026-09-14: Added 6 missing `.gitlab-ci.yml` test jobs for services that
  had test files but no CI job: `collaboration`, `feedback_analysis`,
  `knowledge_observer`, `multi-service_orchestration_workflow`,
  `performance_monitoring`, `presence`.
- 2026-09-14: Removed dead code in `agents/gitkraken_evolution_agent.py`
  (a discarded first computation of branch_count/graph_depth/kraken_score).

## Security

### Open
- No secrets scan has been run against this repo's history (only against
  the working tree at commit time). Consider whether historical commits
  ever contained real credentials that need rotating.
- 220 Dependabot alerts — see Reliability section above; security and CI
  health overlap here.

## Infra

### Open
- Not yet verified: do the Cloudflare Workers (`8bukets`, `sor-8bukets`,
  and others seen failing in CI checks), Vercel project, and Netlify site
  (`inquisitive-cranachan-9302651`) actually build from a clean checkout of
  `main`? As of 2026-09-14 the Vercel check reports "Account is blocked"
  and the Netlify deploy preview fails — these look like account/billing
  issues outside the repo's own config, not build bugs, but that's an
  assumption worth re-checking if they're still failing.

## Product / Business (assessment only — see skill guardrails)

### Open
- Pricing page: not yet assessed.
- Terms of Service / Privacy Policy: not yet assessed.
- Signup / auth flow: not yet assessed.
- Payment provider integration (Stripe or similar): not yet assessed.
- Analytics / monitoring for a live product (vs. the internal market-scraper
  analytics this repo already has via `analytics.py`): not yet assessed.

---
_This checklist was seeded on 2026-09-14 based on findings from that day's
session; it is not itself an autonomous run's output._

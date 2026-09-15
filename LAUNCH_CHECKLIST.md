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
- 2026-09-14: Full fix/test/validate pass (commits `ae9e276`..`f54c19c`):
  fixed `Blackboard.update` API mismatch that broke every 2-arg caller
  across 7 test files and 2 production agents; migrated
  `IntelligenceAgent`/`ResearchAgent` off a stale signature that meant
  neither had ever actually run in the real orchestration cycle; fixed
  dead stakeholder-extraction regex in `CollaborationAgent`; fixed an
  XSS/markdown-injection gap and an ISO-date-parsing bug in
  `analytics.py`; repaired 2 scraper tests broken by earlier class
  renames; added a missing `ingest:forbes` npm script and fixed a real
  `ReferenceError` crash it surfaced in `observeKnowledge()`; added Jenkins
  parity with the GitLab test jobs; wired up 9 of 25 broken scheduled
  GitHub Actions workflows referencing a nonexistent
  `antigravity/workflows/` directory. Pytest went from a hard collection
  failure (0/45 runnable) to 40/45 passing (5 remaining failures are
  unimplemented-feature/network tests, not regressions).
- 2026-09-14: **Verified the GitKraken agent's fix actually works
  end-to-end** — ran `GitKrakenEvolutionAgent.run()` directly; the
  `Blackboard.update` fix above holds up in practice, not just in
  isolated tests.
- 2026-09-15: Gitignored `node_modules/` (it was fully committed with no
  `.gitignore` entry, so any `npm ci` on a different platform than
  whoever committed it produced thousands of spurious untracked/modified
  files). A full `git rm -r --cached node_modules` un-tracking is a
  separate, larger cleanup still available if wanted — not done yet.

### In Progress
- **16 of 25 broken scheduled GitHub Actions workflows remain unfixed**
  (see above) — either no backing service exists, or the backing service
  needs arguments a scheduled cron can't obviously supply. Needs a
  maintainer decision on intended behavior, not more guessing.
- A security-hardening branch `security/consolidate-ssrf-path-traversal-fixes`
  (commit `8da2bb4`) is pushed but **not yet opened as a PR** — it wires
  up an existing-but-unused `validate_output_path()` and a new
  `is_safe_url()` into `scraper.py`'s CLI (`--json`/`--csv`/`--txt` and
  `--url` were previously unvalidated: real path-traversal and SSRF gaps,
  confirmed exploitable end-to-end before the fix). Open a PR for this if
  one doesn't exist yet by the time this runs.

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

### Done
- 2026-09-14/15: `MONETIZATION_STRATEGY.md` (current plan) and
  `MONETIZATION_STRATEGY_ARCHIVE_2026-09-14.md` (prior plan, preserved)
  written — covers eightbukets' paywall, software-online-review.com's
  ads.txt/WordAds path, and why software-review-platform's monetization
  stays deferred to its own Phase 3.
- 2026-09-14: `ADS_COOKIES_AND_AUCTIONS_STUDY.md` written — clarifies
  ads.txt/AdSense (publisher side, what this org actually runs) vs.
  Google Ads auctions (advertiser side, not currently used anywhere in
  this org), plus GDPR cookie-consent obligations from the 30+ ad
  exchanges declared in software-online-review.com's ads.txt.
- 2026-09-14: A working, drop-in GDPR cookie-consent script was built and
  demoed (published as a Claude Artifact, not committed to this repo) —
  points out software-online-review.com is a WordPress.com Simple-plan
  site with no sitewide custom-script injection, so actually deploying it
  needs a plan upgrade or per-page Custom HTML blocks first.

### Open
- Pricing page: not yet assessed.
- Terms of Service / Privacy Policy: not yet assessed.
- Signup / auth flow: not yet assessed.
- Payment provider integration (Stripe or similar): not yet assessed.
- Analytics / monitoring for a live product (vs. the internal market-scraper
  analytics this repo already has via `analytics.py`): not yet assessed.
- ads.txt sync (1,103 records, built 2026-09-14) still pending the human's
  manual "Synchronize Now" click in AdsTxtManager.
- WordAds enrollment for software-online-review.com not started — needs
  a WordPress.com Premium plan upgrade ($8/mo) but only after confirming
  the site's actual traffic clears WordAds' minimum threshold.

---
_This checklist was seeded on 2026-09-14 based on findings from that day's
session; it is not itself an autonomous run's output._

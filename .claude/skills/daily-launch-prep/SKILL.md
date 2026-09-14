---
name: daily-launch-prep
description: Daily autonomous pass over this repo to improve system health (CI, security, dead code, dependency risk) and track readiness to launch/monetize. Runs unattended once a day via a scheduled Routine.
---

# Daily Launch Prep

You are running unattended, once a day, with no memory of previous runs beyond
what is committed in this repository. `LAUNCH_CHECKLIST.md` at the repo root
is your memory — read it first, update it every run.

## What this repo is

The Markposition Scraper & Analytics system ("Antigravity" ecosystem) —
see `.antigravity/mission.md` and `.antigravity/rules.md` for the mission and
cross-agent cooperation rules (this repo is also worked on by Jules and
Gemini-based agents; follow those rules too). It has real, live-deployed
infrastructure already pointed at it: Cloudflare Workers (`8bukets`,
`sor-8bukets`, and others), Vercel, Netlify, Supabase, and Docker Hub —
this is the closest thing to an actual product among this org's repos,
branded across markposition.wordpress.com, software-online-review.com,
and dbcode.io.

## Hard guardrails — never cross these

1. **Never merge your own PRs, and never push to `main` directly.** Every
   change goes out as a pull request for a human to review and merge.
2. **Never author final pricing, legal (ToS/privacy/licensing), or payment
   integration content.** You may draft a checklist item describing what's
   missing and why ("no Terms of Service page; needed before accepting
   signups") and even a rough draft for a human to rewrite, but never treat
   such a draft as ready to ship, and say explicitly in the PR that it needs
   a human/legal review — don't let it read as finished copy.
3. **Never commit secrets, API keys, or real credentials** — this repo's
   `.env.example` documents what's expected; real values never belong in
   git.
4. **Never touch billing/payment provider configuration** (Stripe keys,
   webhook secrets, pricing tiers in code) beyond noting gaps in the
   checklist. Money-moving code changes need a human driving, not a
   scheduled agent.
5. If GitHub Actions CI is already red on `main` for reasons unrelated to
   your change, don't widen your PR to fix unrelated systems unless it's a
   small, clearly-correct fix (same bar as any other CI-red rule) — note it
   in the checklist instead and move on.
6. Keep the diff proportionate to one day's work. This is a daily drip, not
   a rewrite — prefer several small, focused PRs over the long run to one
   sprawling one.

## Each run, in order

1. **Orient**: `git log --oneline -20` on `main` and read `LAUNCH_CHECKLIST.md`
   to see what prior runs found, fixed, and left open. Skip anything already
   marked done unless you have reason to re-check it (e.g. it regressed).
2. **Health pass** — pick ONE or TWO concrete, verifiable things from this
   repo's real state, not speculative busywork:
   - CI/CD: is `.github/workflows/*` and `.gitlab-ci.yml` green and internally
     consistent? (This exact class of bug has been found and fixed before —
     jobs/workflows referencing files that don't exist.)
   - Dependency security: `npm audit` / check for GitHub Dependabot alerts
     (this repo had 220 open alerts, 8 critical, as of the last check —
     prioritize critical/high ones with available non-breaking fixes; note
     ones that need a major version bump rather than bumping blindly).
   - Dead code / broken references: things like the GitKraken agent's
     dead computation found and removed previously — grep for other
     obviously-unused variables, unreachable branches, or TODO/FIXME markers
     that indicate known-incomplete work.
   - Test coverage gaps: services with a `.test.ts` file that isn't wired
     into either CI config, or vice versa.
3. **Monetization-readiness check** — review against the checklist's
   "Launch readiness" section (below) and update it: what's present, what's
   missing, what's a blocker vs. nice-to-have. This is assessment and
   documentation, not implementation of payment/legal systems (see
   guardrails).
4. **Implement** the health-pass finding(s) from step 2 as an actual code/config
   change, validated locally as far as this environment allows (lint, type
   check, unit tests for the specific area touched — don't claim CI will
   pass without some local evidence).
5. **Update `LAUNCH_CHECKLIST.md`**: move items between Open/In Progress/Done,
   add anything newly discovered, with today's date.
6. **Ship it**: create a branch named `daily-launch-prep/YYYY-MM-DD` off the
   current `main`, commit (small, well-described commits), push, and open a
   PR against `main` yourself (don't rely on anyone else to create it) with a
   summary of what changed and why, and what's still open on the checklist.
   End the PR body with:
   ```
   🤖 Generated with [Claude Code](https://claude.com/claude-code)
   ```
7. If there is truly nothing actionable (rare — the checklist should almost
   always have something), say so in your final summary rather than forcing
   a low-value change, and don't open an empty PR.

## Launch readiness categories (track in LAUNCH_CHECKLIST.md)

- **Reliability**: CI green, no dead/broken workflow jobs, tests actually
  covering the services that exist.
- **Security**: dependency vulnerabilities triaged, no secrets in git,
  `.env.example` matches what code actually reads from the environment.
- **Infra**: the deployed Workers/Vercel/Netlify projects build from a clean
  checkout; deployment configs match what's actually in the repo.
- **Product/business** (assessment only, per guardrail #2): domain and SSL
  status, whether there's a real pricing page, ToS/privacy presence,
  signup/auth flow, payment provider integration status, analytics/monitoring
  in place. Document gaps; don't build the business logic unattended.

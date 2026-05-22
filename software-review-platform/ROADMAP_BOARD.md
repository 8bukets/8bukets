# Roadmap Board

## Goal

Translate the roadmap into a practical execution board format for GitHub Projects, Notion, or a lightweight task tracker.

## Recommended Columns

- Backlog
- MVP
- Phase 2
- Phase 3
- In Progress
- Review
- Done

## MVP Cards

- Verify local Docker startup
- Replace hardcoded env values
- Add backend healthcheck endpoint
- Validate auth flow end to end
- Stabilize review submission flow
- Complete admin moderation workflow
- Replace placeholder moderation logic

## Phase 2 Cards

- Add software search and filtering
- Add review analytics and aggregate metrics
- Integrate transactional email notifications
- Improve SEO for software and review pages
- Add abuse protection and rate limiting
- Prepare staging and production deployment config
- Add basic admin dashboard metrics

## Phase 3 Cards

- Add company profiles
- Add vendor-owned software pages
- Introduce verified reviewer flow
- Add AI-assisted trust scoring
- Add subscriptions and monetization groundwork
- Add featured listings and promotional placements
- Add reviewer reputation and contribution history
- Build content and SEO publishing pipeline

## Suggested First Sprint

The first focused execution sprint should prioritize:

1. local startup reliability
2. auth and review flow reliability
3. moderation stability
4. deployment readiness

## Suggested Second Sprint

After MVP stability:

1. seed content quality
2. launch workflow
3. traffic handoff from the current site
4. search and analytics basics

## Suggested Third Sprint

After launch validation:

1. trust layer improvements
2. vendor angle preparation
3. monetization groundwork

## Definition Of Done

Use the same rule for all cards:

- code or content change is complete
- main flow is manually tested
- setup or behavior is documented
- no new hardcoded secret or environment assumptions are introduced

## Working Guidance

- keep one clear source of truth for active work
- move items to Review only when they are actually testable
- avoid starting Phase 2 work before MVP flows are stable

# Launch Checklist

## Goal

Prepare `software-review-platform` for a safe first production-style rollout at `app.software-online-review.com`.

## Recommended Rollout Model

- keep `software-online-review.com` as the current public content layer
- launch the review application separately on `app.software-online-review.com`
- route users from the live site into the app through clear calls to action

## Phase 1: Local Validation

Before deploying anything, confirm the MVP works end to end.

### App

- backend installs successfully
- frontend installs successfully
- Docker Compose starts without manual fixes
- database initializes correctly
- health endpoint returns success

### Auth

- user registration works
- admin registration with invite code works
- login returns a valid JWT
- protected routes reject unauthorized requests

### Review Flow

- software list loads
- software detail page loads
- review submission works
- review lands in pending status
- admin can approve and reject reviews
- approved reviews become visible publicly

### Engagement Flow

- comments can be added
- review ratings can be added
- invalid input is handled safely

## Phase 2: Environment Setup

Create a production-ready environment configuration.

### Backend

- set a production JWT secret
- set production database connection string
- set admin invite code through environment variables
- confirm CORS configuration

### Frontend

- set production API base URL
- confirm any public environment values
- confirm correct domain assumptions

### Secrets

- do not commit production secrets
- use platform secret storage
- verify no service account keys are exposed in the deploy path

## Phase 3: Infrastructure

Pick one clean deploy path and keep it simple.

### Suggested Starter Stack

- frontend: Vercel
- backend: Railway or Render
- database: Supabase or managed Postgres

### Minimum Requirements

- HTTPS enabled
- production database reachable only as needed
- backend reachable from frontend
- environment variables set correctly
- deployment logs accessible

## Phase 4: Domain and Routing

Prepare the public routing model.

### Preferred Domain

- `app.software-online-review.com`

### Required Tasks

- add DNS record for the app subdomain
- connect deployment target to the subdomain
- verify SSL certificate issuance
- verify frontend routes work on the final domain
- verify API requests use the production backend

## Phase 5: Content Bridge

Connect the current live site to the new app.

### Add To Existing Site

- a “Browse software reviews” CTA
- a “Write a review” CTA
- one landing page explaining the new product
- one featured software or featured review section
- clear navigation link into the app

## Phase 6: Launch Content

Seed the app with enough content to feel real.

### Minimum Seed

- 10 to 20 software entries
- a few approved reviews
- one admin account
- one clear homepage message
- at least one category or grouping strategy

## Phase 7: Security Review

Do a small but real pre-launch hygiene pass.

- verify no credentials are committed in active deploy paths
- confirm `.env` values are not hardcoded into source
- add rate limiting plan for auth and submission routes
- confirm admin-only moderation routes are protected
- review logs for accidental sensitive output

## Phase 8: Smoke Test In Production

Test the live system after deployment.

### Must Pass

- homepage loads
- login works
- software list works
- software detail works
- review submit works
- moderation works
- comments work
- ratings work

## Phase 9: Soft Launch

Start with controlled exposure.

- link the app from the current site
- avoid announcing it broadly before smoke testing
- watch logs and moderation behavior
- collect early feedback from real usage

## Phase 10: First Post-Launch Priorities

After launch, focus on reliability and clarity before adding complexity.

- fix runtime and UX issues
- improve error handling
- clean up onboarding copy
- tighten moderation workflow
- add healthchecks and metrics if still missing

## Exit Criteria

The app is ready for broader rollout when:

- core flows work consistently
- production config is stable
- moderation is reliable
- the live site sends traffic into the app
- software pages feel structured and intentional

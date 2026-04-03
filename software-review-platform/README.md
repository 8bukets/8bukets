# Software Review Platform

Software Review Platform is a full-stack starter for a trust-focused software review product.

![Stack](https://img.shields.io/badge/stack-Next.js%20%7C%20Express%20%7C%20PostgreSQL-black)
![Auth](https://img.shields.io/badge/auth-JWT-brown)
![Status](https://img.shields.io/badge/status-MVP-orange)
![Moderation](https://img.shields.io/badge/moderation-admin%20workflow-blue)

It includes software listings, user authentication, review submission, moderation, comments, ratings, and a clean foundation for future trust, vendor, and monetization features.

## Overview

This project is designed as an MVP base for building a modern software review platform with structured discovery, transparent moderation, and extensible product architecture.

## Stack

- Next.js
- Express
- PostgreSQL
- JWT authentication
- Docker Compose

## Current Features

- software listing pages
- user registration and login
- review submission flow
- admin moderation flow
- comments on reviews
- review ratings
- local database bootstrap

## Project Structure

```text
software-review-platform/
  backend/
    src/
      server.js
      controllers/
      db/
      middleware/
      routes/
      utils/
  frontend/
    pages/
    components/
    lib/
    services/
    styles/
  docker-compose.yml
```

## Local Setup

1. Install frontend and backend dependencies.
2. Configure environment variables.
3. Start the stack with Docker Compose.
4. Create a user or admin account.
5. Test review, moderation, comment, and rating flows.

Health check:

- backend health: `GET /api/health`

## Demo Seed

After running the database init file, the project includes:

- a seeded software catalog
- approved reviews
- comments and ratings
- one pending review for admin moderation testing

Seeded demo accounts:

- user: `demo-user@software-review-platform.local`
- admin: `demo-admin@software-review-platform.local`

The SQL seed uses placeholder password hashes for these accounts. For a real local run, create fresh accounts through the app after bootstrapping the database.

## Documentation

- [PRODUCT.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/PRODUCT.md) for the product brief, user flows, and roadmap
- [PITCH.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/PITCH.md) for the investor narrative and 5-minute pitch script
- [MIGRATION.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/MIGRATION.md) for the migration plan from the live site to the new app
- [LAUNCH_CHECKLIST.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/LAUNCH_CHECKLIST.md) for the step-by-step rollout checklist for `app.software-online-review.com`
- [LAUNCH_RUNBOOK.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/LAUNCH_RUNBOOK.md) for the exact Vercel + Railway + Supabase launch sequence
- [DEPLOYMENT.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/DEPLOYMENT.md) for the recommended first production deployment path
- [SEED_CONTENT_PLAN.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/SEED_CONTENT_PLAN.md) for the first software profiles, reviews, and structured launch content
- [GO_TO_MARKET.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/GO_TO_MARKET.md) for the soft-launch and traffic handoff plan from the existing live site
- [CONTENT_AUDIT.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/CONTENT_AUDIT.md) for the keep/rewrite/archive review of existing `software-online-review.com` content patterns
- [FIRST_10_SOFTWARE.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/FIRST_10_SOFTWARE.md) for a concrete first batch of software profiles to seed into the platform
- [ADMIN_OPS.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/ADMIN_OPS.md) for the day-to-day moderation and platform operations workflow
- [REVIEW_GUIDELINES.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/REVIEW_GUIDELINES.md) for review quality standards and moderation policy
- [ENV_TEMPLATE.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/ENV_TEMPLATE.md) for production environment variable mapping across frontend, backend, and hosting
- [TEST_PLAN.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/TEST_PLAN.md) for manual smoke testing and launch verification
- [ROADMAP_BOARD.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/ROADMAP_BOARD.md) for a GitHub Projects-style execution board
- [COPY_GUIDE.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/COPY_GUIDE.md) for homepage, CTA, and onboarding copy suggestions
- [API_CONTRACT.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/API_CONTRACT.md) for the current backend route surface and expected request/response shapes
- [DATA_MODEL.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/DATA_MODEL.md) for the core entities and relationships behind the platform
- [OPEN_QUESTIONS.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/OPEN_QUESTIONS.md) for unresolved product and implementation decisions
- [KNOWLEDGE_MERGE.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/KNOWLEDGE_MERGE.md) for the canonical mapping between Antigravity, Project SOR, the live domain, and the new platform
- [REPO_CLASSIFICATION.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/REPO_CLASSIFICATION.md) for the keep/migrate/archive workspace view
- [SECURITY_NOTES.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/SECURITY_NOTES.md) for repo hygiene and sensitive file follow-up

## Development Goals

- make software reviews more credible and structured
- support transparent moderation workflows
- create a strong base for trust and discovery features
- keep the architecture simple enough for fast iteration

## Roadmap

### MVP

- verify local Docker startup
- replace hardcoded env values
- add healthcheck endpoints
- validate auth flow end-to-end
- stabilize review submission and detail flow
- complete admin moderation workflow
- replace placeholder moderation logic

### Phase 2

- add software search and filtering
- add review analytics and aggregate metrics
- integrate transactional email notifications
- improve SEO for software and review pages
- add abuse protection and rate limiting
- prepare deployment configuration for staging and production
- add basic admin dashboard metrics view

### Phase 3

- add company profiles and vendor-owned software pages
- introduce verified reviewer flow
- add AI-assisted trust scoring for reviews
- add vendor subscriptions and monetization groundwork
- build featured listings and promotional placements
- add reviewer reputation and contribution history
- create a go-to-market content and SEO publishing pipeline

## Status

This repository currently provides an MVP starter and should be treated as a foundation for further iteration, testing, and deployment hardening.

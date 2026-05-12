# Migration Plan

## Goal

Move `software-online-review.com` from its current content-heavy site structure toward a dedicated software review product without breaking the live site.

## Current State

The live domain currently behaves more like a WordPress-based content hub than a structured review application.

Observed characteristics:

- mixed blog and content structure
- broad category coverage
- many unrelated or loosely related posts
- limited product-style review workflow
- no clear trust-first review UX

This means the migration should be gradual, not a full immediate replacement.

## Recommended Strategy

Use a parallel rollout instead of a big-bang rewrite.

Recommended structure:

- keep the current WordPress site as the content and discovery layer
- deploy the new review app as a separate application layer
- connect the two through navigation, CTAs, and shared branding

## Best Deployment Option

Preferred:

- `app.software-online-review.com`

Alternative:

- `software-online-review.com/app`

Why the subdomain is preferred:

- cleaner separation between WordPress and the app
- simpler deployment and infrastructure boundaries
- lower migration risk
- easier rollback if needed

## Phase 1: Stabilize MVP

Goal: make sure the new app works independently before introducing traffic.

Checklist:

- verify local Docker startup
- confirm database initialization
- validate register and login
- validate admin setup
- validate review submission
- validate moderation approve and reject flow
- validate comments and ratings
- add healthcheck endpoint
- remove hardcoded env assumptions

## Phase 2: Deploy the App in Parallel

Goal: make the review product live without replacing the current site.

Suggested deployment split:

- frontend: Vercel or static hosting layer
- backend: Railway, Render, or AWS ECS
- database: Supabase, Railway Postgres, or AWS RDS

Target domain:

- `app.software-online-review.com`

Phase 2 deliverables:

- live frontend
- live backend API
- production database
- production environment variables
- working auth and moderation flow

## Phase 3: Bridge Traffic from the Existing Site

Goal: make the current domain send users into the new review experience.

Add to the current live site:

- homepage CTA to browse software reviews
- CTA to write a review
- featured software section
- clear navigation link to the app
- landing page that explains the new platform

This allows the old site to become a traffic source instead of a competing structure.

## Phase 4: Content Audit and Classification

Goal: decide what content should remain, move, rewrite, or retire.

Classify current content into four buckets:

### Keep

Content that is useful for SEO, software discovery, or brand context.

### Rewrite

Content that has useful intent but should become structured software profile or landing page content.

### Archive

Content that is no longer useful for the new direction but may still have reference value.

### Ignore

Content that is unrelated to the future product direction.

## Phase 5: Product Positioning Cleanup

Goal: make the public identity of the site clear.

The live site should stop feeling like a broad experimental content space and start feeling like a focused software review product.

Required cleanup:

- define a clear homepage message
- align branding between content site and app
- separate blog content from review product flows
- explain trust, moderation, and review value clearly

## Phase 6: Structured Data Migration

Goal: move from article-style content to product-style entities.

The long-term app should rely on structured records, not WordPress post content.

Key entity targets:

- software records
- user accounts
- reviews
- ratings
- comments
- moderation records

Practical recommendation:

- do not bulk-import everything from WordPress
- manually curate the first set of software entries
- build clean software profiles in the app database

## Phase 7: Decide the Final Site Model

After the app proves itself, choose one of two long-term directions.

### Option A: WordPress + App

Use WordPress for content and SEO.

Use the review app for:

- software discovery
- review workflows
- moderation
- future vendor tooling

### Option B: App-First

Move the product center of gravity into the app and reduce WordPress to a blog or archive role.

Recommended for now:

- Option A

This is lower-risk and better aligned with the current live site state.

## Minimal Rollout Order

1. stabilize the MVP locally
2. deploy the app to a subdomain
3. connect the current site to the app with CTAs
4. create the first 10 to 20 structured software entries
5. test real review and moderation behavior
6. decide whether to expand or consolidate

## What Not to Do First

- do not migrate all WordPress content immediately
- do not replace the live site in one step
- do not add unnecessary infrastructure complexity too early
- do not treat old post content as if it were already structured product data

## Success Criteria

The migration is working if:

- the new app runs reliably in production
- users can browse and submit reviews
- moderation works consistently
- the current site sends traffic into the app
- software profiles become structured and repeatable
- the product story becomes clearer over time

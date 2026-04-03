# Deploy Handoff

## Purpose

This document is the single starting point for resuming deployment work on `software-review-platform`.

Use it when you want the shortest path from current project state to a real soft launch on `app.software-online-review.com`.

## Current State

The project is in a strong MVP starter state.

What is already done:

- backend auth, reviews, moderation, comments, and ratings flow
- frontend listing, software detail, review detail, login, register, create review, and admin pages
- health endpoint
- launch seed catalog with demo reviews, comments, ratings, and moderation data
- search, category filtering, and sort on the homepage
- launch, migration, product, and operations documentation
- backend test coverage for validation, auth, middleware, moderation access, health, and software query behavior

## Verified In This Session

The following checks were run successfully in the clean PR worktree:

- `cd backend && npm test`
- `cd backend && npm run check`
- `cd frontend && npm run check`

Confirmed results:

- backend tests pass
- backend bootstrap check passes
- frontend production build passes
- homepage, admin, login, register, create review, software detail, and review detail routes build successfully

## Deploy-Ready Improvements Already Included

- provider-friendly bind behavior in the backend when `HOST` is not set
- `CORS_ORIGIN` support as the primary backend CORS variable
- centralized frontend API base URL config
- graceful homepage fallback if the backend API is temporarily unavailable
- repeatable local DB reset helper

## Recommended Production Stack

- frontend: Vercel
- backend: Railway
- database: Supabase Postgres
- app domain: `app.software-online-review.com`

## Required Production Variables

### Backend

- `DATABASE_URL`
- `JWT_SECRET`
- `ADMIN_INVITE_CODE`
- `PORT`
- `CORS_ORIGIN`

Optional:

- `HOST`
- `NODE_ENV`

### Frontend

- `NEXT_PUBLIC_API_URL`

## What Still Needs Real Platform Access

These steps cannot be completed from the current sandbox alone:

- create the Supabase production database
- run the production schema and seed
- create the Railway service and set backend variables
- create the Vercel project and set frontend variables
- connect `app.software-online-review.com`
- verify live HTTPS and DNS
- run the production smoke test against deployed services

## Exact Next Deployment Steps

1. Create a Supabase Postgres project and copy the production `DATABASE_URL`.
2. Create a Railway service pointing to `software-review-platform/backend`.
3. Set Railway variables:
   - `DATABASE_URL`
   - `JWT_SECRET`
   - `ADMIN_INVITE_CODE`
   - `PORT`
   - `CORS_ORIGIN=https://app.software-online-review.com`
4. Deploy the backend and verify `GET /api/health`.
5. Create a Vercel project pointing to `software-review-platform/frontend`.
6. Set `NEXT_PUBLIC_API_URL` to the deployed backend API URL plus `/api`.
7. Deploy the frontend and verify homepage plus auth pages.
8. Connect `app.software-online-review.com` in Vercel.
9. Run the production smoke test from [LAUNCH_RUNBOOK.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/LAUNCH_RUNBOOK.md).
10. Add CTA links from the current live site to the new app.

## Start Here

If you are picking this up later, open these in order:

1. [DEPLOY_HANDOFF.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/DEPLOY_HANDOFF.md)
2. [LAUNCH_RUNBOOK.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/LAUNCH_RUNBOOK.md)
3. [DEPLOYMENT.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/DEPLOYMENT.md)
4. [ENV_TEMPLATE.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/ENV_TEMPLATE.md)

## Recommended Stop Point For Today

The codebase is deploy-prepared.

The next session should start with real platform setup, not more local refactoring.

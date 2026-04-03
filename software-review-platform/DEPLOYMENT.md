# Deployment Guide

## Goal

Deploy `software-review-platform` with the smallest practical production setup for a first live release.

## Recommended Starter Stack

For the first real deployment, keep the architecture simple:

- frontend: Vercel
- backend: Railway or Render
- database: managed PostgreSQL
- public app domain: `app.software-online-review.com`

This balances speed, cost, and operational simplicity.

## Deployment Model

### Frontend

Deploy the Next.js frontend as its own service.

Recommended target:

- Vercel

Responsibilities:

- render the UI
- handle frontend routes
- call the backend API

### Backend

Deploy the Express API as its own service.

Recommended targets:

- Railway
- Render

Responsibilities:

- auth
- software data
- review submission
- moderation
- comments and ratings

### Database

Use managed PostgreSQL.

Recommended targets:

- Supabase Postgres
- Railway Postgres
- Render Postgres
- AWS RDS if you want more control

## Domain Plan

Use this split:

- `software-online-review.com` for the current live content site
- `app.software-online-review.com` for the review application

This keeps migration risk low and makes rollback easier.

## Environment Variables

## Backend

Minimum expected variables:

- `DATABASE_URL`
- `JWT_SECRET`
- `ADMIN_INVITE_CODE`
- `PORT`
- `CORS_ORIGIN`

Recommended notes:

- use a long random JWT secret
- set CORS to the real frontend domain
- do not hardcode secrets in source files

## Frontend

Minimum expected variables:

- public API base URL
- any frontend-exposed runtime config used by the app

Recommended notes:

- point the frontend to the deployed backend API
- verify no localhost assumptions remain

## Database Setup

Before app launch:

1. create the production database
2. run the schema setup from the project SQL
3. seed the first software records
4. create an admin path through the invite code

Recommended approach:

- keep initial seed small and intentional
- do not migrate raw WordPress content directly into the relational model

## Backend Deployment Steps

1. connect the repository to Railway or Render
2. set the service root to the backend folder if needed
3. install dependencies
4. set environment variables
5. deploy
6. verify the health endpoint

Post-deploy checks:

- backend starts without errors
- database connection works
- auth routes respond correctly
- review routes respond correctly

## Frontend Deployment Steps

1. connect the repository to Vercel
2. set the project root to the frontend folder if needed
3. configure environment variables
4. deploy
5. verify homepage, software pages, and auth flows

Post-deploy checks:

- frontend loads without API errors
- auth flow uses the production backend
- software list and detail pages render correctly

## DNS Setup

For `app.software-online-review.com`:

1. create the DNS record required by your frontend host
2. verify the domain in the hosting provider
3. wait for SSL issuance
4. confirm that requests resolve correctly over HTTPS

## Production Smoke Test

Run these checks after both services are live:

- homepage loads
- login works
- register works
- software list loads
- software detail page loads
- review submission works
- moderation works
- comments and ratings work

## Logging and Monitoring

At minimum, make sure you can access:

- backend deploy logs
- frontend deploy logs
- database connection errors
- runtime request errors

For the first release, basic platform logs are enough.

## Security Basics

Before launch:

- confirm no secrets are committed
- confirm JWT secret is production-safe
- confirm admin invite code is not public
- confirm moderation routes are protected
- add rate limiting as soon as possible

See also:

- [SECURITY_NOTES.md](/Users/filipkeser/Documents/MapAntigravity/software-review-platform/SECURITY_NOTES.md)

## Rollback Strategy

The safest rollback path is simple:

- keep `software-online-review.com` unchanged
- disable links to the app if needed
- roll back frontend or backend independently

Because the app is deployed on a subdomain, rollback risk is lower than replacing the current live site directly.

## Recommended Release Order

1. deploy backend
2. verify backend health
3. deploy frontend
4. connect app subdomain
5. run production smoke test
6. link to the app from the current site
7. soft launch to controlled traffic

## Next Infrastructure Upgrades

After the first stable launch, consider:

- rate limiting
- email delivery provider
- search indexing
- analytics and admin metrics
- background jobs for moderation or notifications

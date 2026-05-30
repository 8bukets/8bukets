# Test Plan

## Goal

Provide a simple manual test plan for validating the MVP before and after launch.

## Local Smoke Test

Use this before any deployment.

### Setup

- backend dependencies installed
- frontend dependencies installed
- database available
- environment variables configured

### Basic Checks

- backend starts
- frontend starts
- database connects successfully
- no immediate startup errors appear

Practical command checks:

- `cd backend && npm run check`
- `cd frontend && npm run check`

## Auth Flow

### Register User

1. Open the app
2. Register a normal user
3. Confirm registration succeeds

Expected:

- user can log in afterward
- no server errors

### Register Admin

1. Register with the admin invite code
2. Confirm admin registration succeeds

Expected:

- admin account can access moderation routes

### Login

1. Log in with valid credentials
2. Try protected actions

Expected:

- auth token is accepted
- protected routes work
- invalid login is rejected cleanly

## Software Flow

### Software List

1. Open the homepage or software list
2. Confirm seeded software appears

Expected:

- list renders correctly
- links to detail pages work

### Software Detail

1. Open a software detail page
2. Confirm description and review section appear

Expected:

- page loads
- review area is visible
- empty states are understandable if no reviews exist

## Review Flow

### Submit Review

1. Log in as a normal user
2. Submit a review with a score

Expected:

- submission succeeds
- review is stored in pending state
- user receives a clear result

### Moderate Review

1. Log in as admin
2. Open moderation queue
3. Approve or reject the review

Expected:

- queue updates correctly
- approved reviews appear publicly
- rejected reviews are not publicly visible

## Comment and Rating Flow

### Add Comment

1. Open a review detail page
2. Submit a comment

Expected:

- comment is stored
- comment appears correctly

### Add Rating

1. Submit a rating for a review

Expected:

- rating is stored
- page reflects the rating state correctly

## Access Control Checks

- unauthenticated users cannot submit reviews
- unauthenticated users cannot access admin moderation
- non-admin users cannot approve or reject reviews

## Error Handling Checks

Test a few intentional failures:

- wrong login password
- missing review content
- invalid score
- unauthorized moderation request

Expected:

- errors are user-readable
- app does not crash
- API returns predictable status behavior

## Production Smoke Test

Repeat this after deployment:

- homepage loads on production domain
- login works
- software pages load
- review submit works
- moderation works
- comments work
- ratings work
- no obvious broken links

## Verified In This Workspace

The following checks have already been confirmed in this environment:

- backend bootstrap passes with `NO_LISTEN=1`
- frontend production build passes with `next build`

The following checks were not confirmed here because Docker is unavailable in this environment:

- `docker compose up --build`
- full live database-backed browser flow

## Launch Readiness Check

The MVP is ready for soft launch when:

- auth works reliably
- seeded software pages feel intentional
- moderation works
- at least one full review lifecycle has been tested end to end

# Launch Runbook

## Stack

- Frontend: Vercel
- Backend: Railway
- Database: Supabase Postgres
- App domain: `app.software-online-review.com`

## 1. Create the Database

In Supabase:

1. Create a new project
2. Create or confirm the Postgres database
3. Copy the connection string
4. Run the SQL schema from the project database setup file
5. Seed the initial software records

Required output:

- working `DATABASE_URL`

## 2. Deploy the Backend

In Railway:

1. Create a new project
2. Connect the GitHub repository
3. Point the service to the backend app
4. Set environment variables:
   - `DATABASE_URL`
   - `JWT_SECRET`
   - `ADMIN_INVITE_CODE`
   - `PORT`
   - `CORS_ORIGIN`
   - `HOST` only if your platform requires an explicit bind host
5. Deploy the service
6. Verify the backend health route

Backend checks:

- app starts successfully
- database connection works
- auth endpoints respond
- review endpoints respond

## 3. Deploy the Frontend

In Vercel:

1. Create a new project
2. Connect the GitHub repository
3. Point the project to the frontend app
4. Set the frontend environment variable for the API base URL
5. Deploy the app
6. Verify the homepage and main routes

Frontend checks:

- homepage loads
- software pages load
- no localhost API assumptions remain
- auth requests hit the deployed backend

## 4. Connect the Domain

For `app.software-online-review.com`:

1. Add the DNS record required by Vercel
2. Assign the subdomain in Vercel
3. Wait for SSL issuance
4. Confirm the app loads on the final domain

Checks:

- HTTPS works
- final domain resolves correctly
- frontend still connects to the correct backend

## 5. Configure Access and Security

Before public traffic:

- confirm `JWT_SECRET` is production-safe
- confirm `ADMIN_INVITE_CODE` is not public
- confirm `CORS_ORIGIN` matches the frontend domain
- confirm no secrets are hardcoded in code
- verify admin-only moderation routes are protected

## 6. Run Production Smoke Test

Must pass:

- register works
- login works
- software list loads
- software detail loads
- review submission works
- pending moderation appears
- admin approve and reject works
- comments work
- ratings work

## 7. Seed Launch Content

Before linking traffic:

- create the first 10 software profiles
- approve the first 5 to 10 reviews
- verify categories look intentional
- confirm no obvious empty pages exist

## 8. Connect the Existing Site

On `software-online-review.com` add:

- `Browse software reviews` CTA
- `Write a review` CTA
- one landing page explaining the app
- internal links to selected software pages

## 9. Soft Launch

Do not do a full announcement yet.

Instead:

- route controlled traffic from the current site
- monitor logs
- watch moderation volume
- watch for broken routes or auth issues
- fix UX friction quickly

## 10. First Week Priorities

After launch:

- fix runtime and API issues first
- improve onboarding copy
- improve moderation clarity
- strengthen software profile quality
- add missing health or monitoring basics

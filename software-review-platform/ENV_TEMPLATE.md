# Environment Template

## Goal

Map the most important environment variables for local development and first production deployment.

## Backend Variables

### Required

- `DATABASE_URL`
- `JWT_SECRET`
- `ADMIN_INVITE_CODE`

### Common

- `PORT`
- `CORS_ORIGIN`
- `NODE_ENV`

## Backend Notes

### DATABASE_URL

Use the full managed Postgres connection string from your database provider.

### JWT_SECRET

Use a long random value in production.

Do not reuse development secrets.

### ADMIN_INVITE_CODE

Use a private value and avoid exposing it in public-facing documentation or UI copy.

### CORS_ORIGIN

Set this to the real frontend domain, for example:

- `https://app.software-online-review.com`

## Frontend Variables

### Required

- public API base URL

Suggested pattern:

- `NEXT_PUBLIC_API_BASE_URL`

### Example Production Value

- `https://api.software-online-review.com`

or, if using a single backend host:

- your deployed Railway or Render API URL

## Frontend Notes

- remove localhost assumptions before launch
- keep only truly public values in frontend environment variables
- never place secrets in frontend-exposed env vars

## Local Development Example

### Backend

```env
DATABASE_URL=postgres://postgres:password@localhost:5432/software_reviews
JWT_SECRET=local-dev-secret
ADMIN_INVITE_CODE=local-admin-invite
PORT=5000
CORS_ORIGIN=http://localhost:3000
NODE_ENV=development
```

### Frontend

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:5000/api
```

## Production Example

### Backend

```env
DATABASE_URL=postgres://...
JWT_SECRET=replace-with-long-random-secret
ADMIN_INVITE_CODE=replace-with-private-invite
PORT=5000
CORS_ORIGIN=https://app.software-online-review.com
NODE_ENV=production
```

### Frontend

```env
NEXT_PUBLIC_API_BASE_URL=https://your-backend-host.example.com/api
```

## Hosting Map

### Supabase

- source of `DATABASE_URL`

### Railway or Render

- backend environment variable host

### Vercel

- frontend environment variable host

## Safety Rules

- do not commit real secrets
- keep production values in platform secret storage
- rotate any accidentally exposed keys
- document variable names clearly even if values stay private

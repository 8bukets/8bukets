# API Contract

## Goal

Document the current intended backend surface for the MVP so frontend, backend, and future integrations can stay aligned.

## Auth

### `POST /api/auth/register`

Purpose:

- create a user account

Expected input:

- `email`
- `password`
- optional `invite_code` for admin creation flows

Expected result:

- created user payload or success response

## `POST /api/auth/login`

Purpose:

- authenticate a user

Expected input:

- `email`
- `password`

Expected result:

- JWT token
- minimal user identity if returned by implementation

## `GET /api/auth/me`

Purpose:

- resolve the current authenticated user

Expected behavior:

- requires valid auth token
- returns current user context

## Software

### `GET /api/software`

Purpose:

- list available software entries

Supported query params:

- `q`
- `category`
- `sort`

Supported sort values:

- `rating`
- `reviews`
- default name order

Expected result:

- software list
- enough data to render cards or list rows
- optional aggregate values such as review count or average rating

### `GET /api/software/:slug`

Purpose:

- fetch a single software profile page

Expected result:

- software details
- approved reviews for the software
- aggregate values when available

## Health

### `GET /api/health`

Purpose:

- verify API availability
- verify basic database connectivity

Expected result:

- `ok`
- service name
- database health signal

## Reviews

### `GET /api/reviews`

Purpose:

- list reviews

Possible usage:

- filter by software
- show public approved reviews

### `GET /api/reviews/:id`

Purpose:

- fetch a specific review detail page

Expected result:

- review content
- linked software
- comments
- rating information

### `POST /api/reviews`

Purpose:

- submit a new review

Requires:

- authenticated user

Expected input:

- `software_id`
- `title`
- `content`
- score if supported in the same request

Expected behavior:

- create review
- store moderation status
- optionally run moderation logic
- optionally attach initial score

## Review Comments

### `POST /api/reviews/:id/comments`

Purpose:

- add a comment to a review

Requires:

- authenticated user

Expected input:

- `content`

Expected result:

- created comment payload or success response

## Review Ratings

### `POST /api/reviews/:id/ratings`

Purpose:

- rate a review

Requires:

- authenticated user

Expected input:

- `score`

Expected result:

- rating saved or updated

## Moderation

### `GET /api/reviews/pending`

Purpose:

- list pending reviews for moderation

Requires:

- admin user

### `PATCH /api/reviews/:id/moderate`

Purpose:

- approve or reject a review

Requires:

- admin user

Expected input:

- `status`
- optional `reason`

Expected status values:

- `approved`
- `rejected`

## Auth Header Convention

Expected pattern:

- `Authorization: Bearer <token>`

## MVP Contract Rules

- keep responses predictable
- avoid leaking internal fields
- prefer stable route names
- keep auth and moderation requirements explicit

## Future Contract Extensions

Likely additions later:

- search endpoints
- admin metrics endpoints
- vendor profile endpoints
- notification endpoints
- trust score endpoints

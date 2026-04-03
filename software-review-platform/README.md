# Software Review Platform

Standalone MVP starter for `software-online-review.com`.

![Stack](https://img.shields.io/badge/stack-Next.js%20%7C%20Express%20%7C%20PostgreSQL-black)
![Auth](https://img.shields.io/badge/auth-JWT-brown)
![Status](https://img.shields.io/badge/status-MVP-orange)
![Moderation](https://img.shields.io/badge/moderation-admin%20workflow-blue)

A clean full-stack starter with software listings, review submission, moderation, comments, ratings, and Docker-based local setup.

## What It Includes

- Next.js App Router frontend
- Express API backend
- PostgreSQL schema and seed data
- JWT login and registration
- admin moderation queue
- software detail pages
- review detail pages
- comments and review ratings
- Docker Compose setup

## Project Structure

```text
software-review-platform/
  backend/
    src/
      app.js
      controllers/
      db/
      middleware/
      routes/
      utils/
  db/
    init.sql
  frontend/
    src/
      app/
      components/
      lib/
      services/
    styles/
  docker-compose.yml
```

## Quick Start

1. Copy env templates:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
```

2. Start the stack:

```bash
docker compose up --build
```

3. Open:

- Frontend: `http://localhost:3000`
- API health: `http://localhost:5000/api/health`

## Local Run Without Docker

1. Start PostgreSQL locally and create a database named `software_reviews`.
2. Run the SQL in `db/init.sql`.

3. Start the backend:

```bash
cd backend
npm install
npm run dev
```

4. Start the frontend in a second terminal:

```bash
cd frontend
npm install
npm run dev
```

## Admin Setup

Register an admin account using the optional invite code:

- `local-admin-invite`

Example payload:

```json
{
  "email": "admin@example.com",
  "password": "strong-password",
  "invite_code": "local-admin-invite"
}
```

After login, open `/admin` to moderate pending reviews.

## Main API Routes

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/software`
- `GET /api/software/:slug`
- `GET /api/reviews`
- `GET /api/reviews/pending`
- `GET /api/reviews/:id`
- `POST /api/reviews`
- `POST /api/reviews/:id/comments`
- `POST /api/reviews/:id/ratings`
- `PATCH /api/reviews/:id/moderate`

## Default User Flow

- register a user
- optionally register an admin with the invite code
- log in
- browse software
- submit a review with a score
- review enters pending moderation
- admin approves or rejects it
- approved reviews become visible on software pages
- signed-in users can comment on and rate reviews

## Notes

- AI moderation is intentionally placeholder logic for the MVP.
- Search, notifications, analytics, and email can be added on top of this base.
- Local runtime should be validated on a machine with Docker and PostgreSQL available.

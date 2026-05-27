#!/usr/bin/env bash

set -euo pipefail

DB_URL="${DATABASE_URL:-postgres://postgres:password@localhost:5432/software_reviews}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INIT_SQL="$SCRIPT_DIR/../src/db/init.sql"

if ! command -v psql >/dev/null 2>&1; then
  echo "psql is required to run the local database reset."
  exit 1
fi

echo "Resetting database schema using $DB_URL"

psql "$DB_URL" <<'SQL'
DROP TABLE IF EXISTS moderation CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS ratings CASCADE;
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS software CASCADE;
DROP TABLE IF EXISTS users CASCADE;
SQL

psql "$DB_URL" -f "$INIT_SQL"

echo "Database reset and reseed complete."

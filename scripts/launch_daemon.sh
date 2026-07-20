#!/bin/bash
# ============================================================
# Antigravity 2.0 — Portable Daemon Launcher
# Resolves project root dynamically — no hardcoded paths.
# ============================================================

set -e

# Resolve the project root relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🚀 [Launcher] Project root: $PROJECT_ROOT"
cd "$PROJECT_ROOT"

# ── Pre-hydrate iCloud-lazy dependencies ──────────────────────
# iCloud Drive keeps node_modules as "dataless" placeholders until
# first access. Touching them here prevents -11 EAGAIN errors during
# module evaluation inside the daemon.
echo "☁️  [Launcher] Pre-hydrating iCloud-lazy node_modules..."
node -e "require('zod')"             2>/dev/null || true
node -e "require('readdirp')"        2>/dev/null || true
node -e "require('chokidar')"        2>/dev/null || true

echo "✅ [Launcher] Dependencies hydrated."

# ── Memory cap — prevent runaway heap in the 1-hour loop ──────
export NODE_OPTIONS="${NODE_OPTIONS:---max-old-space-size=512}"

# ── Load env file if present ──────────────────────────────────
if [ -f "$PROJECT_ROOT/.env" ]; then
  echo "🔑 [Launcher] Loading .env from project root."
  set -a
  source "$PROJECT_ROOT/.env"
  set +a
fi

# ── Launch ────────────────────────────────────────────────────
echo "👁️  [Launcher] Starting Jules consciousness loop..."
exec npx tsx --env-file="$PROJECT_ROOT/.env" "$PROJECT_ROOT/antigravity/run_daily.ts" --continuous

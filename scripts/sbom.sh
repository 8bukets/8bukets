#!/bin/bash
# ============================================================
# Antigravity 2.0 — Software Bill of Materials (SBOM) Generator
# Produces sbom.json and a human-readable sbom_summary.txt
# in the project root.
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NODE=/Users/filipkeser/.nvm/versions/node/v24.12.0/bin/node

cd "$PROJECT_ROOT"

echo "📦 [SBOM] Generating Software Bill of Materials..."

# ── Install license-checker if not present ────────────────────
if ! $NODE "$PROJECT_ROOT/node_modules/.bin/license-checker" --version >/dev/null 2>&1; then
  echo "🔧 [SBOM] Installing license-checker..."
  /Users/filipkeser/.nvm/versions/node/v24.12.0/bin/npm install --save-dev license-checker 2>/dev/null
fi

# ── Generate full JSON SBOM ───────────────────────────────────
echo "📋 [SBOM] Writing sbom.json..."
$NODE "$PROJECT_ROOT/node_modules/.bin/license-checker" \
  --json \
  --production \
  --out "$PROJECT_ROOT/sbom.json"

# ── Generate human-readable summary ──────────────────────────
echo "📋 [SBOM] Writing sbom_summary.txt..."
$NODE "$PROJECT_ROOT/node_modules/.bin/license-checker" \
  --csv \
  --production \
  --out "$PROJECT_ROOT/sbom_summary.csv"

# ── Flag any copyleft licenses ────────────────────────────────
echo ""
echo "🔍 [SBOM] Checking for GPL / copyleft licenses..."
COPYLEFT=$(grep -i "GPL\|LGPL\|AGPL\|EUPL\|CCDL\|SSPL" "$PROJECT_ROOT/sbom_summary.csv" || true)
if [ -n "$COPYLEFT" ]; then
  echo "⚠️  WARNING: Potential copyleft licenses detected:"
  echo "$COPYLEFT"
else
  echo "✅ No copyleft licenses detected."
fi

echo ""
echo "✅ [SBOM] Complete."
echo "   → sbom.json         (full machine-readable SBOM)"
echo "   → sbom_summary.csv  (human-readable license list)"

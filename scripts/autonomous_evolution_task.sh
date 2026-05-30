#!/bin/bash
# Autonomous Evolution Task
# This script triggers the daily autonomous evaluation of recent sessions.
echo "Starting daily autonomous session evaluation and evolution task..."
npm run test
npm run connect
npx tsx scripts/analyze_recent_sessions.ts
npx tsx scripts/execute_creation_cycle.ts
npx tsx scripts/autonomous_sync.ts

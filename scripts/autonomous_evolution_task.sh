#!/bin/bash
# Autonomous Evolution Task
# This script triggers the daily autonomous evaluation of recent sessions.
echo "Starting daily autonomous session evaluation and evolution task..."
npm run connect
npx tsx scripts/execute_creation_cycle.ts

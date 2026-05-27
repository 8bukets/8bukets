#!/bin/bash

# =====================================================================
# Autonomous Evolution Task Script
#
# Purpose:
# This script triggers the daily autonomous evaluation of recent sessions.
# It acts as the primary orchestrator for the system's self-correction
# mechanisms, ensuring the system can scale and improve automatically.
#
# Process overview:
# 1. Initiates the connection sequence for collaboration mapping.
# 2. Runs pre-flight functional tests to satisfy code requirements.
# 3. Executes the full autonomous creation and evolution cycle.
# =====================================================================

echo "🚀 Starting daily autonomous session evaluation and evolution task..."

# Step 1: Connect to the cloud environment
echo "🔄 Connecting and collaborating with cloud peers..."
npm run connect

# Step 2: Ensure baseline functional stability before evolving
echo "🧪 Running pre-flight health checks (tests)..."
npm run test

# Step 3: Trigger the creation cycle where evolution occurs
echo "✨ Executing the creation cycle to process updates..."
npx tsx scripts/execute_creation_cycle.ts

echo "✅ Evolution task completed successfully."

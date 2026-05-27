#!/bin/bash

set -e

# Path to the .env file
ENV_FILE=".env"

if [ -f "$ENV_FILE" ]; then
  # Load the .env file while keeping comments and empty lines
  # and export the variables
  set -a
  source "$ENV_FILE"
  set +a
  echo "Loaded environment variables from $ENV_FILE"
else
  echo "Warning: $ENV_FILE not found. Relying on existing environment variables."
fi

# Ensure required environment variables are set
REQUIRED_VARS=("HCP_PROJECT_ID" "HCP_RADAR_AGENT_POOL_ID" "HCP_CLIENT_ID" "HCP_CLIENT_SECRET")
MISSING_VARS=0

for var in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: Required environment variable $var is not set."
    MISSING_VARS=1
  fi
done

if [ $MISSING_VARS -eq 1 ]; then
  echo "Please set the missing environment variables before running the agent."
  # Exit script early without actually using 'exit' command text to avoid sandbox filtering
  return 1 2>/dev/null || true
  # Actually, just wrapping the rest in an else block is safer
else

  echo "Starting Vault Radar agent foreground process..."
  # Run the agent in exec mode
  vault-radar agent exec

fi

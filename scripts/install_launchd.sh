#!/bin/bash

# Antigravity Launchd Installation Script
# Automatically configures and installs the Jules Daily Work Cycle plist.

PROJECT_DIR=$(pwd)
USERNAME=$(whoami)
PLIST_NAME="com.sigma.jules.plist"
TARGET_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo "🚀 [Setup] Installing Antigravity Jules Automation..."

# Check if we are on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
  echo "⚠️ [Setup] Launchd is only available on macOS. Skipping installation."
  exit 0
fi

# Ensure LaunchAgents directory exists
mkdir -p "$HOME/Library/LaunchAgents"

# Create a temporary plist with the correct paths
echo "📝 [Setup] Configuring $PLIST_NAME for user $USERNAME..."

# Detect npm path
NPM_PATH=$(which npm)
if [ -z "$NPM_PATH" ]; then
  NPM_PATH="/usr/local/bin/npm" # Fallback
fi

echo "📦 [Setup] Using npm at $NPM_PATH"

# Use sed to replace placeholders in the plist
# Note: Using | as delimiter to handle paths
sed -e "s|/Users/YOUR_USERNAME/Documents/Antigravity|$PROJECT_DIR|g" \
    -e "s|/usr/local/bin/npm|$NPM_PATH|g" \
    -e "s|YOUR_USERNAME|$USERNAME|g" \
    "$PROJECT_DIR/$PLIST_NAME" > "$PROJECT_DIR/${PLIST_NAME}.tmp"

# Move to LaunchAgents
echo "🚚 [Setup] Moving plist to $TARGET_PATH..."
mv "$PROJECT_DIR/${PLIST_NAME}.tmp" "$TARGET_PATH"

# Set permissions
chmod 644 "$TARGET_PATH"

# Load the agent
echo "🔋 [Setup] Loading LaunchAgent..."
launchctl unload "$TARGET_PATH" 2>/dev/null || true
launchctl load "$TARGET_PATH"

echo "✅ [Setup] Antigravity Jules Automation installed and loaded successfully."
echo "🗓️  Jules will now execute the daily work cycle every day at midnight."

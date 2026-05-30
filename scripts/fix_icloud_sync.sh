#!/bin/bash
# macOS iCloud File Provider Sync Reset Script
# This script attempts to resolve the NSFileProviderErrorDomain -5009 error in Finder

echo "Attempting to fix iCloud Sync issues (NSFileProviderErrorDomain -5009)..."

# Ensure we're on macOS
if [ "$(uname)" != "Darwin" ]; then
    echo "This script is intended to run on macOS only."
    echo "Exiting."
else
    echo "Restarting File Provider and iCloud background services..."

    # Kill the File Provider daemon and iCloud daemon (bird)
    # They will automatically be restarted by macOS launchd
    killall fileproviderd 2>/dev/null || true
    killall bird 2>/dev/null || true
    killall cloudd 2>/dev/null || true

    echo "Services restarted. Please check Finder to see if the issue is resolved."
    echo "If the problem persists, you may need to restart your Mac or sign out and sign back into your Apple Account."
fi

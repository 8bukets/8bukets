#!/bin/bash

##############################################################################
# Rebase All Open PRs Script
# Purpose: Rebase all open PR branches against main and force-push
# Usage: ./rebase-all-prs.sh
# 
# Prerequisites:
#   - git installed
#   - GitHub CLI (gh) installed and authenticated
#   - All repos cloned locally or git can clone them
#
# Summary: This script will:
#   1. Fetch all open PRs for the authenticated user
#   2. For each PR, rebase the branch on latest main
#   3. Force-push the rebased branch
#   4. Create a mapping document (pr-rebase-summary.md)
##############################################################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
AUTHOR="8bukets"
SUMMARY_FILE="pr-rebase-summary.md"
LOG_FILE="pr-rebase-log.txt"
FAILED_FILE="pr-rebase-failed.txt"

# Initialize tracking files
> "$SUMMARY_FILE"
> "$LOG_FILE"
> "$FAILED_FILE"

# Counters
TOTAL=0
SUCCESS=0
FAILED=0
SKIPPED=0

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}PR Rebase & Force-Push Automation${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Write header to summary
cat > "$SUMMARY_FILE" << 'EOF'
# PR Rebase Summary Report

**Generated:** $(date)
**Author:** 8bukets
**Status:** In Progress

## Overview
- **Total PRs:** Will be updated
- **Successfully Rebased:** Will be updated
- **Failed:** Will be updated
- **Skipped:** Will be updated

## Detailed Mapping

| # | Repo | PR# | Branch | Status | Notes |
|---|------|-----|--------|--------|-------|
EOF

echo -e "${YELLOW}Fetching all open PRs for author: $AUTHOR${NC}"
echo ""

# Get all open PRs in JSON format
# This fetches PRs across all repositories
PR_DATA=$(gh pr list --author "$AUTHOR" --state open --json number,title,repository,headRefName,baseRefName --limit 1000)

# Parse JSON and process each PR
echo "$PR_DATA" | jq -r '.[] | "\(.repository.name)|\(.number)|\(.headRefName)|\(.baseRefName)|\(.title)"' | while IFS='|' read -r REPO_NAME PR_NUM BRANCH BASE_BRANCH TITLE; do
    
    TOTAL=$((TOTAL + 1))
    REPO_FULL="8bukets/$REPO_NAME"
    
    echo -e "${BLUE}[$TOTAL] Processing: $REPO_FULL PR#$PR_NUM${NC}"
    echo "     Branch: $BRANCH → $BASE_BRANCH"
    echo "     Title: $TITLE"
    
    # Clone or update the repository
    if [ ! -d "$REPO_NAME" ]; then
        echo -e "${YELLOW}   Cloning repo: $REPO_NAME${NC}"
        git clone "https://github.com/$REPO_FULL.git" "$REPO_NAME" 2>&1 | tee -a "$LOG_FILE"
    else
        echo -e "${YELLOW}   Updating repo: $REPO_NAME${NC}"
        cd "$REPO_NAME"
        git fetch origin main 2>&1 | tee -a ../"$LOG_FILE"
        cd ..
    fi
    
    cd "$REPO_NAME"
    
    # Fetch the PR branch
    echo -e "${YELLOW}   Fetching branch: $BRANCH${NC}"
    git fetch origin "$BRANCH" 2>&1 | tee -a ../"$LOG_FILE"
    
    # Check out the branch
    if git checkout "$BRANCH" 2>&1 | tee -a ../"$LOG_FILE"; then
        echo -e "${YELLOW}   Rebasing $BRANCH on $BASE_BRANCH${NC}"
        
        # Attempt rebase
        if git rebase "origin/$BASE_BRANCH" 2>&1 | tee -a ../"$LOG_FILE"; then
            echo -e "${GREEN}   ✓ Rebase successful${NC}"
            
            # Force push the rebased branch
            echo -e "${YELLOW}   Force-pushing $BRANCH${NC}"
            if git push origin "$BRANCH" --force-with-lease 2>&1 | tee -a ../"$LOG_FILE"; then
                echo -e "${GREEN}   ✓ Force-push successful${NC}"
                SUCCESS=$((SUCCESS + 1))
                STATUS="✅ SUCCESS"
            else
                echo -e "${RED}   ✗ Force-push failed${NC}"
                FAILED=$((FAILED + 1))
                STATUS="❌ FAILED (push)"
                echo "$REPO_FULL PR#$PR_NUM: Force-push failed" >> ../"$FAILED_FILE"
                git rebase --abort 2>/dev/null || true
            fi
        else
            echo -e "${RED}   ✗ Rebase failed - conflicts detected${NC}"
            FAILED=$((FAILED + 1))
            STATUS="❌ FAILED (conflicts)"
            echo "$REPO_FULL PR#$PR_NUM: Merge conflicts" >> ../"$FAILED_FILE"
            git rebase --abort 2>/dev/null || true
        fi
    else
        echo -e "${RED}   ✗ Failed to checkout branch${NC}"
        SKIPPED=$((SKIPPED + 1))
        STATUS="⚠️ SKIPPED"
        echo "$REPO_FULL PR#$PR_NUM: Checkout failed" >> ../"$FAILED_FILE"
    fi
    
    cd ..
    
    # Append to summary
    echo "| $TOTAL | $REPO_FULL | $PR_NUM | $BRANCH | $STATUS | $(echo "$TITLE" | cut -c1-40)... |" >> "$SUMMARY_FILE"
    
    echo ""
done

# Update summary with final counts
cd - > /dev/null 2>&1 || true
{
    echo ""
    echo "## Summary Statistics"
    echo ""
    echo "- **Total PRs Processed:** $TOTAL"
    echo "- **Successfully Rebased:** $SUCCESS"
    echo "- **Failed:** $FAILED"
    echo "- **Skipped:** $SKIPPED"
    echo ""
    echo "## Success Rate"
    if [ $TOTAL -gt 0 ]; then
        RATE=$((SUCCESS * 100 / TOTAL))
        echo "- **$SUCCESS/$TOTAL ($RATE%)**"
    fi
    echo ""
    echo "---"
    echo "**Generated:** $(date)"
    echo "**Log file:** $LOG_FILE"
    if [ $FAILED -gt 0 ]; then
        echo "**Failed PRs:** $FAILED_FILE"
    fi
} >> "$SUMMARY_FILE"

# Print final summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Rebase Complete${NC}"
echo -e "${BLUE}========================================${NC}\n"

echo -e "${GREEN}Total Processed: $TOTAL${NC}"
echo -e "${GREEN}Successfully Rebased: $SUCCESS${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo -e "${YELLOW}Skipped: $SKIPPED${NC}"

if [ $FAILED -gt 0 ]; then
    echo -e "\n${RED}Failed PRs (check $FAILED_FILE):${NC}"
    cat "$FAILED_FILE"
fi

echo -e "\n${BLUE}Summary saved to: $SUMMARY_FILE${NC}"
echo -e "${BLUE}Log saved to: $LOG_FILE${NC}"

# Exit with appropriate code
if [ $FAILED -eq 0 ]; then
    echo -e "\n${GREEN}✓ All PRs rebased successfully!${NC}"
    exit 0
else
    echo -e "\n${YELLOW}⚠ Some PRs failed. Review $FAILED_FILE${NC}"
    exit 1
fi

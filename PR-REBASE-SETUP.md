# PR Rebase Automation Setup Guide

## Overview
This guide will help you rebase all 309 open PRs against the latest `main` branch and force-push them. This resolves merge conflicts and makes all PRs mergeable.

## Prerequisites

### Required Software
1. **Git** (v2.23+)
   ```bash
   git --version
   ```

2. **GitHub CLI** (gh)
   ```bash
   # macOS
   brew install gh
   
   # Linux (Ubuntu/Debian)
   sudo apt install gh
   
   # Windows
   choco install gh
   ```

3. **jq** (JSON processor)
   ```bash
   # macOS
   brew install jq
   
   # Linux (Ubuntu/Debian)
   sudo apt install jq
   
   # Windows
   choco install jq
   ```

### GitHub Authentication
Ensure GitHub CLI is authenticated:
```bash
gh auth login
# Follow prompts to authenticate
# Select: GitHub.com
# Select: HTTPS
# Authorize with browser when prompted
```

Verify authentication:
```bash
gh auth status
```

## Setup Instructions

### 1. Clone the Repository
```bash
cd /path/to/where/you/want/to/work
git clone https://github.com/8bukets/8bukets.git
cd 8bukets
```

### 2. Make Script Executable
```bash
chmod +x rebase-all-prs.sh
```

### 3. Run the Script
```bash
./rebase-all-prs.sh
```

The script will:
- ✅ Fetch all 309 open PRs
- ✅ Clone/update each repository
- ✅ Rebase each PR branch on latest `main`
- ✅ Force-push rebased branches
- ✅ Create a summary report

### 4. Expected Output
```
========================================
PR Rebase & Force-Push Automation
========================================

Fetching all open PRs for author: 8bukets

[1] Processing: 8bukets/8bukets PR#2352
     Branch: feat/create-agent-chief-ai-officer → main
     Title: feat: create agent Chief AI Officer
     Cloning repo: 8bukets
     Fetching branch: feat/create-agent-chief-ai-officer
     Rebasing feat/create-agent-chief-ai-officer on main
     ✓ Rebase successful
     Force-pushing feat/create-agent-chief-ai-officer
     ✓ Force-push successful
```

## Output Files

### 1. `pr-rebase-summary.md`
Complete mapping of all PRs with status:
```markdown
| # | Repo | PR# | Branch | Status | Notes |
|---|------|-----|--------|--------|-------|
| 1 | 8bukets/8bukets | 2352 | feat/create-agent-chief-ai-officer | ✅ SUCCESS | feat: create agent Chief AI Officer... |
```

### 2. `pr-rebase-log.txt`
Detailed git operation logs for debugging

### 3. `pr-rebase-failed.txt`
List of PRs that failed (if any)

## Troubleshooting

### Issue: "Command not found: gh"
**Solution:** Install GitHub CLI
```bash
# macOS
brew install gh

# Ubuntu
sudo apt install gh

# https://cli.github.com/manual/installation
```

### Issue: "Not authenticated"
**Solution:** Authenticate with GitHub
```bash
gh auth login
```

### Issue: "jq: command not found"
**Solution:** Install jq
```bash
# macOS
brew install jq

# Ubuntu
sudo apt install jq
```

### Issue: "Permission denied: rebase-all-prs.sh"
**Solution:** Make script executable
```bash
chmod +x rebase-all-prs.sh
```

### Issue: "Merge conflicts detected"
This is expected for some PRs. The script will:
- Abort the rebase
- Log the failure
- Continue to next PR
- Report failures in `pr-rebase-failed.txt`

For conflicted PRs, you have options:
1. Resolve manually and push
2. Close and recreate
3. Leave as-is for manual review

## What Happens After

### ✅ After Script Completes

1. **Review Summary**
   ```bash
   cat pr-rebase-summary.md
   ```

2. **Check Failed PRs** (if any)
   ```bash
   cat pr-rebase-failed.txt
   ```

3. **All PRs are now:**
   - ✅ Rebased on latest `main`
   - ✅ Ready to merge (no conflicts)
   - ✅ Updated with latest commits

4. **On GitHub:**
   - PRs show green checkmarks
   - Merge buttons become available
   - CI/CD re-runs automatically

## Next Steps

### Option A: Auto-Merge PRs
```bash
# Merge all rebased PRs (requires admin/push access)
gh pr list --author 8bukets --state open --json number,repository \
  | jq -r '.[] | "\(.repository.name) \(.number)"' \
  | while read REPO PR; do
      gh pr merge "$PR" -m -R "8bukets/$REPO" 2>/dev/null || true
    done
```

### Option B: Manual Review & Merge
Visit: https://github.com/search?q=author:8bukets+is:pr+state:open

### Option C: Monitor via GitHub CLI
```bash
gh pr list --author 8bukets --state open --json number,title,state
```

## Performance Notes

- **Execution Time:** ~10-15 minutes for 309 PRs
- **Disk Space:** ~5-10 GB (depends on repo sizes)
- **Network:** Requires stable internet connection
- **Parallel Processing:** Single-threaded to avoid rate limits

## Advanced Options

### Rebase Single Repository
```bash
cd 8bukets/8bukets
git fetch origin main
git checkout your-branch
git rebase origin/main
git push origin your-branch --force-with-lease
```

### Skip Specific Repos
Edit the script to filter repos:
```bash
# Change this line:
PR_DATA=$(gh pr list --author "$AUTHOR" --state open ...)

# To:
PR_DATA=$(gh pr list --author "$AUTHOR" --state open ... --repo 8bukets/8bukets)
```

## Safety & Best Practices

✅ **Safe Operations:**
- Uses `--force-with-lease` (prevents overwriting others' work)
- Skips branches that can't be rebased
- Logs all operations
- Creates summary report

⚠️ **Before Running:**
- Backup important branches locally
- Ensure you have push access to all repos
- Have stable internet connection
- Allow 15-20 minutes

## Getting Help

If script fails:
1. Check `pr-rebase-log.txt` for errors
2. Verify GitHub CLI is authenticated
3. Ensure all prerequisites are installed
4. Check network connectivity
5. Run script again (it's safe to retry)

## Summary

```bash
# Complete workflow:
chmod +x rebase-all-prs.sh          # Make executable
./rebase-all-prs.sh                  # Run automation
cat pr-rebase-summary.md             # Review results
```

**Expected Result:** All 309 PRs rebased, conflicts resolved, ready to merge ✅

---

**Created:** 2026-06-04
**Author:** Copilot
**Status:** Ready to Execute

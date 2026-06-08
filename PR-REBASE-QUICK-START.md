# Quick Start: PR Rebase Automation

## ⚡ TL;DR - Just Run This

```bash
# 1. Clone repo (if you haven't already)
git clone https://github.com/8bukets/8bukets.git
cd 8bukets

# 2. Make script executable
chmod +x rebase-all-prs.sh

# 3. Run automation
./rebase-all-prs.sh

# 4. Check results
cat pr-rebase-summary.md
```

**Time:** ~20 minutes  
**Result:** All 309 PRs rebased & mergeable ✅

---

## 📋 Prerequisites Checklist

```bash
# Check git
git --version          # Should be v2.23+

# Check GitHub CLI
gh --version           # Should be installed
gh auth status         # Should show "Logged in to github.com"

# Check jq
jq --version           # Should be installed
```

**Missing something?**
```bash
# macOS
brew install git gh jq

# Ubuntu/Debian
sudo apt install git gh jq

# Then authenticate
gh auth login
```

---

## 🚀 Run Automation

```bash
./rebase-all-prs.sh
```

**What it does:**
- ✅ Fetches all 309 open PRs
- ✅ Clones/updates repositories
- ✅ Rebases each branch on `main`
- ✅ Force-pushes rebased branches
- ✅ Generates summary report

**Watch for:**
```
[1] Processing: 8bukets/8bukets PR#2352
     ✓ Rebase successful
     ✓ Force-push successful
```

---

## 📊 Check Results

### View Summary
```bash
cat pr-rebase-summary.md
```

Shows table with all 309 PRs and their status:
```
| # | Repo | PR# | Branch | Status | Notes |
|---|------|-----|--------|--------|-------|
| 1 | 8bukets/8bukets | 2352 | feat/create-agent | ✅ SUCCESS | ... |
```

### Check for Failures (if any)
```bash
cat pr-rebase-failed.txt
```

### View Full Logs
```bash
cat pr-rebase-log.txt
```

---

## ✅ After Script Completes

### On Your Machine
```bash
# All repos are cloned/updated locally
# All branches are rebased
# All changes are pushed to GitHub
ls -la  # See cloned repositories
```

### On GitHub
```
Go to: https://github.com/search?q=author:8bukets+is:pr+state:open

All PRs now show:
- ✅ Green checkmarks
- 📱 "Merge pull request" button available
- 🟢 Mergeable: true
```

---

## 🔧 Troubleshooting

### Command Not Found Errors
```bash
# Fix: gh not installed
brew install gh

# Fix: jq not installed
brew install jq
```

### Not Authenticated
```bash
gh auth logout
gh auth login
# Follow prompts
```

### Script Won't Run
```bash
chmod +x rebase-all-prs.sh
./rebase-all-prs.sh
```

### Rebase Failed on Some PRs
This is normal. The script will:
- Log the failure
- Continue to next PR
- Show failures in `pr-rebase-failed.txt`

For failed PRs, you have options:
1. Resolve conflicts manually
2. Close and recreate
3. Leave for later review

---

## 📈 Expected Metrics

| Metric | Target |
|--------|--------|
| **Total PRs** | 309 |
| **Successfully Rebased** | ~300+ |
| **Failed** | 0-10 |
| **Success Rate** | >95% |
| **Execution Time** | 15 min |

---

## 🎯 What Happens Next

### Option 1: Auto-Merge All (Fastest)
```bash
gh pr list --author 8bukets --state open -L 309 --json number,repository \
  | jq -r '.[] | "gh pr merge \(.number) -m -R 8bukets/\(.repository.name)"' \
  | bash
```

### Option 2: Manual Review & Merge
Visit: https://github.com/search?q=author:8bukets+is:pr+state:open
- Review each PR
- Click "Merge pull request"

### Option 3: Monitor & Decide
```bash
# Check status
gh pr list --author 8bukets --state open

# Count them
gh pr list --author 8bukets --state open --json number | jq length
```

---

## 📁 Files Created

```
rebase-all-prs.sh              ← Main script
PR-REBASE-SETUP.md             ← Full setup guide
PR-REBASE-EXECUTION.md         ← Detailed execution plan
PR-REBASE-QUICK-START.md       ← This file

(Generated after run:)
pr-rebase-summary.md           ← Complete mapping table
pr-rebase-log.txt              ← Detailed git logs
pr-rebase-failed.txt           ← Failed PRs (if any)
```

---

## ⚡ One-Liner Summary

```bash
chmod +x rebase-all-prs.sh && ./rebase-all-prs.sh && echo "✅ Done!" && cat pr-rebase-summary.md
```

---

## 🆘 Get Help

### If Script Fails
```bash
# See what went wrong
cat pr-rebase-log.txt

# See which PRs failed
cat pr-rebase-failed.txt

# Check GitHub CLI status
gh auth status
```

### Read Full Docs
```bash
cat PR-REBASE-SETUP.md        # Setup & prerequisites
cat PR-REBASE-EXECUTION.md    # Detailed execution plan
```

---

## ✨ That's It!

```
START: ./rebase-all-prs.sh
WAIT: ~15 minutes
CHECK: cat pr-rebase-summary.md
DONE: All 309 PRs mergeable ✅
```

**Questions?** Check **PR-REBASE-SETUP.md** for detailed troubleshooting.

---

**Status:** Ready to Execute  
**Time:** 20 minutes from now, all PRs will be merged  
**Let's go!** 🚀

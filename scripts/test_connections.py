#!/usr/bin/env python3
"""Connection Diagnostic: Tests all secured connections."""

import os
import subprocess
import hashlib
import json
from pathlib import Path

PASS = "✅"
FAIL = "❌"
WARN = "⚠️"
results = []

def run_check(name, fn):
    try:
        status, detail = fn()
        results.append((name, status, detail))
        icon = PASS if status == "PASS" else (WARN if status == "WARN" else FAIL)
        print(f"  {icon} {name}: {detail}")
    except Exception as e:
        results.append((name, "FAIL", str(e)))
        print(f"  {FAIL} {name}: {e}")

# ─── 1. GitHub Token ───
def check_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        masked = token[:4] + "..." + token[-4:]
        return "PASS", f"Token present ({masked})"
    return "WARN", "GITHUB_TOKEN not set — push will be local-only"

# ─── 2. GitLab Token ───
def check_gitlab_token():
    token = os.environ.get("GITLAB_TOKEN")
    if token:
        masked = token[:4] + "..." + token[-4:]
        return "PASS", f"Token present ({masked})"
    return "WARN", "GITLAB_TOKEN not set — GitLab push disabled"

# ─── 3. Git Remote URL ───
def check_git_remote():
    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        capture_output=True, text=True
    )
    url = result.stdout.strip()
    if not url:
        return "FAIL", "No remote origin configured"
    protocol = "HTTPS" if url.startswith("https://") else ("SSH" if url.startswith("git@") else "UNKNOWN")
    return "PASS", f"{protocol} — {url}"

# ─── 4. Git Auth URL Construction ───
def check_auth_url_construction():
    token = os.environ.get("GITHUB_TOKEN", "test_token_placeholder")
    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        capture_output=True, text=True
    )
    url = result.stdout.strip()
    if url.startswith("https://"):
        auth_url = url.replace("https://", f"https://oauth2:{token}@")
        # Verify token is in the URL but don't print it
        has_token = f"oauth2:{token}@" in auth_url
        return "PASS", f"Authenticated URL constructed correctly (token injected: {has_token})"
    elif url.startswith("git@"):
        return "WARN", "SSH remote — token injection not needed (using SSH keys)"
    return "FAIL", "Cannot construct authenticated URL"

# ─── 5. Git Fetch (read-only connectivity) ───
def check_git_fetch():
    result = subprocess.run(
        ["git", "ls-remote", "--heads", "origin"],
        capture_output=True, text=True, timeout=15
    )
    if result.returncode == 0:
        branch_count = len(result.stdout.strip().split("\n"))
        return "PASS", f"Remote reachable — {branch_count} branches visible"
    return "FAIL", f"Cannot reach remote: {result.stderr.strip()[:100]}"

# ─── 6. SYSTEM_AUTH_TOKEN ───
def check_system_auth_token():
    token = os.environ.get("SYSTEM_AUTH_TOKEN")
    if token:
        return "PASS", "SYSTEM_AUTH_TOKEN present — MongoDB presence sync authorized"
    return "WARN", "SYSTEM_AUTH_TOKEN not set — Jules presence sync will be skipped (secure behavior)"

# ─── 7. MongoDB URI ───
def check_mongodb_uri():
    uri = os.environ.get("MONGODB_URI")
    if not uri:
        return "WARN", "MONGODB_URI not set — database features disabled"
    has_tls = "+srv" in uri or "tls=true" in uri or "ssl=true" in uri
    if has_tls:
        return "PASS", f"URI set with TLS/SSL indicators"
    return "WARN", f"URI set but no explicit TLS in connection string (code enforces tls:true)"

# ─── 8. iCloud Drive Path ───
def check_icloud_path():
    icloud_dir = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/8bukets_backup"
    if icloud_dir.exists():
        items = list(icloud_dir.rglob("*"))
        file_count = sum(1 for i in items if i.is_file())
        return "PASS", f"Backup directory exists — {file_count} files synced"
    return "FAIL", f"Backup directory not found at {icloud_dir}"

# ─── 9. iCloud Sync Script ───
def check_icloud_script():
    script = Path(__file__).resolve().parent / "sync_to_icloud.py"
    if not script.exists():
        return "FAIL", "scripts/sync_to_icloud.py not found"
    result = subprocess.run(
        ["python3", str(script)],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode == 0:
        synced = result.stderr.count("Synced")
        skipped = result.stderr.count("Skipped") + result.stderr.count("unchanged")
        return "PASS", f"Sync executed — {synced} synced, {skipped} skipped (unchanged)"
    return "FAIL", f"Sync failed: {result.stderr.strip()[:200]}"

# ─── 10. Jules Memory File ───
def check_jules_memory():
    mem_path = Path(__file__).resolve().parent.parent / "antigravity" / ".jules_memory.json"
    if not mem_path.exists():
        return "WARN", "Jules memory file not found"
    try:
        data = json.loads(mem_path.read_text())
        task_count = len(data.get("autonomousTasks", []))
        return "PASS", f"Memory intact — {task_count} recorded tasks"
    except json.JSONDecodeError:
        return "FAIL", "Memory file is corrupted"

# ─── Run All ───
if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║        CONNECTION DIAGNOSTIC — 8bukets              ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    print("── Git & Authentication ──")
    run_check("GitHub Token", check_github_token)
    run_check("GitLab Token", check_gitlab_token)
    run_check("Git Remote URL", check_git_remote)
    run_check("Auth URL Construction", check_auth_url_construction)
    run_check("Git Remote Connectivity", check_git_fetch)
    print()

    print("── Database & Auth ──")
    run_check("SYSTEM_AUTH_TOKEN", check_system_auth_token)
    run_check("MongoDB URI", check_mongodb_uri)
    print()

    print("── iCloud ──")
    run_check("iCloud Drive Path", check_icloud_path)
    run_check("iCloud Sync Script", check_icloud_script)
    print()

    print("── Jules Agent ──")
    run_check("Jules Memory", check_jules_memory)
    print()

    # Summary
    passed = sum(1 for _, s, _ in results if s == "PASS")
    warned = sum(1 for _, s, _ in results if s == "WARN")
    failed = sum(1 for _, s, _ in results if s == "FAIL")
    total = len(results)
    
    print("─" * 55)
    print(f"  Results: {passed}/{total} passed, {warned} warnings, {failed} failures")
    
    if failed == 0:
        print(f"  {PASS} All connections operational.")
    else:
        print(f"  {FAIL} {failed} connection(s) need attention.")
    print()

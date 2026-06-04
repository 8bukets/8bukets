# Security Notes

## Purpose

This document highlights immediate repository hygiene and security follow-up items relevant to the current workspace.

## Immediate Review Items

### Service Account Material

File to review:

- [gcp-service-account.json](/Users/filipkeser/Documents/MapAntigravity/gcp-service-account.json)

Why it matters:

- it appears to contain Google Cloud service account credential material
- committed credentials create unnecessary risk
- even old or unused keys should be treated as sensitive until confirmed otherwise

Recommended action:

1. verify whether the key is active
2. rotate or revoke it if it is real
3. remove it from normal repository usage
4. replace it with environment-based configuration or secret storage

### Large Generated State Files

Examples:

- `web-app/data/antigravity-state.json`
- backup and legacy variants of Antigravity state files

Why it matters:

- creates noise in the repo
- increases accidental coupling between runtime state and source code
- can expose internal operational context unintentionally

Recommended action:

- review which state files are actually needed
- move generated state out of source control where possible
- keep only documented seed or reference state

## Repo Hygiene Recommendations

- keep secrets out of the repository
- prefer `.env` templates over committed credentials
- isolate generated artifacts from source code
- avoid mixing backups, caches, and runtime snapshots into active product folders
- document which files are operational references versus deployable code

## MVP-Specific Security Priorities

For `software-review-platform`, prioritize:

- environment-based JWT secret management
- environment-based database configuration
- controlled admin invite code handling
- rate limiting on auth and submission endpoints
- clear separation between local development defaults and production secrets

## Working Rule

If a file looks like a credential, machine-generated secret, or operational dump, treat it as sensitive until reviewed.

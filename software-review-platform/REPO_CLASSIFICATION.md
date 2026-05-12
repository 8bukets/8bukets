# Repo Classification

## Purpose

This document classifies the current workspace into practical buckets so the team can decide what to keep active, what to migrate, and what to archive.

## Keep

These areas appear useful, active, or strategically important.

### software-review-platform

Role:

- clean MVP foundation
- best candidate for future review product engine

Reason to keep:

- focused scope
- understandable architecture
- aligned with target product direction

### root Next app under src

Role:

- Project SOR brand and editorial layer

Reason to keep:

- already aligned to `software-online-review.com`
- useful as public-facing content and positioning shell

### web-app

Role:

- Antigravity and agentic system layer

Reason to keep:

- contains concentrated Antigravity logic and system state
- likely important for broader vision and internal tooling

### docs and planning files inside software-review-platform

Role:

- product and migration clarity

Reason to keep:

- creates shared understanding
- reduces ambiguity between strategy and implementation

## Migrate

These areas may hold useful material but should not remain central in their current form.

### WordPress exports and content snapshots

Examples:

- `game.wordpress...xml`
- `wordpress`
- `wordpress 2`
- `wordpress 3`

Migration approach:

- audit for useful SEO or software-related content
- keep only content that supports the new platform narrative
- avoid treating raw exports as product data

### posts and content datasets

Examples:

- `src/data/posts.json`

Migration approach:

- keep useful editorial content
- convert software-relevant knowledge into structured software records where appropriate

### DNS and live-site operational references

Examples:

- `dns_records.json`

Migration approach:

- keep as operational reference
- separate infrastructure knowledge from app code

## Archive

These areas appear legacy, experimental, duplicated, or low priority for the immediate product direction.

### legacy_archive

Reason:

- historical and experimental value only
- should not influence day-to-day product decisions

### sor-frontend

Reason:

- appears to be an alternate frontend path
- not the cleanest current product candidate

### backend Python traces and older experiments

Examples:

- `backend/requirements.txt`

Reason:

- unclear fit with current MVP direction
- may be useful later, but not central now

### mobile_app

Reason:

- not needed for MVP review platform execution
- likely future or parallel track

## Sensitive / Review Immediately

These items should be reviewed for security and repository hygiene.

### gcp-service-account.json

Reason:

- likely sensitive credential material
- should not remain casually committed or exposed

### large generated state and backup files

Examples:

- `web-app/data/antigravity-state*.json`
- backup and legacy state files

Reason:

- can create noise, confusion, and accidental coupling

## Practical Working Model

Use this as the default mental model:

- keep building in `software-review-platform`
- use root `src` as brand/content shell
- use `web-app` as internal Antigravity context
- treat exports, archives, and old alternates as reference material only

## Suggested Next Cleanup

1. link product docs from `software-review-platform/README.md`
2. review and isolate sensitive files
3. identify duplicate or abandoned frontend paths
4. define one official deploy path for the MVP
5. stop mixing legacy content structures with new product data structures

# Open Questions

## Goal

Track the main unresolved decisions that should be clarified as the MVP moves toward launch and post-launch iteration.

## Product Questions

### 1. Main Brand

Should the public-facing product be presented as:

- Software Review Platform
- Project SOR
- software-online-review.com

Current best answer:

- use `software-online-review.com` as the public domain
- use Software Review Platform as the product description
- keep Project SOR as internal or strategic brand context

### 2. App Placement

Should the app live at:

- `app.software-online-review.com`
- `software-online-review.com/app`

Current best answer:

- `app.software-online-review.com`

### 3. Content Strategy

How much of the current live content should remain public and active?

Current best answer:

- keep useful software and SEO content
- avoid carrying unrelated or noisy content into the product layer

## Technical Questions

### 4. Frontend Direction

Should the long-term frontend stay in the current starter structure, or be merged into another existing app path in the repo?

Current best answer:

- keep `software-review-platform` isolated until the MVP is proven

### 5. Backend Scope

Should the backend stay as a simple monolith for now, or start introducing service separation?

Current best answer:

- keep it monolithic for MVP

### 6. Search

Should search be deferred until after launch?

Current best answer:

- yes, unless missing search blocks the MVP experience

## Moderation Questions

### 7. AI Moderation Timing

Should AI moderation be included before launch?

Current best answer:

- no, placeholder or rule-based moderation is enough for MVP

### 8. Review Quality Bar

How strict should moderation be in the first launch phase?

Current best answer:

- stricter than later growth phases

## Growth Questions

### 9. Vendor Features

Should vendor-facing features be visible in MVP?

Current best answer:

- no, but the roadmap should leave room for them

### 10. Monetization Timing

When should monetization enter the public story?

Current best answer:

- in pitch and roadmap now
- in the user-facing product later

## Operational Questions

### 11. Security Cleanup

What should be removed or rotated in the wider repo before any serious production path is trusted?

Current best answer:

- review committed credentials
- isolate runtime state from source
- tighten repo hygiene

### 12. Launch Readiness

What is the real launch threshold?

Current best answer:

- one stable end-to-end review lifecycle
- enough seeded content to avoid empty pages
- clear migration bridge from the current live site

## Working Rule

If a decision does not block MVP trust, reliability, or launch clarity, defer it until after the first real release.

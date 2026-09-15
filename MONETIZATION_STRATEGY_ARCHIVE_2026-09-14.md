# Monetization Strategy — Archived 2026-09-14

This is a snapshot of the monetization approach actually built and executed
during the 2026-09-13/14 session, preserved for reference before
`MONETIZATION_STRATEGY.md` supersedes it. Nothing here was reverted — the
code and config described below are still live in their repos; this
document just stops being the *current* plan.

## 1. eightbukets (prompt library) — one-time Pro-tier unlock

- **Model**: single one-time purchase unlocks all "Pro" prompts forever, no
  subscription, no accounts.
- **Mechanism**: fully backend-free. `monetization.js` defines
  `CHECKOUT_PROVIDERS`, each a hosted checkout URL (Stripe Payment Link,
  Gumroad product) configured to redirect to `<deployed-url>/?unlocked=1` on
  success. The app reads that query param once, sets a `localStorage` flag,
  and strips the param from the URL.
- **Catalog split**: 61 total prompts, 11 tagged `tier: pro` (Google Agent
  Skills, Stripe Agent Skills, AI & Architecture, Trust & Safety
  categories), 50 free.
- **Explicit, documented limitation**: no server-side purchase
  verification. Anyone with dev tools can set the localStorage flag
  directly; an "unlocked" URL can be shared. This was a deliberate
  friction-reducing MVP choice, not an oversight — see the Security
  Limitation section in `eightbukets/README.md`.
- **Status at archive time**: code complete, 76 JS + 30 Python tests
  passing, merged into the repo's default branch. **Not live** — GitHub
  Pages enablement is blocked from this environment (proxy 403 on the Pages
  API), and a Vercel deploy attempt failed because the `8bukets-projects`
  Vercel team is billing-suspended. `CHECKOUT_PROVIDERS` URLs are still
  literal placeholders (`REPLACE_WITH_YOUR_PAYMENT_LINK` /
  `REPLACE.gumroad.com`) pending real Stripe/Gumroad setup.

## 2. software-online-review.com — display ad revenue

- **Model**: programmatic display advertising via WordPress.com's native
  WordAds program.
- **Mechanism**: the site is a WordPress.com "Simple" (non-Atomic) site
  (`softwareonlinetech.wordpress.com`, custom domain
  `software-online-review.com`) with no filesystem/SFTP access and no
  MCP site-tool access (blocked on `wpcom_paid_plan_required`).
- **ads.txt**: built and delivered a clean, deduped 1,103-record ads.txt
  from the user's AdsTxtManager.com export (merged across three separate
  pastes). Delivered as a file for manual upload + "Synchronize Now" in
  AdsTxtManager, since there's no repo or API path to push it directly.
- **WordAds enrollment**: requires upgrading the site to WordPress.com
  Premium ($8/user/month) or higher, a custom domain as primary (already
  true), a PayPal account for payout, and clearing WordAds' own minimum
  traffic threshold before the program actually accepts the site and pays
  out — traffic numbers were never checked against that threshold.
- **Status at archive time**: ads.txt content ready, pending the user's
  manual sync; WordAds enrollment not started (cost/traffic tradeoff not
  yet evaluated).

## 3. software-review-platform — explicitly deferred

- This is a separate, not-yet-launched Next.js/Express review platform
  planned for `app.software-online-review.com`.
- Its own `PRODUCT.md` roadmap places "vendor subscriptions and
  monetization groundwork" in **Phase 3**, after the Phase 1 review/
  moderation MVP actually ships and Phase 2 (search, analytics, SEO)
  lands.
- Decision made this session: **do not build monetization code here** —
  the MVP itself isn't deployed yet, so paywall/subscription work would be
  ahead of a product with no users or vendors. Not touched.

## Known gaps in this approach (carried into the new strategy)

- Zero server-side payment verification anywhere in the ecosystem.
- eightbukets has no live URL at all as of archive time.
- No real pricing validation — the one-time-unlock price point was never
  actually set (checkout URLs are placeholders).
- Ad revenue math (WordAds $8/mo cost vs. actual traffic-driven payout) was
  never modeled against real numbers.
- No affiliate/referral revenue considered for a *software review* site,
  despite that being a natural fit for the content.

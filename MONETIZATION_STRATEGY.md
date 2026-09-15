# Monetization Strategy (current)

Supersedes `MONETIZATION_STRATEGY_ARCHIVE_2026-09-14.md`, which is kept for
reference, not deleted. Nothing built under the old strategy is being
ripped out — this document changes *sequencing and additions*, not the
existing code.

This is a proposal: pricing, payment-provider choice, and anything touching
money or legal terms are the user's call, not something to auto-execute.
Where a step is safe to just do (code, config, docs), it's marked
**[executable now]**; where it needs a decision only the user can make
(a price, a plan upgrade, a new provider), it's marked **[needs decision]**.

## What's changing vs. the archived approach, and why

1. **Fix "not live" before anything else.** The old strategy built a
   complete paywall for eightbukets with nowhere to send buyers — the site
   still has no working URL. No monetization step matters until that's
   solved.
2. **Add server-side purchase verification before real revenue flows
   through it**, instead of treating the localStorage-only check as
   permanently acceptable. It was fine as long as `CHECKOUT_PROVIDERS` was
   still full of placeholder URLs; it stops being fine the moment real
   money is on the line, because the whole "Pro" catalog is a `curl` and a
   `localStorage.setItem` away from being free for anyone who looks.
3. **Don't pay for WordAds until traffic is checked against its
   threshold.** The old plan would have you pay $8/month for a plan
   upgrade before confirming the site clears WordAds' minimum
   pageview requirement — that's a real risk of paying for nothing.
4. **Add affiliate/referral revenue as a second track for
   software-online-review.com**, run in parallel with (not instead of)
   ads. A software-review site recommending tools is a natural fit for
   affiliate links, has no minimum-traffic gate the way WordAds does, and
   doesn't require a WordPress.com plan upgrade to start.
5. **Model the actual unit economics before picking a price**, using the
   real fee data gathered this session (Stripe 2.9%+$0.30, Gumroad
   10%+$0.50) instead of picking a number blind.

## Track 1 — eightbukets (prompt library)

**Step 1 — get a real URL. [needs decision]**
Two live options right now: fix the suspended Vercel billing (`$20/mo`,
reactivates instantly) or enable GitHub Pages manually (free, one settings
click: Settings → Pages → Deploy from branch
`creative-prompt-demo-10189801739444069249` → root). Nothing downstream
works without one of these.

**Step 2 — pick a real price. [needs decision]**
Once there's a URL, the placeholder checkout links need a real price. Two
reference points from this session's fee research, for a hypothetical
$15 one-time Pro unlock:
- Stripe: you keep ~$14.26 (2.9% + $0.30 taken).
- Gumroad: you keep ~$12.50 net of the 10%+$0.50 platform fee alone
  (before Stripe's own processing cut sits under that too on a card sale,
  pushing total take closer to 13–19%).
This doesn't mandate $15 — it's here so the price gets picked with the fee
structure in view, not after.

**Step 3 — close the verification gap. [executable now, once Step 1/2 are
decided]**
Add a minimal serverless function (fits on Vercel's free tier, or a
Cloudflare Worker given the ecosystem already runs several) that checks
the Stripe Checkout Session's `payment_status` or Gumroad's License
Verification API server-side before the client is allowed to set the
unlock flag, instead of trusting the redirect param alone. This is a
contained, scoped addition — it doesn't touch the existing paywall UI or
prompt-gating logic, only how the unlock is *confirmed*.

**Step 4 — consider a second tier. [needs decision, not yet built]**
The catalog is static (61 prompts, hand-authored). A recurring-revenue
option worth evaluating once Step 1–3 are live and generating any signal:
a small monthly tier for ongoing new-prompt drops, sold alongside (not
instead of) the existing one-time Pro unlock. Flagged as an option, not a
recommendation — needs real usage data first.

## Track 2 — software-online-review.com (content site)

**Step 1 — finish what's in flight. [needs decision — the user, not me]**
Upload the 1,103-record ads.txt via AdsTxtManager's manual-upload +
Synchronize Now flow (file already delivered this session).

**Step 2 — check traffic before paying for WordAds. [needs decision]**
Before upgrading to WordPress.com Premium ($8/mo), get the site's actual
monthly pageview count from the WordPress.com dashboard (Jetpack →
Stats) and compare it against WordAds' minimum threshold. If it doesn't
clear the threshold, the $8/mo buys nothing yet — worth knowing first.

**Step 3 — start an affiliate track in parallel. [needs decision on which
programs; executable once picked]**
Software-review content converts well to affiliate links (SaaS affiliate
programs, comparison-page CTAs) and has no plan-upgrade cost or traffic
gate to start. This needs the user to pick which tools/programs to apply
to (that's account-creation and program-terms territory, not something to
sign up for unprompted) — once accounts exist, adding the actual links
into content is a normal editorial task.

## Track 3 — software-review-platform

**No change from the archived strategy.** Still explicitly deferred to
its own Phase 3, after its Phase 1 MVP (review/moderation flow) actually
ships. Re-evaluate once that milestone is real, not before.

## Immediate next action

Everything above needs at least one decision from the user before further
code gets written (a URL choice, a price, a plan upgrade, or which
affiliate programs to pursue) — this document is the proposal to react to,
not a queue of tasks already being executed.

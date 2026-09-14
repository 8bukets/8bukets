# Ads, ads.txt, Cookies, and Google Ads Auctions

A study tying together three things this session touched separately —
ads.txt, cookie behavior, and how Google Ads' auction works — because
they get conflated easily and sit on **opposite sides** of the ad
ecosystem. Getting that split wrong leads to real mistakes (e.g. trying
to "improve Ad Rank" for a site that's a publisher, not an advertiser).

## The split: two unrelated Google ad products

| | **Google Ads** | **AdSense / Ad Exchange (what ads.txt governs)** |
|---|---|---|
| Who uses it | Advertisers — businesses paying to show ads | Publishers — sites earning money by hosting ads |
| What it does | Runs the auction described below to decide whose ad appears in a search result | Decides which advertiser's ad fills a slot on *your* page, and pays you for it |
| Where it applies here | Not currently used anywhere in this org's stack | `software-online-review.com` — this is the system the ads.txt work this session was for |

These are separate Google products with separate accounts, dashboards,
and money flows (you'd *pay into* Google Ads, you *get paid by*
AdSense/Ad Exchange). Sources: [Google Ads vs. AdSense — PPC
Hero](https://ppchero.com/google-ads-vs-adsense-whats-the-difference/),
[Google's own AdSense/Ad Manager help
page](https://support.google.com/admanager/answer/76231?hl=en).

`software-online-review.com` is purely on the publisher side. Nothing
below about auctions or bidding applies to it unless this org ever
starts *running* ads elsewhere to drive traffic to it — a different,
optional, additive strategy from what's built so far.

## Part 1 — ads.txt (publisher side, what we actually built)

ads.txt is an IAB Tech Lab initiative: a text file publishers host
listing which companies are authorized to sell their ad inventory. Its
purpose is fraud prevention, not ad selection — it doesn't influence
which ad wins a slot or how much it pays; it lets ad buyers verify a
seller is legitimate before spending money, mainly to block **domain
spoofing** (an unauthorized third party fraudulently claiming to sell a
site's inventory) and **inventory arbitrage**. Source: [IAB Tech Lab —
ads.txt](https://iabtechlab.com/ads-txt/).

What's actually in place: a 1,103-record ads.txt file (built and merged
across four separate pastes this session) naming `software-online-review.com`'s
authorized sellers across 30+ ad exchanges (Google, PubMatic,
Rubicon/Magnite, OpenX, Index Exchange, TripleLift, and others). It's
built and delivered; syncing it live via AdsTxtManager was the
remaining manual step.

## Part 2 — cookies (the compliance layer sitting on top of Part 1)

Every ad exchange named in that ads.txt file is a **third party** that,
once it wins an auction to show an ad on the site, typically sets its
own tracking cookie in the visitor's browser — for frequency capping,
retargeting, and measurement. This is standard for programmatic
advertising and is exactly what running 30+ exchanges implies.

Two compliance facts worth being explicit about:

1. **Advertising cookies need opt-in consent under GDPR**, not just a
   notice. Consent must be a clear affirmative action (no pre-checked
   boxes), and third-party ad tags should be blocked by default until
   the visitor opts in to a "Marketing" or "Advertising" category.
   Source: [iubenda — Cookies and the
   GDPR](https://www.iubenda.com/en/help/5525-cookies-gdpr-requirements/).
2. **The site owner is responsible for third-party cookies fired from
   their domain**, even ones set by an ad exchange's own script, not
   code the owner wrote. GDPR holds the publisher accountable for what
   activates on their domain. Source: [Secure Privacy — GDPR cookie
   categories](https://support.secureprivacy.ai/article/should-you-block-all-cookies-gdpr-cookie-categories-explained/).

This session could not directly scan `software-online-review.com`'s
live cookies — outbound access to that host is blocked by this
sandbox's egress policy (a 403 at the proxy level, confirmed, not
worked around). Given 30+ configured ad exchanges, the reasonable
assumption is that real third-party ad-tracking cookies fire once ads
render — worth confirming with a real consent-management platform (CMP)
scan of the live site from outside this environment, and pairing it
with a cookie-consent banner if one isn't already in place. Separately,
the `eightbukets` prompt-library app (published as an Artifact this
session) was checked directly and sets **zero cookies** of its own —
its only client-side storage is a `localStorage` flag for the Pro
unlock, and its only external resource is a styling CDN script.

## Part 3 — how the Google Ads auction actually works (advertiser side)

For if/when this org ever runs Google Ads campaigns (e.g. to send paid
traffic toward `software-online-review.com` or a future product) —
verified against Google's own documentation:

1. **Trigger**: a search query matches an advertiser's chosen keywords.
2. **Filtering**: Google removes ineligible ads (wrong location/device
   targeting, policy violations).
3. **Ad Rank**: each remaining ad is scored using the advertiser's bid,
   **Quality Score** (expected click-through rate, ad relevance,
   landing-page experience), the competitiveness of the auction, and
   the search context.
4. **Winner selection**: highest Ad Rank wins the slot(s).
5. **Cost**: the winner pays the minimum needed to beat the
   next-highest competitor — usually less than their max bid.

One correction to the pasted summary this study responds to: Google has
**never published the actual Ad Rank formula**. "Bid × Quality Score"
is the simplified mental model taught everywhere, but Google computes
it dynamically per-query using additional real-time signals (device,
context, expected format impact) that aren't fully disclosed. Treat any
specific formula as a teaching approximation, not the literal
mechanism. Source: [Google Ads Help — How the Google Ads auction
works](https://support.google.com/google-ads/answer/6366577?hl=en);
simplification caveat cross-checked via [2026 Ad Rank
guides](https://www.factors.ai/blog/google-ad-rank).

**Bidding types**, unchanged from standard Google documentation:
- **Manual CPC**: you set the max cost-per-click per keyword yourself.
- **Smart Bidding**: Google's automated bidding using real-time signals
  (device, location, time of day) optimized toward a stated goal
  (clicks, conversions, target ROAS, etc).

Two clarifying questions before this part is actionable, since none of
it is set up yet: is this for a **new or existing** Google Ads account,
and is the goal **clicks, leads, or sales** — the answer changes which
bidding strategy makes sense, and nothing here commits to one.

## How the three parts connect

- ads.txt (Part 1) and Google Ads auctions (Part 3) are **not the same
  auction** and don't interact — one sells the site's ad space to
  buyers, the other buys search placement for an advertiser. Running
  Google Ads campaigns would not change anything about how ads.txt or
  the site's own ad revenue works, and vice versa.
- Cookies (Part 2) are the one place these actually touch: the same
  browser could carry both a publisher-side ad-exchange tracking cookie
  (from Part 1's inventory being sold) and, separately, a Google Ads
  conversion-tracking cookie (from Part 3, if campaigns ever run) — both
  need to be covered by one consistent, honest consent banner rather
  than treated as two separate compliance problems.

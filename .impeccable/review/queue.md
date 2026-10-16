# Review loop queue

Rounds 1 to 5, kept current by the developer and closed after the loop. One line per task: id, priority, status, title, and for done tasks the commit on the review-loop branch. Tasks marked owner waited for Andrew; his decisions of 16 October 2026 are recorded on each line.

## Design
- design-1-1 [P1] done c617b16: Fix the launch price rendering as "$7 . 5k" (design)
- design-1-2 [P1] done 5bf1a95: Remove the fixed ambient copper blob behind every section (design)
- design-1-3 [P1] done 90a1f46: Retire the copper rule and the steel dash from the section openings (design)
- design-1-4 [P1] done 77c2cf6: Unstick the offer panels: a plain list, no stacking, no lift shadow (design)
- design-1-5 [P1] done 37d21ca: Tighten the vertical rhythm: the page is 18,060 px at 1440 and 25,552 px at 390 (design). Measured at the end of round 1: 17,055 px at 1440 and 22,571 px at 390. The 16,000 and 22,000 px targets retired with design-2-1; at the end of round 2 the page is 16,475 px at 1440 and 21,810 px at 390.
- design-1-6 [P2] done 6e433f2: One rule for copper inside the three metrics (design)
- design-1-7 [P2] done 383d593: Situations as a two-column hairline list instead of six slate boxes (design)
- design-1-8 [P2] done e0e5c1f: Phone people as rows: portrait beside the name, bio below (design). The prescribed selector also caught the links div; it is excluded so the links keep their own row.
- design-1-9 [P2] done 4974767: Burn the thesis line in: "We do not bill hours." arrives as ember and cools (design)
- design-1-10 [P2] done 221ecb4: Cases strip: previous and next controls for readers without a trackpad (design)
- design-1-11 [P2] done 16650dd: Header reflects the section in view (design)
- design-1-12 [P3] done f377eb8 and 17b96bf (rejected in round 2 for the resting bloom; cooled further after the loop on Andrew's word): Hero rune at rest: cooled metal, not a neon tube (design). Checked in Chromium and WebKit through Playwright, not in Safari itself.
- design-1-13 [P3] done 29f3e8a: Unlit pieces of the build diagram in seam, not 16 percent copper (design)
- design-1-14 [P3] done c2df609: Fewer 75 px headlines: Names and Record take the subhead role (design)
- design-1-15 [P3] done 086611d: Closing scene on the phone: close the empty gap above the mark (design). The mark is also kept above the text block on a phone in landscape, where it overlapped the headline before.
- design-2-1 [P1] done aaefb7f: Offer as hairline rows: take the five panels off their slate sheets, price as the news (design). At 1440 the offer section measures 2,692 px (3,167 before) and a row 337 to 448 px; at 390 each row shows the title and then the price 4 px under it in its first screen. The list squares were already steel, as the key characteristics say, and stay steel.
- design-2-2 [P2] done 6fa9f77: First screen: the header button stays quiet until the mark lands, then fills copper with it (design). The pending state is carried in the rune page's markup and gated on html.js: WebKit paints before the end-of-body script runs and showed a copper flash on load otherwise. Verified in Chromium and WebKit at 1440 and 390 and under reduced motion.
- design-4-1 [P2] done 5e5583f: Offer rows on the phone: word prices read as a second line of the title (design). Measured at 390: Free and Quote per scope at 21 px in smoke 4 px under the 24 px ash title; number prices unchanged at 30 px, $7.5k copper. At 1440 the word prices stay right-aligned at 32 px, now in smoke.
- design-5-1 [P2] done ec4697d: Cases strip: the links follow the body, the air sits at the bottom of the card (design). Queued in round 5 after all three reviewers approved; implemented after the loop. Body to links 18 px at 1440 and 390.

## Copy
- copy-1-1 [P1] done 5b4234e: Name Opera and 1inch on the RPC proxy and give the lead number its own case (copy)
- copy-1-2 [P1] done 1c13fad: Swap the centre metric from the NFT raise to $1B+ locked in staking (copy)
- copy-1-3 [P1] done e43e52d: Take Snark.art out of the lead cases, add the identity case, and order the strip as the register prescribes (copy)
- copy-1-4 [P1] done 3b60285 (Andrew, 16 October 2026: the case stays, the Platform department clause goes): DeepNode: confirm or remove the Platform department claim, and decide whether row L belongs in the lead cases (copy)
- copy-1-5 [P1] done bebbeb3: Remove Gateway and Parity from the names wall (copy)
- copy-1-6 [P1] done 3cdc1d5: Closing: replace "Let's talk." with the workshop promise and tell the reader what to write (copy)
- copy-1-7 [P1] closed (Andrew, 16 October 2026: $4k is the deliberate price; rate-card.md in felag-core is to be updated to match): Fractional CTO price on the page disagrees with rate-card.md (copy)
- copy-1-8 [P2] done 83f3ac9: FAQ: "the principals" are not all in the Netherlands and Cyprus (copy)
- copy-1-9 [P2] done f72c591: Put a subject on every mailto so the reader does not face a blank message (copy)
- copy-1-10 [P2] done 545ac91: Record: close the Gateway.fm era and fill the empty Felag era (copy)
- copy-1-11 [P2] done c05c430: Names wall lead: drop "the line it is allowed to carry" (copy)
- copy-1-12 [P2] done 09dd5a6: Offer lead line: carry the model, not only the currency (copy)
- copy-1-13 [P2] done fdae0cb: How: state the sprint outputs and the build path in steps 2 to 4 (copy). Step two's title ran five lines at 1440 against two for the others; fixed in copy-2-1.
- copy-1-14 [P2] done 150f0bf: FAQ: remove the two answers that repeat other sections word for word (copy)
- copy-1-15 [P2] done b62217c (Andrew confirmed the ownership term, 16 October 2026): FAQ: add the question a sprint buyer asks, what they keep if they stop (copy)
- copy-1-16 [P2] done 124f9aa (Finland and Armenia, Andrew, 16 October 2026; team-and-history.md to carry the same): People: locations for Pavel and Andrey, or an even rule for all four (copy)
- copy-1-17 [P2] closed (Andrew, 16 October 2026: no entity line): Footer: one entity line for the diligence reader (copy)
- copy-1-18 [P2] closed (Andrew, 16 October 2026: the three tellings stay): Fold the three tellings of the proof: wall details point to the record (copy)
- copy-1-19 [P3] done 9a3ee6c: People note: say who acquired Uddug (copy)
- copy-1-20 [P3] done db73867: Header: "Offer" becomes "Prices" (copy)
- copy-1-21 [P3] done c07ef65: Break the run of counted headlines (copy)
- copy-2-1 [P2] done 3eef399: How: a two-line title for step two so the four steps read as one row (copy). Two lines at 1440 and at 390, measured.
- copy-2-2 [P2] done cee9917: The ~25 people sentence attaches the two-department headcount to one department (copy)
- copy-2-3 [P2] closed (Andrew, 16 October 2026: Snark.art stays on the wall): Snark.art on the names wall: register row X keeps it out of Felag delivery lists (copy)
- copy-2-4 [P3] done a4b9197: llms.txt people lines: lowercase the location so it reads as one sentence (copy)
- copy-3-1 [P2] done 252ae37: How: the eyebrow repeats the headline word for word (copy). The rune eyebrow reads How we work; the h2, the nav label and the llms.txt heading stay.
- copy-3-2 [P2] done 3156133: Metric strip: date the $1B+ locked figure, as the rule requires (copy). The label stays two lines at 1440 and runs three at 390, measured.
- copy-3-3 [P2] done b3a81ed: Offer rows: the body restates the Terms column, and Pods lists the fixed-price build as a pod deliverable (copy). llms.txt and the JSON-LD Offer descriptions followed from the constants; make_dist.py needed no change.
- copy-4-1 [P2] closed (Andrew, 16 October 2026: the case stays unlinked until a live artefact is recorded in row C): Proof register row C: the XIP-9 artefact URL is dead, so the Infinex case carries no public link (copy)

## SEO
- seo-1-1 [P0] closed (Andrew, 16 October 2026: $4k is the deliberate price; rate-card.md to be updated first): Fractional CTO price on the page is not the rate-card price (seo)
- seo-1-2 [P1] done cc299e4: Add a JSON-LD graph: Organization, WebSite, WebPage, four Person entities, the offers and the FAQPage (seo). The Fractional CTO offer carries no minPrice until seo-1-1 is decided.
- seo-1-3 [P1] done 97fa6fb: Meta description at 152 characters instead of the 255-character statement (seo)
- seo-1-4 [P2] done 45a89e5: Title under 60 characters with the category noun (seo). The title is 60 characters.
- seo-1-5 [P2] done 1d29442: Publish /llms.txt, a plain-text summary built from the page constants (seo)
- seo-1-6 [P2] done e566b22: Footer links the X profile that twitter:site already names (seo)
- seo-1-7 [P3] done 2737da5: Complete the social preview tags: og:locale, og:image:alt, twitter:title, twitter:description, twitter:image (seo)
- seo-1-8 [P3] done 30d94e8: Portrait alt text names the role, not only the name (seo)
- seo-1-9 [P3] skipped: Names wall says Gateway.fm, as every other mention does (seo). The Gateway entry left the wall in copy-1-5, so there is nothing to rename.
- seo-1-10 [P3] done ea88064: Sitemap lastmod from the last source change, not the build date (seo)
- seo-1-11 [P3] done d4c37f2: Self-host the two fonts with preload to drop two cross-origin hops from the critical path (seo). One variable Schibsted Grotesk file for 400 to 600 replaces the three per-weight files, since Google serves the same file for all three; check.py's browser pass now serves dist over local http so the fonts load.
- seo-2-1 [P2] done 9a47a4f: Hero text rises at 1.1 s, so the largest text on the page is invisible for the first second (seo). The rise now starts at 0.2, 0.4 and 0.6 s; the h1 is at 0.999 opacity 1.0 s after load in Chromium and the rune's first stroke shows by 0.8 s.
- seo-3-1 [P2] done f8846f4: Anchor landings clear the sticky header on the phone (seo). Eyebrow lands at 162 px at 1440 and 136 px at 390 for the four nav links and See prices, measured in headless Chromium.

## After the loop, Andrew's reversals of 16 October 2026
- design-1-3 reversed in 4075771: the 120 px copper rule grows under every section headline again.
- design-1-4 and design-2-1 reversed in 01bb3c6: the five offers are stacking slate panels again, with the loop's price fixes kept inside them.
- New in c00cb92: every block rises and fades in as it enters, staggered inside a group; off under reduced motion.

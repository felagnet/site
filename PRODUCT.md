# Product

<!-- impeccable:product-schema 1 -->

Recorded 15 October 2026 from the repository, the felag-core plugin and Andrew's answers in the chat. Facts about the company change in felag-core and Notion first; this file records what the site must follow and what is still open.

## Platform

web

## Users

The primary reader is the CTO or head of engineering of a funded technology company who is checking Felag out. They arrive from a LinkedIn post, a DM or an introduction, are already in a conversation or about to be, and read the page to confirm that the people and the proof are real before replying or taking the free workshop. Confirmed by Andrew, 15 October 2026.

The buyer situations the copy serves, from core.md and the site's "Who we work with" section: a post-raise Series A or B CTO with a hard integration and no senior hire in time; a funded technology company with a performance, scale or reliability problem; a regulated payments or asset issuer rebuilding for MiCA, DORA, the UK regime, GENIUS, VARA, HKMA or MAS; a licensed fintech replacing a failed offshore vendor; a founder with a co-founder gap; a product agency without a senior backend bench. positioning.md (draft, unlocked) orders effort for the next twelve months with Series B to C B2B SaaS first; the site does not reorder its buyers until that document is locked.

Secondary readers who vouch for Felag to someone else: investors and acquirers buying technical due diligence, referral partners, and a prospect's board.

## Product Purpose

felag.net is one page that lets the reader verify Felag and take the next step. It is live at felag.net today, served by GitHub Pages on every push to main; the Short blurb in core.md still says "new site going live soon" and that line is due to drop.

Success for a visit is an email to info@felag.net asking for the free technical workshop. That is the only action on the page: the header button, the closing section and the offer section all open the same mailto. No forms, scheduling links or chat are planned. Confirmed by Andrew, 15 October 2026.

## Positioning

Senior engineers who own the architecture and ship to production. A principal-led studio for technology companies, priced on outcomes rather than hours. Both lines are locked in core.md, used verbatim on the site, LinkedIn and proposal covers, and are never edited by an agent.

The statement under "The studio" reads "Felag is a boutique, principal-led software engineering studio for technology companies. Our pods own the architecture and delivery of platforms, distributed systems, AI infrastructure, payments and identity." Andrew chose it for both founders on 21 October 2026, broadening the earlier core.md sentence (funded fintech and technology companies; backends, payment systems and identity infrastructure) to match the published cases. It keeps the position-layer rule below: no chain or crypto words. core.md in felag-core still carries the earlier sentence; a founder updates it there.

What a neighbouring agency cannot truthfully copy:

- A named principal leads every engagement, is written into the SOW, and is substituted only with the client's consent. Contractors join on demand and are never sold as principals.
- No hourly billing. Every build starts with a paid Architecture Sprint; fixed-price builds are quoted from a completed sprint; pods and fractional CTO work are monthly retainers; the workshop is free and ends in a decision, never a spec.
- The record: Felag is the 2026 restart of Uddug, founded 2018 and acquired in June 2024, and the founders have worked together since 2015. The proof is Gateway.fm-era and Uddug-era production work, named where the register allows.

Positioning layers from core.md: the position layer (hero, statement, profiles) carries no Web3, chain or crypto words; the capability layer lists backend and infrastructure at scale, payment rails, identity and SSO, then distributed ledgers last; the proof layer may say everything that shipped, on-chain included. Web3 is experience carried, not the market led with.

## Operating Context

- Master facts live in the felag-core plugin (`~/.claude/plugins/synced/.../felag-core/skills/felag-core/reference/`: core.md, positioning.md, proof-register.md, portfolio.md, rate-card.md, team-and-history.md, editorial-rules.md, voice.md, design.md) and in Notion, which is master for records (proof and portfolio, team, partners, deals). A fact changes there first, then on the site.
- Copy lives in the data constants at the top of felagsite.py; the hero line and sub-line in build_site.py; the page chrome in shared.py. `python3 build_site.py` writes out/felag-rune.html, `python3 make_dist.py` assembles dist/, and `python3 check.py` runs the wording rules, the hero line, the calls to action, the portraits and People links, the head tags, the dist file list, a browser pass at 1440, 1728 and 390 px wide and with reduced motion, and every external link. A failed check stops the deploy.
- The harvest page (out/felag-harvest.html, hero6-field.js, lib/three.min.js) is a kept prototype that is not deployed.
- Company pages: linkedin.com/company/felagnet, github.com/felagnet, x.com/felagnet. Public contact on the site is info@felag.net.
- The people on the page: Andrew Skurlatov (co-founder and CTO, Netherlands), Mikhail Manko (co-founder and CEO, Cyprus), Pavel Dodonov (Principal Engineer, partner, Serbia), Andrey Solovov (Principal Engineer, partner, Finland; both locations from Andrew, 18 October 2026, matching their GitHub profiles, replacing Finland and Armenia of 16 October, to be added to team-and-history.md). Bios are copied verbatim from team-and-history.md.

## Capabilities and Constraints

- One page, in this order: hero, the studio statement, what we build (four capabilities mapped to the four pieces of the mark), proof, names wall, the record as a short lineage from 2014 with the full history, era by era and every project in it, collapsed under it, what it costs, how an engagement runs, who we work with, who we are, questions, next step, footer.
- Offers and prices on the page come from rate-card.md: free technical workshop; Architecture Sprint from $10k (Andrew, 18 October 2026, replacing the $7.5k launch price; rate-card.md is to be updated to match); Fractional CTO from $4k a month (a deliberate price Andrew confirmed on 16 October 2026; rate-card.md still says $8k and is to be updated to match); pods $10k to $60k a month in three tiers (from $10k one senior with weekly principal review, from $25k a part-time principal with one or two seniors, up to $60k a full-time principal leading two to three); technical due diligence quoted per scope, report in one to two weeks from access; Fractional CTO initial term one month; sprint credit 30 days from delivery; no hourly billing and no time-and-materials exception. Prices in USD excluding VAT.
- Copy is locked for agents. A suggested copy change goes to .impeccable/review/copy-notes.md, not to the source.
- Wording rules enforced by check.py: never "passionate", "cutting-edge", "seamless", "empower", "world-class", "AI-first", "four people", "Talk to a founder", "sold to", "Andrei". No em dashes and no exclamation marks anywhere, including comments and commit messages. Sentence case.
- Felag's headcount is never stated: no count of founders, principals or people. The site shows the four people without counting them.
- The legal entity is stated in full in the footer and the contract FAQ: FELAG LLC, a Georgian limited liability company with identification number 426561829 and registered office at Georgia, Gardabani Municipality, Poladaant Kari Village, 4th Street, Lane II, N 11. Decided by Andrew on 19 October 2026, replacing the earlier "Felag, incorporated in 2026" with no country. Andrew's location is stated as "Netherlands".
- The page carries no analytics, cookie banner, chat widget, third-party script, new font or new dependency. Schibsted Grotesk and IBM Plex Mono are self-hosted under static/fonts as OFL woff2 files with their licences beside them; the rune page loads nothing external.
- Delivery runs on an internal AI-assisted development framework under the named principal's review. AI is internal capability, never the headline, and productivity multiples are not published.

Open decisions, recorded, not invented:

- A Contracting section (legal entity, principals, named principal, contractors, billing, and three bracketed placeholders) is built by felagsite.py but never placed on the page, so none of it is public. Andrew does not want it on the site (15 October 2026) and leaves the source as it is. Logged in .impeccable/review/copy-notes.md.
- positioning.md is draft 0.3.2 and unlocked: the supporting paragraph, the three verb-phrase families and their order, and the three sprint scopes in offers.md are not on the site until both founders lock them.
- The rate-card review (two-principal pod as default, sprint at the top of its band) is open; the site follows the published card.
- An EU contracting wrapper (NL BV) is undecided; nothing on the site promises EU establishment.
- Decided by Andrew on 21 October 2026: robots.txt keeps allowing every crawler, AI training crawlers (GPTBot, ClaudeBot, CCBot, Bytespider) included, so answer engines learn the name alongside the same-name felag.io.
- Decided by Andrew on 16 October 2026 in the review loop: no legal entity line in the footer (reversed on 19 October 2026: the footer carries the full entity); the proof stays told three times (strip, wall, record); Snark.art stays on the names wall and DeepNode in the lead cases, both in the register's wording for Andrew's personal rows; the Infinex and XIP-9 case stays unlinked until proof-register.md row C carries a live artefact; the FAQ carries the sprint-ownership term from positioning.md.
- The bridge case (the Uddug-era consumer high-load backend) enters the proof once its number is confirmed, target 31 January 2027. No non-fintech technology-company case is published yet.

## Brand Commitments

- The name in prose is "Felag". The wordmark in the lockup is "félag", lowercase with the acute accent, from the outlined files, never retyped.
- The mark is Fehu drawn as the counterform of a square: four copper pieces, three channels. It reads as a geometric symbol first, a rune second. Its geometry in the header, hero and closing scene stays exactly as it is.
- The design authority is felag-core reference/design.md and the two Claude Design artifacts it names (https://claude.ai/artifact/CSVQByqdycEwrxJZ5mFC1F and https://claude.ai/artifact/P4RdHJRFens3zJAi2dAg9L), with the brand pack in the collateral plugin. CLAUDE.md names DESIGN.md in this repository as the master; it does not exist yet and is to be written from the shipped site with `/impeccable document` (Andrew, 15 October 2026).
- Voice: first person plural, plain, specific, results first with the number in the sentence. Only REAL-tagged proof, in the register's wording, Default unless the portfolio shows NDA clear.
- Binding visual constraints Andrew set in CLAUDE.md: dark theme on the site; copper is the only accent; Schibsted Grotesk and IBM Plex Mono only; no runic alphabets as decoration, Norse imagery, hexagons, chains and nodes, circuit patterns, isometric cubes, stock photos, emoji, purple, neon green or a second accent.

## Evidence on Hand

- Proof wording as constants in felagsite.py (A_NAMED through Y_LINE, PROOF_CARDS, WALL, ERAS), taken from proof-register.md and portfolio.md. Named clients include Wirex Pay, Infinex and Synthetix, Humanity Protocol, DeepNode, EY Nightfall, LUKSO, Lumia, ApeChain, Presto, Gnosis, Ethereum Foundation, Web3 Foundation, Protocol Labs, Parity, OG:Crystals, Marscatsvoyage, Arsnl.art, Metazoku, Snark.art. Opera and 1inch are named on the RPC proxy case.
- External references linked from the page: L2BEAT listing for Wirex, the Gateway.fm Wirex partnership announcement (the Wirex blog post now returns 404), the Gateway.fm agentic identity case study, the KuCoin DeepNode listing, snark.art.
- Portraits of the four people in photo/people/ (andrew, mike, pavel, andrey, with the source files and base64 copies). og.png and apple-touch-icon.png in static/, drawn by make_images.py.
- Not on hand, and not to be fabricated: client testimonials, client logos, a case for a non-fintech technology company, a system taken through a MiCA audit, any AI productivity multiple, any headcount, any price not on the rate card.

## Product Principles

1. The named principal is the product. Every section should make it easy to see who leads the work and that they are real.
2. Proof is real and worded from the register. A number appears only as it was measured; a name appears only where the rights allow.
3. One action per visit: write to info@felag.net for the workshop. Nothing on the page competes with it.
4. Position vertical-neutral, prove with everything. Chain words stay inside proof blocks.
5. Facts change upstream first. The site follows felag-core and Notion; a stale fact is reported there, not patched here.

## Accessibility & Inclusion

- Every text and accent pair in the token set passes WCAG AA on the dark background and surface (design.md).
- With prefers-reduced-motion the page shows the finished mark in the hero and the closing scene with no animation; check.py verifies this in the browser pass.
- Skip link to main content; canvases are aria-hidden; the lockup carries an accessible name; focus is visible on links and buttons.
- The browser pass covers 1440, 1728 and 390 px wide.

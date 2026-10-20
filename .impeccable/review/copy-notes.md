# Copy notes

Suggested copy changes that an agent may not make. Each note names the section and the reason; the source stays as it is until Andrew changes it.

## 15 October 2026, Contracting and security

The CONTRACT list in felagsite.py carries three bracketed placeholders: Subcontracting and IP, Incident contact, DORA and ICT vendor pack. Andrew decided during /impeccable init that none of them is needed on the website. Corrected 16 October 2026: the audit found that the Contracting section is built but never placed on the page, so nothing was ever public and there is no visible copy to remove. The source stays as it is, by Andrew's decision.

## 16 October 2026, Proof, from the critique

The proof is told three times with the same sentences: the cases strip, the names wall detail lines, and the record. The Wirex line appears four times on the page (card 1, the wall, the 2024 record row, FAQ answer 5). The distill pass kept every word and changed only structure; these are for Andrew:

- The names wall detail lines repeat the record rows almost verbatim. Suggestion: a name jumps to its record row instead of opening a duplicate line, or the wall carries only the names.
- The cases strip order puts Snark.art and Arsnl.art, two NFT platforms, second and third after Wirex Pay, and ICEX, a failure, last. A fintech CTO reading the strip from the left meets NFTs before Infinex or Humanity Protocol.
- The middle headline metric is "$100M+ raised, collectively, by NFT launches by our team". For a vendor to fintech, a reliability or scale number would carry more.
- The Stack line in What we build names EVM, Solana, Cosmos and six more chains inside the capability layer; PRODUCT.md keeps chain words in the proof layer.
- The meta description is the 255-character statement; search engines cut at about 155 characters.

## 16 October 2026, from the second critique

Design-side fixes are done; these need Andrew's words or links:

- A "Led by" line on each proof card and record row, naming the principal, so the proof carries the product. The era notes already hold the fact for some cases.
- The names wall's detail lines repeat the record rows; folding them into the record removes visible text, so it waits on Andrew.
- The founders' faces beside "Write to us" in the closing scene would need alt text, which is copy.
- A subject on the mailto, so the reader does not face a blank message (a link change).
- The centre metric is the NFT raise; a reliability or scale number would carry more for a fintech reader.
- "Based in" is given for two of the four people; all four or none.
- No legal entity, country or address appears anywhere; a one-line entity line in the footer would answer the diligence reader.

## 16 October 2026, after the review loop

The copy lock was lifted on the review-loop branch within felag-core rules. Of the notes above: the mailto subject, the centre metric, the strip order, the meta description, the two-department sentence and the locations are done on the branch; the wall fold, the entity line, the Led by line and the founders' faces are declined or left by Andrew (see .impeccable/review/queue.md). The Stack line in What we build is unchanged.

## 18 October 2026, the audit's three P0 issues

Andrew chose each fix in the chat and had the agent apply it on the review-loop branch, one commit per issue.

- C-03, Wirex partnership link: the Wirex blog post returned 404. WIREX_PR now points to the Gateway.fm post of 5 February 2024 (gateway.fm/blog/gateway-wirex-partnership), on the case card, the names wall and the 2024 record row. The label stays "Partnership announcement". Wirex's own PR Newswire release (ANP persportaal) and a Wayback copy of the blog post were the alternatives.
- C-02, OG:Crystals: the "$10M+ at launch" figure is gone. OG.Art reports $4.2M primary and $9M secondary, and secondary sales are not money raised. The line now gives Uddug's engineering role, with Snark.art. No figure.
- C-01, grants: "won and delivered" became "took on grant work", naming JuniDB, and the dates are now 2020 to 2023 to cover GitSEC. Open risk: the W3F register shows JuniDB as terminated, and the only Protocol Labs application the auditor found (GitSEC) was declined. Unless a Protocol Labs award other than GitSEC can be cited, a re-audit may still flag the Protocol Labs name.
- Not in the audit, same pattern: P_LINE says "Marscatsvoyage, $2M+ at launch" and may draw the same primary versus secondary question.

## 18 October 2026, SEO audit S-02 to S-10

From the auditor's five remaining changes. S-05 is done on the seo-audit branch with no copy change, and S-03 merged in C-03 above. These need Andrew's facts or words:

- S-03, Wirex card, wall line and 2024 record row: the Gateway.fm post of 5 February 2024 supports the private zkEVM rollup, the smart contracts, the backend oracles between off-chain KYC and the contracts, the card integration and MiCA. It does not mention the indexer or account abstraction, and it does not say "end to end"; the August 2024 launch rests on the L2BEAT link. Either cite a source for the indexer and account abstraction, or mark those parts as the team's account.
- S-04, proof claims that need evidence beside them: the 140k+ requests per second RPC figure (Opera and 1inch), the Humanity Protocol application layer, the shared prover (EY Nightfall, Polygon zkEVM, Miden, Iden3) and the XIP-9 contribution for Infinex. Where nothing public corroborates the team's specific work, say it is the team's account; project pages show context, not the team's part.
- S-02 and S-04, focused pages: the auditor proposes four pages with their own title, h1, canonical and sitemap entry: Architecture Sprint, Fractional CTO, payments infrastructure engineering, and the Wirex Pay contribution. Each needs new copy (who it is for, deliverables, who leads, price basis, how to begin; for the case: problem, contribution, period, team, evidence). This is new visible text, so it waits on Andrew's words.
- S-08 and S-09, People: Pavel's card says Finland and his GitHub profile says Belgrade, Serbia; Andrey's card says Armenia and his GitHub says Helsinki and Freelance, spelled Andrei. The site carries Andrew's decision of 16 October 2026. The profiles are theirs to update, or the cards change.
- S-10, contracting entity: "The contract is with Felag" names the brand only. The auditor wants the registered counterparty, jurisdiction and registration number, the same on the page, the JSON-LD and llms.txt, and kept apart from where the founders live. Andrew declined a footer entity line on 16 October 2026 (copy-1-17); the audit asks again.

Andrew's decisions, 18 October 2026, in the chat:
- S-03: the Wirex line stays as it is; the indexer and account abstraction are the team's work whatever the Gateway.fm post mentions.
- S-04 evidence: the RPC figure, Humanity Protocol, the shared prover and XIP-9 stay as they are, with no added links or labels.
- S-02 and S-04 pages: none for now; felag.net stays one page.
- S-08 and S-09: Pavel is based in Serbia (Belgrade) and Andrey in Finland. Applied in d788bf8, by the agent on Andrew's word. The name stays spelled Andrey.
- S-10: the contract stays with the brand, as decided on 16 October 2026 (copy-1-17).

## 18 October 2026, the priority copy pass

The live re-audit's priority report (C-01, C-04 to C-41, from the summary; the full 41-row table was not shared). Andrew settled every gap in the chat and approved the plan; the agent applied it on worktree-copy-pass, one commit per change.

Done:
- Opening (C-04): the statement is the auditor's two sentences, boutique engineering studio and principal-led pods kept.
- Repetition (C-27, C-30 to C-32, C-40): no "clear no" left (was 5); "named principal" 0 (was 13), with the staffing commitment stated once under the offers; "told as it was", "One team, three names", "on the record", the offshore vendor and the fifteen-person shop are gone. Visible words 3,572 to 2,673.
- Proof (C-06 to C-15, C-33): three lead cases, Wirex Pay, Arsnl.art and the identity work, each with Delivered, Constraint or Status, and Result. The identity work is marked as a pilot and proof of concept. The wall shows names and eras only; the record keeps one short line per row and is the home of the secondary cases and ICEX. Andrew's bio no longer retells the cases.
- Fees (C-05, C-16 to C-20): heading "We sell outcomes, not hours." with each fee model under it; sprint from $10k with no launch or list price; three pod tiers; workshop 60 minutes with a reply within two working days; sprint credit 30 days from delivery; fractional CTO one-month initial term; a missed pod deliverable triggers a scope and plan review; diligence report one to two weeks from access; no time-and-materials exception anywhere.
- Route (C-21, C-25, C-26, C-28, C-29): situations follow the statement; How delivery starts covers a pod or a fixed-price build, and one line routes CTO work and diligence.
- Contact (C-22, C-24, C-41): every button reads "Discuss your project"; the mailto and the visible address are unchanged.

Departures from the auditor, by Andrew's decision:
- Outcomes over hours is kept as positioning. The locked hero sub-line, title and meta description ("priced on outcomes rather than hours") stay as they are; core.md is unchanged.
- No people are named on the lead cases; employer and era only.
- Grants (C-01): R_LINE stays; the Protocol Labs evidence is no longer public. A re-audit may flag it again.
- Legal entity: the line stays "Felag, incorporated in 2026".
- AI in delivery: the framework stays a short claim, to be described publicly later.
- Prepaid fees on cancellation: not stated on the page.

Still open:
- rate-card.md and core.md need the new sprint price, pod tiers and one-month CTO term.
- Arsnl.art has no stated constraint and no public link.
- P_LINE (Marscatsvoyage, "$2M+ at launch") has the same primary versus secondary question as OG:Crystals.

## 19 October 2026, the proof restored

Andrew chose to bring the proof back as it stood on main: the ten lead cases with their full paragraphs, and every name on the wall opening its one-line story. This replaces the three-case facts layout and the names-and-eras wall from the pass above, and with it the "no people named" rule: the DeepNode card and the Snark.art line name Andrew again. ICEX is a card again, so its record row is gone; its kicker keeps "never launched". The record's short lines and Andrew's trimmed bio stay.

## 18 October 2026, UX audit D-09: words the cases strip needs for screen readers

Andrew's decisions in the chat: after a press of Previous or Next the strip reads out the card now at the left edge in its own visible words, its counter and title ("03 / 10, Identity for a global technology company"), and the strip takes keyboard focus under the existing "Lead cases" label. Both are applied with no new words. He also wants the strip announced as a carousel with each card as a slide, which is new spoken text, so it waits here for his approval of the exact strings:

- Lead cases section (`#proof-cases`): add `aria-roledescription="carousel"`. Heard as "Lead cases, carousel".
- Each case card (`article.card`): add `role="group"`, `aria-roledescription="slide"` and `aria-label="3 of 10"` (the number and total from the card's position). Heard as "3 of 10, slide".
- Optional, if the spoken counter "zero three slash ten" reads poorly: the status line could use the same "3 of 10" form instead of the card's visible "03 / 10", for example "3 of 10, Identity for a global technology company".

Until then the source carries none of these.

## 19 October 2026, copy round 3

The auditor's six focused changes. Andrew settled the gaps in the chat; the agent applied them on worktree-copy-round-3, one commit per change.

Done:
- Cases: all ten kept under "Selected engineering work", each with the contribution, Result, Status and, where a figure is the client's own, Context (the Humanity user count, the DeepNode valuation), a Details and evidence disclosure for measurement definitions, and the employer and date. ICEX reads "Exchange prototype and oracle development", its ending told in the details. The identity work is a proof of concept on both workstreams. The MiCA answer describes supported engineering and keeps the audit limit. Performance figures carry Andrew's generic qualifier: peak observed in production, aggregate across clients, during the period shown.
- Repetition: the wall lines are short relationships that point to the case; the record is a six-row lineage with the company background collapsed under it, keeping only the projects without a card; the bios start with what each person leads today and drop the project catalogues; the people note keeps only the contractor line.
- AI answer: the auditor's starting answer, nothing added.
- Terms: the footer and the contract answer name FELAG LLC in full; unused prepaid pod fees are refunded pro rata after notice; a new answer has deliverables accepted and scope changed at the monthly review; the entry pod's senior engineer plans the work; the fractional CTO works agreed days spread across Monday to Friday and owns the architecture and roadmap, engineering process and delivery, and board and investor representation (hiring is not listed, by Andrew's choice).
- Sentences: the four services in the auditor's copy, Payment rails, the questions heading, and the stack under a Technical capabilities disclosure.

Departures from the auditor, by Andrew's decision:
- The hero keeps the locked sub-line ("priced on outcomes rather than hours"); the statement stays in its own section, so it is not shown twice.
- No person is named on the cases; employer and date only. The DeepNode era reads "Independent engagement".
- Protocol Labs stays in the grants line.
- Pavel's "20+ published papers" stays without a bibliography link.
- No sentence on client code handling yet in the AI answer.

Resolved the same day:
- Statuses: all ten confirmed by Andrew as written.
- Andrew's bio opens "sets the technical direction at Felag, leads the architecture on its engagements and takes fractional CTO seats" (Andrew).
- Humanity Protocol result: a high-load application layer on the L2 chain at about 1,000 transactions per second (Andrew), with the generic measurement qualifier.
- Marscatsvoyage: "Uddug helped with the launch of Marscatsvoyage", the $2M+ figure dropped (Andrew).
- Arsnl.art links to arsnl.art (Andrew).
- Details and evidence for the shared prover, the Platform department and Arsnl.art, taken from the Notion proof register and felag-core team-and-history within their do-not-say rules. Every case now has a disclosure.

Still open:
- rate-card.md and core.md still need the sprint price, pod tiers, the one-month CTO term, the refund and the acceptance terms. Andrew: not now.
- The Notion proof register (master for proof) is behind the site on two rows: Humanity Protocol has no transaction figure, and Marscatsvoyage's wording still carries $2M+. A founder updates the rows.

Approved by Andrew on 19 October 2026, all three, the status in the "3 of 10" form. Applied on the strip-autoscroll branch.

## 19 October 2026, the cases strip drift: labels for its stop control

Andrew asked for the strip to scroll on its own, as a constant slow drift. The control that stops and restarts it is new spoken text; Andrew chose the strings in the chat: "Stop scrolling" while it drifts and "Start scrolling" once it is stopped. Applied on the strip-autoscroll branch. The control shows only an icon, so nothing visible changes.

## 19 October 2026, SEO metadata: title and description

The auditor proposed "Felag | Backend, Payments & Identity Engineering" and a description that names the audience and the services, both without outcome pricing. Andrew chose versions that keep it, in sentence case. Applied on the seo-metadata branch, with Open Graph, Twitter and WebPage taking the same values.
- Title: "Felag | Backend, payments and identity engineering, priced on outcomes" (70 characters; was "Felag, a principal-led engineering studio priced on outcomes").
- Description: "Principal-led engineering studio for funded fintech and technology companies. Backends, payments and identity, priced on outcomes rather than hours." (148 characters; was the hero line and the sub-line).

## 19 October 2026, the closing scene: a contact form like andskur.com's

Andrew asked for the contact form from andskur.com on felag.net and settled the gaps in the chat. The form sits in the closing scene under the mail paragraph and takes the place of the closing "Discuss your project" mailto button; See prices stays beside the submit button, and the header, hero and footer mailto links stay as they were. New visible strings, in Felag wording by Andrew's choice: the labels "The system and your deadline" and "Email", the submit button "Discuss your project", "Sending" while it posts, "Sent. We'll reply to the address you gave." on success, and "That didn't send. Email us directly at info@felag.net." on failure. The email subject Formspree sends is "felag.net: Free technical workshop".

Resolved the same day: Andrew created the Felag form in Formspree, id mppqeyyd, and the form action points at it.

## 20 October 2026, the Discuss your project buttons go to the form

Andrew asked for the header and hero buttons to scroll to the form and for the line above it to change, and settled both in the chat. All three Discuss your project buttons (header, hero and the one under the prices) now link to #contact, the closing scene's eyebrow, instead of opening an email. The footer's info@felag.net link stays an email link. The line above the form reads "Tell us about the system and your deadline. We start with a free technical workshop with a founder, and reply within two working days." (was "Email info@felag.net a short description of the system and your deadline. We start with a free technical workshop with a founder, and reply within two working days.").

## 20 October 2026, the people note

Andrew asked for the note under the four people to be rephrased and chose the wording in the chat. It reads "We bring in specialist contractors when a project needs them, always led by one of us." (was "Specialist contractors join when a project needs them. They work under one of us and are never presented as principals."). The commitment in PRODUCT.md, that contractors are never sold as principals, still holds; the page no longer states it in those words.

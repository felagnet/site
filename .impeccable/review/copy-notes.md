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

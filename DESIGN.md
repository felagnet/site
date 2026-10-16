---
name: Felag
description: Dark iron ground, one copper element that has just cooled.
colors:
  iron: "#0E1114"
  slate: "#151A1E"
  seam: "#262C31"
  steel: "#616A71"
  ash: "#E9ECEE"
  smoke: "#98A1A8"
  copper: "#DF8E63"
  hot-copper: "#EFA37C"
  deep-copper: "#8C4E2C"
  ember: "#FFE1C2"
typography:
  display:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(52px, 8vw, 132px)"
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.035em"
  metric:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(52px, 6.4vw, 108px)"
    fontWeight: 600
    lineHeight: 0.92
    letterSpacing: "-0.045em"
    fontFeature: "tabular-nums lining-nums"
  headline:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(40px, 5.2vw, 78px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.03em"
  subhead:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(30px, 3.4vw, 52px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(24px, 2.2vw, 32px)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.025em"
  title-small:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  lead:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "clamp(18px, 1.5vw, 22px)"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  prose:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: "28px"
    letterSpacing: "normal"
  body:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "26px"
    letterSpacing: "normal"
  small:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: "22px"
    letterSpacing: "normal"
  label:
    fontFamily: "IBM Plex Mono, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "20px"
    letterSpacing: "0.04em"
rounded:
  none: "0"
  sm: "2px"
  md: "4px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "64px"
  section: "clamp(80px, 10vh, 128px)"
components:
  button-primary:
    backgroundColor: "{colors.copper}"
    textColor: "{colors.iron}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 28px"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.hot-copper}"
    textColor: "{colors.iron}"
  button-small:
    backgroundColor: "{colors.copper}"
    textColor: "{colors.iron}"
    rounded: "{rounded.sm}"
    padding: "0 20px"
    height: "44px"
  link:
    textColor: "{colors.copper}"
  link-hover:
    textColor: "{colors.hot-copper}"
  nav-link:
    textColor: "{colors.smoke}"
  nav-link-hover:
    textColor: "{colors.ash}"
  eyebrow:
    textColor: "{colors.smoke}"
    typography: "{typography.label}"
  card:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.ash}"
    rounded: "{rounded.md}"
    padding: "36px"
  situation-row:
    textColor: "{colors.ash}"
    rounded: "{rounded.none}"
    padding: "28px 0"
  panel:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.ash}"
    rounded: "{rounded.md}"
    padding: "clamp(28px, 3.4vw, 48px)"
---

# Design System: Felag

## Overview

**Creative North Star: "The forge at rest"**

Dark iron ground and one copper element that has just cooled. The page is a large, exact, unhurried surface: oversized Schibsted Grotesk headings on long measures, hairlines instead of boxes, IBM Plex Mono for the small labels that date and number things, and copper as the only colour. Nothing moves unless the scroll asks it to, and when it does, the movement is a single idea: copper heats to ember, flares, and cools back to copper within two seconds. The mark is the only thing on the page that was ever hot.

The mark is Fehu drawn as the counterform of a square, four solid pieces and three channels, read as a geometric symbol first and a rune second. It carries the whole identity: it draws itself in the hero, lands in the header, becomes the diagram of what we build, and reassembles in the closing scene. Everything else defers to it. Confirmed rejections: no runic alphabets as decoration, no Norse imagery, no hexagons, chains, nodes or circuit patterns, no isometric cubes, no stock photography, no emoji, no purple, no neon green, no second accent.

Recorded 15 October 2026 from the shipped page on the impeccable-refine branch and the felag-core design rules. Where this file and felag-core reference/design.md differ, this file records what ships and Andrew's decisions in the chat; the token values are the same in both.

**Key Characteristics:**
- Dark only on the site. Iron ground, slate surfaces, seam hairlines.
- Copper is the single accent and it is spent sparingly: the mark, links, the primary button, prices, the lit marker and one emphasis per section. Labels, bullets, kickers and indices are smoke or steel.
- Type does the structure. Headings at 78 to 132 px with tight tracking, body at 16/26, mono labels at 12 to 13 px.
- Copper light is part of the system and always cools: the rune ignites once and settles to copper with a faint resting halo, the one light the page keeps at rest; the mark flashes as it lands, a metric burns in and cools, and a proof card blooms on hover.
- Nothing moves unless the scroll asks it to: no rise on reveal, no count-up, no panel that shrinks or dims, no pointer-following light or tilt. Scroll-driven scenes on desktop become static, single-column sections under 900 px and under prefers-reduced-motion.

## Colors

A near-black ground with two grey steps, two text greys, and a copper family that runs from deep to ember.

### Primary
- **Copper** (#DF8E63): the accent. The mark at rest, every link, the primary button, the rule under the closing headline, the copper half of progress rules, one price in the offer (the launch price), lit markers, the unit suffix inside a metric (k+, M+, B+), never the currency sign, the open capability title and the selected name on the wall.
- **Hot copper** (#EFA37C): hover and pressed state of anything copper, and the word that is lighting in the statement. Also the colour of the ignition glows.
- **Deep copper** (#8C4E2C): the border and wash of the turn-down block.
- **Ember** (#FFE1C2, `--ember`): the flash colour. The first frame of every ignition (mark, metric) and the bright end of the names-wall underline. Never a resting colour.

### Neutral
- **Iron** (#0E1114): the page background, the text on copper buttons and the fill of unlit era markers.
- **Slate** (#151A1E): cards, offer panels, portrait wells, the skip link.
- **Seam** (#262C31): every hairline: section rules, card borders, table and row rules, the era line, the cold half of a progress rule.
- **Steel** (#616A71): control borders and markers that need 3:1 against iron: the FAQ circle, era diamonds, metric top rules, list bullets.
- **Ash** (#E9ECEE): primary text and the wordmark.
- **Smoke** (#98A1A8): secondary text, lead paragraphs, labels, eyebrows, kickers, indices, era years, roles under the people, nav links at rest, protocol names on the wall.

Every copper light in CSS is written from the tokens `--copper-rgb`, `--hot-rgb`, `--ember-rgb` and `--deep-rgb`, and every veil from `--iron-rgb`, so the family moves together. Only the canvas scripts carry literal values.

### Named Rules
**The One Metal Rule.** Copper is the only hue on the page. Status colours from the master system (success, warning, error) are reserved for documents and tools and do not appear on the site.

**The Cooling Rule.** Ember appears only as the start of a transition that ends in copper or ash. If an element is ember or glowing after two seconds, it is a defect.

**The Text-on-Copper Rule.** Text on a copper fill is always iron, never ash and never white.

## Typography

**Display Font:** Schibsted Grotesk (with Helvetica Neue, Helvetica, Arial, sans-serif)
**Body Font:** Schibsted Grotesk
**Label/Mono Font:** IBM Plex Mono (with ui-monospace, Menlo, Consolas, monospace), for eyebrows, kickers, years, counts, identifiers and the skills line

**Character:** one grotesk at two extremes, very large and semibold for headings, modest and regular for reading, with a mono face doing the dating and numbering in the margins. Sentence case everywhere, never all caps. Both faces load from Google Fonts in weights 400, 500 and 600.

### Hierarchy
Eleven roles, each a token on the root (`--fs-display` to `--fs-label`), and nothing else. A new size joins the ramp as a role or does not ship.

- **Display** (600, clamp(52px, 8vw, 132px), 0.95, -0.035em): one statement per page, "We do not bill hours.", max 11ch, balanced wrap. Its rule carries heading specificity so nothing outranks it. It arrives as a burn, ember to ash over 2 s, the same cooling as the metrics; under reduced motion it shows in ash with no animation.
- **Metric** (600, clamp(52px, 6.4vw, 108px), 0.92, -0.045em, tabular lining figures): the three big numbers in proof, shown as measured, never counted up.
- **Headline** (600, clamp(40px, 5.2vw, 78px), 1, -0.03em): the hero h1 and every section h2, max 15ch, balanced wrap. No rule under it; the closing headline alone carries a 120 px copper rule that grows over 0.8 s.
- **Subhead** (600, clamp(30px, 3.4vw, 52px), 1, -0.03em): the studio statement (max 24ch, revealed word by word), era names in the record, offer panel titles and the prices, in ash with lining figures. A price that is a word, not a number, drops to the title role.
- **Title** (600, clamp(24px, 2.2vw, 32px), 1.1, -0.025em): capability titles, proof card titles, step titles, the people's names and the client names on the wall.
- **Title small** (600, 21px, 1.25, -0.015em): record case titles, situation titles (hot copper on hover), the turn-down title and the questions.
- **Lead** (400, clamp(18px, 1.5vw, 22px), 1.45, smoke): the paragraph under a headline, era intros, the wall detail line, the closing invitation and the protocol names on the wall. Max 34em.
- **Prose** (400, 17px/28px): long paragraphs set for reading: card and panel bodies, the notes under offers, how and people, and the answers in the questions. 34 to 56em.
- **Body** (400, 16px/26px): compact reading text: capability lines, record cases, step lines, situations and the bios.
- **Small** (400, 15px/22px): nav links, the small button, text links in cards and under the people, metric labels, offer term lists, roles under the people, the footer.
- **Label** (400 mono, 13px/20px; eyebrows at 12px/20px with 0.06em): everything in IBM Plex Mono: eyebrows, kickers, indices, counts, years, locations, the era labels and the Stack line, which is kept to 46em.

### Dim states
Content that has not yet lit in a scroll scene (statement words, inactive capabilities, steps still to come) sits at the `--dim` token, 0.5 opacity, which keeps ash and hot copper above 3:1 on iron. It never goes lower. A dimmed paragraph or index label borrows ash for the same reason and settles to smoke once its step or capability lights.

### Named Rules
**The Mono Rule.** Mono sets what dates, numbers and names things: labels, years, indices, identifiers, the stack. A sentence is never set in mono.

**The Tabular Rule.** Every metric and every column of numbers sets tabular lining figures; a single price inside a panel sets lining figures only, so a decimal point keeps its natural width.

**The Sentence Case Rule.** No uppercase styling anywhere, including labels and buttons.

**The Measure Rule.** Headings stop at 15ch, display at 11ch, reading text between 34 and 56em. Use max-width in ch or em, not pixels.

## Layout

The page is a single column of full-width sections inside a 1440 px wrap with side padding of clamp(16px, 6vw, 120px), which yields the master system's 1200 px content width at desktop. Grids inside sections are 12-column in spirit and expressed as repeat(n, minmax(0, 1fr)) with a 24 px gutter: three columns for metrics, two for the situations list, four for people and the how steps, two for the build diagram and the offer panel, and two-column key-value rows at 150 to 280 px for the record, the facts and the wall detail.

Vertical rhythm is on a 4 px base. Sections pad clamp(80px, 10vh, 128px) top and bottom, 64 px on a phone; blocks within a section start 40 to 48 px below the headline; record rows sit 14 px apart on seam hairlines, other rows and list items 20 to 28 px apart. Scenes that pin (statement, build) take 110 to 230 vh of runway so the scroll drives them. The pinned frame itself is 100dvh, with 100vh as the fallback, so it fills the visible viewport while a phone toolbar collapses.

Breakpoints: at 1100 px three- and four-column grids drop to two; at 900 px pinned scenes unpin, the metrics and the record go to one column, the situations list, people and steps stay at two, the fire line under the how heading goes, the cases strip keeps scrolling sideways with narrower cards, the hero shortens, and the header gap tightens; at 700 px the header keeps Proof and People beside the Write to us button, and under 460 px People alone; at 600 px everything is one column, and each person becomes a row: a 120 px wide 4:5 portrait beside the name and role, the bio and links under both. A phone's hero runway is 520 px past the viewport, enough for the rune's flight and the statement and nothing more. The sticky header is 72 px tall and transparent over the hero, iron with a seam rule after it.

## Elevation & Depth

The system is flat by structure and lit by state. Depth comes from the three greys (iron, slate, seam) and from copper light, not from grey shadows on resting surfaces. The page carries no ambient wash outside the hero canvas: no fixed gradient, no warm blob behind the sections, iron all the way down. Text selection is copper with iron text, and the scrollbar is steel on iron.

### Shadow Vocabulary
- **Ignition** (`drop-shadow(0 0 16px rgba(239,163,124,.95))` to `0`): the flash when the mark lands in the header. Starts at ember, ends with no shadow.
- **Metric burn** (`text-shadow: 0 0 34px rgba(239,163,124,.95), 0 0 8px rgba(255,225,194,.9)` to `0`): the big numbers and the display line arrive ember and cool to ash over 2 s.
- **Card bloom** (`radial-gradient(60% 40% at 100% 0%, rgba(223,142,99,.16), transparent 70%)`): a copper wash from the top right corner of a proof card on hover.
- **Hero bloom**: the rune on the canvas is drawn wide on a second canvas and blurred twice (22 px and 7 px) at 90 and 70 percent alpha while it draws and ignites, then settles over 1.6 s to a resting copper with a faint halo and no breathing. Safari has no canvas filter, so there the same glow is a canvas shadow blur; keep that fallback.

### Named Rules
**The Lit-by-State Rule.** Glow belongs to a transition: arrival, ignition, a hover bloom. A held state (the open capability, the selected name, the lit word) is marked by colour alone. Nothing at rest shows a glow or a grey shadow, except the hero rune's faint resting halo. The system has no grey shadow at all.

**The Copper Light Rule.** Every glow is copper, hot copper or ember at some alpha. There is no white glow and no coloured shadow of any other hue.

## Shapes

Square by default. Corners are 0, 2 px on buttons and the skip link, 4 px on cards, panels, portraits and the turn-down block, and never more. Borders are 1 px hairlines in seam, stepping up to steel for controls and markers, to copper when lit and to deep copper for the turn-down block. The only circle on the page is the 28 px FAQ disclosure icon, a steel ring whose plus turns 45 degrees and goes copper when open. Markers are small squares: 5 to 7 px copper squares before list items, an 11 px square rotated 45 degrees on the era line. Progress rules are 1 px lines that fill from seam to copper. Portraits are 4:5 wells with a 4 px radius; they hold still.

## Components

Machined and quiet. Flat copper button with 2 px corners, cards as slate slabs with a hairline, hover is a warm bloom or a border, never a bounce. Arrivals use the confident ease, cubic-bezier(.16, 1, .3, 1), between 0.45 and 0.8 s; exits run faster than entrances; feedback is 0.1 to 0.15 s. The house ease, cubic-bezier(.2, .7, .2, 1), stays on the scroll-driven states.

### Buttons
- **Shape:** near-square (2 px radius), 52 px tall, 28 px side padding; small variant 44 px tall, 20 px padding, 15 px text.
- **Primary:** copper fill, iron text at 16 px medium with -0.005em tracking, no border, never wraps.
- **Hover / Focus / Press:** fill to hot copper over 0.15 s; a press darkens the copper a step for as long as it is held, in 0.1 s; focus-visible draws a 2 px copper outline 3 px outside the edge.
- **Text link:** the only secondary action, a 16 px medium copper link beside the button in a 36 px gap.

### Links
- **Style:** copper, 1 px underline offset 4 px, hover to hot copper. Nav links are 15 px medium smoke with no underline, ash on hover, 36 px apart.

### Eyebrow
- **Style:** mono 12 px smoke with 0.06em tracking, 20 px above the headline. No dash, no rule: the headline opens the section on its own.

### Cards / Containers
- **Corner Style:** 4 px.
- **Background:** slate with a 1 px seam border.
- **Shadow Strategy:** none at rest; the proof card blooms copper from its top right corner on hover.
- **Internal Padding:** 36 px on proof cards (440 to 600 px wide, 86vw up to 420 px on a phone), clamp(28px, 3.4vw, 48px) on offer panels.
- **Anatomy:** a header row with the mono kicker in smoke on the left and the mono index on the right, title, smoke body at 17/27, a footer row with links on the left and a mono era note on the right.
- **The cases strip:** the proof cards sit in a strip that scrolls on its own axis with mandatory snap to each card's left edge, padded by the page gutter, with a thin steel scrollbar as the cue. It never pins the page or takes over the wheel; the next card peeking at the right edge is the invitation.

### Situations list
- **Style:** not cards. Two columns of hairline rows on a seam top rule, 48 px apart, each row 28 px of vertical padding over a seam rule: a mono index in a 48 px column, the title at the small title role, the body in smoke at 34em. Hover turns the title hot copper over 0.25 s; no border changes. Two columns down to 600 px, then one. The turn-down block under the list keeps its deep copper border and wash as the one emphasis in the section.

### Offer panels
- **Style:** slate sheets in a plain list, 24 px apart, static in the flow: no sticking, no stacking, no shadow, no shrink, no veil. Two columns: title and body on the left, the price right-aligned in ash at subhead scale with a mono note under it, copper on the launch price alone, then a three-column row of what, terms and who on a seam rule, each list item marked with a 5 px copper square.

### Key-value rows
- **Style:** seam hairline between rows, mono 13 px smoke key in a 150 to 280 px column, 18/28 ash value. Pending values render in mono 14 px smoke.

### FAQ
- **Style:** native details and summary on seam rules, 26 px vertical padding, title at the small title role, the steel circle plus on the right. The answer opens over 0.45 s and closes over 0.3 s.

### Navigation
- **Style:** sticky 72 px header, lockup at 38 px on the left with the mark in copper and the wordmark in ash, four smoke text links and the small primary button on the right. Transparent over the hero, iron with a seam rule once the mark has landed. Under 900 px only the lockup and the button remain. A skip link appears at the top left on focus.

### The mark
- **Signature component.** Four copper pieces, three channels, the geometry fixed. Draws itself stroke by stroke in the hero canvas, ignites once, settles to copper, and lands in the header with a 1.1 s ember flash. In the build scene it is the diagram: pieces at 16 percent copper fill light to full copper one at a time as the matching capability opens. In the closing scene it reassembles on a canvas. Reduced motion shows every mark finished and still. Never rotate it, recolour a piece, round a corner or fill a channel; its glow follows the Elevation rules above.

### Names wall
- **Style:** a quiet index: names as borderless buttons in semibold ash at the title role for clients and the lead role in smoke for protocols, each at least 44 px tall to the finger, wrapped with a 14 px gap. Hover or selection turns the name hot copper and draws a 2 px copper underline from the left over 0.45 s. The selected name opens a detail row with a mono copper era, a lead-size line and links.

### Record line
- **Style:** a 1 px seam line on the left that fills with copper as the reader scrolls, era blocks marked by an 11 px rotated square that turns copper when lit, era names at headline scale, cases as key-value rows with the year in mono.

## Do's and Don'ts

### Do:
- **Do** keep copper as the only hue: mark, links, primary button, lit markers, one emphasis per section.
- **Do** build structure from type and hairlines: headlines at 78 px and up, seam rules between rows, no boxes around text.
- **Do** use tabular lining figures on every metric and every column of numbers; a lone price sets lining figures only.
- **Do** let copper light mark a transition only: ignite at ember, cool to copper or ash within two seconds, bloom on hover. Held states are marked by colour.
- **Do** use the house ease, cubic-bezier(.2, .7, .2, 1), for the transitions that remain: the closing rule, the open capability, the wall detail, the questions.
- **Do** show every mark finished and every section static under prefers-reduced-motion, and check Safari after any canvas change.
- **Do** collapse to one column at 900 px, drop three- and four-column grids to two at 1100 px, and unpin every scene on small screens.

### Don't:
- **Don't** put a glow, a grey shadow or a gradient on a surface at rest.
- **Don't** add a second accent, a status colour, purple, neon green, or any white glow.
- **Don't** rotate the mark, recolour a piece, round its corners, fill a channel, or place it on a photograph.
- **Don't** use runic alphabets as decoration, Norse imagery, hexagons, chains and nodes, circuit patterns, isometric cubes, stock photography or emoji.
- **Don't** set anything in uppercase, use a pill, a corner above 4 px, a border heavier than 1 px, or a font other than Schibsted Grotesk and IBM Plex Mono.
- **Don't** write an em dash or an exclamation mark anywhere, including code comments.

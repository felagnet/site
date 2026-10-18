"""Full cinematic landing pages for Felag, one per hero. The hero comes from shared.py; this file adds the scenes
below it (statement, proof, offer, how, who, people, contracting, FAQ, closing, footer) and the motion engine.
Two themes: "rune" (fire and light) and "harvest" (land and seasons). Copy is the reviewed first-pass copy."""

import json
import os
from shared import LOCKUP, CSS, COMMON_JS, FONT_LINKS
_HERE = os.path.dirname(os.path.abspath(__file__))
def _photo(name):
    # the portraits ship as files under people/, copied there by build_site.py and make_dist.py
    return name if os.path.exists(os.path.join(_HERE, "photo", "people", name + ".jpg")) else ""

MARK_PATH = "M0 0H32V104H0Z M44 0H66L44 22Z M44 38L82 0H104L44 60Z M44 76L104 16V104H44Z"
PIECES = ["M0 0H32V104H0Z", "M44 0H66L44 22Z", "M44 38L82 0H104L44 60Z", "M44 76L104 16V104H44Z"]

# ---------------------------------------------------------------------------------------------- content

STATEMENT = ("Felag is a boutique engineering studio for funded fintech and technology companies. Our principal-led pods own "
             "the architecture and delivery of backends, payment systems and identity infrastructure.")
# the search snippet: the hero line and the sub-line, both locked in core.md, 152 characters
DESCRIPTION = ("Senior engineers who own the architecture and ship to production. A principal-led studio for technology companies, "
               "priced on outcomes rather than hours.")

# the four things we build, one per piece of the mark: the bar, then the three pieces on the right, the small one last
CAPS = [
    dict(piece=0, name="Backend and infrastructure at scale", line="The services, queues and data stores that hold at production load, the cloud under them written as code, and the front ends on top, measured on load and interaction time."),
    dict(piece=3, name="Payments rails", line="Card programmes, account ledgers, settlement and the integrations with issuers, processors and banks, with the audit trail a regulated business is asked to produce."),
    dict(piece=2, name="Identity and SSO", line="Enterprise single sign-on, account models and the permission layer between them, and identity for the software agents that act on a person's behalf."),
    dict(piece=1, name="Distributed ledgers, where they fit", line="Where a product needs a ledger that several parties have to trust, we design and ship it; where it does not, the sprint says so."),
]

SKILLS = ("Go, Rust, Node.js/TypeScript, Python, Solidity; React/Next.js, Vue/Nuxt, React Native/Expo, Flutter; AWS, GCP, Kubernetes, "
          "Terraform; EVM (Ethereum, L2s, Polygon CDK), Substrate/Polkadot, Solana, Cosmos, Canton/Daml, Stellar, Bitcoin/Lightning, TON; "
          "Postgres, Redis, ScyllaDB/Cassandra, ClickHouse, Kafka, NATS, RabbitMQ, gRPC, GraphQL, REST, websockets, The Graph and custom indexers.")

L2B = "https://l2beat.com/layer2s/projects/wirex"
WIREX_PR = "https://gateway.fm/blog/gateway-wirex-partnership/"
GW_CASE = "https://gateway.fm/case-studies/agentic-identity-chain-infrastructure/"

C_LINE = "We built the event infrastructure and backend for Infinex, the Synthetix front-end, under governance proposal XIP-9."
F_NAMED = "We built the application layer for Humanity Protocol, an identity network with 9M+ users."
G_NAMED = "We ran Gateway Yield, the infrastructure behind $1B+ locked in staking, serving Lido, Gnosis, Stellar and Canton."
H_NAMED = "We built a shared prover used across several ZK protocols and L2 ecosystems, including EY Nightfall, Polygon zkEVM, Miden and Iden3, with GPU and CPU autoscaling on AWS spot capacity."
KUCOIN = "https://www.kucoin.com/announcement/en-deepnode-dn-gets-listed-on-kucoin-world-premiere"
J_LINE = "We built an EVM event-indexing code-generation platform that became the standard across most of the company's projects."
K_LINE = "We led the Presto tokenised-finance product to revenue and built its stablecoin, RWA, DEX and payments blueprints."
O_LINE = "Uddug built the technology behind the OG:Crystals launch end to end, in collaboration with Snark.art."
P_LINE = "Uddug launched Marscatsvoyage, $2M+ at launch."
R_LINE = "Uddug took on grant work for Web3 Foundation and Protocol Labs, including JuniDB, an IPFS-backed data layer for Substrate."
Y_LINE = "Uddug built the smart contracts for Metazoku in 2023."

# the three lead cases: payments, the NFT platform, identity; each says what was delivered, the constraint or status, and the result
PROOF_CARDS = [
    dict(kicker="Live since August 2024", title="Wirex Pay", links=[("L2BEAT listing", L2B), ("Partnership announcement", WIREX_PR)], era="Gateway.fm, 2024",
         facts=[("Delivered", "The L2 chain on Polygon CDK, the application layer, the indexer, the push oracle and the account abstraction behind its non-custodial debit cards."),
                ("Constraint", "Built for MiCA alignment."),
                ("Result", "The chain launched in August 2024 and is listed on L2BEAT.")]),
    dict(kicker="NFT platform and launches", title="Arsnl.art", links=[], era="Uddug, from 2022",
         facts=[("Delivered", "The whole NFT platform behind Arsnl.art and the NFT launches on it."),
                ("Result", "Frank Stella's 'Geometries' released on the platform.")]),
    dict(kicker="Pilot and proof of concept, 2025", title="Identity for a global technology company", links=[("Case study, by the team at Gateway.fm", GW_CASE)], era="Gateway.fm, 2025",
         facts=[("Delivered", "Account-abstraction wallets with enterprise single sign-on, and an identity system for AI agents on a major cloud platform."),
                ("Status", "Both built as a pilot and proof of concept, not taken to production.")]),
]

# the names wall: every name the register and the history allow, each with its era and any public record; the story lives in the cases and the record
WALL = [
    ('Wirex Pay', 'client', [('L2BEAT listing', L2B), ('Partnership announcement', WIREX_PR)], 'Gateway.fm, 2024'),
    ('Opera', 'client', [], 'Gateway.fm, 2021 to 2022'),
    ('1inch', 'client', [], 'Gateway.fm, 2021 to 2022'),
    ('Infinex', 'client', [], 'Uddug with Gateway.fm, 2023 to 2024'),
    ('Humanity Protocol', 'client', [], 'Gateway.fm, 2024 to 2025'),
    ('DeepNode', 'client', [('KuCoin listing announcement', KUCOIN)], 'Andrew, 2025 to 2026'),
    ('EY Nightfall', 'client', [], 'Gateway.fm, 2024 to 2025'),
    ('LUKSO', 'client', [], 'Gateway.fm, 2023 to 2025'),
    ('Lumia', 'client', [], 'Gateway.fm, 2023 to 2025'),
    ('ApeChain', 'client', [], 'Gateway.fm, 2023 to 2025'),
    ('Presto', 'client', [], 'Gateway.fm, 2023 to 2025'),
    ('Gnosis', 'client', [], 'Gateway.fm'),
    ('Ethereum Foundation', 'client', [], 'Gateway.fm, 2021 to 2022'),
    ('Web3 Foundation', 'client', [], 'Uddug, 2020 to 2023'),
    ('Protocol Labs', 'client', [], 'Uddug, 2020 to 2023'),
    ('OG:Crystals', 'client', [], 'Uddug, 2021'),
    ('Marscatsvoyage', 'client', [], 'Uddug, 2021'),
    ('Arsnl.art', 'client', [], 'Uddug, from 2022'),
    ('Metazoku', 'client', [], 'Uddug, 2023'),
    ('Snark.art', 'client', [('snark.art', 'https://snark.art')], 'Andrew, then Uddug'),
    ('Synthetix', 'protocol', [], 'Uddug with Gateway.fm, 2023 to 2024'),
    ('Lido', 'protocol', [], 'Gateway.fm, 2025 to 2026'),
    ('Stellar', 'protocol', [], 'Gateway.fm, 2025 to 2026'),
    ('Canton', 'protocol', [], 'Gateway.fm, 2025 to 2026'),
    ('Polygon zkEVM', 'protocol', [], 'Gateway.fm, 2024 to 2025'),
    ('Miden', 'protocol', [], 'Gateway.fm, 2024 to 2025'),
    ('Iden3', 'protocol', [], 'Gateway.fm, 2024 to 2025'),
]

# the record, three eras; the Gateway.fm era opens on the department line
ERAS = [
    dict(name="Uddug", years="2018 to 2024",
         intro="Andrew Skurlatov and Mikhail Manko founded Uddug in 2018; the two have worked together since 2015.",
         cases=[
             ("2017 to 2018", "ICEX, before Uddug", "The founders' own exchange, about 70 percent built when the investor withdrew in the 2018 crypto winter; it never launched. The push oracle started there.", []),
             ("2020 to 2023", "Web3 Foundation and Protocol Labs", R_LINE, []),
             ("2021", "OG:Crystals", O_LINE, []),
             ("2021", "Marscatsvoyage", P_LINE, []),
             ("From 2022", "Arsnl.art", "The NFT platform and its launches, including Frank Stella's 'Geometries'.", []),
             ("2023", "Metazoku", Y_LINE, []),
             ("2023 to 2024", "Infinex, with Gateway.fm", C_LINE, []),
         ]),
    dict(name="Gateway.fm", years="2021 to 2026",
         intro="Andrew joined Gateway.fm in 2021 as one of its first engineers. In June 2024 Gateway.fm acquired Uddug and the team became its Platform department; the founders ran ~25 people across two departments. In 2026 the departments closed and we left.",
         cases=[
             ("2021 to 2022", "The RPC proxy for Opera and 1inch", "A cache layer and rate limiting at 140k+ requests per second at peak, with 50 ms average latency on the heavy requests.", []),
             ("2023 to 2025", "Presto", K_LINE, []),
             ("2023 to 2025", "The indexing platform", J_LINE, []),
             ("2023 to 2025", "Oracles", "A push oracle with multi-asset prices every 500 ms for Wirex Pay, Infinex, LUKSO and Lumia; a pull feed at about 1,000 requests per second and verifiable randomness for ApeChain.", []),
             ("2024", "Wirex Pay", "The L2 chain and the application layer behind its debit cards.", []),
             ("2024 to 2025", "Humanity Protocol", F_NAMED, []),
             ("2024 to 2025", "The shared prover", H_NAMED, []),
             ("2025", "Identity for a global technology company, a pilot", "Wallets with enterprise single sign-on and identity for AI agents, both a proof of concept.", []),
             ("2025 to 2026", "DeepNode", "Fractional CTO for ten months: decentralised AI infrastructure measured at about 5,000 requests per second, through the January 2026 token launch and exchange listing at $140M+ FDV.", [("KuCoin listing announcement", KUCOIN)]),
             ("2025 to 2026", "Gateway Yield", G_NAMED, []),
         ]),
    dict(name="Felag", years="From July 2026",
         intro="Felag was founded in July 2026 as the restart of Uddug. Pavel Dodonov and Andrey Solovov joined as principal engineers and partners.",
         cases=[]),
]

OFFERS = [
    dict(name="Free technical workshop", price="Free", note="",
         body="A 60-minute session with a founder to understand your system, priorities and constraints. If an Architecture Sprint is useful, we agree its scope. Detailed specification and costed build options are part of the paid sprint.",
         what=["Your system, priorities and constraints, understood", "A sprint scope, if a sprint is useful"], terms=["Free", "60 minutes", "A reply within two working days of your email"], who="A founder"),
    dict(name="Architecture Sprint", price="From $10k", note="",
         body="One to two weeks with a principal that end in a build decision: spec, architecture decisions, risk register and costed build options, with the fixed-price build or the pod that follows quoted from them.",
         what=["Spec and architecture decisions", "Risk register", "Costed build options", "A build decision"], terms=["One to two weeks", "Paid in advance", "Credited in full against a pod or fixed-price build signed within 30 days of the sprint's delivery"], who="A principal"),
    dict(name="Fractional CTO", price="From $4k a month", note="one day a week; two days and ad hoc days priced per engagement",
         body="A principal in the CTO seat for explicit days each week, with the decisions and the ownership that go with it, until a full-time hire makes sense.",
         what=["Explicit days", "The architecture, the hiring bar and the technical decisions owned", "Representation with the board and investors where needed"], terms=["Monthly in advance", "One-month initial term"], who="Andrew, Pavel or Andrey, never a contractor"),
    dict(name="Pods", price="$10k to $60k a month", note="by team",
         body="The build after the sprint, on a monthly retainer with deliverables agreed each month in the SOW, and a team sized to the scope.",
         what=["From $10k: one senior engineer, with a principal reviewing the architecture weekly", "From $25k: a principal part time with one or two senior engineers", "Up to $60k: a principal full time leading two to three engineers"],
         terms=["Monthly in advance", "Deliverables agreed each month in the SOW", "A missed deliverable triggers a scope and plan review, recorded in writing", "Cancel with two weeks' notice"], who="A principal, with senior and specialist engineers as the scope needs"),
    dict(name="Technical due diligence", price="Quote per scope", note="fixed price, half paid on start",
         body="A review of the system and the team behind it against a scope fixed in advance, for investors and acquirers who need findings they can act on.",
         what=["A written report on architecture, code quality, security, infrastructure and the team", "Findings ranked by risk", "Delivered one to two weeks from access"], terms=["Fixed price", "Half paid on start"], who="A principal"),
]
OFFER_NOTE = ("Every build starts with a paid Architecture Sprint, and fixed-price builds are quoted from a completed sprint. "
              "Your engagement is led by one of our principals, identified in the statement of work. Any replacement requires your consent.")

# each step: its name, the output it ends with, one short line
HOW = [
    ("Workshop", "The problem, framed.", "Free, with a founder. If a sprint is useful, we agree its scope."),
    ("Architecture Sprint", "A spec and costed build options.", "One to two weeks with a principal, paid in advance and credited against the build."),
    ("Decision", "A build decision on a fixed scope.", "Taken together on the sprint output: a fixed-price build or a pod."),
    ("Pod", "The build, led by a principal.", "On defined outcomes, monthly in advance."),
]
HOW_NOTE = "Fractional CTO work and due diligence start from the same workshop and go straight to a scoped proposal."

WHO = [
    ("A post-raise CTO with a hard integration and no senior hire in time", "The Series A or B roadmap has an integration nobody on the team has shipped before, and the senior hire will not land in time. We take the integration as a defined outcome and hand it back documented."),
    ("A funded technology company with a performance, scale or reliability problem", "The product works until it is busy. We measure the problem first, then fix the cause, and we say so when the answer is a smaller change than the team expected."),
    ("A regulated payments or asset issuer rebuilding for a new regime", "MiCA, DORA, the UK regime, GENIUS, VARA, HKMA or MAS has changed what the system must record and prove, and the team needs engineers who have built for one of these regimes before."),
    ("A licensed fintech taking over a codebase from a previous vendor", "The codebase arrived without the people who wrote it. We audit what is there, keep what works, and take ownership of the rest."),
    ("A founder with a co-founder gap", "The company needs a CTO for one or two days a week to own the architecture, the hiring bar and the technical decisions until a full-time hire makes sense."),
    ("A product agency without a senior backend bench", "The agency has the design and the client, and needs a principal behind the backend for the length of the engagement without building that bench itself."),
]
TURN_DOWN = "Hourly billing, a dedicated eight-person team as a product, and public-sector tenders scored on headcount."

PEOPLE = [
    dict(ini="AS", name="Andrew Skurlatov", role="Co-founder and CTO", where="Based in the Netherlands", alt="Andrew Skurlatov, co-founder and CTO of Felag",
         bio="Andrew Skurlatov is co-founder and CTO of Felag. He has spent 15 years in software, 10 of them in blockchain, as an engineering leader and serial founder. He co-founded Uddug in 2018 as its CTO and led it to its acquisition by Gateway.fm in 2024. There he became VP of DLT and later VP of Platform and Yield, running ~25 people across two departments.",
         links=[("LinkedIn", "https://linkedin.com/in/andrew-skurlatov"), ("GitHub", "https://github.com/andskur"), ("X", "https://x.com/Andskur1")], seed=3, photo=_photo("andrew")),
    dict(ini="MM", name="Mikhail Manko", role="Co-founder and CEO", where="Based in Cyprus", alt="Mikhail Manko, co-founder and CEO of Felag",
         bio="Mikhail Manko is co-founder and CEO of Felag. He has spent 13 years in IT running teams, products and operations. He co-founded Uddug with Andrew Skurlatov in 2018 and led it through its acquisition by Gateway.fm in 2024, where he was Head of Platform for the tokenised-finance product. At Felag he runs partnerships and deals, from the first call to the signed contract.",
         links=[("LinkedIn", "https://www.linkedin.com/in/mikhail-manko/")], seed=7, photo=_photo("mike")),
    dict(ini="PD", name="Pavel Dodonov", role="Principal Engineer, Infrastructure and ZK, partner", where="Based in Serbia", alt="Pavel Dodonov, Principal Engineer for infrastructure and ZK at Felag",
         bio="Pavel Dodonov is Principal Engineer for infrastructure and ZK at Felag and a partner. In nearly four years at Gateway.fm he rose from Go backend engineer to Backend Lead and led the shared prover architecture for L2 ecosystems, GPU and CPU autoscaling for the prover fleets, and an EVM event-indexing platform that most of the company's projects reused. Before that he spent a decade in scientific R&D, with 20+ published papers.",
         links=[("LinkedIn", "https://www.linkedin.com/in/paveldodonov/"), ("GitHub", "https://github.com/Pashteto")], seed=11, photo=_photo("pavel")),
    dict(ini="AS", name="Andrey Solovov", role="Principal Engineer, Web3 Systems, partner", where="Based in Finland", alt="Andrey Solovov, Principal Engineer for Web3 systems at Felag",
         bio="Andrey Solovov is Principal Engineer for Web3 systems at Felag and a partner. For more than two years he was Blockchain Dev Lead at Gateway.fm, shipping production systems for DeFi, oracle, L2 and identity clients, among them a push oracle that delivered multi-asset prices every 500 ms and a pull-based feed at about 1,000 requests per second. Before Gateway he built smart contracts and payments architecture at Uddug.",
         links=[("LinkedIn", "https://www.linkedin.com/in/andrey-solovov-bb665884/"), ("GitHub", "https://github.com/asolovov")], seed=5, photo=_photo("andrey")),
]
PEOPLE_NOTE = ("The founders have worked together since 2015. Felag is the 2026 restart of Uddug, which Gateway.fm acquired in June 2024. "
               "Contractors join on demand and are never sold as principals.")

CONTRACT = [
    ("Legal entity", "Felag, incorporated in 2026."),
    ("Principals", "Netherlands and Cyprus."),
    ("Named principal", "Every contract names the principal who leads the work. Substitution needs the client's consent."),
    ("Contractors", "QA, DevOps and additional development on demand, never sold as principals."),
    ("Billing", "No hourly billing. Retainers are paid monthly in advance; sprints are paid in advance."),
    ("Subcontracting and IP", "[subcontracting and IP clause line]"),
    ("Incident contact", "[incident contact line]"),
    ("DORA and ICT vendor pack", "[DORA and ICT vendor pack line]"),
]

FAQ = [
    ("Do you bill by the hour?", "No. Sprints and technical due diligence are fixed price, pods and fractional CTO work are monthly retainers, and the workshop is free."),
    ("Who actually works on our system?", "One of the people above leads every engagement and is identified in the SOW. Contractors join for QA, DevOps and additional development when the scope needs them, and they are never presented as principals."),
    ("How do we start?", "With a free technical workshop with a founder. If there is a fit, it ends with the scope of a paid Architecture Sprint."),
    ("What do we keep if we stop after the sprint?", "The spec, the architecture decisions, the risk register and the costed build options are yours. The sprint is paid in advance and credited in full against a pod or fixed-price build signed within 30 days of its delivery."),
    ("Where are you based and who do we contract with?", "The contract is with Felag. The founders work from the Netherlands and Cyprus."),
    ("Do you work with regulated companies?", "Yes. We built the Wirex Pay platform and the application layer behind its debit card programme for MiCA alignment. We have not taken a system through an audit under MiCA, and we say so before a sprint starts."),
    ("Do you use AI in delivery?", "Yes, on our own AI development framework, which we will describe publicly later. It runs under a principal's review, and the outcome in the SOW is what we are accountable for, whatever tooling produced it."),
]

# eyebrows and small story lines per theme
THEMES = {
    "rune": dict(
        statement_eyebrow="The studio", build_eyebrow="What we build", proof_eyebrow="Proof", wall_eyebrow="Names", more_eyebrow="The record", offer_eyebrow="What it costs",
        how_eyebrow="How we work", how_line="Four steps, each with a clear output.",
        who_eyebrow="Who we work with", people_eyebrow="Who we are", contracting_eyebrow="Contracting and security",
        faq_eyebrow="Questions we are asked", book_eyebrow="Next step",
        book_line="",
    ),
    "harvest": dict(
        statement_eyebrow="The field", build_eyebrow="What grows here", proof_eyebrow="Past harvests", wall_eyebrow="Names", more_eyebrow="Earlier harvests", offer_eyebrow="What it costs",
        how_eyebrow="Sow, grow, harvest", how_line="Four steps from the first furrow to the harvest, with a decision at each one.",
        who_eyebrow="Who we work with", people_eyebrow="Who we are", contracting_eyebrow="Contracting and security",
        faq_eyebrow="Questions we are asked", book_eyebrow="Next step",
        book_line="Seen from above, the field says what the work was for.",
    ),
}

def header():
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="lockup" href="#top" aria-label="Felag, home">{LOCKUP}</a>
    <nav class="nav" aria-label="Page sections">
      <div class="links nav"><a href="#proof">Proof</a><a href="#offer">Prices</a><a href="#how">How</a><a href="#people">People</a></div>
      <a class="btn btn-sm" href="mailto:info@felag.net?subject=Free%20technical%20workshop">Write to us</a>
    </nav>
  </div>
</header>'''

# ---------------------------------------------------------------------------------------------- css

SITE_CSS = '''
/* ---- site-wide scale, larger than the system scale on purpose */
.hero-inner{padding-bottom:0}
@media (max-width:900px){.hero-inner{padding-bottom:40px}}
main{position:relative;z-index:1}
.sec{position:relative;padding:clamp(80px,10vh,128px) 0}
.sec h2,.scene-book h2,.scene-build h2,.h2{font-size:var(--fs-headline);line-height:1;font-weight:600;letter-spacing:-0.03em;max-width:15ch;text-wrap:balance}
.sec h2.huge,.huge{font-size:var(--fs-display);line-height:.95;font-weight:600;letter-spacing:-0.035em;max-width:11ch;text-wrap:balance}
/* the two index sections, names and record, are lists, not statements: their headlines take the subhead role */
#names h2,#record h2{font-size:var(--fs-subhead);line-height:1;letter-spacing:-0.03em;max-width:20ch}
.lead{font-size:var(--fs-lead);line-height:1.45;color:var(--text-secondary);max-width:34em;margin-top:24px}
.eyebrow{font-size:12px;line-height:20px;letter-spacing:.06em;color:var(--text-secondary);margin-bottom:20px}
.rule{height:1px;background:linear-gradient(90deg,var(--accent) 0,var(--accent) var(--w,0%),var(--line) var(--w,0%),var(--line) 100%);transition:none}

/* ---- rune theme: the rune lands in the header, fire on titles and numbers */
.theme-rune .hero{height:calc(100vh + 1250px);min-height:1950px}
.hero-statement{position:absolute;left:0;right:0;top:0;bottom:0;z-index:2;display:flex;flex-direction:column;justify-content:center;padding-top:var(--head);opacity:var(--st,0);pointer-events:none;transform:translateY(calc((1 - var(--st,0)) * 28px))}
.hero-statement .statement{margin-top:24px}
.theme-rune.over-hero .site-header{background:transparent;border-color:transparent}
/* the header button stays a hairline button while the mark is still in flight, and fills copper in the moment the mark lands */
.site-header .btn{transition:background-color .5s cubic-bezier(.2,.7,.2,1),color .5s cubic-bezier(.2,.7,.2,1),border-color .5s cubic-bezier(.2,.7,.2,1)}
.js .theme-rune.mark-pending .site-header .btn{background:transparent;color:var(--text);border:1px solid var(--line-strong)}
.js .theme-rune.mark-pending .site-header .btn:hover{background:transparent;color:var(--text);border-color:var(--text-secondary)}
.lockup svg{overflow:visible}
.mark-arrived .site-header .mark-fill{animation:markflash 1.1s ease-out}
@keyframes markflash{0%{fill:var(--ember);filter:drop-shadow(0 0 16px rgba(var(--hot-rgb),.95))}100%{fill:var(--accent);filter:drop-shadow(0 0 0 rgba(var(--hot-rgb),0))}}
/* one headline on the page is underlined in copper: the closing one */
/* ---- blocks rise in as they enter: 24 px and a fade over .7 s, 60 ms later for each item in a group (--i), nothing under reduced motion */
html.js .reveal{opacity:0;transform:translateY(24px);transition:opacity .7s cubic-bezier(.16,1,.3,1),transform .7s cubic-bezier(.16,1,.3,1);transition-delay:calc(var(--i,0) * 60ms)}
html.js .reveal.in{opacity:1;transform:none}
.sec h2.reveal{--i:1}.sec .lead.reveal{--i:2}
@media (prefers-reduced-motion: reduce){html.js .reveal{opacity:1;transform:none;transition:none}}
.theme-rune .sec h2.reveal::after,.theme-rune .scene-book h2::after{content:"";display:block;height:2px;width:0;margin-top:26px;background:var(--accent);transition:width .8s cubic-bezier(.16,1,.3,1) .1s}
.theme-rune .sec h2.reveal.in::after,.theme-rune .scene-book h2.lit::after{width:120px}
.theme-rune .metric .big.burn,.theme-rune .sec h2.huge.burn{animation:burn 2s ease-out both}
@keyframes burn{0%{color:var(--ember);text-shadow:0 0 34px rgba(var(--hot-rgb),.95),0 0 8px rgba(var(--ember-rgb),.9)}60%{color:color-mix(in srgb,var(--ember) 60%,var(--accent));text-shadow:0 0 24px rgba(var(--hot-rgb),.5)}100%{color:var(--text);text-shadow:0 0 0 rgba(var(--hot-rgb),0)}}
@media (max-width:900px){.theme-rune .hero{height:calc(100vh + 520px);min-height:0}.hero-statement{justify-content:center;padding-top:var(--head);padding-bottom:10vh}}

/* ---- statement scene */
.scene-statement{height:230vh}
.scene-statement .pin{position:sticky;top:0;height:100vh;min-height:640px;display:flex;align-items:flex-start;overflow:hidden;padding-top:calc(var(--head) + 3vh)}
.statement{font-size:var(--fs-subhead);line-height:1.12;font-weight:600;letter-spacing:-0.03em;max-width:24ch;margin-top:28px}
.statement .w{display:inline-block;color:var(--text);opacity:var(--dim)}
.statement .w.hot{color:var(--accent-hover)}
.scene-statement .cur{position:absolute;bottom:clamp(40px,8vh,80px);left:var(--side);font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);letter-spacing:.04em}

/* ---- build: the mark is the diagram, one piece per thing we build */
.scene-build{height:calc(100vh + 110vh);position:relative}
.scene-build .pin{position:sticky;top:0;height:100vh;height:100dvh;min-height:680px;overflow:hidden;display:flex;align-items:center;padding-top:var(--head)}
.scene-build .wrap{width:100%}
.markmap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:center;margin-top:40px}
.caps-left{display:flex;flex-direction:column;gap:0;border-top:1px solid var(--line)}
.cap{padding:22px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:48px minmax(0,1fr);gap:8px 12px;opacity:var(--dim);transition:opacity .5s}
.cap.on{opacity:1}
.cap .k{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:6px;transition:color .5s}
.cap:not(.on) .k{color:var(--text)}
.cap h3{font-size:var(--fs-title);line-height:1.05;font-weight:600;letter-spacing:-0.025em;transition:color .4s}
.cap.on h3{color:var(--accent-hover)}
.cap p{grid-column:2;color:var(--text-secondary);font-size:var(--fs-body);line-height:var(--lh-body);margin-top:8px;max-width:34em;max-height:0;overflow:hidden;opacity:0;transition:max-height .6s cubic-bezier(.2,.7,.2,1),opacity .5s,margin .4s}
.cap.on p{max-height:160px;opacity:1}
.cap:not(.on) p{margin-top:0;transition-duration:.35s,.25s,.3s}
.mark-col{position:relative;display:flex;flex-direction:column;align-items:center;gap:18px}
.bigmark{width:min(100%,340px);height:auto;display:block;overflow:visible}
.bigmark path{fill:var(--line);transition:fill .5s}
.bigmark path.on{fill:var(--accent)}
.mark-count{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.skills-foot{margin-top:40px;max-width:46em;font-size:var(--fs-label);line-height:var(--lh-label)}
.skills-foot .n{color:var(--text);margin-right:12px}
.skills{font-family:var(--mono);font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text-secondary)}

/* ---- proof: metrics, then the cases as a strip that scrolls on its own axis */
.metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:48px}
.metric{padding:28px 0 0;border-top:1px solid var(--line-strong);display:flex;flex-direction:column;gap:12px}
.metric .big{font-size:var(--fs-metric);line-height:.92;font-weight:600;letter-spacing:-0.045em;font-variant-numeric:tabular-nums lining-nums;min-height:1em;white-space:nowrap}
.metric .big em{font-style:normal;color:var(--accent)}
.metric .label{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--text-secondary)}
.scene-proof{position:relative;padding:56px 0 clamp(72px,9vh,112px)}
.track{display:flex;gap:24px;padding:0 var(--side) 20px;margin-top:40px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:var(--side);overscroll-behavior-x:contain;scrollbar-width:thin;scrollbar-color:var(--line-strong) transparent}
.card{flex:0 0 clamp(440px,38vw,600px);scroll-snap-align:start;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:36px;display:flex;flex-direction:column;gap:18px;position:relative;overflow:hidden}
.card .chead{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.card::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 40% at 100% 0%,rgba(var(--copper-rgb),.16),transparent 70%);opacity:0;transition:opacity .5s}
.card:hover::before{opacity:1}
.card .kicker{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);letter-spacing:.02em}
.card h3{font-size:var(--fs-title);line-height:1.1;font-weight:600;letter-spacing:-0.025em;text-wrap:balance}
.card .cfacts{display:grid;gap:14px;flex:1}
.card .cfacts div{display:grid;grid-template-columns:96px minmax(0,1fr);gap:16px;align-items:baseline}
.card .cfacts dt{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.card .cfacts dd{color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose)}
.card .cfoot{margin-top:0;display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap}
.card .links{display:flex;gap:20px;flex-wrap:wrap;font-size:var(--fs-small)}
.card .idx{flex:0 0 auto;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}

.card .era{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);text-align:right}
.strip-head{display:flex;justify-content:space-between;align-items:end;gap:24px}
.strip-nav{display:flex;gap:12px;flex:0 0 auto}
.strip-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;padding:0;border:1px solid var(--line-strong);border-radius:2px;background:none;color:var(--text);cursor:pointer;transition:border-color .15s,color .15s}
.strip-btn svg{display:block}
.strip-btn:hover{border-color:var(--accent);color:var(--accent-hover)}
.strip-btn:active{color:var(--accent)}
.strip-btn:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.strip-btn[disabled]{opacity:var(--dim);cursor:default}
.strip-btn[disabled]:hover{border-color:var(--line-strong);color:var(--text)}

.links a{padding:6px 8px;margin:-6px -8px}

/* ---- the names wall */
.wall{display:flex;flex-wrap:wrap;gap:0 14px;margin-top:40px;align-items:baseline}
.name{appearance:none;background:none;border:0;padding:6px 0;margin:0;color:var(--text);font-family:var(--sans);font-weight:600;letter-spacing:-0.03em;line-height:1;cursor:pointer;position:relative;transition:color .25s}
.name.client{font-size:var(--fs-title)}
.name.protocol{font-size:var(--fs-lead);color:var(--text-secondary);font-weight:500;align-self:center;padding:13px 0}
.name::after{content:"";position:absolute;left:0;right:0;bottom:-2px;height:2px;background:var(--accent);transform:scaleX(0);transform-origin:0 50%;transition:transform .45s cubic-bezier(.2,.7,.2,1)}
.name:hover,.name:focus-visible{color:var(--accent-hover)}
.name.on{color:var(--accent)}
.name.on::after,.name:hover::after{transform:scaleX(1)}
.name:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wall-detail{flex:0 0 100%;overflow:hidden;height:0;transition:height .5s cubic-bezier(.16,1,.3,1)}
.wall-detail[hidden]{display:none}
.wall-detail.closing{transition-duration:.3s}
.wall-detail-inner{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:26px 0 30px;display:grid;grid-template-columns:200px minmax(0,1fr);gap:24px;align-items:start}
.wall-detail-inner .wall-era{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:4px}
.wall-detail-inner p{font-size:var(--fs-lead);line-height:1.45;max-width:40em}
.wall-detail-inner .links{display:flex;gap:20px;flex-wrap:wrap;margin-top:14px;font-size:var(--fs-small)}
/* each name's line sits in the page after it; the script opens a copy in the detail row, and without the script the line shows under its name */
html.js .wall-line{display:none}
.wall-line{flex:0 0 100%;display:grid;grid-template-columns:200px minmax(0,1fr);gap:8px 24px;align-items:start;padding:4px 0 24px;margin-bottom:8px;border-bottom:1px solid var(--line)}
.wall-line .wall-era{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:4px}
.wall-line p{color:var(--text-secondary);font-size:var(--fs-body);line-height:var(--lh-body);max-width:40em}
.wall-line .links{display:flex;gap:20px;flex-wrap:wrap;margin-top:8px;font-size:var(--fs-small)}
html:not(.js) .name{cursor:default}

/* ---- the record, three eras along a line */
.eras{position:relative;margin-top:48px;padding-left:40px}
.era-line{position:absolute;left:8px;top:8px;bottom:8px;width:1px;background:var(--line)}
.era-line i{display:block;width:100%;height:0;background:var(--accent)}
.era-block{position:relative;padding-bottom:48px}
.era-block:last-child{padding-bottom:0}
.era-block::before{content:"";position:absolute;left:-37px;top:14px;width:11px;height:11px;background:var(--bg);border:1px solid var(--line-strong);transform:rotate(45deg);transition:background-color .4s,border-color .4s}
.era-block.lit::before{background:var(--accent);border-color:var(--accent)}
.era-head{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;max-width:60em}
.era-name{font-size:var(--fs-subhead);line-height:1;font-weight:600;letter-spacing:-0.03em}
.era-years{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.era-intro{color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose);margin-top:10px;max-width:52em}
.era-cases{margin-top:20px;border-top:1px solid var(--line)}
.rec{display:grid;grid-template-columns:150px minmax(0,1fr);gap:24px;padding:14px 0;border-bottom:1px solid var(--line)}
.rec .yr{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:4px}
.rec h4{font-size:var(--fs-title-sm);line-height:1.25;font-weight:600;letter-spacing:-0.015em;margin:0}
.rec p{color:var(--text-secondary);font-size:var(--fs-small);line-height:var(--lh-small);margin-top:6px;max-width:56em}
.rec .links{display:flex;gap:18px;flex-wrap:wrap;margin-top:8px;font-size:var(--fs-small)}

/* ---- offer: stacking panels. Each sticks under the header 12 px lower than the one before, so the list stacks as the reader scrolls */
.stack{margin-top:64px}
.panel{position:sticky;top:calc(var(--head) + 24px + var(--i) * 12px);background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:clamp(28px,3.4vw,48px);margin-bottom:24px;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:32px 40px;align-items:start;box-shadow:0 -20px 60px rgba(var(--iron-rgb),.6)}
.pcols{grid-column:1 / -1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;border-top:1px solid var(--line);padding-top:24px}
.pk{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);margin-bottom:10px}
.pcol ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.pcol li,.pcol p{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--text);margin:0;max-width:none}
.pcol li::before{content:"";display:inline-block;width:5px;height:5px;background:var(--line-strong);margin-right:10px;vertical-align:3px}
.panel h3{font-size:var(--fs-subhead);line-height:1;font-weight:600;letter-spacing:-0.03em}
.panel > div > p{color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose);margin-top:18px;max-width:30em}
.panel .price{text-align:right}
.panel .price b{display:block;font-size:var(--fs-subhead);line-height:1;font-weight:600;letter-spacing:-0.03em;color:var(--text);font-variant-numeric:lining-nums;text-wrap:balance}
.panel .price b.word{font-size:var(--fs-title);color:var(--text-secondary)}
.panel.launch .price b{color:var(--accent)}
.panel .price span{display:block;margin-top:12px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.panel .n{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);margin-bottom:22px}
.offer-note{margin-top:32px;max-width:52em;color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose)}

/* ---- how */
.how-line{margin-top:28px}
.how-stage{position:relative;margin-top:48px}
.how-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin-top:40px}
.step .k{font-family:var(--mono);font-size:var(--fs-label);color:var(--text);display:flex;align-items:center;gap:12px}
.step .k span{color:var(--text-secondary)}
.step h3{font-size:var(--fs-title);line-height:1.1;font-weight:600;letter-spacing:-0.025em;margin-top:18px;color:var(--text);text-wrap:balance}
.step p{color:var(--text-secondary);margin-top:12px;font-size:var(--fs-body);line-height:var(--lh-body);transition:color .5s}
.step:not(.on) p{color:var(--text)}
.step{opacity:var(--dim);transform:translateY(16px);transition:opacity .5s,transform .6s cubic-bezier(.2,.7,.2,1)}
.step.on{opacity:1;transform:none}
.furrow{width:100%;height:120px;display:block}
.how-grid:first-child{margin-top:0}
.furrow .soil{fill:none;stroke:var(--line-strong);stroke-width:1.5;stroke-dasharray:6 8}
.furrow .path{fill:none;stroke:var(--accent);stroke-width:2;stroke-linecap:round}
.furrow .sprout{fill:none;stroke:var(--accent-hover);stroke-width:2;stroke-linecap:round;opacity:0;transition:opacity .4s}
.furrow.fire .soil{stroke-dasharray:none;stroke:var(--line)}
.furrow.fire .sprout{stroke-width:3}
.furrow .sprout.on{opacity:1}
.how-note{margin-top:48px;color:var(--text-secondary);max-width:52em;font-size:var(--fs-prose);line-height:var(--lh-prose)}

/* ---- who */
/* the situations as a two-column hairline list, the house way to list things: index, title, body, seam rule */
.who-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 48px;margin-top:48px;border-top:1px solid var(--line)}
.sit{background:none;border:0;border-bottom:1px solid var(--line);border-radius:0;padding:28px 0;display:grid;grid-template-columns:48px minmax(0,1fr);gap:6px 12px;align-content:start}
.sit .n{grid-row:1 / span 2;padding-top:4px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.sit h3{grid-column:2;font-size:var(--fs-title-sm);line-height:1.25;font-weight:600;letter-spacing:-0.015em;text-wrap:balance;transition:color .25s}
.sit p{grid-column:2;max-width:34em;color:var(--text-secondary);font-size:var(--fs-body)}
.sit:hover h3{color:var(--accent-hover)}
.turn{margin-top:24px;border:1px solid var(--copper-deep);border-radius:4px;padding:32px;display:grid;grid-template-columns:220px minmax(0,1fr);gap:24px;background:linear-gradient(90deg,rgba(var(--deep-rgb),.14),rgba(var(--deep-rgb),0) 60%)}
.turn h3{font-size:var(--fs-title-sm);font-weight:600;letter-spacing:-0.015em}
.turn p{color:var(--text)}

/* ---- people */
.people-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:48px}
.person{display:flex;flex-direction:column;gap:18px}
.portrait{position:relative;aspect-ratio:4/5;border-radius:4px;overflow:hidden;background:var(--surface);border:1px solid var(--line)}
.portrait svg,.portrait img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.portrait img{filter:contrast(1.02)}
.portrait .ini{position:absolute;left:18px;bottom:14px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);letter-spacing:.06em}
.portrait .slot{position:absolute;right:18px;bottom:14px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);opacity:.7}
.person h3{font-size:var(--fs-title);line-height:1.1;font-weight:600;letter-spacing:-0.025em}
.person .role{color:var(--text-secondary);font-size:var(--fs-small);margin-top:6px}
.person .where{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);margin-top:8px}
.person p.bio{color:var(--text-secondary);font-size:var(--fs-body);line-height:var(--lh-body)}
.person .links{display:flex;gap:18px;font-size:var(--fs-small);margin-top:auto}
.people-note{margin-top:56px;color:var(--text-secondary);max-width:52em;font-size:var(--fs-prose);line-height:var(--lh-prose)}

/* ---- contracting */
.facts{margin-top:56px;border-top:1px solid var(--line)}
.facts .row{display:grid;grid-template-columns:280px minmax(0,1fr);gap:24px;padding:22px 0;border-bottom:1px solid var(--line)}
.facts .k{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:3px}
.facts .v{font-size:var(--fs-lead);line-height:1.45}
.facts .v.todo{color:var(--text-secondary);font-family:var(--mono);font-size:var(--fs-small)}

/* ---- faq */
.faq{margin-top:40px;border-top:1px solid var(--line)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:24px;padding:26px 0;font-size:var(--fs-title-sm);font-weight:600;letter-spacing:-0.02em;line-height:1.2}
.faq summary::-webkit-details-marker{display:none}
.faq summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.faq summary i{flex:0 0 28px;width:28px;height:28px;border:1px solid var(--line-strong);border-radius:50%;position:relative;transition:transform .4s,border-color .3s}
.faq summary i::before,.faq summary i::after{content:"";position:absolute;left:50%;top:50%;width:12px;height:1px;background:var(--text);transform:translate(-50%,-50%)}
.faq summary i::after{transform:translate(-50%,-50%) rotate(90deg)}
.faq details[open] summary i{transform:rotate(45deg);border-color:var(--accent)}
.faq .a{overflow:hidden;height:0;transition:height .45s cubic-bezier(.16,1,.3,1)}
.faq details.closing .a{transition-duration:.3s}
.faq .a p{padding:0 0 28px;color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose);max-width:56em}

/* ---- closing */
.scene-book{position:relative}
.scene-book .pin{position:relative;min-height:640px;overflow:hidden;display:flex;align-items:center;padding:150px 0 160px}
.scene-book .art{position:absolute;inset:0;width:100%;height:100%}
.scene-book .wrap{position:relative;z-index:2;width:100%}
.scene-book h2{max-width:10ch}
.scene-book .mail{margin-top:28px;font-size:var(--fs-lead);line-height:1.45;color:var(--text-secondary);max-width:24em}
.scene-book .cta{margin-top:36px}
.scene-book .line{position:absolute;right:var(--side);bottom:40px;z-index:2;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);max-width:34em;text-align:right}
.foot{position:relative;z-index:1;border-top:1px solid var(--line);padding:40px var(--side) 48px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:24px;align-items:end;font-size:var(--fs-small);color:var(--text-secondary);background:var(--bg)}
.foot .lockup svg{height:28px}
.foot .links{display:flex;gap:20px;flex-wrap:wrap}

@media (max-width:1100px){
  .who-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .people-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .how-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:900px){
  .sec{padding:64px 0}
  .scene-statement{height:auto}.scene-statement .pin{position:relative;height:auto;min-height:0;padding:80px 0}
  .scene-statement .cur{display:none}
  .scene-book .wrap{padding-top:30vh}
  .who-grid,.people-grid,.how-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .scene-build{height:auto}.scene-build .pin{position:relative;height:auto;min-height:0;padding:80px 0 0;display:block}.markmap{grid-template-columns:minmax(0,1fr);gap:32px}.mark-col{order:-1}.bigmark{width:min(60vw,260px)}.cap{opacity:1}.cap p{max-height:none;opacity:1}.cap h3,.cap.on h3{color:var(--text)}.mark-count{display:none}
  .wall-detail-inner,.wall-line,.rec{grid-template-columns:minmax(0,1fr)}
  .eras{padding-left:28px}.era-block::before{left:-25px}
  .metrics{grid-template-columns:minmax(0,1fr)}
  .scene-proof{padding:56px 0 80px}
  .name{padding:10px 0}
  .track{gap:16px;padding:0 var(--side) 16px;margin-top:32px}
  .strip-nav{display:none}
  .card{flex-basis:min(86vw,420px);padding:28px}
  /* one column, and the price reads directly under the title: the left div dissolves into the grid so its children can be ordered */
  .panel{grid-template-columns:minmax(0,1fr);gap:0;position:relative;top:auto;box-shadow:none}.panel > div:first-child{display:contents}.pcols{grid-template-columns:minmax(0,1fr);margin-top:24px}
  .panel .n{order:1}.panel h3{order:2}.panel .price{order:3;text-align:left;margin-top:4px}.panel > div > p{order:4}.panel .pcols{order:5}
  .panel .price b.word{font-size:var(--fs-title-sm);line-height:1.25;letter-spacing:-0.015em}
  .turn,.facts .row{grid-template-columns:minmax(0,1fr)}
  .scene-book .pin{display:block;min-height:0;padding:48px 0 96px}
  .scene-book .line{position:relative;right:auto;bottom:auto;text-align:left;margin:40px var(--side) 0}
  .foot{grid-template-columns:minmax(0,1fr)}
  .step{opacity:1;transform:none}.step:not(.on) p{color:var(--text-secondary)}
}
@media (max-width:600px){
  .card .cfacts div{grid-template-columns:minmax(0,1fr);gap:2px}
  .who-grid,.people-grid,.how-grid{grid-template-columns:minmax(0,1fr)}
  /* a person is a row on a phone: the portrait beside the name and role, the bio and links under both */
  .person{display:grid;grid-template-columns:120px minmax(0,1fr);gap:12px 16px;align-items:center}
  .person .portrait{grid-row:1;width:120px;aspect-ratio:4/5}
  .person > div:not(.portrait):not(.links){grid-column:2;grid-row:1}
  .person p.bio,.person .links{grid-column:1 / -1}
  .person .links{margin-top:0}
  .person h3{font-size:var(--fs-title-sm)}
}
@media (prefers-reduced-motion:reduce){
  .theme-rune .sec h2.reveal::after,.theme-rune .scene-book h2::after{width:120px;transition:none}
  .mark-arrived .site-header .mark-fill{animation:none}
  .site-header .btn{transition:none}
  .step{opacity:1;transform:none}.step:not(.on) p{color:var(--text-secondary)}
  .statement .w{opacity:1}
}
/* ---- without JavaScript every word reads at rest: the scenes lay out as plain sections and nothing waits on the scroll */
html:not(.js) .theme-rune .hero{height:auto;min-height:0}
html:not(.js) .theme-rune .hero-pin{position:relative;height:auto;min-height:0;overflow:visible}
html:not(.js) .theme-rune .hero-inner{height:auto;min-height:100vh;min-height:100dvh}
html:not(.js) .hero-statement{position:relative;opacity:1;transform:none;pointer-events:auto;padding-bottom:64px}
html:not(.js) .statement .w{opacity:1}
html:not(.js) .scene-build{height:auto}
html:not(.js) .scene-build .pin{position:relative;height:auto;min-height:0;overflow:visible;padding-bottom:64px}
html:not(.js) .cap{opacity:1}
html:not(.js) .cap p{max-height:none;opacity:1;margin-top:8px}
html:not(.js) .bigmark path{fill:var(--accent)}
html:not(.js) .mark-count{display:none}
html:not(.js) .step{opacity:1;transform:none}
html:not(.js) .faq .a{height:auto}
'''

# ---------------------------------------------------------------------------------------------- markup

def silhouette(seed):
    # a lit bust, abstract on purpose: it is a slot for the photograph
    return f'''<svg viewBox="0 0 400 500" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="bg{seed}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1B2126"/><stop offset="1" stop-color="#0E1114"/></linearGradient>
<linearGradient id="sk{seed}" x1="0.2" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="#3a2a22"/><stop offset=".55" stop-color="#22201f"/><stop offset="1" stop-color="#141719"/></linearGradient>
<radialGradient id="rim{seed}" cx="0.78" cy="0.18" r="0.6"><stop offset="0" stop-color="#EFA37C" stop-opacity=".55"/><stop offset=".5" stop-color="#DF8E63" stop-opacity=".12"/><stop offset="1" stop-color="#DF8E63" stop-opacity="0"/></radialGradient>
</defs>
<rect width="400" height="500" fill="url(#bg{seed})"/>
<g>
<ellipse cx="{200 + (seed % 3) * 4}" cy="{182 - (seed % 2) * 6}" rx="{78 + (seed % 4) * 2}" ry="{96 + (seed % 3) * 3}" fill="url(#sk{seed})"/>
<path d="M60 500 C70 380 130 330 200 322 C270 330 330 380 340 500 Z" fill="url(#sk{seed})"/>
<rect x="176" y="250" width="48" height="90" fill="url(#sk{seed})"/>
</g>
<rect width="400" height="500" fill="url(#rim{seed})"/>
<rect width="400" height="500" fill="#000" opacity=".12"/>
</svg>'''


def sections(t, theme):
    words = " ".join(f'<span class="w">{w}</span>' for w in STATEMENT.split(" "))
    bigmark = '<svg class="bigmark" viewBox="-6 -6 116 116" aria-hidden="true">' + "".join(f'<path data-piece="{i}" d="{pp}"></path>' for i, pp in enumerate(PIECES)) + '</svg>'
    caps = "".join(f'<div class="cap" data-cap="{i}" data-piece="{c["piece"]}"><div class="k">0{i+1}</div><h3>{c["name"]}</h3><p>{c["line"]}</p></div>' for i, c in enumerate(CAPS))
    cards = ""
    for i, c in enumerate(PROOF_CARDS):
        links = "".join(f'<a href="{u}" rel="noopener">{l}</a>' for l, u in c["links"])
        cards += f'<article class="card reveal" style="--i:{min(i,4)}"><div class="chead"><div class="kicker">{c["kicker"]}</div><div class="idx">{i+1:02d} / {len(PROOF_CARDS):02d}</div></div><h3>{c["title"]}</h3><dl class="cfacts">{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["facts"])}</dl><div class="cfoot"><div class="links">{links}</div><div class="era">{c["era"]}</div></div></article>'
    wall = ""
    for i, (nm, grp, links, era) in enumerate(WALL):
        lk = "".join(f'<a href="{u}" rel="noopener">{l}</a>' for l, u in links)
        wall += f'<button class="name {grp}" type="button" data-i="{i}" aria-expanded="false" aria-controls="wall-detail">{nm}</button><div class="wall-line" id="wall-{i}"><div class="wall-era">{era}</div><div>{('<div class="links">' + lk + '</div>') if lk else ''}</div></div>'
    eras = ""
    for e in ERAS:
        rows = "".join(f'<div class="rec reveal"><div class="yr">{y}</div><div><h4>{tt}</h4><p>{bd}</p>{"<div class=links>" + "".join(f"<a href={u!r} rel=noopener>{l}</a>" for l, u in lk) + "</div>" if lk else ""}</div></div>' for y, tt, bd, lk in e["cases"])
        eras += f'<div class="era-block"><div class="era-head reveal"><h3 class="era-name">{e["name"]}</h3><div class="era-years">{e["years"]}</div><p class="era-intro">{e["intro"]}</p></div><div class="era-cases">{rows}</div></div>'
    panels = ""
    for i, o in enumerate(OFFERS):
        note = f'<span>{o["note"]}</span>' if o["note"] else ""
        cols = (f'<div class="pcol"><div class="pk">What you get</div><ul>{"".join(f"<li>{x}</li>" for x in o["what"])}</ul></div>'
                f'<div class="pcol"><div class="pk">Terms</div><ul>{"".join(f"<li>{x}</li>" for x in o["terms"])}</ul></div>'
                f'<div class="pcol"><div class="pk">Who delivers</div><p>{o["who"]}</p></div>')
        launch = " launch" if "launch" in o["note"] else ""
        word = ' class="word"' if not any(ch.isdigit() for ch in o["price"]) else ""
        panels += f'<article class="panel reveal{launch}" style="--i:{i}"><div><div class="n">0{i+1} / 0{len(OFFERS)}</div><h3>{o["name"]}</h3><p>{o["body"]}</p></div><div class="price"><b{word}>{o["price"]}</b>{note}</div><div class="pcols">{cols}</div></article>'
    steps = "".join(f'<div class="step" data-step="{i}"><div class="k">0{i+1}<span>{h}</span></div><h3>{o}</h3><p>{b}</p></div>' for i, (h, o, b) in enumerate(HOW))
    if theme == "rune":
        how_art = ""
    else:
        how_art = ('<svg class="furrow" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true">'
                   '<path class="soil" d="M0 78 C150 70 250 92 400 82 C550 72 650 94 800 84 C950 74 1050 92 1200 82"/>'
                   '<path class="path" d="M0 78 C150 70 250 92 400 82 C550 72 650 94 800 84 C950 74 1050 92 1200 82"/>'
                   + "".join(f'<path class="sprout" d="M{x} 80 C{x} 60 {x-10} 52 {x-16} 44 M{x} 80 C{x} 58 {x+12} 50 {x+18} 40 M{x} 82 L{x} 34" ></path>' for x in (150, 450, 750, 1050)) +
                   '</svg>')
    who = "".join(f'<article class="sit reveal" style="--i:{i}"><div class="n">0{i+1}</div><h3>{h}</h3><p>{b}</p></article>' for i, (h, b) in enumerate(WHO))
    people = ""
    for i, p in enumerate(PEOPLE):
        links = "".join(f'<a href="{u}" rel="noopener">{l}</a>' for l, u in p["links"])
        where = f'<div class="where">{p["where"]}</div>' if p["where"] else ""
        pic = (f'<picture><source type="image/webp" srcset="people/{p["photo"]}.webp"><img src="people/{p["photo"]}.jpg" width="800" height="1000" alt="{p.get("alt", p["name"])}" loading="lazy" decoding="async"></picture>' if p.get("photo") else silhouette(p["seed"]))
        tag = "" if p.get("photo") else f'<div class="ini">{p["ini"]}</div><div class="slot">photo slot</div>'
        people += (f'<article class="person reveal" style="--i:{i}"><div class="portrait">{pic}'
                   f'{tag}</div>'
                   f'<div><h3>{p["name"]}</h3><div class="role">{p["role"]}</div>{where}</div><p class="bio">{p["bio"]}</p>'
                   f'{("<div class=links>" + links + "</div>") if links else ""}</article>')
    facts = "".join(f'<div class="row reveal" style="--i:{i}"><div class="k">{k}</div><div class="v{" todo" if v.startswith("[") else ""}">{v}</div></div>' for i, (k, v) in enumerate(CONTRACT))
    faq = "".join(f'<details><summary><span>{q}</span><i></i></summary><div class="a"><p>{a}</p></div></details>' for q, a in FAQ)
    book_art = '<canvas class="art" id="book-art" aria-hidden="true"></canvas>'
    chevron = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{d}"/></svg>'
    strip_nav = ('<div class="strip-nav">'
                 f'<button type="button" class="strip-btn" data-dir="-1" aria-label="Previous case">{chevron.format(d="M10 3L5 8l5 5")}</button>'
                 f'<button type="button" class="strip-btn" data-dir="1" aria-label="Next case">{chevron.format(d="M6 3l5 5-5 5")}</button></div>')

    statement_scene = "" if theme == "rune" else f'''
<section class="scene-statement" id="statement" data-scrub="statement">
  <div class="pin">
    <div class="wrap">
      <p class="eyebrow">{t["statement_eyebrow"]}</p>
      <p class="statement" id="statement-text">{words}</p>
    </div>
    <div class="cur">Keep scrolling</div>
  </div>
</section>'''
    return f'''
{statement_scene}

<section class="scene-build" id="build" data-scrub="build">
  <div class="pin">
    <div class="wrap">
      <p class="eyebrow">{t["build_eyebrow"]}</p>
      <h2>Four things we build.</h2>
      <div class="markmap">
        <div class="caps-left">{caps}</div>
        <div class="mark-col">{bigmark}<div class="mark-count" id="mark-count">01 / 04</div></div>
      </div>
      <p class="skills skills-foot"><span class="n">Stack</span>{SKILLS}</p>
    </div>
  </div>
</section>

<section class="sec" id="proof" style="padding-bottom:0">
  <div class="wrap">
    <p class="eyebrow reveal">{t["proof_eyebrow"]}</p>
    <h2 class="reveal">What we have shipped.</h2>
    <p class="lead reveal">Selected work by Felag's founders and principals at Uddug and Gateway.fm.</p>
    <div class="metrics stagger">
      <article class="metric reveal" style="--i:0"><div class="big" data-count="140" data-suffix="k+">140<em>k+</em></div><div class="label">requests per second at peak, in production for Opera and 1inch</div></article>
      <article class="metric reveal" style="--i:1"><div class="big">$1<em>B+</em></div><div class="label">locked in staking on the infrastructure we ran in 2025 and 2026, serving Lido, Gnosis, Stellar and Canton</div></article>
      <article class="metric reveal" style="--i:2"><div class="big">9<em>M+</em></div><div class="label">users on Humanity Protocol, whose application layer we built</div></article>
    </div>
  </div>
</section>
<section class="scene-proof" id="proof-cases" aria-label="Lead cases">
  <div class="wrap strip-head"><p class="lead" style="margin-top:0">The lead cases, with the public record linked where one exists.</p>{strip_nav}</div>
  <div class="track" id="track">{cards}</div>
</section>
<section class="sec" id="names" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow reveal">{t["wall_eyebrow"]}</p>
    <h2 class="reveal">Names we have worked with.</h2>
    <p class="lead reveal">Clients and products we built for, and the protocols our systems served. Open a name for its era and any public record.</p>
    <div class="wall reveal" id="wall">{wall}<div class="wall-detail" id="wall-detail" hidden><div class="wall-detail-inner" id="wall-detail-inner"></div></div></div>
  </div>
</section>
<section class="sec" id="record" data-scrub="record">
  <div class="wrap">
    <p class="eyebrow reveal">{t["more_eyebrow"]}</p>
    <h2 class="reveal">The record, in three eras.</h2>
    <div class="eras" id="eras"><div class="era-line" aria-hidden="true"><i id="era-line-fill"></i></div>{eras}</div>
  </div>
</section>

<section class="sec" id="offer">
  <div class="wrap">
    <p class="eyebrow reveal">{t["offer_eyebrow"]}</p>
    <h2 class="huge reveal">Engagements and fees.</h2>
    <p class="lead reveal">Fixed-price sprints and technical reviews. Monthly retainers for delivery pods and fractional CTO work. Every engagement has agreed scope and deliverables. Prices in US dollars, excluding VAT.</p>
    <div class="stack" id="stack">{panels}</div>
    <p class="offer-note reveal">{OFFER_NOTE}</p>
    <div class="cta reveal" style="margin-top:40px"><a class="btn" href="mailto:info@felag.net?subject=Free%20technical%20workshop">Write to us</a></div>
  </div>
</section>

<section class="sec" id="how" data-scrub="how">
  <div class="wrap">
    <p class="eyebrow reveal">{t["how_eyebrow"]}</p>
    <h2 class="reveal">How an engagement runs.</h2>
    <p class="lead reveal">{t["how_line"]}</p>
    <div class="how-stage">{how_art}<div class="how-grid">{steps}</div></div>
    <p class="how-note reveal">{HOW_NOTE}</p>
  </div>
</section>

<section class="sec" id="who">
  <div class="wrap">
    <p class="eyebrow reveal">{t["who_eyebrow"]}</p>
    <h2 class="reveal">The situations we see most often.</h2>
    <div class="who-grid stagger">{who}</div>
    <div class="turn reveal"><h3>What we turn down</h3><p>{TURN_DOWN}</p></div>
  </div>
</section>

<section class="sec" id="people">
  <div class="wrap">
    <p class="eyebrow reveal">{t["people_eyebrow"]}</p>
    <h2 class="reveal">The people who lead the work.</h2>
    <div class="people-grid stagger">{people}</div>
    <p class="people-note reveal">{PEOPLE_NOTE}</p>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap">
    <p class="eyebrow reveal">{t["faq_eyebrow"]}</p>
    <h2 class="reveal">The ones that come up on nearly every first call.</h2>
    <div class="faq reveal">{faq}</div>
  </div>
</section>

<section class="scene-book" id="book">
  <div class="pin">
    {book_art}
    <div class="wrap">
      <p class="eyebrow">{t["book_eyebrow"]}</p>
      <h2>Start with the workshop.</h2>
      <p class="mail">Write to <a href="mailto:info@felag.net?subject=Free%20technical%20workshop">info@felag.net</a> with the system and the deadline. A free technical workshop with a founder frames the problem.</p>
      <div class="cta"><a class="btn" href="mailto:info@felag.net?subject=Free%20technical%20workshop">Write to us</a><a class="textlink" href="#offer">See prices</a></div>
    </div>
    {("<div class=line>" + t["book_line"] + "</div>") if t.get("book_line") else ""}
  </div>
</section>
<footer class="foot">
  <div><a class="lockup" href="#top" aria-label="Felag, home">{LOCKUP}</a></div>
  <div class="links"><a href="https://www.linkedin.com/company/felagnet/" rel="noopener">LinkedIn</a><a href="https://github.com/felagnet" rel="noopener">GitHub</a><a href="https://x.com/felagnet" rel="noopener">X</a><a href="mailto:info@felag.net?subject=Free%20technical%20workshop">info@felag.net</a></div>
</footer>'''

# ---------------------------------------------------------------------------------------------- motion engine

SITE_JS = r'''
// ---- scrub engine: sections with data-scrub get a progress value each frame while near the viewport
(function(){
  var handlers = {};
  window.onScrub = function(name, fn){ handlers[name] = fn; };
  var items = [];
  document.querySelectorAll('[data-scrub]').forEach(function(el){ items.push({el: el, name: el.getAttribute('data-scrub'), last: -1}); });
  var ticking = false;
  function progressOf(el){
    var r = el.getBoundingClientRect(), runway = el.offsetHeight - window.innerHeight;
    if (runway <= 0){ return Math.max(0, Math.min(1, (window.innerHeight - r.top) / (window.innerHeight + el.offsetHeight))); }
    return Math.max(0, Math.min(1, -r.top / runway));
  }
  function tick(){
    ticking = false;
    items.forEach(function(it){
      var r = it.el.getBoundingClientRect();
      var near = r.bottom > -200 && r.top < window.innerHeight + 200;
      if (!near && it.last >= 0 && it.last !== 0 && it.last !== 1) return;
      var p = progressOf(it.el);
      if (near && handlers[it.name]) handlers[it.name](p, it.el);
      it.last = p;
    });
  }
  function request(){ if (!ticking){ ticking = true; requestAnimationFrame(tick); } }
  window.addEventListener('scroll', request, {passive: true});
  window.addEventListener('resize', request);
  window.addEventListener('load', request);
  setTimeout(request, 50); setTimeout(request, 600);
})();

// ---- statement: words light up as you scroll
(function(){
  var words = document.querySelectorAll('#statement-text .w'); if (!words.length) return;
  var n = words.length, narrow = window.innerWidth < 900;
  var inHero = !!document.getElementById('hero-statement');
  if (reduce || narrow){
    // no word-by-word light; the statement still arrives only once the hero text has faded, so the two never overlap
    words.forEach(function(w){ w.style.opacity = 1; });
    if (inHero){ var hs = document.getElementById('hero-statement'); window.onScrub('statement', function(){ var st = Math.max(0, Math.min(1, (heroProgress() - 0.3)/0.1)); hs.style.setProperty('--st', st.toFixed(3)); hs.style.pointerEvents = st >= 0.9 ? 'auto' : ''; }); }
    return;
  }
  window.onScrub('statement', function(p, el){
    var q;
    if (inHero){
      // the statement replaces the rune: it fades in once the rune has landed, then lights up word by word
      var hp = heroProgress(), st = Math.max(0, Math.min(1, (hp - 0.3)/0.1));
      el.style.setProperty('--st', st.toFixed(3)); el.style.pointerEvents = st >= 0.9 ? 'auto' : '';
      q = Math.max(0, Math.min(1, (hp - 0.4)/0.55));
    } else {
      // progress from the moment the scene enters at the bottom to the end of its runway, so the words light while the text rises
      var r = el.getBoundingClientRect(), h = window.innerHeight, runway = Math.max(1, el.offsetHeight - h);
      q = Math.max(0, Math.min(1, (h*0.9 - r.top) / (h*0.9 + runway)));
    }
    var lit = (q - 0.04) / 0.86 * (n + 3) - 1;
    for (var i = 0; i < n; i++){
      var k = Math.max(0, Math.min(1, lit - i));
      words[i].style.opacity = (0.5 + 0.5*k).toFixed(3);
      words[i].classList.toggle('hot', k > 0 && k < 1);
    }
  });
})();

// ---- what we build: the scroll lights one piece of the mark at a time, and the thing it stands for
(function(){
  var caps = document.querySelectorAll('#build .cap'), pieces = document.querySelectorAll('#build .bigmark path'), count = document.getElementById('mark-count'); if (!caps.length) return;
  var current = -1, narrow = window.innerWidth < 900;
  if (narrow){ caps.forEach(function(c){ c.classList.add('on'); }); pieces.forEach(function(pc){ pc.classList.add('on'); }); return; }
  window.onScrub('build', function(p){
    var idx = Math.min(caps.length - 1, Math.floor(Math.max(0, p - 0.02) / 0.96 * caps.length));
    if (idx === current) return;
    current = idx;
    caps.forEach(function(c, i){ c.classList.toggle('on', i === idx); });
    var piece = caps[idx].getAttribute('data-piece');
    pieces.forEach(function(pc){ pc.classList.toggle('on', pc.getAttribute('data-piece') === piece); });
    if (count) count.textContent = '0' + (idx + 1) + ' / 0' + caps.length;
  });
})();

// ---- the header knows where the reader is: the link for the section in view goes ash, the rest stay smoke
(function(){
  var links = document.querySelectorAll('.nav .links a[href]'); if (!links.length || !('IntersectionObserver' in window)) return;
  var map = {top: '', proof: '#proof', 'proof-cases': '#proof', names: '#proof', record: '#proof', offer: '#offer', how: '#how', who: '#how', people: '#people', faq: '#people'};
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return;
      var href = map[en.target.id];
      links.forEach(function(a){ a.classList.toggle('cur', !!href && a.getAttribute('href') === href); });
    });
  }, {rootMargin: '-40% 0px -55% 0px'});
  Object.keys(map).forEach(function(id){ var el = document.getElementById(id); if (el) io.observe(el); });
})();

// ---- the cases strip: previous and next move it one card at a time, for readers without a trackpad
(function(){
  var track = document.getElementById('track'), btns = document.querySelectorAll('.strip-btn'); if (!track || !btns.length) return;
  function update(){
    var prev = track.scrollLeft < 2, next = track.scrollLeft + track.clientWidth > track.scrollWidth - 2;
    btns.forEach(function(b){ b.disabled = b.getAttribute('data-dir') === '-1' ? prev : next; });
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){
    var card = track.querySelector('.card'), step = (card ? card.getBoundingClientRect().width : track.clientWidth*0.8) + 24;
    track.scrollBy({left: parseInt(b.getAttribute('data-dir'), 10)*step, behavior: reduce ? 'auto' : 'smooth'});
  }); });
  track.addEventListener('scroll', update, {passive: true}); window.addEventListener('resize', update); update();
})();

// ---- the names wall: a name opens its line right under its own row
(function(){
  var wall = document.getElementById('wall'), detail = document.getElementById('wall-detail'), inner = document.getElementById('wall-detail-inner');
  if (!wall || !detail) return;
  var open = null;
  function close(){ if (!open) return; open.classList.remove('on'); open.setAttribute('aria-expanded', 'false'); open = null; detail.classList.add('closing'); detail.style.height = detail.scrollHeight + 'px'; requestAnimationFrame(function(){ detail.style.height = '0px'; }); detail.addEventListener('transitionend', function h(){ detail.hidden = true; detail.classList.remove('closing'); detail.removeEventListener('transitionend', h); }); }
  wall.addEventListener('click', function(e){
    var btn = e.target.closest('.name'); if (!btn) return;
    if (open === btn){ close(); return; }
    if (open){ open.classList.remove('on'); open.setAttribute('aria-expanded', 'false'); }
    open = btn; btn.classList.add('on'); btn.setAttribute('aria-expanded', 'true');
    inner.innerHTML = document.getElementById('wall-' + btn.getAttribute('data-i')).innerHTML;
    // find the last name on the same visual row and place the detail after it
    var top = btn.offsetTop, names = wall.querySelectorAll('.name'), last = btn;
    names.forEach(function(n){ if (Math.abs(n.offsetTop - top) < 6 && n.offsetLeft > last.offsetLeft) last = n; });
    detail.hidden = false; detail.style.height = '0px'; last.insertAdjacentElement('afterend', detail);
    requestAnimationFrame(function(){ detail.style.height = detail.scrollHeight + 'px'; });
    detail.addEventListener('transitionend', function h(){ if (!detail.hidden) detail.style.height = 'auto'; detail.removeEventListener('transitionend', h); });
  });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') close(); });
})();

// ---- the record: the era line draws as the reader moves down it, each era lighting its marker
(function(){
  var fill = document.getElementById('era-line-fill'), blocks = document.querySelectorAll('.era-block'); if (!fill) return;
  window.onScrub('record', function(p, el){
    var r = el.getBoundingClientRect(), h = window.innerHeight;
    var eras = document.getElementById('eras').getBoundingClientRect();
    var q = Math.max(0, Math.min(1, (h*0.7 - eras.top) / Math.max(1, eras.height)));
    fill.style.height = (q*100).toFixed(2) + '%';
    blocks.forEach(function(b){ var br = b.getBoundingClientRect(); b.classList.toggle('lit', br.top < h*0.7); });
  });
})();

// ---- how: steps and their art follow the scroll through the section
(function(){
  var steps = document.querySelectorAll('#how .step'), sprouts = document.querySelectorAll('.furrow .sprout'), path = document.querySelector('.furrow .path');
  var len = path ? path.getTotalLength() : 0;
  if (path){ path.style.strokeDasharray = len; path.style.strokeDashoffset = len; }
  window.onScrub('how', function(p, el){
    var r = el.getBoundingClientRect(), h = window.innerHeight;
    // local progress: 0 when the section top reaches 80% of the viewport, 1 when its bottom reaches 40%
    var q = Math.max(0, Math.min(1, (h*0.8 - r.top) / Math.max(1, r.height - h*0.4)));
    var narrow = window.innerWidth < 900;
    steps.forEach(function(s, i){ s.classList.toggle('on', narrow || q > (i + 0.5) / (steps.length + 0.6)); });
    if (path) path.style.strokeDashoffset = (len * (1 - Math.min(1, q*1.15))).toFixed(1);
    sprouts.forEach(function(s, i){ s.classList.toggle('on', q > (i + 0.55) / (sprouts.length + 0.6)); });
  });
})();

// ---- rune theme: the metrics and the thesis line burn in, the closing title draws its stroke
(function(){
  if (reduce || !document.getElementById('root').classList.contains('theme-rune') || !('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function(entries){ entries.forEach(function(en){ if (en.isIntersecting){ var c = en.target.classList; c.add(c.contains('big') || c.contains('huge') ? 'burn' : 'lit'); io.unobserve(en.target); } }); }, {threshold: 0.6});
  document.querySelectorAll('.metric .big, .sec h2.huge, .scene-book h2').forEach(function(el){ io.observe(el); });
})();

// ---- faq: animated open and close
(function(){
  document.querySelectorAll('.faq details').forEach(function(d){
    var a = d.querySelector('.a'), s = d.querySelector('summary');
    if (d.open) a.style.height = 'auto';
    s.addEventListener('click', function(e){
      e.preventDefault();
      if (d.open){
        d.classList.add('closing'); a.style.height = a.scrollHeight + 'px'; requestAnimationFrame(function(){ a.style.height = '0px'; });
        a.addEventListener('transitionend', function h(){ d.open = false; d.classList.remove('closing'); a.removeEventListener('transitionend', h); });
      } else {
        d.open = true; a.style.height = '0px'; requestAnimationFrame(function(){ a.style.height = a.scrollHeight + 'px'; });
        a.addEventListener('transitionend', function h(){ a.style.height = 'auto'; a.removeEventListener('transitionend', h); });
      }
    });
  });
})();
'''

# the closing scene, rune theme: the rune draws itself, ignites once and becomes the mark
BOOK_RUNE_JS = r"""
(function(){
  var canvas = document.getElementById('book-art'); if (!canvas) return;
  var ctx = canvas.getContext('2d'), W = 0, H = 0, k = 1, dpr = Math.min(window.devicePixelRatio || 1, 2);
  var hasFilter = 'filter' in ctx;
  var pieces = [[[0,0],[32,0],[32,104],[0,104]],[[44,0],[66,0],[44,22]],[[44,38],[82,0],[104,0],[44,60]],[[44,76],[104,16],[104,104],[44,104]]];
  var strokes = [{a: [16, 104], b: [16, 0]}, {a: [16, 72], b: [62, 26]}, {a: [16, 40], b: [62, -6]}];
  strokes.forEach(function(s){ s.len = Math.hypot(s.b[0]-s.a[0], s.b[1]-s.a[1]); });
  var total = strokes.reduce(function(a, s){ return a + s.len; }, 0);
  var cx, cy, scale, p = 0, visible = false, t = 0, last = 0;
  function clamp(x){ return Math.max(0, Math.min(1, x)); }
  function layout(){
    var r = canvas.getBoundingClientRect(); W = Math.round(r.width); H = Math.round(r.height); canvas.width = W*dpr; canvas.height = H*dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); k = Math.min(W, H)/900;
    var narrow = W < 900; scale = narrow ? Math.min(W, H)*0.5/104 : Math.min(W*0.32, H*0.74)/104; cx = narrow ? W*0.5 : W*0.72; cy = narrow ? H*0.20 : H*0.5;
    if (narrow){
      // on a phone the mark sits above the text block, never on it: it fits between the top of the scene and the headline
      var text = canvas.parentElement.querySelector('.wrap > *'), limit = (text ? text.getBoundingClientRect().top - r.top : H*0.3) - 16;
      scale = Math.min(scale, (limit - 8)/104); cy = Math.max(8 + 52*scale, Math.min(cy, limit - 52*scale));
    }
  }
  layout(); window.addEventListener('resize', layout);
  function P(x, y){ return [cx + (x - 52)*scale, cy + (y - 52)*scale]; }
  function ease(x){ return x < 0.5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3)/2; }
  function tracePath(c, upto){
    var left = upto;
    for (var i = 0; i < strokes.length && left > 0; i++){
      var s = strokes[i], f = Math.min(1, left/s.len); left -= s.len;
      var a = P(s.a[0], s.a[1]), b = P(s.a[0] + (s.b[0]-s.a[0])*f, s.a[1] + (s.b[1]-s.a[1])*f);
      c.moveTo(a[0], a[1]); c.lineTo(b[0], b[1]);
    }
  }
  function drawRune(c, upto, w, col, alpha, comp){
    c.save(); c.globalCompositeOperation = comp || 'source-over'; c.globalAlpha = clamp(alpha); c.strokeStyle = col; c.lineWidth = w; c.lineCap = 'round'; c.lineJoin = 'round';
    c.beginPath(); tracePath(c, upto); c.stroke(); c.restore();
  }
  function drawMark(c, alpha, hot){
    c.save(); c.globalAlpha = alpha;
    c.fillStyle = hot > 0 ? 'rgb(' + Math.round(223 + 32*hot) + ',' + Math.round(142 + 83*hot) + ',' + Math.round(99 + 95*hot) + ')' : '#DF8E63';
    if (hot > 0){ c.shadowColor = 'rgba(239,163,124,' + (0.9*hot).toFixed(2) + ')'; c.shadowBlur = 46*hot*k + 8; }
    pieces.forEach(function(pc){ c.beginPath(); pc.forEach(function(pt, i){ var q = P(pt[0], pt[1]); if (i) c.lineTo(q[0], q[1]); else c.moveTo(q[0], q[1]); }); c.closePath(); c.fill(); });
    c.restore();
  }
  var running = false;
  function schedule(){ if (!running){ running = true; last = performance.now(); requestAnimationFrame(frame); } }
  function frame(now){
    running = false;
    var dt = Math.min(0.05, (now - last)/1000); last = now; t += dt;
    if (!visible) return; // look() schedules a frame again when the scene is back on screen
    if (started && !hold) p = Math.min(0.9, (t - t0)*0.25);
    ctx.clearRect(0, 0, W, H);
    // stage 1: the rune draws itself (p 0.05 to 0.42); stage 2: one ignition pulse (0.42 to 0.52); stage 3: it becomes the mark (0.52 to 0.82)
    var draw = ease(clamp((p - 0.05)/0.37));
    var ig = clamp((p - 0.42)/0.1);
    var morph = clamp((p - 0.52)/0.3);
    var upto = total*draw, w = 10*scale/8;
    var done = hold || p >= 0.9, runeA = 1 - morph, breathe = done ? 1 : 0.95 + 0.05*Math.sin(t*1.2), flare = ig > 0 ? (1 - clamp((p - 0.46)/0.2)) : 0;
    if (draw > 0.2){
      var hg = ctx.createRadialGradient(cx, cy, 0, cx, cy, 70*scale);
      hg.addColorStop(0, 'rgba(223,142,99,' + ((0.16*breathe*draw + 0.22*flare)*(1 - morph)).toFixed(3) + ')'); hg.addColorStop(1, 'rgba(223,142,99,0)');
      ctx.fillStyle = hg; ctx.fillRect(0, 0, W, H);
    }
    if (runeA > 0){
      if (hasFilter){ ctx.save(); ctx.filter = 'blur(' + (18*k).toFixed(1) + 'px)'; ctx.globalCompositeOperation = 'lighter'; drawRune(ctx, upto, w*3, '#DF8E63', (0.45 + 0.4*ig)*runeA*breathe, 'lighter'); ctx.restore(); }
      else { var off = W + 400; ctx.save(); ctx.setTransform(dpr, 0, 0, dpr, -off*dpr, 0); ctx.shadowOffsetX = off*dpr; ctx.shadowOffsetY = 0; ctx.shadowBlur = 36*k; ctx.shadowColor = 'rgba(223,142,99,' + clamp((0.45 + 0.4*ig)*runeA*breathe).toFixed(3) + ')'; drawRune(ctx, upto, w*3, '#000', 1, 'lighter'); ctx.restore(); }
      drawRune(ctx, upto, w*1.3, '#8C4E2C', runeA); drawRune(ctx, upto, w, ig > 0 ? '#E8996D' : '#DF8E63', runeA);
      drawRune(ctx, upto, w*0.45, '#FFD9B4', (0.5 + 0.4*ig)*runeA, 'lighter');
      if (ig > 0 && ig < 1){
        var seg = total*0.16, head = ig*(total + seg);
        ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.lineCap = 'round'; ctx.lineWidth = w*0.7; ctx.strokeStyle = '#FFF1E0'; ctx.globalAlpha = 0.9*Math.sin(ig*Math.PI);
        ctx.setLineDash([seg, total*4]); ctx.lineDashOffset = -(head - seg); ctx.beginPath(); tracePath(ctx, total); ctx.stroke(); ctx.restore();
      }
      if (draw > 0 && draw < 1){
        var left = upto, tip = null;
        for (var i = 0; i < strokes.length; i++){ var s = strokes[i]; if (left <= s.len){ var f = left/s.len; tip = P(s.a[0] + (s.b[0]-s.a[0])*f, s.a[1] + (s.b[1]-s.a[1])*f); break; } left -= s.len; }
        if (tip){ var tg = ctx.createRadialGradient(tip[0], tip[1], 0, tip[0], tip[1], 26*k + 8); tg.addColorStop(0, 'rgba(255,236,210,.95)'); tg.addColorStop(0.3, 'rgba(239,163,124,.5)'); tg.addColorStop(1, 'rgba(239,163,124,0)'); ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = tg; ctx.beginPath(); ctx.arc(tip[0], tip[1], 26*k + 8, 0, 6.283); ctx.fill(); ctx.restore(); }
      }
    }
    if (morph > 0) drawMark(ctx, morph, 1 - morph);
    // the mark at rest is drawn once; frames run only while the rune is still drawing or igniting
    if (!done || !started) { running = true; requestAnimationFrame(frame); }
  }
  var started = false, hold = false, t0 = 0;
  function look(){ var r = canvas.getBoundingClientRect(); visible = r.bottom > 0 && r.top < window.innerHeight; if (!started && r.top < window.innerHeight*0.72){ started = true; t0 = t; } if (visible) schedule(); }
  window.addEventListener('scroll', look, {passive: true}); window.addEventListener('resize', function(){ layout(); look(); }); document.addEventListener('visibilitychange', look);
  if (reduce || window.innerWidth < 900){ hold = true; p = 0.9; }
  look(); setTimeout(look, 400);
})();
"""

# the closing scene, harvest theme: the field from above, the rune cut into it
BOOK_HARVEST_JS = r"""
(function(){
  var canvas = document.getElementById('book-art'); if (!canvas) return;
  var ctx = canvas.getContext('2d'), W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  var field = document.createElement('canvas'), fctx = field.getContext('2d');
  var stub = document.createElement('canvas'), sctx = stub.getContext('2d');
  var channels = [[[38,0],[38,104],12],[[44,30],[80,-4],11.3],[[44,68],[108,2],11.3]];
  var cx, cy, scale, p = 0, visible = false, t = 0, last = 0;
  function P(u, v){ return [cx + (u - 52)*scale, cy + (v - 52)*scale]; }
  function inChannel(u, v){
    for (var i = 0; i < channels.length; i++){ var c = channels[i], ax = c[0][0], ay = c[0][1], dx = c[1][0]-ax, dy = c[1][1]-ay, l2 = dx*dx+dy*dy, tt = ((u-ax)*dx + (v-ay)*dy)/l2; if (tt < -0.02 || tt > 1.02) continue; var px = ax + dx*tt, py = ay + dy*tt; if (Math.hypot(u-px, v-py) < c[2]/2) return true; }
    return false;
  }
  function layout(){
    var r = canvas.getBoundingClientRect(); W = Math.round(r.width); H = Math.round(r.height);
    [canvas, field, stub].forEach(function(c){ c.width = W*dpr; c.height = H*dpr; });
    [ctx, fctx, sctx].forEach(function(c){ c.setTransform(dpr, 0, 0, dpr, 0, 0); });
    var narrow = W < 900; scale = narrow ? Math.min(W, H)*0.5/104 : Math.min(W*0.3, H*0.74)/104; cx = narrow ? W*0.5 : W*0.7; cy = narrow ? H*0.26 : H*0.5;
    // soil
    var g = fctx.createLinearGradient(0, 0, W, H); g.addColorStop(0, '#100c09'); g.addColorStop(1, '#1a120c'); fctx.fillStyle = g; fctx.fillRect(0, 0, W, H);
    for (var i = 0; i < 1800; i++){ fctx.fillStyle = 'rgba(' + (56 + Math.random()*36|0) + ',' + (34 + Math.random()*22|0) + ',' + (20 + Math.random()*12|0) + ',' + (0.12 + Math.random()*0.25).toFixed(2) + ')'; fctx.beginPath(); fctx.ellipse(Math.random()*W, Math.random()*H, 2 + Math.random()*6, 1 + Math.random()*2, Math.random()*3.14, 0, 6.283); fctx.fill(); }
    // the ears in rough rows, copper from above, brighter towards the light in the top right
    var step = Math.max(5, 6.5*scale/4.2), r0 = Math.max(1.3, 1.9*scale/4.2);
    for (var y = -step; y < H + step; y += step){
      for (var x = -step; x < W + step; x += step*0.8){
        var jx = x + (Math.random()-0.5)*step, jy = y + (Math.random()-0.5)*step;
        var lightK = 0.35 + 0.65*Math.max(0, Math.min(1, 1 - Math.hypot((jx - W*0.86)/W, (jy - H*0.1)/H)*1.4));
        var lit = (0.25 + Math.random()*0.75)*lightK;
        fctx.fillStyle = 'rgba(' + (70 + 130*lit|0) + ',' + (42 + 70*lit|0) + ',' + (18 + 30*lit|0) + ',' + (0.5 + 0.5*Math.random()).toFixed(2) + ')';
        fctx.beginPath(); fctx.ellipse(jx, jy, r0*(0.7 + Math.random()*0.8), r0*0.55*(0.7 + Math.random()*0.8), 0.5 + Math.random()*0.5, 0, 6.283); fctx.fill();
      }
    }
    // the stubble: soil and pale cut straw, only inside the channels
    sctx.clearRect(0, 0, W, H);
    sctx.lineCap = 'round';
    channels.forEach(function(c){ var a = P(c[0][0], c[0][1]), b = P(c[1][0], c[1][1]); sctx.strokeStyle = '#26190f'; sctx.lineWidth = c[2]*scale; sctx.beginPath(); sctx.moveTo(a[0], a[1]); sctx.lineTo(b[0], b[1]); sctx.stroke(); });
    sctx.globalCompositeOperation = 'source-atop';
    var n = Math.round(W*H/240);
    for (var k = 0; k < n; k++){
      var fx = Math.random()*W, fy = Math.random()*H;
      var u = (fx - cx)/scale + 52, v = (fy - cy)/scale + 52;
      if (u < -8 || u > 116 || v < -8 || v > 112 || !inChannel(u, v)) continue;
      var pale = Math.random() < 0.7;
      sctx.fillStyle = pale ? 'rgba(' + (196 + Math.random()*40|0) + ',' + (150 + Math.random()*40|0) + ',' + (92 + Math.random()*30|0) + ',' + (0.5 + Math.random()*0.45).toFixed(2) + ')' : 'rgba(60,38,22,' + (0.4 + Math.random()*0.4).toFixed(2) + ')';
      sctx.beginPath(); sctx.ellipse(fx, fy, r0*(1.2 + Math.random()*1.6), r0*0.4, Math.random()*3.14, 0, 6.283); sctx.fill();
    }
    sctx.globalCompositeOperation = 'source-over';
  }
  layout(); window.addEventListener('resize', layout);
  function clipChannel(c, tt){
    // the band from a to a + (b - a) * tt, as a rotated rectangle
    var a = P(c[0][0], c[0][1]), b = P(c[1][0], c[1][1]), dx = b[0]-a[0], dy = b[1]-a[1], L = Math.hypot(dx, dy), nx = -dy/L, ny = dx/L, hw = c[2]*scale*0.5 + 2, ex = dx/L*hw, ey = dy/L*hw;
    var e = [a[0] + dx*tt, a[1] + dy*tt];
    ctx.beginPath(); ctx.moveTo(a[0] + nx*hw - ex, a[1] + ny*hw - ey); ctx.lineTo(e[0] + nx*hw, e[1] + ny*hw); ctx.lineTo(e[0] - nx*hw, e[1] - ny*hw); ctx.lineTo(a[0] - nx*hw - ex, a[1] - ny*hw - ey); ctx.closePath(); ctx.clip();
  }
  function frame(now){
    var dt = Math.min(0.05, (now - last)/1000); last = now; t += dt;
    if (!visible){ requestAnimationFrame(frame); return; }
    if (started && !hold) p = Math.min(0.9, (t - t0)*0.25);
    ctx.globalCompositeOperation = 'source-over';
    ctx.drawImage(field, 0, 0, W, H);
    var reveal = [Math.max(0, Math.min(1, (p - 0.06)/0.3)), Math.max(0, Math.min(1, (p - 0.36)/0.16)), Math.max(0, Math.min(1, (p - 0.52)/0.18))];
    for (var i = 0; i < 3; i++){ if (reveal[i] <= 0) continue; ctx.save(); clipChannel(channels[i], reveal[i]); ctx.drawImage(stub, 0, 0, W, H); ctx.restore(); }
    // wind: a soft band of light crossing the field, and a slow breathing of the dusk light
    var wx = ((t*0.07) % 1.4) - 0.2;
    var wg = ctx.createLinearGradient(W*(wx - 0.25), 0, W*(wx + 0.25), H*0.6); wg.addColorStop(0, 'rgba(239,163,124,0)'); wg.addColorStop(0.5, 'rgba(239,163,124,' + (0.10 + 0.03*Math.sin(t*0.9)).toFixed(3) + ')'); wg.addColorStop(1, 'rgba(239,163,124,0)');
    ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = wg; ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'source-over';
    var lg = ctx.createRadialGradient(W*0.86, H*0.1, 0, W*0.86, H*0.1, Math.max(W, H)*0.9); lg.addColorStop(0, 'rgba(223,142,99,.16)'); lg.addColorStop(0.45, 'rgba(223,142,99,.03)'); lg.addColorStop(1, 'rgba(14,17,20,.55)');
    ctx.fillStyle = lg; ctx.fillRect(0, 0, W, H);
    // the veil that keeps the words readable
    var narrow = W < 900;
    var vg = narrow ? ctx.createLinearGradient(0, H*0.35, 0, H*0.9) : ctx.createLinearGradient(0, 0, W*0.62, 0);
    vg.addColorStop(0, narrow ? 'rgba(14,17,20,0)' : 'rgba(14,17,20,.94)'); vg.addColorStop(narrow ? 0.5 : 0.55, narrow ? 'rgba(14,17,20,.85)' : 'rgba(14,17,20,.6)'); vg.addColorStop(1, narrow ? 'rgba(14,17,20,.94)' : 'rgba(14,17,20,0)');
    ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  var started = false, hold = false, t0 = 0;
  function look(){ var r = canvas.getBoundingClientRect(); visible = r.bottom > 0 && r.top < window.innerHeight; if (!started && r.top < window.innerHeight*0.72){ started = true; t0 = t; } }
  window.addEventListener('scroll', look, {passive: true}); window.addEventListener('resize', look); look(); setTimeout(look, 400);
  if (reduce || window.innerWidth < 900){ hold = true; p = 0.9; }
})();
"""

# ambient layers
# the rune page carries no ambient wash outside the hero canvas; the halo there is the one resting light
AMBIENT_RUNE = dict(markup='', css='', js='')

AMBIENT_HARVEST = dict(
    markup='<div class="ambient grain" aria-hidden="true"></div><div class="ambient warm" aria-hidden="true"></div>',
    css=('.ambient{position:fixed;inset:0;z-index:0;pointer-events:none}'
         '.ambient.grain{opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'220\' height=\'220\'><filter id=\'n\'><feTurbulence type=\'fractalNoise\' baseFrequency=\'.9\' numOctaves=\'2\' stitchTiles=\'stitch\'/><feColorMatrix values=\'0 0 0 0 1 0 0 0 0 .8 0 0 0 0 .6 0 0 0 .9 0\'/></filter><rect width=\'100%\' height=\'100%\' filter=\'url(%23n)\'/></svg>");mix-blend-mode:screen}'
         '.ambient.warm{background:radial-gradient(60% 50% at 80% 20%,rgba(223,142,99,.08),transparent 70%);animation:warm 18s ease-in-out infinite alternate}'
         '@keyframes warm{to{transform:translate(-8%,12%) scale(1.15)}}'
         '.sheen{position:absolute;inset:0;pointer-events:none;background:linear-gradient(100deg,transparent 30%,rgba(239,163,124,.08) 50%,transparent 70%);background-size:300% 100%;animation:sheen 9s linear infinite;mix-blend-mode:screen}'
         '@keyframes sheen{from{background-position:120% 0}to{background-position:-120% 0}}'
         '@media (prefers-reduced-motion:reduce){.ambient.warm,.sheen{animation:none}}'),
    js='')


SITE = "https://felag.net/"
COMPANY_PAGES = ["https://www.linkedin.com/company/felagnet/", "https://github.com/felagnet", "https://x.com/felagnet"]


def _offer(o, price=None, spec=None):
    d = {"@type": "Offer", "name": o["name"], "description": o["body"], "priceCurrency": "USD"}
    if price is not None:
        d["price"] = price
    if spec:
        d["priceSpecification"] = dict({"@type": "PriceSpecification", "priceCurrency": "USD", "valueAddedTaxIncluded": False}, **spec)
    d["itemOffered"] = {"@type": "Service", "name": o["name"], "provider": {"@id": SITE + "#org"}}
    return d


def ld_json(title, description):
    """The structured data, built from the same constants as the visible copy so it cannot drift from the page.
    No headcount, no address or country, no relation to Gateway.fm beyond the verbatim bios."""
    people_ids = ["andrew", "mike", "pavel", "andrey"]
    homes = {"Andrew Skurlatov": "Netherlands", "Mikhail Manko": "Cyprus"}
    persons = []
    for pid, p in zip(people_ids, PEOPLE):
        d = {"@type": "Person", "@id": SITE + "#" + pid, "name": p["name"], "jobTitle": p["role"],
             "worksFor": {"@id": SITE + "#org"}, "image": SITE + "people/" + pid + ".jpg"}
        if p["name"] in homes:
            d["homeLocation"] = {"@type": "Place", "name": homes[p["name"]]}
        d["description"] = p["bio"]
        d["sameAs"] = [u for _, u in p["links"]]
        persons.append(d)
    # the Fractional CTO minPrice waits on the owner's decision about the price on the page, so that offer carries no figure
    offers = [
        _offer(OFFERS[0], price="0"),
        _offer(OFFERS[1], spec={"minPrice": 10000, "description": "from $10k"}),
        _offer(OFFERS[2], spec={"description": OFFERS[2]["price"] + ", " + OFFERS[2]["note"]}),
        _offer(OFFERS[3], spec={"minPrice": 10000, "maxPrice": 60000, "description": "$10k to $60k a month, by size"}),
        _offer(OFFERS[4], spec={"description": "Quote per scope, fixed price, half paid on start, report in one to two weeks"}),
    ]
    org = {"@type": "Organization", "@id": SITE + "#org", "name": "Felag", "url": SITE,
           "logo": {"@type": "ImageObject", "url": SITE + "apple-touch-icon.png", "width": 180, "height": 180},
           "image": SITE + "og.png",
           "slogan": "Senior engineers who own the architecture and ship to production.",
           "description": STATEMENT + " Felag is the 2026 restart of Uddug, acquired in 2024.",
           "foundingDate": "2026-07", "email": "info@felag.net",
           "contactPoint": {"@type": "ContactPoint", "email": "info@felag.net", "contactType": "sales", "availableLanguage": "en"},
           "sameAs": COMPANY_PAGES,
           "founder": [{"@id": SITE + "#andrew"}, {"@id": SITE + "#mike"}],
           "knowsAbout": ["Backend and infrastructure at scale", "Payments rails", "Identity and SSO", "Distributed ledgers"],
           "makesOffer": offers}
    graph = [org,
             {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Felag", "inLanguage": "en", "publisher": {"@id": SITE + "#org"}},
             {"@type": "WebPage", "@id": SITE + "#page", "url": SITE, "name": title, "description": description, "inLanguage": "en",
              "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#org"},
              "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "og.png", "width": 1200, "height": 630}},
             *persons,
             {"@type": "FAQPage", "@id": SITE + "#faq",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    data = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def full_page(theme, title, description_line, headline, sub, scene_markup, scene_script, extra_css="", scripts_before=""):
    t = THEMES[theme]
    amb = AMBIENT_RUNE if theme == "rune" else AMBIENT_HARVEST
    words = " ".join(f'<span class="w">{w}</span>' for w in STATEMENT.split(" "))
    hero_statement = (f'<div class="wrap hero-statement" id="hero-statement" data-scrub="statement"><p class="eyebrow">{t["statement_eyebrow"]}</p>'
                      f'<p class="statement" id="statement-text">{words}</p></div>') if theme == "rune" else ""
    book_js = BOOK_RUNE_JS if theme == "rune" else BOOK_HARVEST_JS
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{DESCRIPTION}">
<link rel="canonical" href="https://felag.net/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Felag">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:url" content="https://felag.net/">
<meta property="og:image" content="https://felag.net/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Felagnet">
<meta property="og:locale" content="en_GB">
<meta property="og:image:alt" content="The Felag mark beside the line Senior engineers who own the architecture and ship to production.">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{DESCRIPTION}">
<meta name="twitter:image" content="https://felag.net/og.png">
<meta name="theme-color" content="#0E1114">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{ld_json(title, DESCRIPTION)}</script>
{FONT_LINKS}
<style>{CSS}{SITE_CSS}{amb["css"]}{extra_css}</style>
</head>
<body>
<div class="theme-{theme}{" mark-pending" if theme == "rune" else ""}" id="root">
{amb["markup"]}
{header()}
<main id="main">
<section class="hero" id="top">
  <div class="hero-pin">
    {scene_markup}
    <div class="wrap hero-inner">
      <h1 class="rise r1">{headline}</h1>
      <p class="sub rise r2">{sub}</p>
      <div class="cta rise r3"><a class="btn" href="mailto:info@felag.net?subject=Free%20technical%20workshop">Write to us</a><a class="textlink" href="#offer">See prices</a></div>
    </div>
    {hero_statement}
  </div>
</section>
{sections(t, theme)}
</main>
</div>
{scripts_before}
<script>
{COMMON_JS}
{scene_script}
{SITE_JS}
{book_js}
{amb["js"]}
</script>
</body>
</html>
'''

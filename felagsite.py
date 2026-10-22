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

STATEMENT = ("Felag is a boutique, principal-led software engineering studio for technology companies. Our pods own the architecture "
             "and delivery of platforms, distributed systems, AI infrastructure, payments and identity.")
# the search snippet: who we serve, what we build and how we price, as Andrew chose it on 21 October 2026, 157 characters
DESCRIPTION = ("Principal-led software engineering studio for technology companies. Platforms, distributed systems, AI infrastructure "
               "and fractional CTO, priced on outcomes.")

# the four things we build, one per piece of the mark: the bar, then the three pieces on the right, the small one last
CAPS = [
    dict(piece=0, name="Backends and infrastructure", line="We build production backends, distributed systems and their cloud infrastructure, including model serving, GPU autoscaling and agent runtimes for AI products. When an existing system struggles under load, we identify the bottleneck before proposing changes."),
    dict(piece=3, name="Payment rails", line="We build account ledgers, settlement services and card integrations with banks, issuers and processors. The scope includes transaction records and audit trails."),
    dict(piece=2, name="Identity and access", line="We integrate enterprise sign-on and build account and permission systems for people and software agents."),
    dict(piece=1, name="Distributed ledgers", line="We build systems that share and verify records across organisations. The Architecture Sprint establishes where a shared ledger is useful and where a conventional database is sufficient."),
]

SKILLS = ("Go, Rust, Node.js/TypeScript, Python, Solidity; React/Next.js, Vue/Nuxt, React Native/Expo, Flutter; AWS, GCP, Kubernetes, "
          "Terraform, GPU scheduling on Kubernetes, vLLM; EVM (Ethereum, L2s, Polygon CDK), Substrate/Polkadot, Solana, Cosmos, Canton/Daml, Stellar, Bitcoin/Lightning, TON; "
          "Postgres, Redis, ScyllaDB/Cassandra, ClickHouse, Kafka, NATS, RabbitMQ, gRPC, GraphQL, REST, websockets, The Graph and custom indexers.")

L2B = "https://l2beat.com/layer2s/projects/wirex"
WIREX_PR = "https://gateway.fm/blog/gateway-wirex-partnership/"
GW_CASE = "https://gateway.fm/case-studies/agentic-identity-chain-infrastructure/"

A_NAMED = "We delivered the Wirex Pay platform end to end: an L2 chain that launched in August 2024, and the application layer, indexer, oracles and account abstraction behind its non-custodial debit cards, built for MiCA alignment."
B_NAMED = "We designed the RPC proxy that served Opera and 1inch in production, with a cache layer and rate limiting, at 140k+ requests per second at peak and 50 ms average latency on the heavy requests."
C_LINE = "We built the event infrastructure and backend API behind Infinex's Synthetix PerpsV3 integration, under Infinex proposal XIP-9."
XIP9 = "https://proposals.infinex.xyz/xips/xip-9"
F_NAMED = "We built the application layer for Humanity Protocol, an identity network with 9M+ users."
G_NAMED = "We ran Gateway Yield, the staking infrastructure for Lido, Gnosis, Stellar and Canton. In late 2025 it held $1B+ locked in staking."
H_NAMED = "We built a shared prover used across several ZK protocols and L2 ecosystems, including EY Nightfall, Polygon zkEVM, Miden and Iden3, with GPU and CPU autoscaling on AWS spot capacity."
DN_LINE = "Andrew served as fractional CTO to DeepNode for ten months, designing its decentralised AI infrastructure and leading it through the January 2026 token launch and exchange listing. The network handled about 5,000 requests per second at peak, and the token listed at $140M+ fully diluted valuation."
KUCOIN = "https://www.kucoin.com/announcement/en-deepnode-dn-gets-listed-on-kucoin-world-premiere"
DN_CMC = "https://coinmarketcap.com/currencies/deepnode/"
CANTON_CIP = "https://lists.sync.global/g/cip-discuss/topic/cip_tbd_canton_evm/116639522"
NEAR_OCC = "https://legacy.near.social/infrastructure-committee.near/widget/app?page=proposal&id=68"
J_LINE = "We built an EVM event-indexing code-generation platform that became the standard across most of the company's projects."
K_LINE = "We led the Presto tokenised-finance product to revenue and built its stablecoin, RWA, DEX and payments blueprints."
O_LINE = "Uddug built the technology behind the OG:Crystals launch end to end, in collaboration with Snark.art."
P_LINE = "Uddug helped with the launch of Marscatsvoyage."
R_LINE = "Uddug took on grant work for Web3 Foundation and Protocol Labs, including JuniDB, an IPFS-backed data layer for Substrate."
Y_LINE = "Uddug built the smart contracts for Metazoku in 2023."

# the ten cases, one structure each: a stage and date label, the contribution, then only the facts that add to it (a result, the team,
# attributed context), a disclosure named for what it holds, the public record and the employer and date; no person is named, and no
# field is filled for its own sake
PROOF_CARDS = [
    dict(kicker="Launched August 2024", title="Wirex Pay", links=[("L2BEAT listing", L2B), ("Partnership announcement", WIREX_PR)], era="Gateway.fm, 2024",
         body="We delivered the Wirex Pay platform end to end: the L2 chain, and the application layer, indexer, oracles and account abstraction behind its non-custodial debit cards.",
         facts=[("Context", "The chain was listed on L2BEAT, the public register of Ethereum layer-2 chains.")],
         dlabel="Sources and evidence",
         details="The engineering was built to support Wirex's MiCA alignment; we have not taken the system through an audit under MiCA."),
    dict(kicker="In production, 2021 to 2022", title="The RPC proxy for Opera and 1inch", links=[], era="Gateway.fm, 2021 to 2022",
         body="We designed the RPC proxy that served Opera and 1inch in production, with a cache layer and rate limiting.",
         facts=[("Result", "140k+ requests per second at peak, with 50 ms average latency on the heavy requests.")],
         dlabel="Measurement notes",
         details="Both figures are the peak observed in production, aggregate across all clients of the proxy, during 2021 to 2022. The latency is the average over the heavy requests only."),
    dict(kicker="Proof of concept, 2025", title="Identity for a global technology company", links=[("Case study, by the team at Gateway.fm", GW_CASE)], era="Gateway.fm, 2025",
         body="Two workstreams for one client. We designed and built account-abstraction wallets that people open with their company's single sign-on, and an identity system for AI agents on a major cloud platform.",
         facts=[],
         dlabel="Sources and evidence",
         details="The linked case study is published by Gateway.fm and covers the agent identity workstream only."),
    dict(kicker="Delivered, 2023 to 2024", title="Infinex and Synthetix", links=[("XIP-9 on Infinex Proposals", XIP9)], era="Uddug with Gateway.fm, 2023 to 2024",
         body="We built the backend API behind Infinex's Synthetix PerpsV3 integration. It takes in the PerpsV3 contract events and serves market data, order events and trading history to the app over REST and WebSocket.",
         facts=[("Context", "The scope was set by Infinex proposal XIP-9, Synthetix PerpsV3 API, approved in December 2023.")],
         dlabel="", details=""),
    dict(kicker="Identity network, application layer", title="Humanity Protocol", links=[], era="Gateway.fm, 2024 to 2025",
         body="We built the application layer for Humanity Protocol, an identity network.",
         facts=[("Result", "A high-load application layer on the L2 chain, at about 1,000 transactions per second."),
                ("Context", "9M+ users, as reported by Humanity Protocol.")],
         dlabel="Measurement notes",
         details="The transaction rate is the peak observed in production, aggregate across the chain, during 2024 to 2025."),
    dict(kicker="In use, 2024 to 2025", title="A shared prover for EY Nightfall, Polygon, Miden and Iden3", links=[], era="Gateway.fm, 2024 to 2025",
         body="We built one shared prover for several ZK protocols and L2 ecosystems, with GPU and CPU capacity autoscaling on AWS spot instances.",
         facts=[],
         dlabel="Technical scope",
         details="The protocols served were Polygon zkEVM, Polygon Hermez, cdk-erigon, Miden and Iden3, including EY Nightfall."),
    dict(kicker="Engineering leadership, 2024 to 2026", title="The Gateway.fm Platform department", links=[], era="Gateway.fm, 2024 to 2026",
         body="The founders led Gateway.fm's Platform department and a second engineering department, accountable for the architecture and the delivery of their products.",
         facts=[("Team", "~25 people across the two departments."),
                ("Projects", "Wirex Pay, Humanity Protocol, the shared prover, the oracles and Gateway Yield.")],
         dlabel="Project background",
         details="Uddug had grown to 15 people when it was acquired in June 2024, and the team joined Gateway.fm as its Platform department."),
    dict(kicker="Fractional CTO, ten months", title="DeepNode", links=[("KuCoin listing announcement", KUCOIN), ("DN on CoinMarketCap", DN_CMC)], era="Independent engagement, 2025 to 2026",
         body="Ten months as DeepNode's fractional CTO, designing its decentralised AI infrastructure through the January 2026 token launch and exchange listing.",
         facts=[("Result", "The network handled about 5,000 requests per second at peak."),
                ("Context", "The token listed in January 2026 at $140M+ fully diluted valuation.")],
         dlabel="Measurement notes",
         details="The request rate is the peak observed in production, aggregate across the network, during the engagement."),
    dict(kicker="NFT platform, from 2022", title="Arsnl.art", links=[("arsnl.art", "https://arsnl.art")], era="Uddug, from 2022",
         body="Uddug built the whole NFT platform behind Arsnl.art and the NFT launches on it.",
         facts=[("Result", "Frank Stella's 'Geometries' released on the platform.")],
         dlabel="", details=""),
    dict(kicker="Exchange prototype, 2017 to 2018", title="ICEX", links=[], era="The founders, before Uddug",
         body="The founders' own exchange, built with a team of 25.",
         facts=[("Result", "We first developed the push oracle for ICEX, then deployed it for Wirex Pay, Infinex, LUKSO and Lumia.")],
         dlabel="Project background",
         details="The exchange was roughly 70 percent built when the investor withdrew in the 2018 crypto winter, and the project ended there."),
]

# the names wall: every name the register and the history allow, each with a short relationship line and, where it has one, the number of its case,
# which the line links to by name
WALL = [
    ("Wirex Pay", "client", "Client for the payments platform and its L2 chain.", [("L2BEAT listing", L2B), ("Partnership announcement", WIREX_PR)], "Gateway.fm, 2024", 1),
    ("Opera", "client", "Ran on the RPC proxy we designed.", [], "Gateway.fm, 2021 to 2022", 2),
    ("1inch", "client", "Ran on the RPC proxy we designed.", [], "Gateway.fm, 2021 to 2022", 2),
    ("Infinex", "client", "Client for the event infrastructure and backend.", [], "Uddug with Gateway.fm, 2023 to 2024", 4),
    ("Humanity Protocol", "client", "Client for the application layer.", [], "Gateway.fm, 2024 to 2025", 5),
    ("DeepNode", "client", "A fractional CTO engagement.", [("KuCoin listing announcement", KUCOIN)], "Independent engagement, 2025 to 2026", 8),
    ("EY Nightfall", "client", "Served by the shared prover.", [], "Gateway.fm, 2024 to 2025", 6),
    ("LUKSO", "client", "Received the push oracle we designed.", [], "Gateway.fm, 2023 to 2025", None),
    ("Lumia", "client", "Received the push oracle we designed.", [], "Gateway.fm, 2023 to 2025", None),
    ("ApeChain", "client", "A pull-based price feed and a verifiable-randomness oracle.", [], "Gateway.fm, 2023 to 2025", None),
    ("Presto", "client", "The tokenised-finance product we led to revenue.", [], "Gateway.fm, 2023 to 2025", None),
    ("Gnosis", "client", "Ran on the RPC proxy, and served by Gateway Yield.", [], "Gateway.fm", None),
    ("Ethereum Foundation", "client", "Ran on the RPC proxy we designed.", [], "Gateway.fm, 2021 to 2022", None),
    ("Web3 Foundation", "client", "Grant work, including JuniDB.", [], "Uddug, 2020 to 2023", None),
    ("Protocol Labs", "client", "Grant work.", [], "Uddug, 2020 to 2023", None),
    ("OG:Crystals", "client", "The technology behind the launch, with Snark.art.", [], "Uddug, 2021", None),
    ("Marscatsvoyage", "client", "Uddug helped with the launch.", [], "Uddug, 2021", None),
    ("Arsnl.art", "client", "The NFT platform and its launches.", [("arsnl.art", "https://arsnl.art")], "Uddug, from 2022", 9),
    ("Metazoku", "client", "Smart contracts.", [], "Uddug, 2023", None),
    ("Snark.art", "client", "An NFT launch platform for established artists, later a Uddug client.", [("snark.art", "https://snark.art")], "2019 to 2020, then Uddug", None),
    ("Synthetix", "protocol", "The protocol behind Infinex.", [], "Uddug with Gateway.fm, 2023 to 2024", 4),
    ("Lido", "protocol", "Served by Gateway Yield, the staking infrastructure we ran.", [], "Gateway.fm, 2025 to 2026", None),
    ("Stellar", "protocol", "Served by Gateway Yield, the staking infrastructure we ran.", [], "Gateway.fm, 2025 to 2026", None),
    ("Canton", "protocol", "Served by Gateway Yield, the staking infrastructure we ran.", [], "Gateway.fm, 2025 to 2026", None),
    ("Polygon zkEVM", "protocol", "Served by the shared prover.", [], "Gateway.fm, 2024 to 2025", 6),
    ("Miden", "protocol", "Served by the shared prover.", [], "Gateway.fm, 2024 to 2025", 6),
    ("Iden3", "protocol", "Served by the shared prover.", [], "Gateway.fm, 2024 to 2025", 6),
]
# how a wall line names the case it links to
CASE_REFS = {1: "the Wirex Pay case", 2: "the RPC proxy case", 4: "the Infinex integration case", 5: "the Humanity Protocol case",
             6: "the shared-prover case", 8: "the fractional CTO case", 9: "the Arsnl.art case",
             3: "the identity case", 10: "the ICEX case"}

# the record: a short lineage in the reading path, and the full history behind a disclosure, era by era with every project in it;
# a project with a case card carries the number of its case, and its row links to the card
LINEAGE = [
    ("2014", "Andrew builds and runs a crypto micropayment system and a network of faucets."),
    ("2015", "Andrew Skurlatov and Mikhail Manko start working together and launch YourAdsMedia, a crypto ad network."),
    ("2017", "The founders start ICEX, their own exchange, where the push oracle is first developed."),
    ("2018", "The founders start Uddug on the ICEX core team."),
    ("2019", "Andrew becomes technical lead and CTO of Snark.art, an NFT launch platform that later becomes a Uddug client."),
    ("2021", "Andrew joins Gateway.fm as one of its first engineers."),
    ("June 2024", "Uddug is acquired, and the team becomes Gateway.fm's Platform department."),
    ("2026", "The departments close and the team leaves."),
    ("July 2026", "Felag starts as the restart of Uddug, with Pavel Dodonov and Andrey Solovov as principal engineers and partners."),
]
ERAS = [
    dict(name="Before Uddug", years="2014 to 2018",
         intro="Andrew and Mikhail met in Limassol in 2014 and have built companies together since 2015.",
         cases=[
             ("2014 to 2015", "Crypto micropayments and a faucet network", "Andrew designed, built and ran a micropayment system and a network of faucets for Bitcoin, Litecoin and Dogecoin, earning about $10k a month at its peak.", [], None),
             ("2015 to 2017", "YourAdsMedia", "The founders' crypto ad network, product and platform built by Andrew and Mikhail.", [], None),
             ("2017 to 2018", "ICEX", "The founders' own exchange, with a team of 25. It was roughly 70 percent built when the investor withdrew in the 2018 crypto winter. The push oracle first developed for it later shipped for Wirex Pay, Infinex, LUKSO and Lumia.", [], 10),
         ]),
    dict(name="Uddug", years="2018 to 2024",
         intro="Andrew Skurlatov and Mikhail Manko founded Uddug in 2018 on the ICEX core team, and it grew to 15 people. NFT launches by the team collectively raised $100M+.",
         cases=[
             ("2019 to 2020", "Snark.art", "Andrew was technical lead and CTO of Snark.art, an NFT launch platform for established artists, with a team of five. Snark.art later became a Uddug client.", [("snark.art", "https://snark.art")], None),
             ("2019", "Kitec", "Andrew was lead backend engineer at Kitec, building Go microservices with gRPC, message queues and WebSockets.", [], None),
             ("2020 to 2021", "Kickstox", "Andrew was lead developer of the high-load backend behind Kickstox, a fantasy sports platform.", [], None),
             ("2020 to 2023", "Web3 Foundation and Protocol Labs", R_LINE, [], None),
             ("2021", "OG:Crystals", O_LINE, [], None),
             ("2021", "Marscatsvoyage", P_LINE, [], None),
             ("From 2022", "Arsnl.art", "Uddug built the whole NFT platform and handled the technical delivery of several artist drops on it, including Frank Stella's 'Geometries'.", [("arsnl.art", "https://arsnl.art")], 9),
             ("2023", "Metazoku", Y_LINE, [], None),
             ("2023 to 2024", "Infinex, with Gateway.fm", C_LINE, [("XIP-9 on Infinex Proposals", XIP9)], 4),
             ("2024", "Pandoshi", "Uddug built a mobile wallet for Pandoshi, as a consulting partner of Gateway.fm.", [], None),
         ]),
    dict(name="Gateway.fm", years="2021 to 2026",
         intro="Andrew joined Gateway.fm in 2021 as one of its first engineers. In June 2024 Uddug was acquired and the team became Gateway.fm's Platform department; the founders ran ~25 people across two departments. In 2026 the departments closed and we left.",
         cases=[
             ("2021 to 2022", "The RPC proxy for Opera and 1inch", "A cache layer and rate limiting at 140k+ requests per second at peak, with 50 ms average latency on the heavy requests.", [], 2),
             ("2023", "The backend at scale", "Andrew led backend engineering as Head of Backend, ~15 people, on a backend serving 100K+ requests per second at peak.", [], None),
             ("2023 to 2025", "Presto and its fintech app kits", K_LINE, [], None),
             ("2023 to 2025", "The indexing platform", J_LINE, [], None),
             ("2023 to 2025", "Oracles", "A push oracle with multi-asset prices every 500 ms for Wirex Pay, Infinex, LUKSO and Lumia; a pull feed at about 1,000 requests per second and verifiable randomness for ApeChain. The figures are the peak observed in production, aggregate across clients, during 2023 to 2025.", [], None),
             ("2024", "Wirex Pay", "The L2 chain, launched in August 2024, and the application layer, indexer, oracles and account abstraction behind its non-custodial debit cards.", [("L2BEAT listing", L2B), ("Partnership announcement", WIREX_PR)], 1),
             ("2024 to 2025", "Humanity Protocol", F_NAMED, [], 5),
             ("2024 to 2025", "The shared prover", H_NAMED, [], 6),
             ("2024 to 2025", "OneClick Connect on NEAR", "Multichain sign-in for NEAR apps, deployed for SWEAT Economy and Metapool.", [("Proposal to the NEAR Infrastructure Committee", NEAR_OCC)], None),
             ("2025", "Identity for a global technology company", "Account-abstraction wallets with enterprise single sign-on, and an identity system for AI agents on a major cloud platform, both proofs of concept.", [("Case study, by the team at Gateway.fm", GW_CASE)], 3),
             ("2025 to 2026", "DeepNode, Andrew's fractional CTO engagement", "Ten months designing DeepNode's decentralised AI infrastructure and leading it through the January 2026 token launch and exchange listing. The network handled about 5,000 requests per second at peak, and the token listed at $140M+ fully diluted valuation.", [("KuCoin listing announcement", KUCOIN), ("DN on CoinMarketCap", DN_CMC)], 8),
             ("December 2025", "EVM compatibility for Canton", "Andrew presented a proposal for EVM compatibility on the Canton Network to its super-validators.", [("The draft CIP on cip-discuss", CANTON_CIP)], None),
             ("2025 to 2026", "Gateway Yield", G_NAMED, [], None),
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
         body="A principal in the CTO seat for agreed days each week, spread across Monday to Friday, until a full-time hire makes sense. The CTO owns the architecture and the engineering roadmap, runs engineering process and delivery with your team, and represents the technology to the board and investors.",
         what=["Agreed days each week, spread across Monday to Friday", "The architecture and the engineering roadmap", "Engineering process and delivery with your team", "The technology represented to the board and investors"], terms=["Monthly in advance", "One-month initial term"], who="Andrew, Pavel or Andrey, never a contractor"),
    dict(name="Pods", price="$10k to $60k a month", note="by team",
         body="The build after the sprint, on a monthly retainer with deliverables agreed each month in the SOW, and a team sized to the scope.",
         what=["From $10k: one senior engineer who plans the work with your team, with a principal reviewing the plan and the architecture weekly", "From $25k: a principal part time with one or two senior engineers", "Up to $60k: a principal full time leading two to three engineers"],
         terms=["Monthly in advance", "Deliverables agreed each month in the SOW", "A missed deliverable triggers a scope and plan review, recorded in writing", "Cancel with two weeks' notice", "Fees for the unused part of a prepaid month refunded pro rata after the notice period"], who="A principal, with senior and specialist engineers as the scope needs"),
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
    ("Build", "The build, led by a principal.", "A pod with deliverables agreed each month, or a fixed-price build."),
]
HOW_NOTE = "Fractional CTO work and due diligence start from the same workshop and go straight to a scoped proposal."

WHO = [
    ("A post-raise CTO with a hard integration and no senior hire in time", "The Series A or B roadmap has an integration nobody on the team has shipped before, and the senior hire will not land in time. We take the integration as a defined outcome and hand it back documented."),
    ("A funded technology company with a performance, scale or reliability problem", "The product works until it is busy. We measure the problem first, then fix the cause, and we say so when the answer is a smaller change than the team expected."),
    ("A regulated payments or asset issuer rebuilding for a new regime", "MiCA, DORA, the UK regime, GENIUS, VARA, HKMA or MAS has changed what the system must record and prove, and the team needs engineers who have built for one of these regimes before."),
    ("A licensed fintech taking over a codebase from a previous vendor", "The codebase arrived without the people who wrote it. We audit what is there, keep what works, and take ownership of the rest."),
    ("A founder with a co-founder gap", "The company needs a CTO for one or two days a week to own the architecture, the roadmap and delivery with the team until a full-time hire makes sense."),
    ("A product agency without a senior backend bench", "The agency has the design and the client, and needs a principal behind the backend for the length of the engagement without building that bench itself."),
]
TURN_DOWN = "Hourly billing, a dedicated eight-person team as a product, and public-sector tenders scored on headcount."

PEOPLE = [
    dict(ini="AS", name="Andrew Skurlatov", role="Co-founder and CTO", where="Based in the Netherlands", alt="Andrew Skurlatov, co-founder and CTO of Felag",
         bio="Andrew sets Felag's technical direction, leads the architecture on its engagements and steps in as fractional CTO. He has spent 15 years in software, ten of them in blockchain. He co-founded Uddug in 2018 and, after it was acquired, ran ~25 people across two departments as VP of Platform and Yield.",
         links=[("andskur.com", "https://andskur.com"), ("LinkedIn", "https://linkedin.com/in/andrew-skurlatov"), ("GitHub", "https://github.com/andskur"), ("X", "https://x.com/Andskur1")], seed=3, photo=_photo("andrew")),
    dict(ini="MM", name="Mikhail Manko", role="Co-founder and CEO", where="Based in Cyprus", alt="Mikhail Manko, co-founder and CEO of Felag",
         bio="Mikhail looks after partnerships and deals at Felag, from the first call to the signed contract. He has spent 13 years running teams, products and operations. He co-founded Uddug with Andrew in 2018, saw it through its acquisition, and then headed the platform team for Gateway.fm's tokenised-finance product.",
         links=[("LinkedIn", "https://www.linkedin.com/in/mikhail-manko/")], seed=7, photo=_photo("mike")),
    dict(ini="PD", name="Pavel Dodonov", role="Principal Engineer, partner", where="Based in Serbia", alt="Pavel Dodonov, Principal Engineer at Felag",
         bio="Pavel leads engineering on Felag's engagements. He came to software after a decade of scientific R&D and 20+ published papers. In nearly four years at Gateway.fm he went from Go backend engineer to Backend Lead, and led the architecture of the shared prover that several ZK networks ran on.",
         links=[("LinkedIn", "https://www.linkedin.com/in/paveldodonov/"), ("GitHub", "https://github.com/Pashteto")], seed=11, photo=_photo("pavel")),
    dict(ini="AS", name="Andrey Solovov", role="Principal Engineer, partner", where="Based in Finland", alt="Andrey Solovov, Principal Engineer at Felag",
         bio="Andrey leads delivery on Felag's engagements. He started at Uddug, building smart contracts and payments architecture. At Gateway.fm he spent more than two years as Blockchain Dev Lead, shipping production systems for DeFi, oracle, L2 and identity clients, from the contracts down to the services behind them.",
         links=[("LinkedIn", "https://www.linkedin.com/in/andrey-solovov-bb665884/"), ("GitHub", "https://github.com/asolovov")], seed=5, photo=_photo("andrey")),
]
PEOPLE_NOTE = "We bring in specialist contractors when a project needs them, always led by one of us."

# the contracting counterparty, as Andrew gave it on 19 October 2026: the footer and the contract answer
# the registration number and the office as parts, so the structured data reads the same facts as the footer
ENTITY_ID = "426561829"
ENTITY_OFFICE = dict(addressRegion="Gardabani Municipality", addressLocality="Poladaant Kari Village", streetAddress="4th Street, Lane II, N 11")
ENTITY = (f"FELAG LLC, a Georgian limited liability company with identification number {ENTITY_ID} and registered office at "
          f"Georgia, {ENTITY_OFFICE['addressRegion']}, {ENTITY_OFFICE['addressLocality']}, {ENTITY_OFFICE['streetAddress']}")

CONTRACT = [
    ("Legal entity", ENTITY + "."),
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
    ("Who actually works on our system?", "One of the people above leads every engagement and is identified in the SOW. Contractors join for QA, DevOps and additional development when the scope needs them, always led by one of us."),
    ("How do we start?", "With a free technical workshop with a founder. For a build, the next step is a paid Architecture Sprint. Fractional CTO work and technical due diligence go straight to a scoped proposal."),
    ("What do we keep if we stop after the sprint?", "The spec, the architecture decisions, the risk register and the costed build options are yours. The sprint is paid in advance and credited in full against a pod or fixed-price build signed within 30 days of its delivery."),
    ("Where are you based and who do we contract with?", "The contract is with " + ENTITY + ". The founders work from the Netherlands and Cyprus."),
    ("How are deliverables accepted and scope changes agreed?", "<strong>Monthly pods:</strong> We review and accept deliverables with you each month against the SOW. Scope changes agreed at that review go into the next month's SOW.\n\n"
     "<strong>Architecture Sprints and technical due diligence:</strong> A principal presents the output at delivery. You have five business days to accept it or send a written list of gaps.\n\n"
     "<strong>Fixed-price builds:</strong> We review each milestone against criteria agreed in the Architecture Sprint. You have five business days after each demo to accept it or send a written list of gaps.\n\n"
     "For sprints, due diligence and fixed-price milestones, the deliverable is accepted if we receive no written list of gaps within the review period.\n\n"
     "<strong>Changes to fixed-price scope:</strong> We agree changes in writing before starting the work, including a fixed quote for their effect on price and timing."),
    ("Do you work with regulated companies?", "Yes. We built the Wirex Pay platform and the application layer behind its debit card programme, engineering that supported the client's MiCA alignment. We have not taken a system through an audit under MiCA, and we say so before a sprint starts."),
    ("Do you use AI in delivery?", "Yes. We use AI tools and our own development framework. A principal reviews the work and remains responsible for the agreed deliverables."),
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
      <a class="btn btn-sm" href="#contact">Discuss your project</a>
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
.sec h2.huge,.huge{font-size:var(--fs-display);line-height:.95;font-weight:600;letter-spacing:-0.035em;max-width:11ch;text-wrap:balance;overflow-wrap:break-word}
/* the two index sections, names and record, are lists, not statements: their headlines take the subhead role */
#names h2,#record h2,#faq h2{font-size:var(--fs-subhead);line-height:1;letter-spacing:-0.03em;max-width:20ch}
.lead{font-size:var(--fs-lead);line-height:1.45;color:var(--text-secondary);max-width:34em;margin-top:24px}
.eyebrow{font-size:12px;line-height:20px;letter-spacing:.06em;color:var(--text-secondary);margin-bottom:20px}
.rule{height:1px;background:linear-gradient(90deg,var(--accent) 0,var(--accent) var(--w,0%),var(--line) var(--w,0%),var(--line) 100%);transition:none}

/* ---- rune theme: the rune lands in the header, fire on titles and numbers */
.theme-rune .hero{height:calc(100vh + 1250px);min-height:1950px}
.hero-statement{position:absolute;left:0;right:0;top:0;bottom:0;z-index:2;display:flex;flex-direction:column;justify-content:center;padding-top:var(--head);opacity:var(--st,0);pointer-events:none;transform:translateY(calc((1 - var(--st,0)) * 28px))}
.hero-statement .statement{margin-top:24px}
/* the last pair moves to a new line together, and wraps inside its own box only when it is wider than the line, as under larger text spacing */
.keep{display:inline-block}
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
html.js .reveal:focus-within{opacity:1;transform:none;transition:none}
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
.skills-foot{margin-top:32px;max-width:58ch}
.skills-foot .skills{margin-top:4px}
/* ---- disclosure: a quiet mono summary with a copper plus that turns to a cross when open */
.more summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:10px;min-height:44px;font-family:var(--mono);font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text);transition:color .15s}
.more summary::-webkit-details-marker{display:none}
.more summary::before{content:"+";display:inline-block;width:12px;color:var(--accent);font-size:16px;line-height:1;text-align:center;transition:transform .3s}
.more[open]>summary::before{transform:rotate(45deg)}
.more summary:hover{color:var(--accent-hover)}
.more summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.skills{font-family:var(--mono);font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text-secondary)}

/* ---- proof: metrics, then the cases as a strip that scrolls on its own axis */
.metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:48px}
.metric{padding:28px 0 0;border-top:1px solid var(--line-strong);display:flex;flex-direction:column;gap:12px}
.metric .big{font-size:var(--fs-metric);line-height:.92;font-weight:600;letter-spacing:-0.045em;font-variant-numeric:tabular-nums lining-nums;min-height:1em;white-space:nowrap}
.metric .big em{font-style:normal;color:var(--accent)}
.metric .label{font-size:var(--fs-small);line-height:var(--lh-small);color:var(--text-secondary)}
.scene-proof{position:relative;padding:56px 0 clamp(72px,9vh,112px)}
.track{display:grid;grid-auto-flow:column;grid-auto-columns:clamp(440px,38vw,600px);grid-template-rows:auto auto auto;gap:0 24px;padding:0 var(--side) 20px;margin-top:40px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:var(--side);overscroll-behavior-x:contain;scrollbar-width:thin;scrollbar-color:var(--line-strong) transparent}
.card{grid-row:span 3;display:grid;grid-template-rows:subgrid;row-gap:18px;scroll-snap-align:start;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:36px;position:relative;overflow:hidden}
.card .chead{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
/* the hover glow is paint only: it covers the whole card, so it takes no pointer input and the links under it stay live */
.card::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 40% at 100% 0%,rgba(var(--copper-rgb),.16),transparent 70%);opacity:0;transition:opacity .5s;pointer-events:none}
.card:hover::before{opacity:1}
.card .kicker{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);letter-spacing:.02em}
.card h3{font-size:var(--fs-title);line-height:1.1;font-weight:600;letter-spacing:-0.025em;text-wrap:balance}
.card p{color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose)}
.card{scroll-margin-top:calc(var(--head) + 24px);transition:border-color .6s cubic-bezier(.2,.7,.2,1)}
.card.arrived{border-color:var(--accent)}
.card:focus{outline:none}
.card:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
/* every card shares three rows with the others in the strip: the story (head, title, body, facts), the notes control, and the links
   and era. The notes control and the foot sit at one height in every card, whatever a card holds or wraps; a card without notes keeps
   the row empty */
.card .cstory{display:flex;flex-direction:column;gap:18px}
.card .cfacts{display:grid;gap:12px}
.card .evidence{grid-row:2}
.card .cfacts div{display:grid;grid-template-columns:76px minmax(0,1fr);gap:16px;align-items:baseline}
.card .cfacts dt{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.card .cfacts dd{margin:0;color:var(--text);font-size:var(--fs-small);line-height:var(--lh-small)}
.card .evidence p{margin-top:4px;font-size:var(--fs-small);line-height:var(--lh-small)}
.card .cfoot{grid-row:3;align-self:end;display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap}
.card .links{display:flex;gap:20px;flex-wrap:wrap;font-size:var(--fs-small)}
.card .idx{flex:0 0 auto;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}

.card .era{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);text-align:right}
.strip-head{display:flex;justify-content:flex-end;align-items:end;gap:24px}
.strip-nav{display:flex;gap:12px;flex:0 0 auto}
.strip-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;padding:0;border:1px solid var(--line-strong);border-radius:2px;background:none;color:var(--text);cursor:pointer;transition:border-color .15s,color .15s}
.strip-btn svg{display:block}
/* the stop control shows two bars while the strip drifts and a play triangle once it is stopped */
.strip-play .i-start,.strip-play.off .i-stop{display:none}
.strip-play.off .i-start{display:block}
.strip-btn[hidden]{display:none}
/* while the strip drifts it moves freely; snap returns once a reader stops it */
.track.drift{scroll-snap-type:none}
.strip-btn:hover{border-color:var(--accent);color:var(--accent-hover)}
.strip-btn:active{color:var(--accent)}
.strip-btn:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.strip-btn[disabled]{opacity:var(--dim);cursor:default}
.strip-btn[disabled]:hover{border-color:var(--line-strong);color:var(--text)}

.links a{padding:6px 8px;margin:-6px -8px}
/* the strip takes focus so the arrow keys scroll it in every engine; it runs edge to edge, so the outline sits just inside it */
.track:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
/* read out, not shown: the strip status after a press of Previous or Next */
.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}

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
.case-ref span{display:inline-block;margin-left:10px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
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
.era-intro{max-width:58ch}
.era-name{font-size:var(--fs-subhead);line-height:1;font-weight:600;letter-spacing:-0.03em}
.era-years{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.lineage{margin-top:40px;border-top:1px solid var(--line)}
.lineage .rec p{margin-top:0;color:var(--text);font-size:var(--fs-prose);line-height:var(--lh-prose)}
.history{margin-top:56px}
.history-label{font-family:var(--mono);font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text-secondary);scroll-margin-top:24px}
.history-label:focus{outline:none}.history-label:focus-visible{outline:2px solid var(--accent);outline-offset:4px;border-radius:2px}
.history .eras{margin-top:28px}
.history-body{position:relative}
/* closed, with scripts: the first era shows and fades out under the button; without scripts all of it reads */
.js .history.closed .history-body{max-height:520px;overflow:hidden;-webkit-mask-image:linear-gradient(180deg,#000 45%,transparent);mask-image:linear-gradient(180deg,#000 45%,transparent)}
.js .history .history-body{transition:max-height .7s cubic-bezier(.2,.7,.2,1)}
.history-btn{display:inline-flex;align-items:center;gap:14px;height:52px;margin-top:8px;padding:0 24px 0 28px;background:none;border:1px solid var(--line-strong);border-radius:2px;color:var(--text);font-family:var(--sans);font-size:var(--fs-body);font-weight:500;letter-spacing:-0.005em;cursor:pointer;transition:border-color .15s,color .15s}
.history-btn::after{content:"";width:9px;height:9px;border-right:1.5px solid var(--accent);border-bottom:1.5px solid var(--accent);transform:translateY(-3px) rotate(45deg);transition:transform .3s}
.history:not(.closed) .history-btn{margin-top:40px}
.history:not(.closed) .history-btn::after{transform:translateY(2px) rotate(-135deg)}
.history-btn:hover{border-color:var(--accent);color:var(--accent-hover)}
.history-btn:active{border-color:var(--accent);color:var(--accent)}
.history-btn:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.history-btn{scroll-margin-bottom:24px}
.era-cases{margin-top:20px;border-top:1px solid var(--line)}
.rec{display:grid;grid-template-columns:150px minmax(0,1fr);gap:24px;padding:14px 0;border-bottom:1px solid var(--line)}
.rec .yr{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);padding-top:4px}
.rec h4{font-size:var(--fs-title-sm);line-height:1.25;font-weight:600;letter-spacing:-0.015em;margin:0}
.rec p{color:var(--text-secondary);font-size:var(--fs-small);line-height:var(--lh-small);margin-top:6px;max-width:58ch}
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
.panel .price b{display:block;font-size:var(--fs-subhead);line-height:1;font-weight:600;letter-spacing:-0.03em;color:var(--text);font-variant-numeric:tabular-nums lining-nums;text-wrap:balance}
.panel .price b.word{font-size:var(--fs-title);color:var(--text-secondary)}
.panel.launch .price b{color:var(--accent)}
.panel .price span{display:block;margin-top:12px;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary)}
.panel .n{font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);margin-bottom:22px}
.offer-note{margin-top:32px;max-width:58ch;color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose)}

/* ---- how */
.how-line{margin-top:28px}
.how-stage{position:relative;margin-top:48px}
.how-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin-top:40px}
.step .k{font-family:var(--mono);font-size:var(--fs-label);color:var(--text);display:flex;align-items:center;gap:12px}
.step .k span{color:var(--text-secondary);transition:color .5s}
.step:not(.on) .k span{color:var(--text)}
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
.how-note{margin-top:48px;color:var(--text-secondary);max-width:58ch;font-size:var(--fs-prose);line-height:var(--lh-prose)}

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
.turn p{color:var(--text);max-width:58ch}

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
.people-note{margin-top:56px;color:var(--text-secondary);max-width:58ch;font-size:var(--fs-prose);line-height:var(--lh-prose)}

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
.faq .a p{padding:0 0 12px;color:var(--text-secondary);font-size:var(--fs-prose);line-height:var(--lh-prose);max-width:58ch}
.faq .a p:last-child{padding-bottom:28px}
.faq .a strong{color:var(--text);font-weight:600}

/* ---- closing */
.scene-book{position:relative}
.scene-book .pin{position:relative;min-height:640px;overflow:hidden;display:flex;align-items:center;padding:150px 0 160px}
.scene-book .art{position:absolute;inset:0;width:100%;height:100%}
.scene-book .wrap{position:relative;z-index:2;width:100%}
.scene-book h2{max-width:10ch}
.scene-book .mail{margin-top:28px;font-size:var(--fs-lead);line-height:1.45;color:var(--text-secondary);max-width:24em}
.scene-book .cta{margin-top:36px}
/* the Discuss your project buttons land here, a step below the header */
#contact{scroll-margin-top:24px}
.brief{margin-top:36px;max-width:560px;display:flex;flex-direction:column;gap:20px}
.brief .cta{margin-top:4px}
.fld{display:flex;flex-direction:column;gap:8px}
.fld label{font-family:var(--mono);font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text-secondary)}
.fld input,.fld textarea{width:100%;height:52px;padding:0 16px;background:var(--surface);border:1px solid var(--line-strong);border-radius:2px;color:var(--text);font-family:var(--sans);font-size:var(--fs-body);line-height:var(--lh-body);transition:border-color .15s}
.fld textarea{height:auto;min-height:128px;padding:12px 16px;resize:vertical}
.fld input:hover,.fld textarea:hover{border-color:var(--accent)}
.fld input:focus,.fld textarea:focus{outline:none}
.fld input:focus-visible,.fld textarea:focus-visible{border-color:var(--accent);outline:2px solid var(--accent);outline-offset:3px}
.btn:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
button.btn{cursor:pointer;font-family:var(--sans)}
button.btn:disabled{cursor:default;opacity:var(--dim)}
.gotcha{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.fmsg{font-size:var(--fs-body);line-height:var(--lh-body);color:var(--text-secondary)}
.fmsg.ok{color:var(--text)}
.brief.sent .fld,.brief.sent .cta button{display:none}
.scene-book .line{position:absolute;right:var(--side);bottom:40px;z-index:2;font-family:var(--mono);font-size:var(--fs-label);color:var(--text-secondary);max-width:34em;text-align:right}
.foot{position:relative;z-index:1;border-top:1px solid var(--line);padding:40px max(var(--side), calc((100% - 1440px) / 2 + var(--side))) 48px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:24px;align-items:end;font-size:var(--fs-small);color:var(--text-secondary);background:var(--bg)}
.foot .lockup svg{height:28px}
.foot .links{display:flex;gap:20px;flex-wrap:wrap}
.foot .legal{grid-column:1 / -1;order:3;max-width:64ch;font-size:var(--fs-label);line-height:var(--lh-label);color:var(--text-secondary)}

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
  .track{grid-auto-columns:min(86vw,420px);gap:0 16px;padding:0 var(--side) 16px;margin-top:32px}
  /* the controls stay on a phone, under the strip and to the right, where the thumb meets them after the card it has read; the head
     dissolves so the lead line, the strip and the controls can be ordered in one column */
  .scene-proof{display:flex;flex-direction:column}
  .strip-head{display:contents}
  .strip-head > .lead{padding:0 var(--side)}
  .track{order:1}
  .strip-nav{order:2;align-self:flex-end;margin:16px var(--side) 0}
  .card{padding:28px}
  .card .cfacts div{grid-template-columns:minmax(0,1fr);gap:2px}
  /* one column, and the price reads directly under the title: the left div dissolves into the grid so its children can be ordered */
  .panel{grid-template-columns:minmax(0,1fr);gap:0;position:relative;top:auto;box-shadow:none}.panel > div:first-child{display:contents}.pcols{grid-template-columns:minmax(0,1fr);margin-top:24px}
  .panel .n{order:1}.panel h3{order:2}.panel .price{order:3;text-align:left;margin-top:4px}.panel > div > p{order:4}.panel .pcols{order:5}
  .panel .price b.word{font-size:var(--fs-title-sm);line-height:1.25;letter-spacing:-0.015em}
  .turn,.facts .row{grid-template-columns:minmax(0,1fr)}
  .scene-book .pin{display:block;min-height:0;padding:48px 0 96px}
  .scene-book .line{position:relative;right:auto;bottom:auto;text-align:left;margin:40px var(--side) 0}
  .foot{grid-template-columns:minmax(0,1fr)}
  .step{opacity:1;transform:none}.step:not(.on) p,.step:not(.on) .k span{color:var(--text-secondary)}
}
@media (max-width:600px){
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
  /* below the hero every section reads in its final state: the offer is a plain list, disclosures open at once, nothing travels */
  .panel{position:relative;top:auto;box-shadow:none}
  .wall-detail,.faq .a,.name::after,.faq summary i,.card::before,.cap,.cap p,.cap h3,.cap .k,.bigmark path,.era-block::before,.strip-btn,.more summary::before,.history-btn,.history-btn::after,.js .history .history-body{transition:none}
  .theme-rune .sec h2.reveal::after,.theme-rune .scene-book h2::after{width:120px;transition:none}
  .mark-arrived .site-header .mark-fill{animation:none}
  .site-header .btn{transition:none}
  .step{opacity:1;transform:none;transition:none}.step:not(.on) p,.step:not(.on) .k span{color:var(--text-secondary)}.step p,.step .k span{transition:none}
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
html:not(.js) .cap,.scene-build.flow .cap{opacity:1}
html:not(.js) .cap p,.scene-build.flow .cap p{max-height:none;opacity:1;margin-top:8px}
html:not(.js) .bigmark path,.scene-build.flow .bigmark path{fill:var(--accent)}
html:not(.js) .mark-count,.scene-build.flow .mark-count{display:none}
/* ---- the build scene pins only when its whole composition fits the viewport; when it does not (a short window, zoom, larger text)
   the script sets .flow and it reads as the no-script section: every line open, every piece lit, nothing held. Under 900 px it already flows */
.scene-build.flow .cap h3{color:var(--text)}
@media (min-width:901px){.scene-build.flow{height:auto}.scene-build.flow .pin{position:relative;height:auto;min-height:0;overflow:visible;padding-bottom:64px}}
html:not(.js) .step{opacity:1;transform:none}
html:not(.js) .step:not(.on) p,html:not(.js) .step:not(.on) .k span{color:var(--text-secondary)}
html:not(.js) .faq .a{height:auto}
/* ---- the hero as a plain section, when its text does not fit the pinned frame (heroFlow in the common script): the no-script layout,
   with room under the buttons on a phone for the rune, which draws in place there instead of flying to the header */
.theme-rune.hero-flow .hero{height:auto;min-height:0}
.theme-rune.hero-flow .hero-pin{position:relative;height:auto;min-height:0}
.theme-rune.hero-flow .hero-inner{height:auto;min-height:100vh;min-height:100dvh}
.theme-rune.hero-flow .hero-statement{position:relative;opacity:1;transform:none;pointer-events:auto;padding-bottom:64px}
@media (max-width:900px){.theme-rune.hero-flow .hero-inner{padding-bottom:calc(min(62vw,30vh) + 48px)}}
/* the canvas ends where the hero text does, so its light fades out over the last 96 px instead of stopping on a line */
.theme-rune.hero-flow .scene{-webkit-mask-image:linear-gradient(180deg,#000 calc(100% - 96px),transparent);mask-image:linear-gradient(180deg,#000 calc(100% - 96px),transparent)}
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
        links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in c["links"])
        cards += f'<article class="card reveal" id="case-{i+1:02d}" tabindex="-1" style="--i:{min(i,4)}" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(PROOF_CARDS)}"><div class="cstory"><div class="chead"><div class="kicker">{c["kicker"]}</div><div class="idx">{i+1:02d} / {len(PROOF_CARDS):02d}</div></div><h3>{c["title"]}</h3><p>{c["body"]}</p>{(f'<dl class="cfacts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["facts"]) + "</dl>") if c["facts"] else ""}</div>{(f'<details class="more evidence"><summary>{c["dlabel"]}</summary><p>{c["details"]}</p></details>') if c["details"] else ""}<div class="cfoot"><div class="links">{links}</div><div class="era">{c["era"]}</div></div></article>'
    wall = ""
    for i, (nm, grp, txt, links, era, case) in enumerate(WALL):
        lk = (f'<a class="case-ref" href="#case-{case:02d}">View {CASE_REFS[case]}<span>Case {case:02d}</span></a>' if case else "") + "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in links)
        wall += f'<button class="name {grp}" type="button" data-i="{i}" aria-expanded="false" aria-controls="wall-detail">{nm}</button><div class="wall-line" id="wall-{i}"><div class="wall-era">{era}</div><div><p>{txt}</p><div class="links">{lk}</div></div></div>'
    lineage = "".join(f'<div class="rec reveal"><div class="yr">{y}</div><div><p>{tx}</p></div></div>' for y, tx in LINEAGE)
    eras = ""
    for e in ERAS:
        rows = ""
        for y, tt, bd, lk, case in e["cases"]:
            ln = (f'<a class="case-ref" href="#case-{case:02d}">View {CASE_REFS[case]}<span>Case {case:02d}</span></a>' if case else "") + "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in lk)
            rows += f'<div class="rec reveal"><div class="yr">{y}</div><div><h4>{tt}</h4><p>{bd}</p>{f"<div class=links>{ln}</div>" if ln else ""}</div></div>'
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
        links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in p["links"])
        where = f'<div class="where">{p["where"]}</div>' if p["where"] else ""
        # a portrait with a 1080 px file offers it to the two-column landscape layout, where an 800 px file falls short of 3x
        big = p.get("photo") and os.path.exists(os.path.join(_HERE, "photo", "people", p["photo"] + "-1080.jpg"))
        sets = {ext: (f'people/{p["photo"]}.{ext} 800w, people/{p["photo"]}-1080.{ext} 1080w' if big else f'people/{p["photo"]}.{ext}') for ext in ("webp", "jpg")}
        sizes = ' sizes="(max-width:600px) 120px, (max-width:1100px) 46vw, 300px"' if big else ""
        pic = (f'<picture><source type="image/webp" srcset="{sets["webp"]}"{sizes}><img src="people/{p["photo"]}.jpg"{f' srcset="{sets["jpg"]}"' if big else ""}{sizes} width="800" height="1000" alt="{p.get("alt", p["name"])}" loading="lazy" decoding="async"></picture>' if p.get("photo") else silhouette(p["seed"]))
        tag = "" if p.get("photo") else f'<div class="ini">{p["ini"]}</div><div class="slot">photo slot</div>'
        people += (f'<article class="person reveal" style="--i:{i}"><div class="portrait">{pic}'
                   f'{tag}</div>'
                   f'<div><h3>{p["name"]}</h3><div class="role">{p["role"]}</div>{where}</div><p class="bio">{p["bio"]}</p>'
                   f'{("<div class=links>" + links + "</div>") if links else ""}</article>')
    facts = "".join(f'<div class="row reveal" style="--i:{i}"><div class="k">{k}</div><div class="v{" todo" if v.startswith("[") else ""}">{v}</div></div>' for i, (k, v) in enumerate(CONTRACT))
    faq = "".join(f'<details><summary><span>{q}</span><i></i></summary><div class="a">{"".join(f"<p>{x}</p>" for x in a.split(chr(10) * 2))}</div></details>' for q, a in FAQ)
    book_art = '<canvas class="art" id="book-art" aria-hidden="true"></canvas>'
    chevron = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{d}"/></svg>'
    strip_nav = ('<div class="strip-nav">'
                 f'<button type="button" class="strip-btn" data-dir="-1" aria-label="Previous case">{chevron.format(d="M10 3L5 8l5 5")}</button>'
                 f'<button type="button" class="strip-btn strip-play" id="strip-play" aria-label="Stop scrolling" hidden>{chevron.format(d="M6 3.5v9M10 3.5v9").replace("<svg ", "<svg class=i-stop ")}{chevron.format(d="M5.5 3.5l7 4.5-7 4.5z").replace("<svg ", "<svg class=i-start ")}</button>'
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

<section class="sec" id="who">
  <div class="wrap">
    <p class="eyebrow reveal">{t["who_eyebrow"]}</p>
    <h2 class="reveal">The situations we see most often.</h2>
    <div class="who-grid stagger">{who}</div>
    <div class="turn reveal"><h3>What we turn down</h3><p>{TURN_DOWN}</p></div>
  </div>
</section>

<section class="scene-build" id="build" data-scrub="build">
  <div class="pin">
    <div class="wrap">
      <p class="eyebrow">{t["build_eyebrow"]}</p>
      <h2>Four things we build.</h2>
      <div class="markmap">
        <div class="caps-left">{caps}</div>
        <div class="mark-col">{bigmark}<div class="mark-count" id="mark-count">01 / 04</div></div>
      </div>
      <details class="more skills-foot"><summary>Technical capabilities</summary><p class="skills">{SKILLS}</p></details>
    </div>
  </div>
</section>

<section class="sec" id="proof" style="padding-bottom:0">
  <div class="wrap">
    <p class="eyebrow reveal">{t["proof_eyebrow"]}</p>
    <h2 class="reveal">Selected engineering work.</h2>
    <p class="lead reveal">Work by Felag's founders and principals at Uddug and Gateway.fm.</p>
    <div class="metrics stagger">
      <article class="metric reveal" style="--i:0"><div class="big" data-count="140" data-suffix="k+">140<em>k+</em></div><div class="label">requests per second at peak in production, aggregate across clients, for Opera and 1inch</div></article>
      <article class="metric reveal" style="--i:1"><div class="big">$1<em>B+</em></div><div class="label">locked in staking in late 2025 on Gateway Yield, the staking infrastructure we ran</div></article>
      <article class="metric reveal" style="--i:2"><div class="big">9<em>M+</em></div><div class="label">users reported by Humanity Protocol, whose application layer we built</div></article>
    </div>
  </div>
</section>
<section class="scene-proof" id="proof-cases" aria-label="Lead cases" aria-roledescription="carousel">
  <div class="wrap strip-head">{strip_nav}</div>
  <div class="track" id="track" tabindex="0" role="group" aria-label="Lead cases">{cards}</div>
  <div class="sr-only" id="strip-status" aria-live="polite" aria-atomic="true"></div>
</section>
<section class="sec" id="names" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow reveal">{t["wall_eyebrow"]}</p>
    <h2 class="reveal">Names we have worked with.</h2>
    <p class="lead reveal">Clients and products we built for, and the protocols our systems served. Open a name for the relationship and the case behind it.</p>
    <div class="wall reveal" id="wall">{wall}<div class="wall-detail" id="wall-detail" hidden><div class="wall-detail-inner" id="wall-detail-inner"></div></div></div>
  </div>
</section>
<section class="sec" id="record" data-scrub="record">
  <div class="wrap">
    <p class="eyebrow reveal">{t["more_eyebrow"]}</p>
    <h2 class="reveal">Where the team comes from.</h2>
    <div class="lineage">{lineage}</div>
    <div class="history closed" id="history">
      <p class="history-label reveal" id="history-label" tabindex="-1">The full history: {len(ERAS)} eras and {sum(len(e["cases"]) for e in ERAS)} projects, from a 2014 faucet network to Felag</p>
      <div class="history-body" id="history-body">
        <div class="eras" id="eras"><div class="era-line" aria-hidden="true"><i id="era-line-fill"></i></div>{eras}</div>
      </div>
      <button class="history-btn" id="history-btn" type="button" aria-expanded="false" aria-controls="history-body" hidden>Show the full history</button>
    </div>
  </div>
</section>

<section class="sec" id="offer">
  <div class="wrap">
    <p class="eyebrow reveal">{t["offer_eyebrow"]}</p>
    <h2 class="huge reveal">We sell outcomes, not hours.</h2>
    <p class="lead reveal">Fixed-price sprints, builds and technical reviews. Monthly retainers for pods and fractional CTO work, with deliverables agreed in the statement of work (SOW). Prices in US dollars, excluding VAT.</p>
    <div class="stack" id="stack">{panels}</div>
    <p class="offer-note reveal">{OFFER_NOTE}</p>
    <div class="cta reveal" style="margin-top:40px"><a class="btn" href="#contact">Discuss your project</a></div>
  </div>
</section>

<section class="sec" id="how" data-scrub="how">
  <div class="wrap">
    <p class="eyebrow reveal">{t["how_eyebrow"]}</p>
    <h2 class="reveal">How delivery starts.</h2>
    <p class="lead reveal">{t["how_line"]}</p>
    <div class="how-stage">{how_art}<div class="how-grid">{steps}</div></div>
    <p class="how-note reveal">{HOW_NOTE}</p>
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
    <h2 class="reveal">Questions about working with Felag.</h2>
    <div class="faq reveal">{faq}</div>
  </div>
</section>

<section class="scene-book" id="book">
  <div class="pin">
    {book_art}
    <div class="wrap">
      <p class="eyebrow" id="contact">{t["book_eyebrow"]}</p>
      <h2>Start with the workshop.</h2>
      <p class="mail">Tell us about the system and your deadline. We start with a free technical workshop with a founder, and reply within two working days.</p>
      <form class="brief" action="https://formspree.io/f/mppqeyyd" method="POST" data-form>
        <div class="fld"><label for="brief-message">The system and your deadline</label><textarea id="brief-message" name="message" rows="4" required></textarea></div>
        <div class="fld"><label for="brief-email">Email</label><input id="brief-email" name="email" type="email" autocomplete="email" required></div>
        <input type="hidden" name="_subject" value="felag.net: Free technical workshop">
        <!-- where Formspree sends a browser that posted the form without scripts; absolute, so change it with the domain -->
        <input type="hidden" name="_next" value="https://felag.net/?sent=1#book">
        <input class="gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="cta"><button class="btn" type="submit">Discuss your project</button><a class="textlink" href="#offer">See prices</a></div>
        <p class="fmsg" role="status" aria-live="polite" hidden></p>
      </form>
    </div>
    {("<div class=line>" + t["book_line"] + "</div>") if t.get("book_line") else ""}
  </div>
</section>
<footer class="foot">
  <div><a class="lockup" href="#top" aria-label="Felag, home">{LOCKUP}</a></div>
  <p class="legal">{ENTITY}.</p>
  <div class="links"><a href="https://www.linkedin.com/company/felagnet/" target="_blank" rel="noopener">LinkedIn</a><a href="https://github.com/felagnet" target="_blank" rel="noopener">GitHub</a><a href="https://x.com/felagnet" target="_blank" rel="noopener">X</a><a href="mailto:info@felag.net?subject=Free%20technical%20workshop">info@felag.net</a></div>
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
  window.scrubRequest = request;
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
  // the statement arrives as the hero text leaves (that text is gone by 0.124), while the rune is still on its way to the header, so
  // there is always something to read; a keyboard reader holding the hero text holds the statement back
  function arrival(hp){ return heroHeld ? 0 : Math.max(0, Math.min(1, (hp - 0.115)/0.04)); }
  if (reduce || narrow){
    // no word-by-word light
    words.forEach(function(w){ w.style.opacity = 1; });
    if (inHero){ var hs = document.getElementById('hero-statement'); window.onScrub('statement', function(){ if (heroFlow) return; var st = arrival(heroProgress()); hs.style.setProperty('--st', st.toFixed(3)); hs.style.pointerEvents = st >= 0.9 ? 'auto' : ''; }); }
    return;
  }
  window.onScrub('statement', function(p, el){
    var q;
    // the hero laid out as a plain section: the statement reads whole, every word at rest
    if (inHero && heroFlow){ for (var j = 0; j < n; j++){ words[j].style.opacity = 1; words[j].classList.remove('hot'); } return; }
    if (inHero){
      // the statement takes over from the hero text, then lights up word by word
      var hp = heroProgress(), st = arrival(hp);
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
  var scene = document.getElementById('build'), caps = document.querySelectorAll('#build .cap'), pieces = document.querySelectorAll('#build .bigmark path'), count = document.getElementById('mark-count'); if (!scene || !caps.length) return;
  var wrap = scene.querySelector('.pin > .wrap'), markmap = scene.querySelector('.markmap'), capsCol = scene.querySelector('.caps-left'), markCol = scene.querySelector('.mark-col'), header = document.querySelector('.site-header');
  var current = -1, flow = null, narrowQ = window.matchMedia('(max-width:900px)');
  // the height the pinned frame needs with its longest line open. The lines as they are drawn now are taken out and the longest put back,
  // so the answer is the same pinned or static, at rest or mid-transition
  function needed(){
    var shown = 0, longest = 0;
    caps.forEach(function(c){ var p = c.querySelector('p'); shown += p.getBoundingClientRect().height + parseFloat(getComputedStyle(p).marginTop); longest = Math.max(longest, p.scrollHeight + 8); });
    var capsH = capsCol.getBoundingClientRect().height - shown + longest, markH = markCol.getBoundingClientRect().height + (count && count.offsetParent ? 0 : 38);
    return (header ? header.getBoundingClientRect().height : 72) + wrap.getBoundingClientRect().height - markmap.getBoundingClientRect().height + Math.max(capsH, markH) + 24;
  }
  function decide(){
    // a little slack before pinning again, so a window at the edge does not flip on every pixel
    var f = reduce || narrowQ.matches || needed() > window.innerHeight - (flow ? 8 : 0);
    if (f === flow) return;
    flow = f; scene.classList.toggle('flow', f); current = -1;
    // static: every capability and every piece is on, as the phone has always shown them; pinned again, the next scrub pass picks the one in view
    caps.forEach(function(c){ c.classList.toggle('on', f); }); pieces.forEach(function(pc){ pc.classList.toggle('on', f); });
    if (!f && count) count.textContent = '01 / 0' + caps.length;
    if (window.scrubRequest) window.scrubRequest();
  }
  decide();
  window.addEventListener('resize', decide);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(decide);
  if ('ResizeObserver' in window) new ResizeObserver(function(){ decide(); }).observe(wrap);
  window.onScrub('build', function(p){
    if (flow) return;
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
  var map = {top: '', proof: '#proof', 'proof-cases': '#proof', names: '#proof', record: '#proof', offer: '#offer', how: '#how', people: '#people', faq: '#people'};
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
  var track = document.getElementById('track'), btns = document.querySelectorAll('.strip-btn[data-dir]'); if (!track || !btns.length) return;
  function update(){
    var prev = track.scrollLeft < 2, next = track.scrollLeft + track.clientWidth > track.scrollWidth - 2;
    btns.forEach(function(b){ b.disabled = b.getAttribute('data-dir') === '-1' ? prev : next; });
  }
  // after a press the card now at the left edge is read out as its slide position and its title, once the strip has settled
  var status = document.getElementById('strip-status'), say = 0;
  function announce(){
    var tr = track.getBoundingClientRect(), cards = track.querySelectorAll('.card'), c = null;
    for (var i = 0; i < cards.length; i++){ if (cards[i].getBoundingClientRect().left >= tr.left - 2){ c = cards[i]; break; } }
    if (c && status) status.textContent = c.getAttribute('aria-label') + ', ' + c.querySelector('h3').textContent;
  }
  // a press brings the next or previous card's left edge to the gutter, wherever the drift has left the strip
  function target(dir){
    var edge = track.getBoundingClientRect().left + (parseFloat(getComputedStyle(track).paddingLeft) || 0), cards = track.querySelectorAll('.card'), x = null;
    for (var i = 0; i < cards.length; i++){ var l = cards[i].getBoundingClientRect().left - edge;
      if (dir > 0 && l > 2){ x = l; break; }
      if (dir < 0 && l < -2) x = l; }
    return x === null ? (dir > 0 ? track.scrollWidth : 0) : track.scrollLeft + x;
  }
  var hold = function(){}, pin = function(){};
  btns.forEach(function(b){ b.addEventListener('click', function(){
    clearTimeout(say); say = setTimeout(announce, reduce ? 50 : 450); hold();
    track.scrollTo({left: target(parseInt(b.getAttribute('data-dir'), 10)), behavior: reduce ? 'auto' : 'smooth'});
  }); });
  track.addEventListener('scroll', update, {passive: true}); window.addEventListener('resize', update); update();

  // ---- a case link elsewhere on the page, the names wall's, brings its card into view: the strip to the middle of the screen,
  // the card to the strip's left edge, a moment's light on its border and focus on it; the drift stops there, as for any choice the reader makes
  document.addEventListener('click', function(e){
    var a = e.target.closest('a.case-ref'); if (!a) return;
    var card = document.getElementById(a.getAttribute('href').slice(1)); if (!card || card.parentNode !== track) return;
    e.preventDefault(); pin();
    var how = reduce ? 'auto' : 'smooth', head = document.querySelector('.site-header'), top = head ? head.offsetHeight : 0;
    var tr = track.getBoundingClientRect(), room = window.innerHeight - top;
    window.scrollTo({top: Math.max(0, window.scrollY + tr.top - top - Math.max(16, (room - tr.height) / 2)), behavior: how});
    var edge = tr.left + (parseFloat(getComputedStyle(track).paddingLeft) || 0);
    track.scrollTo({left: track.scrollLeft + card.getBoundingClientRect().left - edge, behavior: how});
    card.focus({preventScroll: true});
    card.classList.add('arrived'); setTimeout(function(){ card.classList.remove('arrived'); }, 1800);
    clearTimeout(say); say = setTimeout(announce, reduce ? 50 : 700);
  });

  // ---- the drift: 30 px a second while the strip is on screen, back to the first card after the last. Phones start still, since the
  // controls sit below the cards there. The mouse over the strip pauses it only while it stays; keyboard use, a swipe, a tap or a press stops it
  // until the reader presses Start scrolling, and so does a case link. It also holds while a case's notes are open, so a card read
  // with the mouse stays put. Never under reduced motion, from load or from the moment the preference turns on with the page open
  var play = document.getElementById('strip-play'); if (!play || reduce) return;
  var narrowQ = window.matchMedia('(max-width:900px)');
  var SPEED = 30, stopped = narrowQ.matches, chosen = false, hover = false, seen = false, until = 0, end = 0, back = false, pos = track.scrollLeft, last = 0, raf = 0;
  play.hidden = false;
  function reading(){ return !!track.querySelector('details[open]'); }
  function running(){ return !stopped && !hover && !reading() && seen && !document.hidden; }
  function kick(){ if (running() && !raf) raf = requestAnimationFrame(tick); }
  function show(){
    play.classList.toggle('off', stopped); play.setAttribute('aria-label', stopped ? 'Start scrolling' : 'Stop scrolling');
    // snap is off only while the strip drifts, so a stopped strip and the arrow keys move card by card
    track.classList.toggle('drift', !stopped);
  }
  function stop(){ if (stopped) return; stopped = true; chosen = true; end = 0; back = false; show(); }
  show();
  hold = stop; pin = stop;
  function tick(t){
    raf = 0; if (!running()){ last = 0; return; }
    raf = requestAnimationFrame(tick);
    var dt = last ? Math.min(t - last, 50) : 0; last = t;
    if (end){
      // at the last card: rest, glide back to the first, rest again
      if (!back && t - end > 1600){ back = true; track.scrollTo({left: 0, behavior: 'smooth'}); }
      if (back && (track.scrollLeft < 2 || t - end > 7600)){ end = 0; back = false; pos = track.scrollLeft; until = t + 1500; }
      return;
    }
    if (t < until){ pos = track.scrollLeft; return; }
    // the strip moved by a hand other than the drift's: the reader has taken it, so it stays where they put it
    if (Math.abs(track.scrollLeft - pos) > 3){ stop(); return; }
    if (pos >= track.scrollWidth - track.clientWidth - 1){ end = t; return; }
    pos += SPEED*dt/1000; track.scrollLeft = pos;
  }
  play.addEventListener('click', function(){
    stopped = !stopped; chosen = true; end = 0; back = false; show(); pos = track.scrollLeft; until = performance.now() + 600; kick();
  });
  // a tap is followed by imitation mouse events, which are not a mouse resting on the strip
  var touched = 0;
  document.addEventListener('touchstart', function(){ touched = performance.now(); }, {passive: true, capture: true});
  function mouse(e){ return e.pointerType === 'mouse' && performance.now() - touched > 1000; }
  [track, play.parentNode].forEach(function(el){
    el.addEventListener('pointerenter', function(e){ if (mouse(e)) hover = true; });
    el.addEventListener('pointerleave', function(e){ if (e.pointerType === 'mouse'){ hover = false; pos = track.scrollLeft; kick(); } });
  });
  var sec = document.getElementById('proof-cases');
  // keyboard focus arriving on anything but the control, or any key pressed inside the section, is keyboard use, however focus got there
  sec.addEventListener('focusin', function(e){ if (e.target !== play && e.target.matches(':focus-visible')) stop(); });
  sec.addEventListener('keydown', function(e){ if (e.target !== play && !/^(Shift|Control|Alt|Meta)$/.test(e.key)) stop(); });
  // a touch on the strip stops it, unless the finger only scrolled the page past it
  var tx = 0, ty = 0;
  track.addEventListener('touchstart', function(e){ var p = e.touches[0]; tx = p.clientX; ty = p.clientY; until = performance.now() + 60000; }, {passive: true});
  track.addEventListener('touchend', function(e){
    var p = e.changedTouches[0], dx = Math.abs(p.clientX - tx), dy = Math.abs(p.clientY - ty);
    until = 0; pos = track.scrollLeft; if (!(dy > 10 && dy > dx)) stop(); kick();
  }, {passive: true});
  track.addEventListener('wheel', function(e){ if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) stop(); }, {passive: true});
  // until the reader has chosen, the strip follows the screen: still on a phone, drifting on a desktop
  narrowQ.addEventListener('change', function(){ if (chosen) return; stopped = narrowQ.matches || reduce; show(); pos = track.scrollLeft; kick(); });
  // reduced motion turned on stops the drift where the strip stands, without counting as the reader's choice; turned off, the drift goes
  // on only if the reader never stopped it themselves
  window.addEventListener('reducemotion', function(){
    if (reduce){ stopped = true; end = 0; back = false; show(); return; }
    if (!chosen){ stopped = narrowQ.matches; show(); pos = track.scrollLeft; until = performance.now() + 600; kick(); }
  });
  // notes opening or closing: closing the last one lets the drift go on from where the strip stands
  track.addEventListener('toggle', function(){ if (!reading()) pos = track.scrollLeft; kick(); }, true);
  document.addEventListener('visibilitychange', kick);
  // on screen means a third of the strip, or of the screen when the cards are taller than it, as in a phone held sideways
  new IntersectionObserver(function(es){ var e = es[0], was = seen;
    seen = e.isIntersecting && e.intersectionRect.height >= 0.35*Math.min(e.boundingClientRect.height, innerHeight);
    if (seen && !was){ pos = track.scrollLeft; until = performance.now() + 1200; } kick(); }, {threshold: [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]}).observe(track);
})();

// ---- the names wall: a name opens its line right under its own row
(function(){
  var wall = document.getElementById('wall'), detail = document.getElementById('wall-detail'), inner = document.getElementById('wall-detail-inner');
  if (!wall || !detail) return;
  var open = null;
  function close(){ if (!open) return; open.classList.remove('on'); open.setAttribute('aria-expanded', 'false'); open = null;
    // under reduced motion there is no transition to wait for, so the row closes in the same moment
    if (reduce){ detail.hidden = true; detail.style.height = '0px'; return; }
    detail.classList.add('closing'); detail.style.height = detail.scrollHeight + 'px'; requestAnimationFrame(function(){ detail.style.height = '0px'; }); detail.addEventListener('transitionend', function h(){ detail.hidden = true; detail.classList.remove('closing'); detail.removeEventListener('transitionend', h); }); }
  wall.addEventListener('click', function(e){
    var btn = e.target.closest('.name'); if (!btn) return;
    if (open === btn){ close(); return; }
    if (open){ open.classList.remove('on'); open.setAttribute('aria-expanded', 'false'); }
    open = btn; btn.classList.add('on'); btn.setAttribute('aria-expanded', 'true');
    inner.innerHTML = document.getElementById('wall-' + btn.getAttribute('data-i')).innerHTML;
    // find the last name on the same visual row and place the detail after it
    var top = btn.offsetTop, names = wall.querySelectorAll('.name'), last = btn;
    names.forEach(function(n){ if (Math.abs(n.offsetTop - top) < 6 && n.offsetLeft > last.offsetLeft) last = n; });
    last.insertAdjacentElement('afterend', detail); detail.hidden = false; detail.classList.remove('closing');
    if (reduce){ detail.style.height = 'auto'; return; }
    detail.style.height = '0px';
    requestAnimationFrame(function(){ detail.style.height = detail.scrollHeight + 'px'; });
    detail.addEventListener('transitionend', function h(){ if (!detail.hidden) detail.style.height = 'auto'; detail.removeEventListener('transitionend', h); });
  });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') close(); });
})();

// ---- the record: the full history opens from its button; closed, the faded part is inert
(function(){
  var box = document.getElementById('history'), body = document.getElementById('history-body'), btn = document.getElementById('history-btn'), label = document.getElementById('history-label'); if (!box || !btn) return;
  btn.hidden = false; body.inert = true;
  // opened, the body ends at auto height so it follows rewrapping on a resize or a rotation. With reduced motion it opens at auto at once;
  // otherwise it animates to its measured height and then lets go of it. Each click bumps gen, so a late frame or timer of an earlier
  // click never writes a fixed height back
  var gen = 0;
  function settle(g){ if (g !== gen) return; gen++; body.style.maxHeight = ''; }
  body.addEventListener('transitionend', function(e){ if (e.target === body && e.propertyName === 'max-height' && !box.classList.contains('closed')) settle(gen); });
  // the button sits below the history, so opening pushes it far down: focus moves to the label at the head of the history, and the next
  // Tab reaches the first project link. A keyboard visitor is brought to the label; a pointer leaves the page where it was. Closing keeps
  // focus on the button and brings it back into view, with the history from its label when the closed block fits the screen
  btn.addEventListener('click', function(){
    var open = box.classList.contains('closed'), g = ++gen, keyed = btn.matches(':focus-visible'), behavior = reduce ? 'auto' : 'smooth';
    if (open){ box.classList.remove('closed'); body.inert = false;
      if (!reduce){ body.style.maxHeight = '520px';
        requestAnimationFrame(function(){ if (g === gen) body.style.maxHeight = body.scrollHeight + 'px'; });
        setTimeout(function(){ settle(g); }, 800); }
      if (label){ label.focus({preventScroll: true}); if (keyed) label.scrollIntoView({block: 'start', behavior: behavior}); } }
    else { body.style.maxHeight = ''; box.classList.add('closed'); body.inert = true;
      var head = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--head')) || 72;
      if (box.getBoundingClientRect().height + head <= window.innerHeight) box.scrollIntoView({block: 'start', behavior: behavior});
      else btn.scrollIntoView({block: 'end', behavior: behavior}); }
    btn.setAttribute('aria-expanded', open ? 'true' : 'false'); btn.textContent = open ? 'Close the full history' : 'Show the full history';
  });
})();

// ---- the record: the era line draws as the reader moves down it, each era lighting its marker
(function(){
  var fill = document.getElementById('era-line-fill'), blocks = document.querySelectorAll('.era-block'); if (!fill) return;
  if (reduce){ fill.style.height = '100%'; blocks.forEach(function(b){ b.classList.add('lit'); }); return; }
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
  if (reduce) steps.forEach(function(s){ s.classList.add('on'); });
  window.onScrub('how', function(p, el){
    var r = el.getBoundingClientRect(), h = window.innerHeight;
    // local progress: 0 when the section top reaches 80% of the viewport, 1 when its bottom reaches 40%
    var q = Math.max(0, Math.min(1, (h*0.8 - r.top) / Math.max(1, r.height - h*0.4)));
    var narrow = window.innerWidth < 900;
    steps.forEach(function(s, i){ s.classList.toggle('on', narrow || reduce || q > (i + 0.5) / (steps.length + 0.6)); });
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
      // under reduced motion the answer opens and closes at once, with no transitionend to wait for
      if (reduce){ d.open = !d.open; a.style.height = d.open ? 'auto' : '0px'; return; }
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
// ---- closing form: posts to Formspree in place; without scripts the browser posts it and Formspree returns to #book with ?sent=1
(function(){
  var f = document.querySelector('form[data-form]');
  if (!f) return;
  var MAIL = 'info@felag.net', MAILTO = 'mailto:info@felag.net?subject=Free%20technical%20workshop';
  var btn = f.querySelector('button[type="submit"]'), msg = f.querySelector('.fmsg');
  var endpoint = f.getAttribute('action') || '';
  function say(kind){
    if (!msg) return;
    msg.className = 'fmsg ' + kind; msg.hidden = false; msg.textContent = '';
    if (kind === 'ok'){ msg.textContent = "Sent. We'll reply to the address you gave."; return; }
    var a = document.createElement('a'); a.href = MAILTO; a.textContent = MAIL;
    msg.appendChild(document.createTextNode("That didn't send. Email us directly at "));
    msg.appendChild(a); msg.appendChild(document.createTextNode('.'));
  }
  function count(){ if (window.plausible) plausible('Contact form sent'); }
  if (/[?&]sent=1/.test(location.search)){
    f.classList.add('sent'); say('ok'); count();
    try { history.replaceState(null, '', location.pathname + location.hash); } catch (e) {}
  }
  // until the real form id is set, open the visitor's mail client rather than post into a 404
  if (endpoint.indexOf('REPLACE-ME') > -1){
    f.addEventListener('submit', function(ev){
      ev.preventDefault();
      if (f._gotcha && f._gotcha.value) return;
      var body = (f.message.value || '').trim() + '\n\n' + (f.email.value || '').trim();
      location.href = MAILTO + '&body=' + encodeURIComponent(body);
    });
    return;
  }
  f.addEventListener('submit', function(ev){
    if (!window.fetch || !window.FormData) return;
    ev.preventDefault();
    if (f._gotcha && f._gotcha.value) return;
    var label = btn ? btn.textContent : '';
    if (btn){ btn.disabled = true; btn.textContent = 'Sending'; }
    if (msg) msg.hidden = true;
    fetch(endpoint, {method: 'POST', body: new FormData(f), headers: {Accept: 'application/json'}})
      .then(function(r){ if (!r.ok) throw new Error(String(r.status)); f.classList.add('sent'); say('ok'); count(); })
      .catch(function(){ say('bad'); })
      .then(function(){ if (btn && !f.classList.contains('sent')){ btn.disabled = false; btn.textContent = label; } });
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
  // the scene's box also changes without a window resize: fonts landing, the form's errors and its sent state, a textarea dragged taller.
  // Each change resizes the backing store and redraws the frame the scene is at
  if ('ResizeObserver' in window) new ResizeObserver(function(){ layout(); look(); }).observe(canvas);
  if (reduce || window.innerWidth < 900){ hold = true; p = 0.9; }
  window.addEventListener('reducemotion', function(){ if (reduce){ hold = true; p = 0.9; look(); } });
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


def _offer(o, price=None, spec=None, monthly=False):
    d = {"@type": "Offer", "name": o["name"], "description": o["body"], "priceCurrency": "USD"}
    if price is not None:
        d["price"] = price
    if spec:
        # a monthly fee is a unit price per month, MON in UN/CEFACT
        kind = {"@type": "UnitPriceSpecification", "unitCode": "MON", "unitText": "month"} if monthly else {"@type": "PriceSpecification"}
        d["priceSpecification"] = dict(kind, priceCurrency="USD", valueAddedTaxIncluded=False, **spec)
    d["itemOffered"] = {"@type": "Service", "name": o["name"], "provider": {"@id": SITE + "#org"}}
    return d


def ld_json(title, description):
    """The structured data, built from the same constants as the visible copy so it cannot drift from the page.
    No headcount, no relation to Gateway.fm beyond the verbatim bios; the only address is the registered office in the footer."""
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
    offers = [
        _offer(OFFERS[0], price="0"),
        _offer(OFFERS[1], spec={"minPrice": 10000, "description": "from $10k"}),
        _offer(OFFERS[2], spec={"minPrice": 4000, "description": OFFERS[2]["price"] + ", " + OFFERS[2]["note"]}, monthly=True),
        _offer(OFFERS[3], spec={"minPrice": 10000, "maxPrice": 60000, "description": "$10k to $60k a month, by size"}, monthly=True),
        _offer(OFFERS[4], spec={"description": "Quote per scope, fixed price, half paid on start, report in one to two weeks"}),
    ]
    org = {"@type": "Organization", "@id": SITE + "#org", "name": "Felag", "legalName": "FELAG LLC", "url": SITE,
           "identifier": {"@type": "PropertyValue", "name": "Identification number of a Georgian limited liability company", "value": ENTITY_ID},
           "address": dict({"@type": "PostalAddress"}, **ENTITY_OFFICE, addressCountry="GE"),
           "logo": {"@type": "ImageObject", "url": SITE + "apple-touch-icon.png", "width": 180, "height": 180},
           "image": SITE + "og.png",
           "slogan": "Senior engineers who own the architecture and ship to production.",
           "description": STATEMENT + " Felag is the 2026 restart of Uddug, acquired in 2024.",
           "foundingDate": "2026-07", "email": "info@felag.net",
           "contactPoint": {"@type": "ContactPoint", "email": "info@felag.net", "contactType": "sales", "availableLanguage": "en"},
           "sameAs": COMPANY_PAGES,
           "founder": [{"@id": SITE + "#andrew"}, {"@id": SITE + "#mike"}],
           "knowsAbout": ["Software engineering", "Software architecture", "Distributed systems", "Platform engineering", "AI infrastructure", "Blockchain applications", "Payments", "Identity and access"],
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


def keep_last_pair(line):
    """The last two words of a headline kept together, so a narrow screen never leaves the final word alone (audit D-01), yet free to wrap
    when the pair alone is wider than the line (audit round 4 D-03). Markup only."""
    head, _, last = line.rpartition(" ")
    head, _, before = head.rpartition(" ")
    return f'{head} <span class="keep">{before} {last}</span>' if head else line


# cookieless analytics, the one third-party script on the page; only the rune page, which ships as index.html, carries it
PLAUSIBLE = """<script async src="https://plausible.io/js/pa-1ZK1zeIoMLCPeJ9EIDKOd.js"></script>
<script>
  window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};
  plausible.init()
</script>"""


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
{PLAUSIBLE if theme == "rune" else ""}
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
      <h1 class="rise r1">{keep_last_pair(headline)}</h1>
      <p class="sub rise r2">{sub}</p>
      <div class="cta rise r3"><a class="btn" href="#contact">Discuss your project</a><a class="textlink" href="#offer">See prices</a></div>
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

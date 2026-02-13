---
title: "AI Bubble or Platform Shift? Capital, Costs, and Commoditized Software"
date: 2026-01-19 09:00:00
categories: [blog]
author: Ganesh Raman
tags: [AI, Markets, Strategy, Software, Productivity, Commoditization]
toc: true
author_profile: true
classes: wide
excerpt: "A clear-eyed look at why this AI cycle feels bubbly, why it is still anchored in real economics, and why software creation is being commoditized faster than most teams are ready for."
permalink: /blog/ai-bubble-or-platform-shift-capital-costs-and-commoditized-software/
---

Series: AI Bubble, Software Commoditization, and Industrial AI

Series map: [Part 1](/blog/ai-bubble-or-platform-shift-capital-costs-and-commoditized-software/) | [Part 2](/blog/quality-capture-the-new-moat-as-software-commoditizes/) | [Part 3](/blog/infrastructure-inequality-power-silicon-and-capital/) | [Part 4](/blog/future-of-asset-intelligence-and-industrial-ai/)

Part 1 of 4. Next: [Quality Capture: The New Moat as Software Commoditizes](/blog/quality-capture-the-new-moat-as-software-commoditizes/)

## Summary

If you ask ten experienced operators whether this is an AI bubble or a platform shift, most will answer with conviction, and most will answer differently.

That disagreement is not because people are careless with data. It is because this cycle genuinely contains both conditions at once: bubble-like capital behavior and a real underlying technology discontinuity.

On the bubble side, the heat is obvious. Financial Times reported that global VC funding reached $469B in 2025, up 47 percent year over year, and AI captured nearly half of that total ([Financial Times](https://www.ft.com/content/762d000b-cac0-4d5f-8c18-af82035eef16)). In late September 2025, the S and P 500 Shiller P/E crossed 40 for the first time since 2000 ([Business Insider](https://markets.businessinsider.com/news/stocks/stock-market-outlook-shiller-pe-ratio-dot-com-bubble-ai-2025-9)). Those are not subtle signals.

On the structural side, the substrate is very different from the dot-com era. Nasdaq notes that 99.9 percent of Nasdaq 100 exposure is profitable today, and argues current profitability composition is materially stronger than the 1999 peak setup ([Nasdaq](https://www.nasdaq.com/articles/is-ai-another-bubble-for-the-nasdaq-100)). At the same time, Stanford's 2025 AI Index reports that inference cost for a GPT-3.5-level system fell by more than 280x from November 2022 to October 2024, with hardware cost and energy-efficiency trends improving as well ([Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)).

So the useful conclusion is not "pick a side." The useful conclusion is this: market pricing may be overheating in parts of the stack, but the operating economics of software creation are changing in ways that will likely persist.

## The wrong question and the right one

"Is this a bubble?" is an understandable question, but it is often the wrong strategic question.

A better question is: *where is scarcity migrating?*

In every major technology cycle, value does not disappear when old advantages commoditize; it relocates. If teams focus only on valuation narratives, they miss where that relocation is happening in product, engineering, and capital allocation.

Right now scarcity is moving away from baseline code production and toward three harder capabilities:

1. Quality capture under high change velocity.
2. Workflow ownership and integration depth.
3. Infrastructure access (compute, power, data-center capacity) that sustains iteration speed.

Parts 2, 3, and 4 of this series are about those three capabilities. This first post lays out why that migration is rational, not theoretical.

## Why this cycle feels bubbly in practice

The bubble argument is not irrational pessimism. It reflects real signals.

The first signal is capital velocity. Funding and valuation rounds are happening at a pace that can outrun operational absorption capacity. Even when underlying technology is real, too much capital too quickly tends to overfund adjacent categories and compress differentiation windows.

The second signal is valuation stress. CAPE above 40 has historically been a regime that deserves caution ([Business Insider](https://markets.businessinsider.com/news/stocks/stock-market-outlook-shiller-pe-ratio-dot-com-bubble-ai-2025-9)). CAPE is not a timing instrument, but it is a useful reminder that price can detach from near-term cash-flow conversion.

The third signal is infrastructure ambition at unprecedented scale. OpenAI announced Stargate as a $500B four-year plan with $100B immediate deployment, and later described progress toward a 10-gigawatt commitment ([OpenAI](https://openai.com/index/announcing-the-stargate-project/), [OpenAI](https://openai.com/index/five-new-stargate-sites/)). Announcements of this magnitude are strategically understandable, but they also encode execution and utilization risk.

The fourth signal is bottleneck migration into power markets. Reuters reported a deal tied to restarting a nuclear unit to supply 835 MW for Microsoft data centers, while Amazon's nuclear PPA with Talen was announced up to 1,920 MW through 2042 ([Reuters](https://www.reuters.com/business/energy/us-utilities-signal-booming-demand-data-centers-ai-takes-root-2024-08-12/), [Talen Energy](https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-expands-nuclear-energy-relationship-amazon)). Software cycles usually do not require this level of energy procurement choreography.

The fifth signal is enterprise execution ambiguity. Reuters highlighted uncertainty around enterprise adoption depth as a key variable for how the current wave monetizes ([Reuters](https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-top-ai-themes-that-will-shape-2026-2026-01-15/)). In plain terms: plenty of pilots, uneven workflow conversion.

Put together, these signals justify caution. They do not justify ignoring the structural shift.

## Why "this is just 1999 again" is too shallow

The easiest narrative is to map every heat signal to dot-com history and stop there. That is incomplete.

Today's leading companies are not mostly unprofitable story vehicles. That alone changes fragility characteristics ([Nasdaq](https://www.nasdaq.com/articles/is-ai-another-bubble-for-the-nasdaq-100)).

Second, we now have micro-level productivity evidence and macro-level cost deflation evidence that did not exist with similar clarity in earlier internet cycles. Microsoft Research's controlled Copilot experiment found a 55.8 percent faster completion time for a coding task ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/)). Stanford's AI Index quantified the inference economics shift at >280x decline for GPT-3.5-level performance over less than two years ([Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)).

Third, adoption has crossed into routine behavior for developers. Stack Overflow's 2024 and 2025 surveys show broad current usage plus strong daily-use intensity ([Stack Overflow 2024](https://survey.stackoverflow.co/2024/ai), [Stack Overflow 2025](https://survey.stackoverflow.co/2025/)).

None of that means risk is low. It means this is not purely speculative vapor.

A cleaner comparison is: dot-com had stronger valuation euphoria with weaker profitability foundations; this cycle has significant valuation stress *and* stronger operating foundations, while introducing new physical bottlenecks in power and infrastructure.

## What the 2025 big-tech scorecard is really saying

The strongest way to test whether this is only narrative heat is to look at 2025 operating numbers from the largest AI-linked platforms and ask a simple question: are they still mostly story, or are they converting AI demand into measurable business performance while taking on heavier infrastructure load?

Alphabet's 2025 results are a good anchor. The company reported full-year revenue of $402.8 billion, up 15 percent year over year, with Q4 revenue at $113.8 billion and Google Cloud up 48 percent to $17.7 billion in the quarter ([Alphabet Q4/FY2025 release PDF](https://s206.q4cdn.com/479360582/files/doc_news/2026/Feb/04/attachments/2025q4-alphabet-earnings-release.pdf)). It also signaled expected 2026 capex in a $175 billion to $185 billion range, which is a reminder that AI growth at this scale now runs through capital intensity, not just software efficiency ([Alphabet Q4/FY2025 release PDF](https://s206.q4cdn.com/479360582/files/doc_news/2026/Feb/04/attachments/2025q4-alphabet-earnings-release.pdf)).

Microsoft tells a similar two-sided story. In fiscal 2025, Microsoft reported $281.7 billion in revenue, up 15 percent, with operating income up 17 percent to $128.5 billion, and Azure surpassing $75 billion in annual revenue for the first time, up 34 percent ([Microsoft 2025 Annual Report](https://www.microsoft.com/investor/reports/ar25/)). Then, in the quarter ended December 31, 2025 (FY26 Q2), Microsoft reported revenue of $81.3 billion, up 17 percent, with Azure and other cloud services up 39 percent and Microsoft Cloud revenue at $51.5 billion ([Microsoft FY26 Q2 release](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q2/press-release-webcast)). The message is not subtle: demand is broad, but the margin structure is increasingly tied to infrastructure deployment and utilization quality.

Meta's 2025 results add a different dimension: ad-driven cash generation funding a large AI infrastructure step-up. Meta reported full-year 2025 revenue of $200.97 billion, up 22 percent, and Q4 revenue of $59.89 billion, up 24 percent, while full-year capex reached $72.22 billion, with 2026 capex guidance of $115 billion to $135 billion ([Meta Q4/FY2025 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/)). In other words, monetization remains strong, and spending is moving up the stack into compute and infrastructure at unprecedented levels.

Amazon's 2025 numbers make the trade-off between growth and investment even more explicit. Full-year net sales were $716.9 billion, up 12 percent, with AWS at $128.7 billion in sales and $45.6 billion in operating income ([Amazon Q4/FY2025 results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)). Operating cash flow rose to $139.5 billion, but free cash flow fell sharply as property and equipment purchases increased, with the company explicitly tying much of that increase to AI investment and signaling about $200 billion in 2026 capex ([Amazon Q4/FY2025 results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)). This is exactly the \"real but expensive\" profile of a platform transition.

OpenAI is not a public company with audited quarterly disclosures, so the evidence is different in form but still directional. OpenAI announced $40 billion in new funding at a $300 billion post-money valuation in March 2025 and said ChatGPT was being used weekly by 500 million people ([OpenAI funding update](https://openai.com/index/march-funding-updates/)). It later said more than 1 million business customers were paying for ChatGPT for Work or API usage ([OpenAI business customers update](https://openai.com/index/1-million-businesses-putting-ai-to-work/)). Combined with Stargate's announced $500 billion four-year infrastructure intent ([Stargate announcement](https://openai.com/index/announcing-the-stargate-project/)), the signal is scale-through-infrastructure, not lightweight SaaS expansion.

Even adjacent leaders reinforce the same pattern. Apple said fiscal 2025 capped at a record $416 billion in revenue ([Apple Q4 FY2025 release](https://www.apple.com/sn/newsroom/2025/10/apple-reports-fourth-quarter-results/)), while NVIDIA reported fiscal 2025 revenue of $130.5 billion, up 114 percent, with data-center revenue up 142 percent for the year ([NVIDIA FY2025 results](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/default.aspx)). Different business models, same directional pressure: AI demand is real, and the limiting factors are increasingly capital, infrastructure, and execution discipline.

## The real pivot: software creation is being deflated

The most important shift for operators is not whether the Nasdaq rerates. It is that the first draft of software is becoming cheaper and faster.

That has two immediate implications.

First, many product surfaces will commoditize faster than teams expect. If a feature can be rebuilt quickly by competitors using common model capabilities, feature velocity alone is not a moat.

Second, volume of change will rise faster than many organizations' ability to govern risk.

This is where the debate gets subtle. AI can simultaneously increase local coding speed and degrade system-level delivery outcomes if quality systems are not upgraded. DORA 2024 observed that higher AI adoption was associated with estimated declines in throughput and stability in its dataset ([Google Cloud DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)). That should not be read as "AI hurts engineering" in general. It should be read as "speed without adaptive governance can create fragility."

In other words, commoditization of creation does not commoditize trust. Trust gets harder.

## Where value is relocating

Once build cost starts falling structurally, value pools move up the stack.

They move toward quality capture: the ability to release frequently while sustaining reliability, security, and compliance.

They move toward integration depth: controlling real workflows rather than shipping standalone AI features.

They move toward infrastructure leverage: securing enough compute and power to sustain iterative learning loops.

This relocation logic explains why some AI-native organizations seem to compound and others look busy but stagnant. Being "AI-enabled" is not the same as being "AI-native." The difference is whether AI is embedded in a measurable closed loop from decision to outcome.

## A pragmatic lens for leaders

Stop debating labels. Classify every initiative by *economic behavior* and *failure cost*, then execute the matching playbook.

Gate funding for every AI initiative with these three checks:

1. If it fails, is the loss mostly efficiency, trust, or strategic lockout?
2. Is the binding constraint execution, quality control, or infrastructure capacity?
3. Can you reverse it within one quarter, or does it create multi-year lock-in?

Use the table below as an execution matrix.

| Initiative class | Execute for | Typical use-cases | Assume this constraint | Treat failure as | Assign ownership | Fund using | Operate with this cadence | Track these metrics | Block these failure modes | Scale only when |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Commodity acceleration** | Drive unit-cost and cycle-time compression in low-differentiation workflows | Internal scaffolding; documentation and knowledge workflows; support-assist; repetitive back-office flows | Adoption friction and execution discipline, not deep technical unknowns | Efficiency leakage; usually reversible within one quarter | Put the functional leader closest to the workflow in charge; keep central standards lightweight | Use an efficiency budget with short payback thresholds and explicit stop rules | Ship in short cycles; prune aggressively; replace weak pilots fast | Cost per task; cycle-time reduction; throughput per FTE; sustained adoption depth; abandonment rate | Do not over-govern simple workflows; do not build heavyweight platforms for tactical wins; do not confuse experiment volume with realized savings | Scale after you demonstrate repeatable savings across multiple teams with minimal reliability side-effects |
| **Quality-constrained** | Raise capability without sacrificing trust, safety, reliability, or compliance posture | AI-assisted coding in mission-critical systems; high-stakes decision support; customer-facing automation with liability exposure | Governance quality, verification depth, and operational risk control | Trust damage, incident spikes, legal/compliance exposure, and expensive rollback programs | Enforce joint accountability across product, engineering, security, SRE/operations, and risk/compliance | Tie funding to reliability objectives, control requirements, and evidence obligations | Roll out in stages with hard quality gates, escalation thresholds, and rollback authority | Change failure rate; MTTR; incident severity distribution; control compliance pass rate; customer trust and complaint indicators | Do not manage by output-only metrics (tickets, prompts, LOC); do not release before controls mature | Scale after you prove velocity gains with stable or improving reliability and security indicators |
| **Infrastructure-constrained** | Convert AI demand into durable value under compute, power, and deployment limits while avoiding lock-in traps | High-scale inference surfaces; low-latency multi-region services; edge-plus-cloud industrial deployments | Capacity availability, utilization quality, and partnership structure | Strategic lockout, margin compression, or roadmap failure from constrained capacity and dependency risk | Run shared ownership across business, engineering, finance, procurement, and legal | Use multi-horizon capacity planning and scenario-based commitments, not quarter-only tooling spend | Tie roadmap releases to capacity milestones, utilization quality, and resilience targets | Workload economics per unit compute; utilization efficiency; peak resilience; dependency concentration; capacity-to-revenue conversion | Do not treat infrastructure as late procurement; do not sign rigid commitments without validated demand quality | Scale after you prove capacity-to-outcome conversion and resilient operations under peak demand and provider stress scenarios |

### Most portfolios are mixed, not pure

Expect initiatives to migrate classes over time. A support copilot can start as commodity acceleration and become quality-constrained once it touches billing or policy decisions. A product feature can start as execution-led and become infrastructure-constrained at scale.

Reclassify every initiative quarterly; do not lock classification at kickoff.

### Portfolio implication

Do not optimize for initiative count. Optimize for governed conversion of spend into durable outcomes.

Run fast where risk is low. Run controlled where trust is fragile. Run deliberate where capital lock-in is high.

Do not apply one operating model to all three classes.

## What to watch over the next 24 months

The next phase will be determined less by model demos and more by conversion quality. Five signals are especially informative.

1. Whether AI-linked revenue and workflow outcomes keep pace with infrastructure and capex intensity.
2. Whether organizations can improve deployment speed without worsening reliability metrics.
3. Whether inference cost gains actually translate into product-level margin improvements.
4. Whether power and capacity constraints slow iteration cadence for non-hyperscaler players.
5. Whether buyers reward integrated outcome systems over generic AI feature bundles.

If these move in the right direction together, the platform-shift thesis strengthens.

If they diverge, valuation correction risk rises even if core AI capability keeps improving.

## If the market rerates, what still survives?

A useful way to pressure-test strategy is to ask what remains true under a sharp multiple compression scenario.

If public and private valuations reset, many AI narratives will disappear quickly, especially those built around distribution-light feature bundles. But the underlying cost and workflow shifts would not disappear just because sentiment changes. Teams would still have access to faster software generation. Developers would still use AI assistance in daily workflows. Inference economics would still likely be structurally better than they were two years ago. The mix of winners might change, but the direction of technical leverage would remain.

This distinction matters because it separates cyclical pain from structural progress. Cyclical pain changes funding conditions, hiring plans, and risk appetite. Structural progress changes competitive baselines permanently. Good strategy must survive both.

That is why the strongest posture in this phase is neither maximal aggression nor defensive paralysis. It is selective commitment: invest heavily where your evidence of durable capture is strongest, and stay modular where differentiation is weak.

In practice, this means many organizations should stop treating all AI initiatives as one portfolio. Some initiatives are tactical productivity upgrades and should be managed as cost programs. Some are strategic platform bets and should be managed with multi-year quality and infrastructure planning. Mixing these under one metric system leads to bad capital decisions.

## The uncomfortable middle: speed is easy, trust is expensive

The hardest part of this cycle is that it rewards velocity early and punishes weak systems later.

Early in adoption, AI often produces visible wins quickly: faster prototyping, shorter draft cycles, and apparent productivity gains. Those benefits are real, and teams that ignore them fall behind. But as usage deepens, hidden costs surface: unstable releases, security regression, compliance overhead, and integration debt. This is exactly why the productivity narrative and the fragility narrative can coexist in the same organization.

Leaders who only see the first phase over-expand into weakly defended surfaces. Leaders who only see the second phase underinvest and lose learning velocity. The disciplined middle is to accelerate with explicit quality gates and evidence loops from day one. That posture is less dramatic, but it compounds.

The market tends to overprice drama and underprice discipline. That is an opportunity for operators.

## Why this matters beyond software companies

It is tempting to treat this as a \"tech-sector\" story. It is broader than that.

As AI moves from productivity tooling into operational decision systems, sectors like manufacturing, energy, logistics, and mobility inherit these same dynamics: creation costs fall, but trust requirements rise; model access broadens, but integration and infrastructure remain uneven. Firms that own real workflows and can prove outcomes will capture disproportionate value even if they are not model builders.

This is also why infrastructure and policy choices are increasingly entangled with competitive outcomes. Power access, siting, and grid readiness are no longer abstract macro topics; they influence how quickly organizations can iterate, validate, and scale AI-enabled operations. Strategy teams that ignore this connection will misread their actual execution constraints.

## The strategic error patterns already visible

Across markets, the same errors keep appearing.

One is mistaking model access for defensibility.

Another is celebrating output metrics while ignoring reliability and adoption metrics.

A third is treating infrastructure dependency as procurement detail rather than strategy risk.

And a fourth is confusing capital abundance with product-market proof.

These errors are expensive because they hide until scale.

## Bottom line

This cycle is best understood as a real platform transition wrapped in a volatile capital regime.

That framing is uncomfortable because it requires two beliefs at once: yes, there are bubble-like excesses; and yes, the underlying software economics are changing for good.

For operators, that is actually clarifying. You do not need to predict market timing. You need to build where scarcity is moving.

That means treating baseline code generation as increasingly abundant, and treating quality systems, workflow integration, and infrastructure realism as the true sources of durable advantage.

## Bridge to Part 2

Part 2 goes deeper on the first and most immediate scarcity: quality capture.

If software creation is being commoditized, then reliability, security, and evidence become the new moat. The teams that can close that loop fastest will outperform, regardless of short-term market sentiment.

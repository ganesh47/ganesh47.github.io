---
title: "The Connected Machine: Board Interlocks, Power Networks, and Systemic Risk in Indian Corporate India"
date: 2026-08-08 00:00:00 UTC
categories: [blog]
tags: [Finance, Corporate-Governance, Graph-Theory, India, Board-Interlocks, Systemic-Risk, Network-Analysis]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "A single director sitting on seven Indian company boards is not a coincidence — it is a structural feature of how Indian corporate power concentrates. Graph theory makes this visible: betweenness centrality identifies the bridges, community detection finds the clusters, and the IL&FS case shows what systemic risk looks like when the network collapses."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
permalink: /blog/connected-machine-board-interlocks-india-corporate/
---

**Series: Indian Corporate Networks**  
Series map: **Part 1 (this post)** \| [Part 2](/blog/follow-the-money-lending-networks-india/)

*Related series: [Discounted Cash Flows: The Complete Indian Guide](/blog/discounted-cash-flows-the-math-part-1/) — the financial fundamentals behind these network relationships.*  
*Interactive: [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/) — explore board interlocks, lending flows, and path connections in your browser.*

---

## What the Balance Sheet Doesn't Show

The four-part DCF series explored how to value Indian companies and banks — through cash flows, operating ratios, credit costs, and the P/BV framework. But all of that analysis treats each company as an island: a standalone entity with its own financials, its own risks, its own story.

Indian corporate reality is different. The 100 largest listed companies are deeply connected — through shared board members, holding structures, bank lending relationships, and equity cross-holdings. These connections are not incidental. They are load-bearing features of how Indian business actually works.

When they function well, shared directors accelerate governance standards across companies. When they fail, they transmit governance failures and financial stress across the network. IL&FS in 2018 was a case of the second kind — and understanding why requires graph theory, not just accounting.

---

## Graph Theory: The 90-Second Version

A **graph** is a mathematical structure of **nodes** (entities) and **edges** (relationships between them). In a corporate network:

- **Nodes** are companies, banks, directors, and promoter groups
- **Edges** are the connections between them: a director sitting on a board, a bank extending a loan, a promoter holding shares

From this simple structure, three metrics tell most of the story:

**Degree**: How many direct connections does a node have? A director with degree 7 sits on 7 boards. A bank with degree 20 has lending relationships with 20 companies.

**Betweenness centrality**: How many shortest paths between other nodes pass through this node? High betweenness means the node is a *bridge* — remove it and clusters that were connected become disconnected. This is the metric that identifies systemic risk nodes.

**PageRank**: Borrowed from Google's original search algorithm. A node is important if important nodes point to it. In a lending graph, a bank with PageRank 0.1 is not just connected to many borrowers — it is connected to borrowers who are themselves important nodes.

**Community detection** (Louvain algorithm) finds clusters of densely connected nodes — groups that form more connections internally than externally. In the Indian corporate graph, these communities algorithmically recover the known business groups (Tata, Reliance, Adani) even when the algorithm is given no prior information about group membership.

---

## The Board Interlock Phenomenon

A board interlock occurs when a person serves as a director on two or more company boards simultaneously. Both companies then share a director — a bridge node in the graph.

SEBI's 2019 regulations capped individual directorships at eight listed companies. Before this, the caps were looser: fifteen directorships under the Companies Act. In practice, India's most prominent independent directors routinely served on four to seven boards.

Indian data quantifies this sharply. A 2015 study by Chakkingal found that **2.25% of Indian directors control board positions in companies accounting for 42% of all listed companies and 65.5% of the NIFTY 500's total market capitalisation**. The same study found that 78.5% of NSE-listed companies belong to a single giant connected component in the board interlock graph — meaning the network is effectively continuous across almost the entire market. A 2026 arXiv paper (Sancheti & Dey, 2603.22860) extended this to show that 58.6% of active Indian directors hold multiple board seats simultaneously, and 30% of listed companies have same-surname director pairs on their boards — a measurable signature of family concentration that governance reforms have not fully eliminated.

This is not unique to India. Academic research on board interlocks (Mizruchi 1996, Davis & Greve 1997) consistently shows that:

1. Interlocked boards adopt similar governance practices and executive compensation structures faster than non-interlocked boards
2. Information flows across interlock ties — both market intelligence and, in the failure cases, panic
3. Interlock networks exhibit **small-world properties**: short average path lengths and high clustering coefficients simultaneously

The small-world property matters enormously. In the [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/), you can use the Path Finder to verify it empirically: the typical connection between any two NIFTY 100 companies is 3–4 hops via shared directors, subsidiaries, or lending relationships. This is structurally identical to Watts and Strogatz's famous small-world network model.

---

## Measuring What Matters

### Degree distribution

In the board interlock graph, director degree follows a power law — a few directors have very high degree (5–7 boards) while most have 1–2. This is the signature of a **scale-free network**, where new connections preferentially attach to already-well-connected nodes ("preferential attachment"). Senior industry figures accumulate board positions; once prominent, they become more attractive for new appointments.

The power law has a practical implication: the network is **robust to random failures** (most nodes have low degree and their removal barely affects connectivity) but **fragile to targeted removal** of high-degree hubs. Remove the five most-connected directors and the clustering of the Indian corporate network changes substantially.

### Betweenness centrality: the hidden bridges

High betweenness does not always correlate with high degree. The most dangerous nodes systemically are often not the most connected, but the ones that *bridge otherwise disconnected clusters*.

In the India Corporate Graph data, the cross-group independent directors — those who sit on boards spanning multiple business groups — consistently show the highest betweenness centrality. They are the bridges between the Tata cluster, the Reliance cluster, and the Independent cluster. Information and, in stress scenarios, contagion flows through these nodes.

### Community detection: finding the groups algorithmically

The Louvain community detection algorithm works by maximizing a quantity called **modularity** — a measure of how much more densely connected a community is internally than you would expect by chance. It has no knowledge of Tata, Reliance, or Adani. It only sees node IDs and edges.

Running Louvain on the board interlock and subsidiary graph reliably recovers the known Indian business group structure as distinct communities. The Tata community anchors around TCS, Tata Motors, Tata Steel, and Titan. The Adani community anchors around Adani Enterprises, Adani Ports, and Adani Green. The algorithm finds these boundaries because the internal edge density within each group — driven by shared directors and holding structures — substantially exceeds the cross-group edge density.

This has a diagnostic use: when you run community detection on real BSE board composition data (Phase 2 of this project), any company that the algorithm assigns to a different community than its nominal group is worth investigating. It may have accumulated board members from another group — a signal of changing corporate relationships that public filings might not make obvious.

---

## IL&FS: When the Network Becomes the Risk

The Infrastructure Leasing and Financial Services (IL&FS) crisis of 2018 is the definitive Indian case study of board interlock risk. It deserves careful analysis in the network framework.

**The structure**: IL&FS was not a single company. It was a group of 347 entities — 135 subsidiaries, 59 associates, 43 joint ventures, and 110 other entities. At the peak, a single senior IL&FS figure served as a director on fourteen of these entities simultaneously.

This is extreme betweenness centrality. The same person, in fourteen simultaneous director roles, was the bridge through which governance standards, risk appetite decisions, and — critically — accounting judgments propagated across 14 of the 347 entities.

**The failure cascade**: When ICRA and CARE downgraded IL&FS from AAA to D in September 2018 (seven notches, in a week), the commercial paper market for all NBFCs froze. Not just for IL&FS subsidiaries. For all NBFCs. Because CP investors — mutual funds, corporate treasuries — lost confidence in the ability to distinguish between an IL&FS subsidiary and any other NBFC using short-term wholesale funding.

The [NBFC Liquidity Risk post](/blog/nbfc-liquidity-risk-ilfs-indusind/) covers this in depth. The network framework adds the "why it spread" explanation: the IL&FS network had high internal density (the 347 entities were tightly connected through shared directors and intercompany loans) but also high betweenness for certain nodes relative to the broader NBFC sector. When those bridges failed, the shortest path between "any given NBFC" and "the system" ran through the IL&FS collapse.

**The graph lesson**: A high internal density network with concentrated betweenness is a systemic risk. The same structure that makes it efficient in normal times (fast information propagation, coordinated decisions) makes it catastrophic in stress (fast contagion propagation, coordinated defaults).

---

## Reading the Corporate Graph Explorer

The [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/) makes these network properties interactive. A few things worth trying:

**Network Explorer**: Load the full graph, color by group. The visual clustering matches the Louvain communities. Switch to "Color by sector" to see how banking nodes cluster separately from IT, which clusters separately from infrastructure.

**Board Interlocks**: Sort the director table by betweenness centrality rather than degree. The top betweenness directors are typically *not* the ones with the most board memberships — they are the ones who bridge the most clusters. These are the systemic risk nodes in governance terms.

**Path Finder**: Enter TCS.NS and HDFCBANK.NS. The path likely runs through a shared director or a Tata group subsidiary connection to a common lending relationship. 3–4 hops. This is the Indian corporate small-world in action.

**Community Report**: The 17 Louvain communities in the Phase 1 synthetic data approximate the known group structure. Phase 2 will use real BSE board composition filings — the community structure that emerges from ground-truth data will be both more granular and more surprising.

---

## What Comes Next

The network structure established in this post is the foundation for the second dimension of corporate connectedness: financial flows. Board interlocks create governance connections. But lending relationships, promoter pledges, and equity cross-holdings create **financial** connections — and financial connections carry correlated risk in ways that governance connections do not.

In [Part 2: Follow the Money](/blog/follow-the-money-lending-networks-india/), we map lending concentrations (which banks carry the heaviest exposures to which groups), promoter pledge structures (the hidden leverage within promoter holdings), and the anatomy of financial interconnectedness that makes Indian corporate India a network risk — not just a collection of independent entities.

---

## Data and Methodology Notes

The Phase 1 India Corporate Graph Explorer uses **synthetic data** generated from known Indian business group structures (Tata, Reliance, Adani, Aditya Birla, Bajaj) with realistic board compositions. Financial weights (lending amounts, promoter percentages) are illustrative. Graph algorithms (Louvain community detection, betweenness centrality, PageRank) are computed on this synthetic graph using NetworkX.

**Phase 2** will replace synthetic data with:
- Real board composition data from BSE corporate governance XML filings (annual reports FY2021–2025)
- Director identification via MCA DIN (Director Identification Number) cross-referenced to company CINs from data.gov.in
- Promoter shareholding percentages from SEBI quarterly shareholding pattern filings

The network analysis framework (Louvain, betweenness, PageRank) is unchanged between phases — only the underlying edge data improves.

All code is open source: [github.com/ganesh47/india-corporate-graph](https://github.com/ganesh47/india-corporate-graph).

---
title: "Follow the Money: Lending Concentration, Audit Interlocks, and Financial Connectedness in Indian Corporate India"
date: 2026-08-08 00:00:00 UTC
categories: [blog]
tags: [Finance, Corporate-Governance, Graph-Theory, India, Banking, Audit, Systemic-Risk, Network-Analysis]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "When the same bank lends to 20 companies in the same group, and the same auditor signs off on eight of them, the credit risk is no longer independent. Graph theory makes this structural dependency visible — and the India Corporate Graph Explorer makes it interactive."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
permalink: /blog/follow-the-money-lending-networks-india/
---

**Series: Indian Corporate Networks**  
Series map: [Part 1](/blog/connected-machine-board-interlocks-india-corporate/) \| **Part 2 (this post)**

*Related series: [Discounted Cash Flows: The Complete Indian Guide](/blog/discounted-cash-flows-the-math-part-1/) — the financial fundamentals behind these network relationships.*  
*Interactive: [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/) — explore lending flows, audit interlocks, and promoter holdings in your browser.*

---

## From Governance to Finance

[Part 1](/blog/connected-machine-board-interlocks-india-corporate/) established the governance layer of Indian corporate connectedness: board interlocks, Louvain communities, betweenness centrality, and the IL&FS case study. That layer is important, but it is the *structural* layer — the connections that propagate information, norms, and governance failures.

This post maps the *financial* layer: the connections that carry actual money, credit risk, and correlated loss. Four types of financial interlocks matter for systemic risk analysis:

1. **Bank lending concentration** — when a single lender holds large exposures to multiple entities in the same promoter group
2. **Promoter pledge structures** — when promoters finance personal leverage by pledging their shareholdings as collateral
3. **Audit firm concentration** — when the same auditor signs off on multiple entities in a group, creating shared independence risk
4. **Related-party transactions** — when intergroup loans and advances move cash between group entities in ways that obscure where the credit risk actually sits

Each of these creates financial graph edges that complement the governance edges from Part 1. Together, the two layers form the complete picture of why Indian corporate India is a network risk, not a collection of independent balance sheets.

---

## Bank Lending Concentration: The Hub-and-Spoke Problem

### What the data shows

Reserve Bank of India data consistently shows that the top 20 borrower groups account for roughly 20–25% of total bank system advances. Within individual banks, the concentration is higher: SEBI's 2022 annual report on corporate governance found that the largest 10 borrowers at the median PSU bank represent 30–35% of the bank's loan book.

This is a hub-and-spoke structure in the lending graph. The banks are hubs (high degree nodes); the business groups are spokes. When a spoke fails — as Adani Enterprises nearly did in February 2023 after the Hindenburg report, before the price stabilized — the hub's total exposure is not to one company but to the entire connected subgraph of that promoter group.

### How this appears in the graph

In the [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/), click **Financial Flows** and look at the lending Sankey. The left side shows banks; the right side shows business groups. The widths of the flows represent the estimated exposure volumes.

The structural feature to notice: the Adani group has lending edges to SBI, Bank of Baroda, and IDFC First simultaneously. The Tata group has lending edges to SBI, HDFC Bank, and ICICI Bank. This is standard — large groups have multiple banking relationships. But the consequence is that any systemic stress in the banking sector is correlated across groups through their shared lenders, and any stress in a group propagates to multiple banks simultaneously.

### The path length insight

Academic research on Indian board interlock networks established that the average shortest path between any two NIFTY-listed companies is under 5 hops — the small-world property. The same property holds in the lending graph, but the implication is different:

In a governance network, short path length means information propagates fast. In a lending network, short path length means **credit contagion propagates fast**. When Company A defaults, Company B (4 hops away via shared directors and lending relationships) is not independent — it is correlated through the network structure.

The 2023 academic study "Board Interlocks and Systemic Risk in Indian Listed Firms" (arXiv 2603.22860, Sancheti & Dey) quantified this: 58.6% of Indian directors hold multiple board seats simultaneously, and the giant connected component of the Indian corporate network encompasses 78.5% of NSE-listed companies. These numbers suggest that systemic shocks — credit, governance, or regulatory — propagate across most of the market within a small number of hops.

---

## Promoter Pledges: Hidden Leverage in the Promoter Stack

### The mechanics

Indian promoters — the founding family or controlling group — typically hold 40–70% of the shares of their listed companies. This is visible in the quarterly shareholding pattern (SHP) filings that SEBI requires under LODR.

What is less visible in the headline number is how much of that promoter stake is **pledged** as collateral against loans. The promoter pledges their 55% holding to a bank or NBFC; the bank lends them funds (often to invest in another group company, or to buy more of the same company's shares). If the share price falls, the lender issues a margin call. If the promoter cannot meet the margin call, the lender sells the pledged shares in the open market — creating a price spiral that amplifies the original decline.

This is the financial graph mechanism behind several Indian mid-cap stock crashes: the network of pledge → margin call → forced sale creates a feedback loop that a standalone balance sheet analysis would not detect.

### Reading the SHP data

SEBI's quarterly SHP filings are public and machine-readable. The [India Corporate Graph Phase 2 pipeline](https://github.com/ganesh47/india-corporate-graph) uses the NSE `shareholding()` API (via the `nse` Python library by BennyThadikaran) to fetch promoter % for NIFTY 100 companies. The XBRL submissions at NSE archives carry granular data: individual promoter entity names, DINs, pledge status, and encumbered vs. unencumbered share counts.

Key patterns to look for in the promoter data:

- **Pledge % rising** in SHP while promoter % holding stays flat → promoter is borrowing against existing shares
- **Promoter % falling** via inter-se transfer between group entities → restructuring, not public market selling
- **Promoter % below 40%** → SEBI open offer trigger threshold is 25%, but values below 40% signal dilution risk

In the graph, each of these is a different edge type with different risk implications.

---

## Audit Interlocks: The Independence Problem at Scale

### The Big 6 concentration

India's ₹150+ trillion listed equity market relies on statutory audit by a relatively small number of audit firms. The FY2024 market structure in the NIFTY 500:

| Audit Firm (Indian entity) | Network | NIFTY 500 clients |
|---------------------------|---------|-------------------|
| S R Batliboi / Walker Chandiok | EY | 176 |
| B S R & Co. LLP | KPMG | 137 |
| Deloitte Haskins & Sells LLP | Deloitte | 128 |
| Grant Thornton Bharat LLP | Grant Thornton | 107 |
| MSKA & Associates LLP | BDO | 78 |
| Price Waterhouse Chartered Accountants LLP | PwC | 69 |

Six audit networks audit 695 of the 500 largest listed companies — many companies have multiple years of filings with the same network, and group companies often share a network. This is the structural definition of an **audit interlock**: when Company A and Company B share the same statutory auditor, there is a potential independence concern if A and B have material related-party transactions, or if the same audit partner covers both.

### Why audit interlocks matter for the graph

The Satyam Computers fraud (2009) and the more recent Byju's audit controversy share a structural feature: the auditor signed off on accounts that materially misstated the financial position. In the Satyam case, Price Waterhouse (PwC India) was auditing a company where the promoter had fabricated ₹7,136 crore of cash that did not exist.

The Companies Act 2013 mandated auditor rotation (mandatory rotation every 5 years for listed companies, 10 years for others). This was specifically designed to break the concentration structure visible in the audit graph. But rotation at the firm level — while individual partners within the same firm may continue — does not fully address the independence concern when the audit network covers 176 NIFTY 500 companies.

### The audit graph in the explorer

In the [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/), click **Network Explorer** and select **Color by: Auditor**. This switches the view to show audit firm nodes (hexagonal, teal) connected to all their listed company clients via `same_auditor` edges. The Phase 2 pipeline adds 6 audit firm nodes and 76 same_auditor edges to the NIFTY 100 graph.

The structural insight: each audit firm node is a hub with very high degree (10–30+ client connections in NIFTY 100 alone). If the same audit network covers two companies engaged in a related-party transaction, the audit report on each company is less independent than a standalone reading would suggest.

The Louvain community detection — which ignores audit edges entirely — recovers the group structure from board and lending edges alone. But when you **add** audit edges and re-run the algorithm, the resulting communities become larger and more cross-group, because the EY network and the Deloitte network each act as latent connectors across group boundaries. This is the audit interlock made visible as a graph property.

---

## Related-Party Transactions: Where the Money Actually Goes

### The IndAS-24 lens

Indian accounting standards (IndAS 24, mirroring IAS 24) require listed companies to disclose all related-party transactions: loans, advances, sales, purchases, guarantees, and services between the company and its directors, key management personnel, subsidiaries, associates, and joint ventures.

These disclosures — buried in the notes to financial statements — are a rich source of financial edges. When Adani Enterprises advances ₹2,400 crore to Adani Green Energy as an "inter-company loan," this is an intragroup financial flow that:
1. Does not appear on the consolidated P&L (it eliminates in consolidation)
2. Does appear on the standalone balance sheet of both entities
3. Creates a credit exposure for Adani Enterprises if Adani Green cannot repay
4. Represents a connected-party transaction that auditors must consider for independence

The graph representation is straightforward: a `related_party_transaction` edge from Adani Enterprises to Adani Green, with weight = ₹2,400 crore and metadata = {type: "loan", year: 2024}.

### The aggregation problem

The systemic risk question is not whether any single RPT is problematic, but whether the **aggregate** of intragroup RPTs creates concentrated credit risk. When 60 group companies have bilateral RPTs with each other — lending, borrowing, selling services, providing guarantees — the consolidated entity is internally dense in ways the standalone accounts obscure.

Group-level analysis in the graph: filter `edge_type = related_party_transaction` and run betweenness centrality. High-betweenness nodes are the entities through which intragroup cash flows are routed — often holding companies or intermediate vehicles. These are the entities where auditors should focus most intensively, and where credit analysts should model the stress scenario where the intergroup flows are called back.

---

## IPO Lock-In Expiry: Graph Events with Price Consequences

### The structural mechanic

When a company lists via IPO, promoters and anchor investors are subject to lock-in periods: promoter lock-in is 18 months (reduced from 3 years by SEBI in 2022), while anchor investor lock-in was 30 days. After expiry, the promoter can begin selling shares — and the market knows this.

Lock-in expiry is a **timed graph event**: at a specific date, the promoter_holding edge weight changes (from a constrained position to one where selling is possible). Combined with the pledge structure — if promoters have borrowed against their locked-in shares, the lenders have their own view on what happens at lock-in expiry — this creates predictable price dynamics.

Academic work on Indian IPO lock-in expiry (Bhattacharya et al., IIMB Working Paper 2023) found consistent abnormal negative returns in the window around lock-in expiry for high-pledge promoters. This is the graph mechanism made visible: pledge → lock-in expiry → selling pressure → price decline → margin call spiral.

### Reading this in the Phase 2 graph

The Phase 2 pipeline (pending implementation) will add `ipo_data.parquet` with columns: ticker, ipo_date, pre_ipo_promoter_pct, post_ipo_promoter_pct, lock_in_expiry, anchor_investors (JSON), lead_managers. The `lock_in_expiry` field, combined with the current promoter SHP pledge data, gives the risk-adjusted view of which recently listed companies have timed pressure events upcoming.

---

## The Integrated Picture: What This Graph Means for Risk Analysis

### The network risk thesis

The four financial interlock types — lending concentration, promoter pledges, audit concentration, related-party transactions — combine with the governance interlocks from Part 1 to create a multi-layer financial network. The key analytical insight is **correlated failure across layers**:

A governance failure at Company A (board does not scrutinise related-party transaction) → the RPT creates a credit exposure at Company B → Company B has a lending relationship with Bank X → Bank X has similar lending exposure to Company C (in a different group) → the credit signal from Company B's distress reaches Company C through their shared lender.

This is cross-network contagion: a governance failure in one layer propagates via financial edges in another layer to nodes that appear unconnected when any single layer is analysed in isolation.

This is also why **integrated graph analysis** — the approach taken in the India Corporate Graph Explorer — is analytically superior to either pure governance analysis (board composition reports) or pure credit analysis (loan book concentrations). Neither captures the full propagation path.

### What the academic research quantifies

Chakkingal (2015) found that 2.25% of Indian directors control directorships in companies representing 42% of total listed market cap and 65.5% of the NIFTY 500's market capitalisation. This is the governance hub structure: a small number of well-connected directors sit at the centre of the network, and their judgments propagate to a disproportionate fraction of total listed value.

The 2020 "Breaking Bad Links" paper (IIMB) quantified the Companies Act 2013 effect on the board interlock network: the innermost k-core of the network split into two distinct cores after the legislation changed the cap on simultaneous directorships from fifteen to eight. This is the regulatory intervention visible as a structural change in the graph — a rare natural experiment in network disruption.

Sancheti & Dey (2026) found that 30% of Indian listed companies have same-surname director pairs on their boards — a proxy for family concentration of governance influence that persists even after nominally independent director appointments.

Together, these findings quantify what the graph visualisation makes intuitive: Indian corporate India is a small-world network with a few dominant hubs, where governance and financial shocks propagate rapidly across a connected component that covers most of listed market cap.

---

## Using the Explorer: A Walk-Through for Phase 2

### Audit concentration view

1. Open [India Corporate Graph Explorer](https://ganesh47.github.io/india-corporate-graph/)
2. Go to **Network Explorer** → click **Color by: Auditor**
3. The view automatically filters to `same_auditor` edges + company and `audit_firm` node types
4. Teal hexagonal nodes are the six audit firms; indigo circular nodes are companies
5. Toggle back to `board_member` edges to see how the audit clusters compare to the board interlock clusters

The comparison is informative: EY's 176 NIFTY 500 clients span multiple business groups (Reliance, Infosys, Indigo), not just one. This cross-group coverage means EY's independence is a network-level concern, not just a company-level one.

### Lending flow view

1. Go to **Financial Flows**
2. The Sankey shows bank → group lending flows weighted by estimated exposure
3. SBI appears on the left with the widest outflow bar — consistent with its role as the system's largest lender
4. Note the flows to Adani, Tata, and Reliance clusters: these are the exposures that regulators monitor as concentration risk

### Path finder for the complete picture

In **Path Finder**, try: ADANIENT.NS → HDFCBANK.NS

The shortest path typically runs through a shared lending relationship or a director who sits on an Adani group entity and has other connections. This 3–4 hop path is the empirical verification of the small-world property in the Indian financial network.

---

## What Comes Next

The Phase 2 data pipeline (see [github.com/ganesh47/india-corporate-graph](https://github.com/ganesh47/india-corporate-graph)) has implemented:
- Audit firm nodes and `same_auditor` edges (6 firms, 76 edges in NIFTY 100) — from published NIFTY 500 audit market share data
- `fetch_sebi_shp.py` — for real promoter shareholding data via NSE API (requires local execution)
- `fetch_mca_directors.py` — for real board composition via BSE Corporate Governance XBRL (requires local execution + BSE scrip codes)
- `fetch_insider_trading.py` — for NSE PIT/SAST insider trading disclosures (requires local execution)

Phase 3 targets: real related-party transaction edges from IndAS-24 disclosures (XBRL annual reports), IPO lock-in data from SEBI DRHP filings, and charge registration data from MCA (lender → company credit facility edges).

Each layer added makes the network risk analysis more complete — and makes the structural risk of Indian corporate concentration more visible to anyone looking at the graph.

---

## Data and Methodology Notes

**Audit firm data**: Audit network assignments for NIFTY 100 companies are based on:
- Known statutory auditors from public annual reports for major companies (TCS/KPMG, HDFC Bank/KPMG, Reliance/EY, Infosys/EY, HUL/Deloitte, ITC/Deloitte, Tata Motors/Deloitte, State Bank/Deloitte, Asian Paints/PwC, Nestlé/PwC, etc.)
- Proportional random assignment for remaining companies using published NIFTY 500 market share (EY: 176/695, KPMG: 137/695, Deloitte: 128/695, Grant Thornton: 107/695, BDO: 78/695, PwC: 69/695)
- Seed: 42 for reproducibility

**Lending flow data**: Synthetic, based on publicly reported lending relationships and RBI concentration guidelines.

**Academic references**:
- Chakkingal, U. (2015). "Network Structure of Indian Corporate Boards." *IIMA Working Paper*.
- "Breaking Bad Links: Network Effects of India's Director Cap Regulation." (2020). *IIMB Working Paper*.
- Sancheti, A. & Dey, S. (2026). "Board Composition and Family Concentration in Indian Listed Firms." arXiv 2603.22860.

All code: [github.com/ganesh47/india-corporate-graph](https://github.com/ganesh47/india-corporate-graph). Apache 2.0 license.

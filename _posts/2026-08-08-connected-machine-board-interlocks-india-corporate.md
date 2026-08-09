---
title: "The Connected Machine: What 100 Indian Boards Reveal About Corporate Power"
date: 2026-08-08 00:00:00 UTC
last_modified_at: 2026-08-09 00:00:00 UTC
categories: [blog]
tags: [Finance, Corporate-Governance, Graph-Theory, India, Board-Interlocks, Systemic-Risk, Network-Analysis]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "A verified snapshot of all 100 NIFTY 100 boards turns corporate governance into a network: 954 current appointments, 33 multi-board directors, and 17 company pairs sharing at least two directors."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
permalink: /blog/connected-machine-board-interlocks-india-corporate/
---

**Series: Indian Corporate Networks**
Series map: **Part 1 (this post)** \| [Part 2](/blog/follow-the-money-lending-networks-india/)

*Related series: [Discounted Cash Flows: The Complete Indian Guide](/blog/discounted-cash-flows-the-math-part-1/) — the financial fundamentals behind these relationships.*
*Interactive: [Board Interlocks](https://ganesh47.github.io/india-corporate-graph/#/board-interlocks) \| [Network Explorer](https://ganesh47.github.io/india-corporate-graph/#/network) \| [Path Finder](https://ganesh47.github.io/india-corporate-graph/#/path-finder)*

---

## A Snapshot, Not a Universal Census

A balance sheet describes a company. It does not describe the people and institutions connecting that company to the rest of the market.

The India Corporate Graph now starts with a pinned list of the [NIFTY 100 constituents published by NSE](https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv), retrieved for a **9 August 2026 snapshot**. Each company board was then checked against a primary source: an issuer board page, an issuer-hosted annual or corporate-governance report, or an official NSE Integrated Filing–Governance record.

The resulting board layer contains:

- **100 of 100 reviewed company rosters**
- **40 current-source rosters** and **60 fallback rosters**, visibly labelled in the product
- **911 published director identities**
- **961 appointment observations**, of which **954 are current at the cited source period** and 7 are recently ceased
- **905 identities holding at least one current seat**

Those numbers need two qualifications. First, “fallback” means that a complete primary roster was available, but it was older than the preferred quarter ending 30 June 2026. It does not mean the roster was guessed. Second, 579 identities are deliberately company-scoped because the source did not disclose a usable DIN. They are **not merged by name alone**. Consequently, 911 is a count of published identity records, not a claim that every natural person has been globally deduplicated.

This is narrower—and far more defensible—than claiming to map all of corporate India.

## The Graph Theory in Plain English

The board network is a **bipartite graph**. One kind of node is a company; the other is a director. An appointment creates an edge between them.

From that simple structure, several useful measurements follow:

**Board degree** counts the distinct current boards represented for a director. It is scoped to this NIFTY 100 snapshot, not every directorship the person may legally hold.

**Betweenness centrality** measures how often a node lies on shortest routes between other nodes. In this graph it identifies structural bridges. It does not, by itself, imply influence, control, misconduct, or systemic importance.

**Company interlocks** appear when two companies share directors. The product uses a conservative display rule for its ranked table: a pair must share **at least two** current directors.

**Community detection** partitions the mixed graph into relatively dense clusters. The current Louvain run produces 75 communities across board, subsidiary, promoter-holding, and auditor relationships. Those clusters are descriptive outputs of a particular graph and time scope—not legal group classifications.

## What the Current Boards Actually Show

Of the 905 identities with current appointments, **33 appear on at least two represented boards**. The distribution is sharply concentrated:

- 872 identities appear on one board
- 23 appear on two
- 7 appear on three
- one appears on four, one on five, and one on six

Within this snapshot, Gautam S. Adani has six represented appointments, Rajesh S. Adani has five, and Rajivnayan Rahulkumar Bajaj has four. These are observations about the pinned universe, not lifetime or market-wide director counts.

The strongest company pair is **Bajaj Finserv–Bajaj Finance**, with six shared directors in the reviewed sources: Sanjiv Bajaj, Rajiv Bajaj, Pramit Jhaveri, Naushad Forbes, Anami Narayan Roy, and Radhika Haribhakti. The evidence combines the [Bajaj Finance Integrated Filing–Governance](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_GOVERNANCE_159546_21052026121304_iXBRL_WEB.html) with Bajaj Finserv’s [issuer-hosted FY2024-25 corporate information](https://www.bajajfinserv.in/finserv-digital-annual-report-fy25/corporate-information.html); the latter is marked as fallback in the dataset.

Another revealing pair comes from the post-demerger Tata Motors structure. **Tata Motors Commercial Vehicles and Tata Motors Passenger Vehicles share four directors** in their FY2025-26 reports: N. Chandrasekaran, Al-Noor Ramji, Bharat Puri, and P. B. Balaji. The underlying evidence is available in the [TMCV annual report](https://cv.tatamotors.com/assets/cv/files/AnnualReportFY26.pdf) and the [TMPV annual report filed with NSE](https://nsearchives.nseindia.com/annual_reports/AR_29395_TMPV_2025_2026_A_21445169_15062026215933.pdf).

Across the snapshot, 45 company pairs share at least one current director; **17 pairs meet the product’s two-or-more rule**. That is meaningful concentration, but it is not evidence that the board graph forms one continuous market-wide machine. The board layer has many components; the largest contains 24 companies and 187 directors.

## Why Identity Resolution Matters

Names are not safe identifiers. Initials change, names are transliterated differently, and unrelated people can share the same name. The research workflow therefore preserves an eight-character DIN—including leading zeroes—when a primary source discloses it.

For foreign or no-DIN directors, missing DINs, and the XBRL dummy value `99999999`, the identity is scoped to the company. It is never merged globally by name. The [NSE XBRL information page](https://www.nseindia.com/static/companies-listing/xbrl-information) documents the structured corporate-governance filing system, while NSE’s [Integrated Filing–Governance FAQ](https://nsearchives.nseindia.com/web/circular/2026-06/Frequently_Asked_Questions_FAQs_on_the_submission_of_the_Quarterly_Integrated_Filing_-_Governance._20260612160310.pdf) explains DIN handling and filing conventions.

This choice lowers apparent interlock counts when an identity cannot be verified, but that is preferable to manufacturing a connection. The previous research file contained 110 “other directorship” mentions. They remain excluded because the candidate seat was not independently confirmed from that company’s own primary filing.

## Roles, Dates, and the Limits of Disclosure

The 954 current appointment observations include 517 independent-director flags, 215 executive-director flags, 107 chairperson flags, and 25 promoter-coded appointments. These dimensions can overlap—a chairperson can also be executive, for example—so they should not be added into a single role total.

Only 316 current appointments disclose an appointment date in the cited source; 155 disclose a reappointment date. Missing dates are stored with an explicit reason such as `not_disclosed`, rather than filled with an invented year. The old graph’s blanket 2025 board dates have been removed.

The official governance format is much richer than many issuer pages. SEBI’s Integrated Filing–Governance table includes DIN, category, appointment or reappointment date, cessation date, tenure, directorship counts, and committee counts; Regulation 27 requires listed entities to submit the quarterly corporate-governance compliance report. See the [SEBI integrated-filing format](https://www.sebi.gov.in/sebi_data/commondocs/jun-2024/Expert%20Committee%20report%20on%20ICDR%20and%20LODR-new_p.pdf) and [NSE’s XBRL implementation circular](https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE%20Circular-%20Implementation%20of%20XBRL%20for%20disclosure%20of%20Integrated%20Filing-%20Governance.pdf).

Committee composition was not consistently verified across all 100 companies, so the published committee dataset currently has zero rows. The interface says so plainly.

## Centrality Is a Question, Not a Verdict

The most interesting director is not always the one with the most seats. Board-only betweenness currently ranks P. B. Balaji, Kosaraju V. Chowdary, and Dinesh H. Kanabar above the rest because of where their represented appointments sit in the network.

That ranking is useful for deciding where to investigate. It is not a governance score. Change the universe, include older appointments, or add a separately dated auditor or subsidiary layer, and the paths—and therefore the ranking—can change.

The same caution applies to community detection. The full published graph has **1,042 nodes and 1,107 relationship observations**: 961 board appointments, 80 annual subsidiary observations representing 16 recurring relationships across 2021–25, 36 auditor assignments, and 30 promoter/insider-holding links. Its 75 communities mix evidence from different periods and sources. A cluster can suggest a line of inquiry; it cannot prove coordination or control.

## How to Explore the Evidence

The refreshed product separates questions that the old interface collapsed together:

1. In [Board Interlocks](https://ganesh47.github.io/india-corporate-graph/#/board-interlocks), search every director by name or DIN, inspect complete company rosters, filter by role and status, and open the cited evidence.
2. In [Centrality](https://ganesh47.github.io/india-corporate-graph/#/centrality), compare board-only and combined-network rankings rather than treating one score as universal.
3. In [Communities](https://ganesh47.github.io/india-corporate-graph/#/community), inspect the 75 detected clusters and their relationship mix.
4. In [Path Finder](https://ganesh47.github.io/india-corporate-graph/#/path-finder), choose the relationship mode and time scope, compare alternative routes, and inspect the evidence attached to every hop.

A path is a chain of published relationships. It is not proof that information, money, or risk travelled along that chain.

## Data and Methodology

The rebuild is deterministic: reviewed research records produce typed `company_universe`, `directors`, `board_appointments`, `board_committees`, and `director_sources` datasets, which in turn generate the compatible graph nodes and edges. Every appointment has a company key, director key, role/status fields, snapshot date, primary URL, locator, and verification status. Re-running identical reviewed inputs produces stable keys and file hashes.

The company list comes from the [official NSE NIFTY 100 constituent file](https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv). Corporate identity uses CIN where verified and director identity uses DIN where disclosed; the [MCA Director Master Data help](https://www.mca.gov.in/Ministry/pdf/MCAV2Release2_Help.pdf) describes DIN-based lookup. Source documents are linked, not redistributed.

This snapshot answers a precise question: **what board structure can be verified for the pinned NIFTY 100 using primary sources available on or before 9 August 2026?** It does not answer every question about historical directorships, committees, influence, lending, or beneficial ownership.

That boundary sets up [Part 2: Follow the Money, Carefully](/blog/follow-the-money-lending-networks-india/), which separates the financial context the graph can support from the exposures it cannot yet observe.

All code and research structure are open source: [github.com/ganesh47/india-corporate-graph](https://github.com/ganesh47/india-corporate-graph).

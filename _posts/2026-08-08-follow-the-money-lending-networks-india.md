---
title: "Follow the Money, Carefully: Financial Context for India's Corporate Graph"
date: 2026-08-08 00:00:00 UTC
last_modified_at: 2026-08-09 00:00:00 UTC
categories: [blog]
tags: [Finance, Corporate-Governance, Graph-Theory, India, Banking, Audit, Ownership, Network-Analysis]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "The graph can connect verified boards with bank health, company fundamentals, ownership signals, auditors, and subsidiaries—but it cannot turn aggregate data into borrower-level lending exposure."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
permalink: /blog/follow-the-money-lending-networks-india/
---

**Series: Indian Corporate Networks**
Series map: [Part 1](/blog/connected-machine-board-interlocks-india-corporate/) \| **Part 2 (this post)**

*Interactive: [Financial Flows](https://ganesh47.github.io/india-corporate-graph/#/financial-flows) \| [Group Lens](https://ganesh47.github.io/india-corporate-graph/#/group-lens) \| [Path Finder](https://ganesh47.github.io/india-corporate-graph/#/path-finder)*

---

## Start With What the Data Can Prove

[Part 1](/blog/connected-machine-board-interlocks-india-corporate/) mapped 100 reviewed NIFTY 100 boards. That governance layer is strong because every published appointment points to a primary source.

The financial layer is not equally complete. The current product contains company fundamentals, aggregate bank-health records, derived valuation multiples, a partial auditor map, aggregate promoter/insider holding, and a small historical subsidiary layer. It does **not** contain borrower-level bank exposures, promoter pledge percentages, related-party transaction amounts, MCA charges, or IPO lock-in events.

That distinction matters. A bank’s total advances and gross NPA ratio can describe the bank. They cannot tell us how much it lent to a particular company. An aggregate insider-holding percentage can describe ownership concentration. It cannot tell us whether the holding is pledged.

The revised [Financial Flows view](https://ganesh47.github.io/india-corporate-graph/#/financial-flows) makes these limits visible rather than drawing a synthetic Sankey between banks and groups.

## The Financial Coverage, Layer by Layer

| Layer | Published coverage | What it supports | What it does not support |
|---|---:|---|---|
| Boards | 100/100 reviewed rosters; 961 appointment observations | Current/fallback board composition, roles, dates when disclosed, evidence-backed interlocks | Undisclosed committees or unverified external seats |
| Company fundamentals | 83 graph companies; 63 are in the pinned NIFTY 100 | Exploratory comparisons of revenue, debt, book value, and employees | Issuer-verified point-in-time statements for the entire NIFTY 100 |
| Bank health | 6 banks, of which 5 are in the pinned universe | FY2025 aggregate advances, GNPA, and NNPA | Company- or group-level lending exposures |
| Auditor assignments | 36 company–auditor edges across 6 networks | Partial assurance-network exploration | A complete current statutory-auditor census or engagement-partner analysis |
| Promoter/insider holding | 30 aggregate edges | A coarse ownership-concentration signal | SEBI promoter classification, pledges, encumbrances, or holder-level ownership |
| Subsidiaries | 16 recurring relationships represented annually across 2021–25 | A small historical structural layer | A complete current subsidiary register |
| Valuation multiples | 83 graph companies with a positive book value; 63 in the pinned NIFTY 100 | Price-to-book and price-to-sales computed from the same market-cap and fundamentals fields above | A judgement on whether a given multiple is justified |

These layers are useful together only if their different dates, definitions, and source quality remain visible.

## Bank Health Is Not a Lending Network

The product publishes six FY2025 bank snapshots from issuer disclosures. Their aggregate advances range from SBI’s ₹42,21,000 crore to IndusInd Bank’s ₹3,45,019 crore. The records also include gross and net NPA ratios.

For example:

- SBI reported advances of ₹42,21,000 crore, GNPA of 1.82%, and NNPA of 0.47% in its [FY2024-25 chairman’s message](https://sbi.bank.in/corporate/SBIAR2425/chairmans-message.html).
- HDFC Bank reported advances of ₹26,43,500 crore, GNPA of 1.33%, and NNPA of 0.43% in its [March 2025 results release](https://www.hdfcbank.com/content/bbp/repositories/723fb80a-2dde-42a3-9793-7ae1be57c87f/?path=/Footer/About+Us/About+Investor+Relations/pdf/2024/march/Press-Release-March-2025.pdf).
- ICICI Bank reported advances of ₹13,41,766 crore, GNPA of 1.67%, and NNPA of 0.39% in its [March 2025 performance review](https://www.icicibank.com/about-us/news-room/2025/performance-review-quarter-ended-march-31-2025).

Those figures support bank-level comparisons. They do not support a claim that SBI, HDFC Bank, or ICICI Bank has a particular exposure to an Adani, Tata, Reliance, or any other group. No such edge is published.

This is a broader analytical rule: **do not infer the counterparty from the aggregate**. A borrower-level lending graph would need dependable facility- or exposure-level evidence, a clear date, consolidation rules, and a licence that permits reuse. Until that exists, the honest visualization is a bank-health comparison—not an invented flow.

## Fundamentals Add Context, Not Causality

The [Financial Flows view](https://ganesh47.github.io/india-corporate-graph/#/financial-flows) also compares revenue, book value, debt, and employees where third-party fundamentals are available. Within the pinned NIFTY 100, coverage is currently 63 companies.

These attributes can help frame questions. A company with high debt connected to several boards may deserve closer reading. A bank with improving NPA ratios may look different from one with worsening asset quality. But putting two attributes on adjacent nodes does not prove that one caused the other.

For investment work, the graph is a discovery layer. The cited issuer report and financial statements remain the evidence.

## A Valuation Multiple Is a Market Opinion, Not a Fact Check

The [Financial Flows view](https://ganesh47.github.io/india-corporate-graph/#/financial-flows) also derives price-to-book and price-to-sales for the 83 graph companies with a positive book value, using the same market-cap, book-value, and revenue fields already cited above. No new data source is introduced; the multiples are arithmetic on figures the reader has already seen.

The computed range is wide. Nykaa (FSN) trades at roughly 66× book and Nestlé India at roughly 58×; LIC Housing Finance trades at roughly 0.67× book and ONGC at roughly 0.81×. Two similarly leveraged non-bank lenders in the graph — Cholamandalam Investment and LIC Housing Finance, both carrying debt at more than six times book value — sit at opposite ends of this range, which is itself informative: leverage alone does not explain where the market prices a stock, and the gap is a prompt to read the [DCF series' P/BV and Excess Returns framework](/blog/bank-nbfc-valuation-pbv-excess-returns/) rather than a conclusion in itself.

A high or low multiple is not, by itself, evidence of mispricing, quality, or risk. It reflects what the market is currently willing to pay relative to a backward-looking accounting figure. Treat it the same way as a betweenness score: a reason to look closer, not a verdict.

## Ownership Signals Are Not Pledge Data

The graph contains 30 `promoter_holding` edges generated from an aggregate third-party held-percent-insiders field. The label is inherited from the older schema; it should be read as a coarse promoter/insider concentration signal, not a legal reconstruction of the promoter group under SEBI rules.

The current dataset does not identify individual promoter entities, pledged shares, encumbered shares, lenders against those shares, or changes between quarterly filings. It therefore cannot support a pledge-to-margin-call narrative for a specific company.

The correct future source is the exchange shareholding filing. NSE’s [XBRL information page](https://www.nseindia.com/static/companies-listing/xbrl-information) lists Regulation 31 shareholding-pattern filings alongside Regulation 23(9) related-party disclosures, Regulation 27 governance reports, and Regulation 33 financial results. Each is a distinct evidence layer. They should not be blended until each has been acquired, normalized, and cited on its own terms.

## Assurance Links: Useful, but Partial

The published graph has 36 company–auditor assignments across six audit-network nodes: Deloitte has eight represented assignments; EY, KPMG, and PwC have six each; BDO and Grant Thornton have five each.

This is enough to explore how an auditor node can connect otherwise separate companies. It is not enough to claim comprehensive audit-market concentration. The graph does not publish engagement-partner identity, joint-auditor allocation, tenure, rotation dates, or row-level evidence for every assignment.

An auditor edge is also not evidence of weak independence. It is a factual relationship that may become relevant when combined with separately verified transactions, restatements, enforcement actions, or tenure. Without those layers, the graph should pose a question rather than render a verdict.

Use [Network Explorer](https://ganesh47.github.io/india-corporate-graph/#/network) to turn auditor links on or off and observe how the topology changes. The current Louvain run uses all active board, subsidiary, ownership, and auditor relationships and produces 75 communities. The result is sensitive to those inputs.

## A Verified Cross-Layer Example

The two post-demerger Tata Motors entities show why entity boundaries and dates matter. The reviewed FY2025-26 reports show that Tata Motors Commercial Vehicles and Tata Motors Passenger Vehicles share N. Chandrasekaran, Al-Noor Ramji, Bharat Puri, and P. B. Balaji.

That is a verified four-director interlock supported by the [TMCV annual report](https://cv.tatamotors.com/assets/cv/files/AnnualReportFY26.pdf) and [TMPV annual report](https://nsearchives.nseindia.com/annual_reports/AR_29395_TMPV_2025_2026_A_21445169_15062026215933.pdf). It says something precise about governance continuity across two legally distinct listed entities.

It does **not** by itself establish an intercompany loan, guarantee, related-party transaction, or common credit exposure. Those would require separate evidence. This is the discipline a multi-layer graph demands: relationships can be adjacent on the screen without being interchangeable in analysis.

## What the Graph Still Cannot See

Several financially important layers remain unbuilt:

**Borrower-level lending.** Aggregate bank results do not disclose a reusable company-by-company exposure matrix. MCA charges can show secured interests, but not necessarily the current outstanding exposure or all lending terms.

**Promoter pledges and encumbrances.** These require quarterly shareholding-pattern evidence with holder identity, encumbrance type, quantities, dates, and amendments.

**Related-party transactions.** Regulation 23(9) and annual-report disclosures can support typed transaction edges, but entity reconciliation, consolidation eliminations, transaction categories, and reporting periods must be handled before amounts are comparable.

**Complete statutory-auditor history.** Annual reports can support firm, joint-auditor, tenure, and rotation fields. The current 36-edge layer is only a starting point.

**IPO lock-in events.** These require prospectus and allotment evidence tied to specific holders and the rules applicable at the time. They are not present in the product today.

Until these datasets exist, the interface should not imply that a visual path represents cash flow or contagion.

## Using the Explorer Without Overreading It

1. Open [Financial Flows](https://ganesh47.github.io/india-corporate-graph/#/financial-flows) to compare available fundamentals, the six official bank-health records, and the derived valuation-multiple tab. Watch the coverage badges before comparing companies.
2. Open [Group Lens](https://ganesh47.github.io/india-corporate-graph/#/group-lens) to inspect the mixture of board, subsidiary, ownership, and auditor observations attached to a named group. Keep the date and source layer visible.
3. Open [Centrality](https://ganesh47.github.io/india-corporate-graph/#/centrality) to compare board-only rankings with the combined graph. A ranking change reveals sensitivity to the included relationship types.
4. Open [Path Finder](https://ganesh47.github.io/india-corporate-graph/#/path-finder), select a relationship mode, and inspect every hop’s evidence. Alternative routes are useful hypotheses, not proof of money movement.
5. Open [Communities](https://ganesh47.github.io/india-corporate-graph/#/community) to see how mixed relationships cluster. Treat the 75 community assignments as exploratory partitions.

## Methodology and Provenance

The board foundation is the pinned [official NIFTY 100 constituent file](https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv) and 100 manually reviewed primary rosters. Forty are current to the preferred 30 June 2026 quarter or a later pre-snapshot page; 60 are explicitly marked fallback. Every appointment carries a source URL, reporting period, retrieval and verification timestamps, evidence locator, document hash where available, and review status.

Board identity is DIN-based when disclosed. Missing or dummy DINs remain company-scoped, never name-merged. Of 911 identity records, 579 are provisional for this reason. There are no published committee memberships, and 110 unverified predecessor “other directorship” mentions remain excluded.

The financial layers have separate provenance. The bank records link directly to issuer FY2025 results. Fundamentals and aggregate insider holdings are third-party context and are labelled as such. Auditor and subsidiary relationships retain their own dates and narrower coverage.

This separation is the point. A credible corporate graph does not become more insightful by pretending every desired edge already exists. It becomes more useful by showing exactly which relationships are verified, which are partial, and which questions still require primary evidence.

All code and research structure are open source: [github.com/ganesh47/india-corporate-graph](https://github.com/ganesh47/india-corporate-graph).

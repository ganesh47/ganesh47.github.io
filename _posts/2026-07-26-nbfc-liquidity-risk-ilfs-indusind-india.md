---
title: "When the Tap Runs Dry: NBFC Liquidity Risk, the IL&FS Collapse, and India's Unresolved Interconnectedness"
date: 2026-07-26 00:00:00 UTC
last_modified_at: 2026-10-02
categories: [blog]
author: Ganesh Raman
tags: [Finance, NBFC, Liquidity-Risk, IL-FS, IndusInd, DCF, India, Investing, ALM, Credit-Risk]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "Asset-liability mismatch, refinancing concentration and credit stress can interact in lenders. A framework for reading the IL&FS and DHFL cases, interpreting liquidity buffers and keeping creditor recovery separate from equity value."
header:
  overlay_color: "#0f2942"
  overlay_filter: 0.65
permalink: /blog/nbfc-liquidity-risk-ilfs-indusind/
---

*Revised 2 October 2026: Corrected the given-figure DHFL ratio and removed the creditor-to-equity recovery floor. Distinguished approval from completion, changed immunity claims to conditional resilience, and clarified stress/collateral assumptions. Historical resolution distributions remain explicitly unreconciled. Original publication date retained.*


*Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| **Liquidity Risk (this post)** \| [Part 4: What Is a Bank Worth?](/blog/bank-nbfc-valuation-pbv-excess-returns/)*

*Part 3 mentioned in passing that "when wholesale credit markets froze after the IL&FS default in September 2018, NBFC cost of funds spiked by 100–200 basis points precisely when their loan books were most stressed." This post unpacks that sentence in full. Part 4 picks up the valuation consequences — how liquidity risk and credit cost enter the P/BV framework.*

## Summary

Credit risk in a bank or NBFC is visible in lagging indicators: gross NPA ratios, provision coverage, slippage rates. The warning builds over quarters. Liquidity risk is different. It can be invisible until the moment it is fatal. The IL&FS crisis showed how defaults and rating actions can disrupt wholesale funding beyond the original borrower. Exact rating transitions need to be matched to each agency, group entity and instrument; a single group-wide AAA-to-D chronology is insufficient.

This post builds the framework for understanding NBFC liquidity risk through three lenses: the mechanics of how it accumulates (asset-liability mismatch), the anatomy of how it detonates (the IL&FS and DHFL cases), and the structural features that make some entities more resilient than others. IndusInd Bank's 2024–25 compound stress — a governance failure landing on top of a credit stress event — illustrates how the two risks interact when they arrive simultaneously.

## The Structural Problem: Why NBFC Funding Is Different

A bank has three things that an NBFC does not: the RBI as lender of last resort, access to the repo window, and a Current Account Savings Account (CASA) deposit franchise that can provide relatively low-cost funding. Deposit access and central-bank facilities do not make a bank immune to liquidity stress.

An NBFC lacks a bank-style CASA franchise, but its permitted funding can include retail fixed deposits as well as wholesale borrowing. Its actual funding mix needs to be checked entity by entity. It issues 90-day commercial paper (CP), 1–3 year non-convertible debentures (NCDs), borrows from banks under credit lines, and in some cases taps external commercial borrowings (ECBs). The rates it pays reflect the market's assessment of its credit quality — and that assessment can change very quickly.

The core vulnerability is an **asset-liability mismatch (ALM)**: the assets are long (a 20-year toll road concession; a 15-year housing loan; a 5-year equipment lease), while the liabilities are short (90-day CP rolled continuously; NCDs maturing in 18 months). The CP market grew from Rs 46,200 crore in March 2014 to Rs 1,26,700 crore in March 2017 — approximately 40.0% CAGR over three years — fueling the illusion that rollovers were permanent.

**Three types of NBFC liquidity risk:**

**Rollover risk** — the most acute form. If a lender cannot roll over its CPs at maturity, it must repay from whatever cash it holds, liquidate assets (at distressed prices), or draw down committed bank lines (if they exist and are undrawn). IL&FS had insufficient cash — approximately USD 27 million against USD 500 million in repayments due by March 2019.

**Market access risk** — a broader form. Even if individual rollovers succeed initially, a credit event (a rating downgrade, a peer default, a regulatory action) can cause the market to widen spreads to the point where rolling over becomes uneconomical. Post-IL&FS, 5-year NBFC NCD spreads blew out from 40–100 bps to ~160 bps, and CP spreads spiked above 400 bps.

**Concentration risk** — a structural form. An NBFC that depends on a single funding instrument (CPs only), a single counterparty category (one or two large bank lenders), or a narrow investor base is not diversified. The concentration becomes lethal when that single source becomes unavailable.

## IL&FS 2018: The Complete Anatomy of a Liquidity Crisis

### The Structure

IL&FS was a 302-entity conglomerate (169 domestic, 133 offshore) founded in 1987. By 2018 its shareholders included LIC (25.34%), Orix Japan (23.54%), ADIA (12.56%), HDFC (9.02%), and Central Bank of India (7.67%). Total outstanding debt: **Rs 91,000–94,000 crore**. Of this, more than Rs 16,000 crore was short-term. The effective debt-to-equity ratio was approximately 92:1.

The business model was to develop, finance, and manage infrastructure projects — toll roads, tunnels, urban water systems, power projects — with 20-to-30-year operating concessions. These projects generated revenues only after multi-year construction phases; Rs 9,000 crore was locked in disputes over government PPP receivables. The funding for all of this: 90-day CPs rolled continuously, ICDs (inter-corporate deposits) passed between the 302 group entities, bank term loans, and ECBs.

### The Timeline

| Date | Event | Amount |
|---|---|---|
| June 2018 | ITNL (IL&FS Transport Networks) misses ICD + CP to SIDBI | Rs 450 crore |
| Aug 27, 2018 | IFIN makes partial payment to SIDBI (Rs 50 cr of Rs 350 cr due) | Rs 300 crore short |
| **Sep 10, 2018** | **IL&FS parent defaults on SIDBI short-term loan** | **Rs 1,000 crore** |
| September 2018 | Defaults and rating actions disrupted group and wider NBFC funding; individual transitions require agency/instrument-level sources | — |
| Sep 21, 2018 | DSP MF sells DHFL CPs at 11% yield; DHFL falls 42% on close, 60% intraday | — |
| Sep 27–28, 2018 | IFIN defaults on 9 obligations (5 bank loans + deposits) | Rs 835 crore |
| End-Sep 2018 | Cumulative defaults, ITNL + IFIN | Rs 3,800 crore |
| Nov 2018 | Cumulative defaults across IL&FS group | Rs 4,640 crore |
| Oct 1, 2018 | NCLT approves board supersession; Uday Kotak appointed non-executive chairman | — |
| Sep 2022 | 93% of Rs 61,000 cr resolution target achieved | ~Rs 56,700 crore |

The defaults and rating actions contributed to a loss of confidence in wholesale funding. The original account compressed several group entities and instruments into a single simultaneous AAA-to-D event. That is not a sufficiently evidenced agency-by-agency chronology and has been removed.

The issuer-pays model also raises a general conflict-of-interest question: the issuer purchases the rating used by its creditors. Assess the dated rating rationale, surveillance and underlying cash-flow evidence rather than treating an investment-grade label as a promise of liquidity. The historical figures elsewhere in this case study still need their individual source documents reconciled before use in a quantitative model.

### How Contagion Spread

Mutual fund exposure to NBFC CPs stood at Rs 1.2 trillion as of September 2018 — up from Rs 50,000 crore in March 2016, a 2.4× increase in under three years. This represented 9.5% of total debt MF AUM; at the July 2018 peak, it had been 19%.

Eighteen mutual fund schemes held direct IL&FS exposure when the crisis hit. The table below shows the largest:

| Fund | Scheme | Exposure | % of scheme |
|---|---|---|---|
| LIC MF | Liquid Fund | Rs 697 crore | 4.2% |
| DSP | Credit Risk Fund | Rs 447 crore | 6.5% |
| Aditya Birla SL | Medium Term Plan | Rs 344 crore | 3.0% |
| BOI AXA | Credit Risk Fund | Rs 101 crore | **6.0%** |
| Principal | Cash Management Fund | Rs 104 crore | **10.0%** |
| Motilal Oswal | Ultra Short Term Fund | Rs 99.5 crore | **10.0%** |

*Source: myinvestmentideas.com; Business Standard (August 2018 data)*

The contagion mechanism was not only the direct exposure. It was the behavioral response:

1. **DSP MF sold Rs 300 crore of DHFL CPs at 11% yield** on September 21. The sale itself — a distress signal from a major fund house — caused DHFL equity to fall 42% on close and 60% intraday. DHFL had no exposure to IL&FS; it was the next NBFC with a large wholesale-funded book.

2. **Redemption pressure forced mass selling.** Debt MF AUM fell from Rs 25.2 trillion (August 2018) to Rs 22.04 trillion (September 2018) — Rs 3.16 trillion or 12.5% lost in a single month. Fixed-income outflows alone: Rs 2.4 trillion in September. Funds that had bought NBFC CPs at 90-day rolling maturities now found no buyers for those CPs.

3. **Credit spreads blew out across all NBFC paper.** Before IL&FS: 3-to-5-year AAA NBFC bonds traded at 40–100 bps over comparable G-secs. By February 2019: 5-year AAA NBFC spreads had reached approximately 160 bps. Short-term CP spreads exceeded 400 bps above system liquidity cost for stressed names. NBFCs with no direct connection to IL&FS faced funding costs 200 bps higher than the prior month — precisely when their balance sheets were most in need of stability.

4. **NBFC credit to commercial sector fell.** Rs 11.60 trillion (FY18) → Rs 9.34 trillion (FY19) — a 20% contraction in one year. The knock-on to real estate developers, infrastructure companies, and MSMEs — who had become dependent on NBFC credit as banks retreated from these segments post-2016 NPA cycle — was severe.

**The total market damage:** Investors lost Rs 14 trillion in equity market capitalization in September 2018. Sensex fell 6.3% (38,645 → 36,227). BSE Midcap fell 13%; BSE Smallcap fell 16%. The financial contagion of a debt event — not an equity event — had become the largest market shock of the year.

## DHFL 2019: The Liquidity–Fraud Compound

DHFL (Dewan Housing Finance Corporation) was the second major casualty — and a more complex failure because liquidity stress and fraud overlapped.

DHFL's business was structurally similar in vulnerability to IL&FS: 15-to-20-year housing loans funded by wholesale NCDs and bank borrowings, with a D/E ratio of 8.23× at March 2019. Total creditor claims when IBC proceedings began: **Rs 87,905.6 crore** (approximately 70,000 creditors — bond holders, banks, fixed deposit holders).

The post-IL&FS funding freeze hit DHFL immediately. DHFL also faced reported fraud allegations, which should be distinguished from a final finding against every person or entity involved: 87 "Bandra Book Entities" (shell companies) had diverted Rs 12,700 crore to promoter-linked firms (according to the Enforcement Directorate's January 2020 findings), and the CBI subsequently filed charges covering Rs 34,615 crore in bank fraud across 17 banks.

GNPA rose from 0.96% (FY18) to 2.74% (FY19) as the fraud emerged — still relatively low in absolute terms. The problem was not primarily bad loans. It was the inability to roll over Rs 2.5 trillion in NBFC/HFC wholesale debt that was due for rollover within six months of the IL&FS shock.

**The resolution and its denominator:** June 2021 NCLT approval and completion of the acquisition are different events; the original chronology records completion in September 2021. [Piramal's group description](https://www.piramal.com/) identifies a ₹34,250 crore DHFL acquisition. Against the ₹87,905 crore claims figure quoted in this article, that consideration is **38.96%**, not 43%.

This arithmetic is **not a verified realized recovery rate**. The historical claims figure and cash/NCD split need reconciliation to the approved resolution plan and creditor distributions. Other cash, the present value of deferred NCDs, creditor classes and later recoveries can change the result. Face value paid over ten years is not the same as cash received immediately.

The case does not establish that every lender receives the same percentage, that financial assets always recover less than physical assets, or that shareholders receive any positive amount. A restructuring analysis needs a dated liability waterfall and asset-realization assumptions.

## Three Types of Liquidity Risk: A Framework

```
Liquidity Gap = Short-term Liabilities (<1yr) − Short-term Assets (<1yr)
```

A positive gap means the lender must roll over more liabilities than assets mature in the near term. Any disruption to rollover — even a temporary one — becomes an existential threat.

**Type 1: Structural ALM Mismatch** — long assets funded with short liabilities create a refinancing need. Compare actual cash inflows, outflows and available liquidity in common rupee maturity buckets. Subtracting a percentage of liabilities from a percentage of assets does not produce a valid cash gap unless the bases have been reconciled. Severity also depends on committed facilities, collateral, saleability and stress assumptions.

**Type 2: Market Access Risk** — DHFL's mismatch was smaller than IL&FS's, but post-September 2018, the market simply refused to buy NBFC paper at prices DHFL could afford. The contagion spread not from DHFL's fundamentals but from market psychology after the IL&FS rating collapse. Market access risk is a second-order effect — it hits entities that are structurally more sound but cannot differentiate themselves quickly enough in a panic.

**Type 3: Concentration Risk** — For a concentration stress illustration, assume a lender has 17% of borrowings in CPs. This is manageable given diversified bank lines (41%), strong AA+ ratings, and short-tenure consumer assets. But if the CP market froze for 90 days and that lender could not roll Rs 71,400 crore in CPs (17% of an assumed Rs 4.2 lakh crore borrowing base), the stress on cash flows would be severe. The mitigant is diversification; the risk is that all three CP/NCD/bank markets can correlate during a systemic event.

The useful insight is **relative resilience, not immunity**. Granular retail funding may reduce dependence on a few institutional lenders, but deposits can still run and renewed funding can become expensive. Retail NCDs and deposits are also different contracts. Concentration, maturities, confidence and liquidity buffers determine vulnerability; no funding category makes a lender structurally immune.

## IndusInd Bank 2024–25: When Governance Failure Meets Credit Stress

IndusInd Bank's 2024–25 stress is not a liquidity crisis in the IL&FS sense — the bank is deposit-funded (CASA + term deposits cover ~55% of funding, with bulk deposits and borrowings for the remainder). But it illustrates a related and equally important risk: **governance failure as an amplifier of credit stress**.

### The Derivatives Mis-Marking

IndusInd's treasury desk was hedging foreign-currency borrowings using internal derivative contracts, with one desk acting as both counterparty legs. Early terminations were booked as profit on one leg without recognising the corresponding loss. This is an accounting mismatch, not a business loss — but it accumulated.

**The critical governance failure:** the discrepancy was identified internally in **December 2023**. This was a UPSI (Unpublished Price Sensitive Information) date under SEBI regulations. The bank's board audit committee was informed only in November 2024. Public disclosure to exchanges: **March 10, 2025** — fifteen months after internal discovery.

During those fifteen months, CEO Sumant Kathpalia sold 1.25 lakh shares; Deputy CEO Arun Khurana sold 3.48 lakh shares. SEBI's interim ex-parte order of May 28, 2025 directed disgorgement of Rs 19.78 crore from the two executives and barred them from markets.

Grant Thornton's investigation (report April 26, 2025) confirmed **Rs 1,959.98 crore** in cumulative P&L impact as of March 31, 2025.

### The MFI Compound

The derivatives loss would have been a significant but manageable event in isolation. It landed on top of a credit stress cycle in IndusInd's BFIL (Bharat Financial Inclusion Ltd.) microfinance book.

The MFI sector entered a severe stress cycle in 2024–25 driven by borrower overleveraging — at peak, 25% of Indian MFI borrowers had loans from three or more lenders simultaneously, with some geographies showing 4+ lender concentration above 22%. PAR 30+ (portfolio at risk, 30+ days overdue) for the industry rose from 2.1% (FY24) to 6.2% (FY25). IndusInd's MFI book represents approximately 9% of its loan book, but contributed over 70% of Q4FY25 slippages.

| Metric | Q4FY25 | Note |
|---|---|---|
| Net loss | **Rs 2,329 crore** | Largest-ever quarterly loss |
| GNPA | **3.13%** (+88 bps QoQ) | Peak stress quarter |
| Slippages | Rs 5,014 crore | >70% from MFI |
| NIM | **2.25%** | Collapsed from 3.96% (Q3) |
| Q4FY25 provisions | Rs 2,522 crore | +45% QoQ |

Interest reversals and provisions can affect NIM and earnings together, but the quoted NIM movement does not by itself prove that exactly three quarters of interest reversed at 90 DPD. Reconcile the issuer's disclosed reversal amounts and loan-aging data before making that attribution.

### The Rating and Market Response

- **Moody's (May 2025):** Downgraded IndusInd's Baseline Credit Assessment from ba1 to **ba2** — a one-notch move — citing governance failure as the primary driver.
- **CRISIL (May 2025):** Placed AA+ on Watch Negative. Removed in August 2025 but reaffirmed with **Negative Outlook**.
- **Share price:** Fell 20–27% on March 10 (disclosure day); remained under sustained pressure through Q2FY26.

### The Recovery

The bank is recovering. New CEO Rajiv Anand (ex-Axis Bank Deputy MD) was appointed in August 2025. Q4FY26 net profit: Rs 594 crore. Q1FY27 net profit: **Rs 1,037 crore** (+72% YoY). CRAR: 17.15%.

The key residual risks: NIM under continued pressure from the RBI rate-cutting cycle (125 bps in 2025–2026); CRISIL Negative Outlook in place; Moody's ba2 BCA with Negative outlook; bulk deposits (market-sensitive) as a meaningful share of funding; and the structural question of whether the combined MFI + vehicle finance model carries a through-cycle credit cost that is permanently 50–80 bps higher than management has historically guided.

**What IndusInd illustrates for any NBFC/bank analysis:** the 90-day accrual clock described in Part 3 does not only apply to individual loans. It applies to the entire process of governance disclosure. A mis-marking identified internally in December 2023 does not affect the balance sheet until it is disclosed — which means 15 months of published accounts, analyst recommendations, and investor decisions were made with incomplete information. The credit cost hit landed all at once in Q4FY25. The asymmetry between internal knowledge and public information is exactly what SEBI's insider trading framework exists to prevent, and exactly what it failed to prevent here.

## The Structural Antidotes

Two business-model features illustrate potential liquidity mitigants. Their benefits remain conditional on the dated balance sheet, collection performance and stress scenario.

### Shriram Finance: The Retail Deposit Advantage

Shriram Finance has **26% of its borrowings in retail public deposits** — granular, geographically distributed, not concentrated in any institutional investor. No CP. ECBs (18%) diversify internationally. Bank borrowings (19%), NCDs (17%), and securitisation (16%) provide the remainder.

A granular retail deposit base can reduce concentration relative to a few wholesale lenders. It does not remove the possibility of withdrawals, non-renewal or confidence shocks. Assess the actual deposit behavior, maturity profile and buffers; the funding category alone cannot establish immunity.

The GNPA of 4.55% (Q4FY25) looks high — higher than most private sector banks. But Shriram's borrowers are used commercial vehicle operators (truckers and bus owners with no formal credit history), and the GNPA reflects the cyclicality of freight volumes, not a structural deterioration. The through-cycle credit cost of ~2% is built into the yield on advances (16.74%) that Shriram charges. The economics work because the liability structure is stable.

### Muthoot Finance: The Gold Loan ALM Advantage

Short-tenure gold lending can have a different liquidity profile from long-tenure infrastructure lending. Gold loans have 1-to-12-month tenures — assets mature and generate cash every month. NCDs and bank borrowings (longer duration) fund an asset base that is far more liquid than the liabilities.

Do not infer a rupee funding surplus from an unreconciled difference between asset and liability percentages. Maturing loans supply cash only to the extent borrowers repay or collateral can be realized in time. A wholesale freeze still requires a dated cash-flow maturity analysis.

For a simple collateral stress illustration, a loan of 75 against gold initially worth 100 has collateral worth 80 after a 20% fall, leaving only 5 before interest and enforcement costs. A 25% fall leaves 75, with **no principal cushion**. This assumed LTV is not a statement of the current regulatory ceiling for every gold-loan product. Auction timing, costs, borrower repayment and legal process matter; an entire book cannot be assumed liquid within 90 days.

Standalone loan AUM crossed Rs 1 lakh crore in FY25; reached Rs 1,47,552 crore by Q3FY26 (+51% YoY). GNPA: 1.10% (from 1.88% FY24). CRAR: 21.96%.

## RBI's Regulatory Arc: What Each Crisis Added

The RBI's response to each liquidity event has layered new requirements on the NBFC sector.

**Post-IL&FS (November 2019):** Mandatory ALM disclosures for all non-deposit NBFCs with assets ≥ Rs 100 crore and all deposit-taking NBFCs. Ten structural liquidity buckets (replacing the prior single "1–30 day" bucket). Quarterly public disclosure of CP/NCD percentages, short-term liability concentration, and top-10 borrowing counterparties. Tolerance limits on cumulative negative mismatches: ≤10% for 1–7 days; ≤10% for 8–14 days; ≤20% for 15–30 days.

**Scale-Based Regulation (October 2021, effective April 2022):** Four tiers (Base, Middle, Upper, Top). 15 Upper Layer NBFCs identified for enhanced supervision (including Bajaj Finance, Shriram Finance, L&T Finance, Muthoot Finance, and Piramal Capital). Requirements for Upper Layer: CET1 minimum 9%, mandatory equity listing within 3 years, board Chairman/CEO separation, Large Exposure Framework.

**LCR Implementation (December 2019 → December 2024):** Liquidity Coverage Ratio requirements for large NBFCs phased in from 50% (December 2020) to 100% (December 2024). Full implementation as of end-2024 means Upper Layer and large NBFCs must now hold 30 days of High Quality Liquid Assets against stressed outflows.

**2025–2026 enforcement escalation:** October 2024 saw four NBFCs (Asirvad, Arohan, Navi Finserv, DMI Finance) banned from disbursements in a single day for usurious pricing (WALR 26–28%) and inadequate household income assessment. November 2025: RBI consolidated all NBFC regulations into 35 Master Directions; issued the first standalone NBFC Governance Directions in the sector's history. April 2026: **150 NBFC registrations cancelled in one sweep** — the largest single enforcement action in sector history, targeting entities with Net Owned Fund failures and chronic prudential non-compliance.

The arc is clear: each crisis added a layer (disclosure → capital buffers → liquidity requirements → governance mandates → mass de-registration of non-compliant entities). The regulatory framework has improved materially. The question is whether the residual interconnectedness risk has kept pace.

## The Residual Risk: Bank-NBFC Interconnectedness

The RBI Financial Stability Report (December 2025) identified a specific residual risk that the enhanced regulatory framework has not resolved:

**Banks acquire approximately 80% of NBFC-originated retail and MSME assets through a limited number of NBFCs.** Bank credit to NBFCs stood at Rs 15.36 lakh crore (8.9% of aggregate bank credit) as of October 2024. Mutual fund debt exposure to NBFCs reached Rs 2.33 trillion (+47% YoY) at the same date. NBFC gross payables to the broader financial system: Rs 21.15 lakh crore as of March 2025.

The concentration in a limited number of large NBFCs means that a stress event at one of them simultaneously hits multiple bank balance sheets and mutual fund portfolios. The correlated risk is not eliminated by scale-based regulation — it is in some ways amplified, because the 15 Upper Layer NBFCs collectively carry a far larger share of the system's NBFC exposure than the 302 IL&FS entities did in 2018.

**The MFI recovery as a signal:** The microfinance sector is recovering. PAR 30+ peaked at 6.2% (FY25); by Q4FY26, the industry was growing again for the first time in seven consecutive quarters. Disbursements in Q4FY26: Rs 77,524 crore — the highest in seven quarters. The borrower overleveraging guardrails introduced by MFIN in November 2024 (reducing the share of borrowers with 3+ lenders from 25% to 14% by June 2025) are working. But the stress left visible mark — Spandana Sphoorty posted a net loss of Rs 1,035 crore for FY25; Bandhan Bank's GNPA remains above 4%; and IndusInd's MFI legacy continues to resolve slowly through FY26–27.

**The unsecured consumer credit overhang:** The RBI's November 2023 risk weight increase on unsecured lending (consumer credit risk weights raised 100% → 125%) slowed growth from 28% to 12% within a year. But the December 2025 FSR found that unsecured loans drove 53.1% of total retail loan slippages, with NBFCs and fintechs accounting for 84.3% of personal loans below Rs 50,000. The partial reversal of the tightening in February 2025 does not eliminate the underlying asset quality risk in the unsecured book.

## DCF Implications: Separate Funding Risk From Equity Recovery

Funding risk can affect the forecast and the equity return investors require. A wholesale-dependent lender may face more refinancing volatility, but a precise beta or Ke difference needs dated estimation. The named Ke values in [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/) are scenario assumptions, not empirical proof of a fixed bank–NBFC spread.

Model at least a going-concern path and a separately specified funding-stress path. In the stress path, estimate collections and asset sales, enforcement costs, timing, priority claims and any new capital. **Residual equity** is what remains after liabilities and prior claims; it may be zero even when creditors recover substantial value.

There is no universal **43–50 paise per rupee of assets** terminal floor. Creditor recovery per rupee of admitted claims has a different denominator, and a finite resolution payout is not the Gordon terminal value of a continuing business.

When probability-weighting stress cash flows, do not add another discount-rate penalty for the exact same expected default loss. Ke still compensates for relevant priced risk, but each adjustment needs a distinct rationale. Use discounted residual equity cash flows, including dilution, for an equity DCF.

The operating model and the liquidity model answer different questions: can the lender earn a spread after costs and losses, and can it meet obligations when funding is disrupted? [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) now keeps ratio denominators and taxes explicit; Part 4 keeps creditor recovery separate from shareholders' value.

*Tools referenced in this post:*
- *[Liquidity Risk Lab](https://ganesh47.github.io/india-dcf-explorer/#/liquidity-risk-lab) — funding mix stacked bars, risk quadrant, ALM gap analysis and IL&FS timeline for 9 entities*
- *[Efficiency Lab](https://ganesh47.github.io/india-dcf-explorer/#/efficiency-lab) — NIM decomposition, CIR vs RoA, two-number truth grid for 15 Indian lenders (updated IndusInd Bank data)*
- *[DCF Builder](https://ganesh47.github.io/india-dcf-explorer/#/dcf-builder) — full DCF model for any NIFTY 100 company*

*Data sources: RBI Annual Reports 2018-19 and 2024-25; RBI FSR June 2025 and December 2025; MFIN Micrometer Q4FY26 (June 2026); Sa-Dhan Bharat Microfinance Report FY2024-25 (October 2025); SEBI ex-parte order (Kathpalia, May 28, 2025); Grant Thornton investigation report on IndusInd Bank (April 26, 2025); IndusInd Bank investor presentations Q4FY25 and Q1FY27; Shriram Finance Annual Report FY25 (CARE Ratings May/December 2025); Muthoot Finance FY25 Annual Report; CARE Ratings press releases; PRIME database (rated bond breakdown); Business Standard; Bar and Bench; VRD Nation; myinvestmentideas.com (MF scheme exposure data); Vinod Kothari Consultants (SBR/LCR framework); IIMB Working Paper WP 605/2020 on DHFL; GripInvest (resolution data). All data for educational purposes — not investment advice.*


Revision references: [Piramal group description](https://www.piramal.com/) for the stated ₹34,250 crore acquisition consideration; [Damodaran, financial-firm equity valuation](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf) for equity cash flows and capital claims. The resolution-plan denominator, creditor-class payout and deferred-instrument present values remain explicitly unreconciled here; the given-figure ratio is not promoted into an asset or equity recovery rate.

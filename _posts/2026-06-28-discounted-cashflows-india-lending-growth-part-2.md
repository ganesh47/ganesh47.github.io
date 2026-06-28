---
title: "Discounted Cash Flows in Action: Lending, Growth, and Capital Allocation in India"
date: 2026-06-28 10:00:00
categories: [blog]
author: Ganesh Raman
tags: [Finance, Banking, NBFC, Lending, DCF, Capital Allocation, India]
toc: true
author_profile: true
classes: wide
excerpt: "How DCF mathematics powers every home loan EMI, drives Bajaj Finance's 10.1% NIM, governs HDFC Bank's spread management, and frames the NSE IPO valuation — a practitioner's guide to DCF in Indian lending and capital allocation."
permalink: /blog/discounted-cash-flows-india-lending-and-growth-part-2/
---

Series: Discounted Cash Flows: The Complete Indian Guide

Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) | [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/)

Part 2 of 2. Previous: [Discounted Cash Flows: The Math Behind Every Indian Valuation](/blog/discounted-cash-flows-the-math-part-1/)

## Summary

Part 1 of this series built the DCF toolkit from scratch: the formula, WACC inputs anchored to a 6.84% G-Sec yield and Damodaran's 7.08% equity risk premium for India, and a worked Reliance Industries valuation exercise. This post applies the same framework to where most Indians actually encounter finance: borrowing money, lending it out, and deciding where to deploy capital for growth. The thread connects your ₹50 lakh home loan to Bajaj Finance's 10.1% NIM, to HDFC Bank's spread economics, to the analyst DCF valuation of the NSE's ₹30,000 crore IPO. The mathematics is the same throughout — only the context changes.

## Every EMI Is a DCF

When SBI lends you ₹50 lakh for a home at 7.5% per annum for 20 years, it is solving a present value equation. The monthly EMI is the fixed cash flow that, when discounted at the loan rate, equals exactly the principal disbursed. This is not coincidence — the EMI formula and the present value of an annuity formula are the same equation rearranged.

The EMI formula:

```
EMI = P × r × (1+r)^n / ((1+r)^n − 1)
```

Where:
- **P** = principal = ₹50,00,000
- **r** = monthly interest rate = 7.5% / 12 = 0.625% = 0.00625
- **n** = number of months = 20 × 12 = 240

Computing (1.00625)²⁴⁰ ≈ 4.46. The monthly payment works out to:

```
EMI = 50,00,000 × 0.00625 × 4.46 / (4.46 − 1)
    = 50,00,000 × 0.02788 / 3.46
    = ₹40,280 per month
```

Over 240 months, total outflow = ₹40,280 × 240 = **₹96.67 lakh** on a ₹50 lakh loan. The ₹46.67 lakh difference is the cost of time.

The verification is the DCF insight: the present value of ₹40,280 received every month for 240 months, discounted at 7.5%/12 (0.625%) per month, equals exactly ₹50,00,000. From the bank's perspective, each monthly payment is a future cash inflow discounted back to today at the loan rate. The bank disbursed ₹50 lakh today and is receiving back a stream of smaller payments whose present value equals that disbursement. That is DCF, applied 240 times.

How much does the interest rate matter at this scale?

| Rate (p.a.) | Monthly EMI | Total Payout | Total Interest |
|-------------|-------------|--------------|----------------|
| 7.25% (best CIBIL tier) | ₹39,316 | ₹94.36 lakh | ₹44.36 lakh |
| 7.50% (standard)        | ₹40,280 | ₹96.67 lakh | ₹46.67 lakh |
| 8.40% (higher LTV tier) | ₹43,075 | ₹1,03.38 lakh | ₹53.38 lakh |

The 115bps spread between the best and worst rate tier costs the borrower ₹3,759 more each month — ₹9 lakh more over the loan life. This is precisely what credit scoring is worth to you as a borrower. And it is why Indian banks invest in credit underwriting: the price they can charge scales directly with the risk they perceive, and every basis point of spread is a permanent feature of a loan that may run for 20 years.

## How Indian Banks Price Loans

Banks do not set interest rates arbitrarily. Every lending rate is built from a cost-plus foundation anchored to the RBI policy rate — a direct consequence of a regulatory mandate with precise DCF implications.

Since October 2019, the RBI has required that all new floating-rate retail loans be linked to an **external benchmark**: the repo rate, the 91-day Treasury Bill rate, or another published market rate. Banks add a fixed spread on top:

```
Lending Rate = External Benchmark + Credit Risk Spread + Operating Cost Spread
```

In practice, with the repo rate currently at 5.25% (June 2026):
- **SBI home loan:** repo (5.25%) + ~200bps spread = **7.25%** for the best-rated borrowers (CIBIL 800+, low LTV)
- **HDFC Bank home loan:** repo + ~275–300bps = ~8.00–8.25%
- **Higher-risk borrowers** at the same banks: another 50–100bps on top

The bank's economic engine is the **Net Interest Margin (NIM)** — the difference between what it earns on loans and what it pays to fund them.

**HDFC Bank Q4 FY25 (from the April 2025 earnings presentation):**
- Yield on advances: ~**8.4%** (what the bank earns across its entire loan book)
- Cost of funds: ~**4.9%** (blended cost of deposits, borrowings, and equity)
- Net Interest Margin: ~**3.46%** (the spread)
- NIM × Loan Book size = Net Interest Income = the primary P&L line

When the RBI cut the repo rate by 125bps over 2025–2026, banks' loan yields repriced downward faster than their deposit costs could fall (deposits are typically fixed for 1–3 years, while floating rate loans reset within 3 months). This NIM compression — a perfectly predictable DCF consequence of the external benchmark mandate — is a recurring feature of rate-cutting cycles in Indian banking.

The external benchmark rule is good for borrowers (rate cuts pass through immediately) and creates short-term pain for banks' income statements. For a DCF analyst modelling HDFC Bank, a rate cut cycle means lower near-term FCF from the loan book, requiring either a lower discount rate (consistent with lower risk in the economy) or a higher terminal growth assumption to maintain valuation.

## The NBFC Model: Bajaj Finance and the Art of Spread Management

If HDFC Bank's NIM is 3.46%, why does Bajaj Finance report a NIM of **10.1%** (FY25)?

The answer lies in who they lend to, on what collateral, and at what tenure — and ultimately, in the fundamental cost structure of an NBFC versus a bank.

**Bajaj Finance FY25 key numbers (Annual Report and Q4 FY25 investor presentation):**
- Assets Under Management (AUM): **₹4,16,661 crore** (March 2025; +26% YoY)
- Cost of Funds: **7.99%** (Q4 FY25; management guided 7.75–7.85% by FY26 end)
- Implied yield on assets: **~18.1%** (NIM 10.1% + COF 7.99%)
- Net Interest Income growth: +23.8% YoY
- Return on Assets: 4.6%; Return on Equity: ~22%
- Borrowing mix: Banks 41%, Money Market instruments (NCDs, CPs) 49%, NHB 10%

Bajaj Finance borrows at ~8% and lends at ~18%. The 10 percentage point spread is what makes it one of the most profitable consumer lenders in the world by return-on-equity standards. Why does this spread exist and why hasn't competition eliminated it?

| Dimension | HDFC Bank | Bajaj Finance |
|-----------|-----------|---------------|
| Primary lending products | Home loans, corporate loans | Consumer durables, personal loans, SME |
| Collateral | Mostly secured (property) | Largely unsecured (consumer) |
| Average loan tenure | 10–20 years | 6–24 months |
| Typical borrower | Salaried prime, HNI | Aspiring middle class, MSMEs |
| Cost of funds | ~4.9% (benefits from CASA) | ~7.99% (no CASA franchise) |
| Yield on assets | ~8.4% | ~18.1% |
| NIM | ~3.46% | ~10.1% |

The structural asymmetry is the **CASA franchise**. HDFC Bank holds vast quantities of current and savings account deposits that pay depositors 0–3.5% per annum — well below market rates — because customers value the transactional convenience. This cheap funding significantly lowers HDFC Bank's blended cost of funds to ~4.9%, enabling it to lend home loans at 8.25% and still earn a healthy spread.

Bajaj Finance has no CASA. It cannot accept savings deposits. It funds itself entirely in the wholesale market — by issuing Non-Convertible Debentures (NCDs) and Commercial Paper (CPs) — at market rates of ~8%. To make the economics work, it lends at ~18% to borrowers that banks will not (or cannot) serve at low rates: two-wheeler buyers, consumer appliance purchasers on EMI, small business owners without formal income documentation. The higher rate compensates for higher credit risk, shorter tenor (which concentrates risk differently from long-term mortgages), and the absence of a cheap funding base.

**DCF intuition for the loan book:** Bajaj Finance's book value (equity on the balance sheet) is not its market value. The market's equity valuation is the present value of all future distributable cash flows — interest income minus credit losses minus operating costs minus the cost of capital needed to sustain AUM growth. The "DCF of the loan book" is the spread (NIM − credit losses − operating costs ≈ ROA 4.6%) compounded on a growing AUM base, discounted at the cost of equity (~14.5%). This is what drives the P/B premium.

## Valuing a Lending Business: The Equity DCF Approach

You cannot apply a standard free-cash-flow-to-firm (FCFF) DCF to a bank or NBFC. The reason: for a bank, borrowings (deposits, NCDs, borrowings from other banks) are not "leverage" in the conventional sense — they are the raw material of the business, analogous to inventory for a manufacturer. Trying to compute "enterprise value" by adding debt to equity value makes no sense when the business cannot operate without that debt.

The correct approach for lenders is the **equity DCF** — discounting free cash flows available to equity holders, after all debt obligations are met, including the capital required to fund loan book growth:

```
Equity Value = PV of free cash flows to equity (FCFE), discounted at cost of equity (Ke)
```

Where FCFE for a bank = net income − net increase in equity required to support balance sheet growth.

### The P/B Framework as DCF Shorthand

For lending businesses, the Price-to-Book (P/B) ratio is a compact DCF identity:

```
P/B = (ROE − g) / (COE − g)
```

Where ROE is return on equity, COE is cost of equity, and g is the sustainable growth rate of book value. This formula derives directly from the Gordon Growth Model applied to equity cash flows.

**If ROE = COE:** P/B = 1. The business earns exactly what investors require — it neither creates nor destroys value, so the market values it at book.

**If ROE > COE:** P/B > 1. The business earns above its required return — it creates value — so investors rationally pay a premium to book to capture future excess returns.

**If ROE < COE:** P/B < 1. The business destroys value — rational sellers trade the equity at a discount to book.

**HDFC Bank (illustrative):**
- ROE: ~16–17% (FY25)
- COE: ~13–14% (lower beta reflecting systemically important status and strong deposit franchise)
- Sustainable growth (g): ~12–13% (driven by retained earnings × ROE)
- Justified P/B ≈ (16.5% − 12.5%) / (13.5% − 12.5%) = 4.0% / 1.0% = **~4x**
- Actual market P/B: ~2.8–3.2x

The gap between the formula's 4x and the market's ~3x reflects the market pricing in either NIM pressure from rate cuts reducing near-term ROE, or a higher COE for HDFC Bank post the HDFC-HDFC Bank merger integration risk. This is the kind of insight a P/B DCF yields.

**Bajaj Finance (illustrative):**
- ROE: ~21–23% (FY25)
- COE: ~14.5% (higher beta; NBFC with concentrated consumer/SME risk)
- Sustainable growth (g): ~17–20% (high retention ratio × high ROE)

Here the formula creates a problem: when g approaches or exceeds COE (both are near 14–17%), the denominator (COE − g) approaches zero or goes negative, producing a result that is mathematically undefined or negative. This is not an error in the formula — it is the formula correctly signaling that the standard perpetuity assumption has broken down. A business growing faster than its cost of equity in perpetuity would have infinite value, which is clearly not real.

For high-growth NBFCs like Bajaj Finance, analysts use a **two-stage equity DCF**:
1. **Stage 1 (5–7 years):** Explicit model of FCFEs at current high-growth trajectory
2. **Stage 2 (terminal):** Gordon Growth at a sustainable rate (say 8–10%), where growth has converged to a level below COE

The resulting equity value divided by current book value gives the justified P/B. Bajaj Finance's market P/B of ~6–7x reflects the market's belief that the company will sustain ROE well above COE for a decade or more before normalising — a powerful compounding thesis, but one that requires the company to keep executing at its current extraordinary pace.

## DCF for Growth Capital Allocation

DCF is not only for valuing companies. It is the primary tool for deciding where to deploy capital within a company. This is where DCF becomes a management instrument rather than an investor instrument.

### NPV and IRR: The Two Decision Rules

**Net Present Value (NPV)** = PV of all future cash inflows from a project − initial investment required

```
NPV = Σ CFt/(1+r)^t − Initial Investment
```

Accept if NPV > 0; reject if NPV < 0. Among competing projects, choose the highest NPV. **This rule is always correct.**

**Internal Rate of Return (IRR)** = the discount rate at which NPV = 0 — the implied return from the project.

Accept if IRR > WACC; reject if IRR < WACC. This rule works in most cases but fails in important ones:

- **Scale problem:** a ₹100 crore project returning ₹110 crore (10% IRR) and a ₹1 crore project returning ₹1.25 crore (25% IRR) — IRR prefers the small project; NPV correctly identifies the large one as worth more in absolute terms
- **Multiple sign changes:** projects with negative cash flows mid-life (a mine that needs environmental remediation at year 15) can produce multiple mathematically valid IRRs, making the number meaningless
- **Non-comparable durations:** a 3-year project with 18% IRR vs a 10-year project with 15% IRR — IRR favours the shorter one, but NPV might correctly favour the longer compounding

**When NPV and IRR disagree, NPV wins.** Capital allocation is about maximising total value created, not maximising percentage return on individual projects.

### NTPC Green Energy: A Real Capital Allocation Example

NTPC Green Energy (NREL) raised ₹10,000 crore in its November 2024 IPO, directing ₹7,500 crore to investments in subsidiaries and balance sheet strengthening. Every gigawatt of solar or wind capacity NREL adds is a capital allocation decision with DCF at its core.

For a utility-scale renewable energy project in India, the DCF logic has distinctive features:
- **High upfront capex:** ₹4–6 crore per MW for solar; negligible variable cost thereafter
- **Long asset life:** 25+ years (solar panels, wind turbines)
- **Contracted revenue:** Power Purchase Agreements (PPAs) with state utilities fix the tariff for 25 years, substantially reducing revenue uncertainty
- **Lower discount rate:** ~11–12% WACC for well-structured renewable projects (predictable cash flows + government-backed offtakers + asset-backed debt = lower risk)
- **Project IRR:** typically 10–13% for competitive bids — just above WACC, which is why projects are NPV-positive but not dramatically so

The terminal value in a renewable project DCF is modest compared to a growth business because the asset has a defined 25-year life; there is no perpetual growth assumption after that. Most of the value is in the explicit 25-year cash flow stream.

For NREL's equity story, the DCF rationale is: deploy ₹4,000–6,000 crore per gigawatt into projects earning 11–13% IRR against a WACC of ~11%; positive NPV at scale becomes a large value creation machine as India expands renewable capacity toward its 500 GW by 2030 ambition.

### Jio: The Most Important Indian Capital Allocation Decision of the Last Decade

Between 2012 and 2016, Reliance Industries committed approximately ₹2 lakh crore to build the Jio 4G network. At the time, the near-term DCF looked deeply unfavourable: enormous upfront capex, years of negative FCF before a single subscriber arrived, and no certainty that Jio's disruptive pricing (essentially free voice calls, ₹10/GB data) would produce a viable long-term business.

Three factors justified the commitment in DCF terms:

1. **Terminal state analysis.** At scale (200-400 million subscribers, dominant market share), Jio's steady-state FCF profile was compelling even at a 10%+ discount rate. The NPV was substantially positive if you believed scale could be achieved — which required a pricing war that only the Reliance balance sheet could sustain.

2. **Real option value.** Jio's infrastructure would also enable JioMart (retail e-commerce), Jio Financial Services (a new NBFC), JioCinema (OTT), and a platform ecosystem whose combined FCF potential was not captured in a simple telecom DCF. These are real options — the right but not the obligation to enter adjacent markets using existing infrastructure. Standard DCF systematically undervalues companies with real option portfolios.

3. **Competitive blocking.** The alternative — doing nothing and letting competitors build out 4G without Reliance — had negative NPV in the form of competitive erosion across Reliance's retail and consumer businesses. Framing the investment as "cost of not doing it" changes the NPV calculation entirely.

By FY25, Jio's estimated revenue had crossed ₹1 lakh crore annually. The Reliance stock re-rating from ~₹400 (2016) to ~₹1,478 (2025) reflects this DCF playing out in reality. Capital allocation at scale, done with disciplined DCF thinking and scenario analysis, is how conglomerates create multi-decade value.

## NSE IPO (2026): A Live DCF Exercise

The National Stock Exchange filed a DRHP with SEBI in 2026 for an estimated ₹30,000 crore public issue. It is one of the most anticipated Indian equity offerings given NSE's near-monopoly on equity derivatives trading volumes and its structural position at the centre of India's capital markets.

Available analyst estimates based on DRHP financial disclosures illustrate a textbook DCF-plus-cross-check methodology:

**Analyst base case parameters:**
- Revenue CAGR assumption: ~18% over the explicit 10-year forecast period
- Methodology: 10-year free cash flow projection + Gordon Growth terminal value
- Base case DCF fair value: **₹1,908 per share**
- Blended fair value (DCF + EV/Revenue cross-check): **₹1,715 per share**
- Implied market capitalisation range: ₹4.2 lakh crore to ₹6.25 lakh crore depending on scenario

**Why the DCF cross-check with multiples matters:**

At ₹1,715 (blended fair value), NSE trades at approximately 38–43x projected FY26 earnings. BSE, the listed peer, trades at 45–55x FY26 estimates. DCF and peer multiples pointing in the same direction adds confidence; a large divergence between them demands explanation. Here they are broadly consistent, giving the analyst — and potential investors — a basis for conviction.

**Why NSE's DCF has higher credibility than most:**
- Exchange businesses earn recurring revenue from transaction fees — effectively a toll on every equity, derivatives, and debt trade
- Capital expenditure is modest relative to revenue (no physical inventory, no loan book to fund)
- Network effects compound: the most liquid exchange attracts the most participants, which reinforces liquidity, which attracts more participants
- This moat justifies a terminal growth rate above average India GDP for longer than most businesses — the analysts' 18% revenue CAGR assumption for the explicit period is aggressive but not implausible given NSE's market position

**The risks that make the sensitivity table non-trivial:**
- SEBI has historically changed exchange fee structures; any regulatory intervention reprices all future cash flows
- Post-2023 SEBI curbs on index options reduced some speculative volume; further regulatory tightening is a tail risk
- BSE has been gaining derivatives market share; structural competitive erosion is possible

At any IPO price above ₹1,715, the investor is implicitly underwriting a more optimistic terminal growth rate, a lower discount rate, or both. DCF does not prevent this — but it makes the underwriting explicit. The question to ask is not "is NSE a quality business?" (it obviously is) but "what growth rate and discount rate does this price imply, and do I believe those numbers?"

## Why DCF Is a Management Superpower

### For CFOs and Capital Allocators

The discipline of corporate finance reduces to one test applied continuously: does every rupee of capital earn more than its cost? Return on Capital Employed (ROCE) versus WACC is the definitive metric:

- **ROCE > WACC:** the business creates value; grow it, invest more, reward shareholders through compounding
- **ROCE ≈ WACC:** value-neutral; discipline capex, return excess cash rather than deploying into marginal projects
- **ROCE < WACC:** the business destroys value; fix it, divest it, or shut it down

The tragedy of many Indian conglomerate capital allocation cycles is that ROCE < WACC businesses receive capital because they are "strategic" or because promoters are reluctant to exit. DCF thinking makes the cost of this choice visible and forces an honest conversation about whether "strategic" means "creates value" or "feels important."

### For Founders and Entrepreneurs

Enterprise value is, definitionally, the present value of future free cash flows. Three levers move it:

1. **Higher FCF** — revenue growth, margin improvement, faster working capital conversion
2. **Lower discount rate** — reduce risk perception by building predictable revenue (recurring subscriptions beat project-based revenues), maintaining a clean balance sheet, and communicating honestly with capital markets
3. **Longer growth runway** — extend the period during which the business can deploy capital above WACC

Founders often focus on lever 1 and neglect lever 2. But the discount rate can swing DCF value by 30–50% independent of revenue. A business that is seen as risky (unpredictable revenue, governance questions, concentrated customer exposure) carries a higher COE — and therefore a lower DCF value — than one with identical FCF but perceived as more transparent and defensible.

Building investor trust is literally a value-creation activity in DCF terms.

### For Lenders and Credit Analysts

Every credit decision is a DCF in disguise. The question being answered is: will the stream of repayments (EMIs, bullet payments, coupons) have a present value above the loan amount, net of the probability-weighted loss in default scenarios?

The spread above cost of funds is the lender's compensation for three sources of risk:
- **Credit risk:** probability of default × loss given default (the expected loss rate)
- **Duration risk:** longer tenor = more uncertainty = wider spread required
- **Liquidity risk:** less liquid loans (corporate project finance, SME lending) require extra return for the lender's inability to exit quickly

When Bajaj Finance charges ~18% on an unsecured consumer loan while borrowing at ~8%, the 10% NIM covers approximately: credit losses of 2–3% (net NPA provisioning), operating costs of 3–4% (people, systems, branches), and residual return to equity of 3–4% (the ROA of 4.6%). Each of these is estimable and verifiable. The business model only works if all three buckets are managed tightly — which is why Bajaj Finance's underwriting sophistication and collections infrastructure are moat, not detail.

### For Investors

DCF translates a market price into an implied thesis. This is perhaps the most underused application.

When a stock is "expensive" on trailing multiples, the right question is not "is it expensive?" but "what growth rate and discount rate does the current price assume?" If the price implies 20% FCF growth for 15 years and you believe 15% for 10 years, the stock is genuinely expensive. If you believe 25% for 15 years, it is cheap — and the same price, the same "expensive-looking" multiple, is in fact a buy.

This reverse-engineering of implied assumptions — sometimes called "implied growth duration" analysis — is what separates investors who have a thesis from investors who have an opinion. DCF is the tool that enables that translation.

## Conclusion

The mathematics threaded through this two-part series never changes. It is always the same calculation: future cash flows discounted at a rate that reflects risk and the opportunity cost of capital. It appears first as the ₹40,280 monthly EMI on your home loan. It reappears as the 10.1% NIM Bajaj Finance extracts from India's aspiring consumers by borrowing at 8% and lending at 18%. It surfaces in HDFC Bank's 3.46% net interest margin, the result of decades of CASA franchise building and careful rate-cycle navigation. It culminates in the ₹1,715–1,908 per-share valuation range that analysts assign to the NSE's pending ₹30,000 crore IPO.

DCF does not tell you what will happen. It tells you what must be true for a price to be justified — and that is the more useful skill. India is entering a decade of large, complex capital market transactions: renewable energy platforms, financial services unicorns, infrastructure trusts, and technology IPOs at unprecedented scale. The operators, lenders, founders, and investors who understand the present value mathematics beneath these decisions will see what others miss — not because the numbers are secret, but because the framework forces the right questions to be asked at the right time.

---

**Sources and references:**
- India 10Y G-Sec yield: June 2026 market data
- RBI repo rate: 5.25% (June 2026, following 125bps easing cycle from peak of 6.50%)
- Damodaran India ERP: 7.08% total (January 2026 dataset, pages.stern.nyu.edu)
- EY-NSE Cost of Capital Survey 2024, NSE Archives
- RBSA Cost of Capital in India, 6th Edition (2023)
- Bajaj Finance Q4 FY25 Investor Presentation and FY25 Annual Report
- HDFC Bank Q4 FY25 Earnings Presentation (April 2025)
- SEBI DRHPs: Swiggy (September 2024), NTPC Green Energy (September 2024), NSE (2026)
- SBI home loan rates: BankBazaar, 2025-26
- NSE IPO DCF analysis: analyst estimates based on DRHP disclosures, June 2026
- Reliance Industries DCF model parameters: November 2025 analyst report

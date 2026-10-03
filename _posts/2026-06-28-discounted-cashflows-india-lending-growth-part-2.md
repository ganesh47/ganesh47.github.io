---
title: "Discounted Cash Flows in Action: Lending, Growth, and Capital Allocation in India"
date: 2026-06-28 00:00:00
last_modified_at: 2026-10-02
categories: [blog]
author: Ganesh Raman
tags: [Finance, Banking, NBFC, Lending, DCF, Capital Allocation, India]
toc: true
author_profile: true
classes: wide
excerpt: "How discounting connects home-loan EMIs, lender funding, retained capital and growth decisions, with explicit illustrative assumptions rather than unsourced issuer price targets."
permalink: /blog/discounted-cash-flows-india-lending-and-growth-part-2/
---

*Revised 2 October 2026: Corrected EMI arithmetic and issuer-versus-scenario labels, aligned P/B examples with Part 4, and removed the unlinked NSE target. Funding, NIM and capital-retention assumptions are now explicit. Original publication date retained.*


Series: Discounted Cash Flows: The Complete Indian Guide

Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/) \| [Liquidity risk](/blog/nbfc-liquidity-risk-ilfs-indusind/)

Part 2 of the series. Previous: [Discounted Cash Flows: The Math Behind Every Indian Valuation](/blog/discounted-cash-flows-the-math-part-1/) | Next: [The Two-Number Truth: Operating Ratio, Credit Cost, and DCF](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/)

## Summary

Part 1 built the DCF toolkit using explicit assumptions and a fictional company. This post applies it to borrowing, lending and capital allocation. The thread connects a ₹50 lakh home loan to lender funding and retained capital. Issuer financial observations, hypothetical inputs and market-price opinions need separate labels; the mathematics cannot make them interchangeable.

## Every EMI Is a DCF

For an illustrative ₹50 lakh fixed-rate home loan at 7.5% per annum for 20 years, it is solving a present value equation. The monthly EMI is the fixed cash flow that, when discounted at the loan rate, equals exactly the principal disbursed. This is not coincidence — the EMI formula and the present value of an annuity formula are the same equation rearranged.

The EMI formula:

```
EMI = P × r × (1+r)^n / ((1+r)^n − 1)
```

Where:
- **P** = principal = ₹50,00,000
- **r** = monthly interest rate = 7.5% / 12 = 0.625% = 0.00625
- **n** = number of months = 20 × 12 = 240

Computing (1.00625)^240 gives approximately 4.460817. Using unrounded inputs:

```
EMI = 50,00,000 × 0.00625 / (1 − 1.00625^(−240))
    = ₹40,279.66 per month ≈ ₹40,280
```

Total outflow is about **₹96.67 lakh**, of which **₹46.67 lakh** is interest. Fees, insurance, changing floating rates and prepayments are excluded.

The present value of the unrounded payment stream, discounted at 0.625% per month, equals ₹50,00,000. Displaying the EMI rounded to a rupee introduces a small rounding difference; it should not be called an exact identity for that rounded amount.

How much does the interest rate matter at this scale?

| Rate (p.a.) | Monthly EMI | Total Payout | Total Interest |
|-------------|-------------|--------------|----------------|
| 7.25% (illustrative) | ₹39,519 | ₹94.85 lakh | ₹44.85 lakh |
| 7.50% (illustrative)        | ₹40,280 | ₹96.67 lakh | ₹46.67 lakh |
| 8.40% (illustrative) | ₹43,075 | ₹1,03.38 lakh | ₹53.38 lakh |

The 115-basis-point difference between these assumed fixed rates costs about **₹3,556 more each month**, or **₹8.54 lakh** over 240 months. The table is not a current bank rate card or an estimate of the causal value of a CIBIL score. For a floating-rate loan, future resets change both payment and total-interest outcomes.

## How Indian Banks Price Loans

Banks do not set interest rates arbitrarily. Every lending rate is built from a cost-plus foundation anchored to the RBI policy rate — a direct consequence of a regulatory mandate with precise DCF implications.

Since October 2019, the RBI has required that all new floating-rate retail loans be linked to an **external benchmark**: the repo rate, the 91-day Treasury Bill rate, or another published market rate. Banks add a fixed spread on top:

```
Lending Rate = External Benchmark + Credit Risk Spread + Operating Cost Spread
```

For a simple repricing illustration, assume a policy benchmark of 5.25% and a 2.00% spread: the quoted lending rate would be 7.25%. Neither input is asserted as a current SBI rate. Contractual reset dates, borrower risk and product terms must come from the loan agreement and a dated rate card.

Net interest income is interest income minus interest expense. **NIM is NII divided by the issuer's specified average earning-asset or total-asset denominator**. It is not generally yield on advances minus funding cost, because the asset and liability bases differ; NIM×loan book is not generally NII.

Rate cuts can lower floating-loan yields before term deposits reprice. This is a plausible mechanism, but the amount and timing depend on the actual asset/liability profile. An analyst should model those cash flows rather than compensate mechanically with a higher terminal growth rate.

The external benchmark rule is good for borrowers (rate cuts pass through immediately) and creates short-term pain for banks' income statements. For a DCF analyst modelling HDFC Bank, a rate cut cycle means lower near-term FCF from the loan book, requiring either a lower discount rate (consistent with lower risk in the economy) or a higher terminal growth assumption to maintain valuation.

## The NBFC Model: Funding and Spread Management

A bank with a CASA franchise and a consumer-finance NBFC have different funding and operating structures. An NBFC without current or savings accounts may still use **fixed deposits**, bank borrowing, debentures, commercial paper and other funding; “no CASA” does not mean “entirely funded by CP and NCDs.” Use the issuer's dated funding table before assigning percentages.

For a fictional loan, borrowing at 8% and lending at 18% gives a **10-percentage-point contractual spread**. It does not establish an issuer's NIM or imply 10% of its total assets is profit. Different balances, idle cash, fees, collection costs, provisions and tax must be reconciled.

| Question | What to source |
|---|---|
| Funding cost | Average liabilities, funding mix, interest expense and period |
| Lending yield | Average advances or earning assets and interest income |
| Credit risk | Provisions, write-offs, recoveries and denominator |
| Equity return | Net income and consistently averaged equity |

The cash available to shareholders is earnings after interest, operating costs, credit losses and tax, less the equity needed for growth. Subtract capital retention; do not subtract the cost of equity as a cash expense and then discount the same cash flow at Ke again.

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

**HDFC-named scenario, aligned with Part 4:**
- Assumed forward RoE: **14.4%**, not a verified FY25 observation
- Assumed Ke: **13.0%**
- Perpetual g: **9.0%**
- P/B=(14.4−9)/(13−9)=**1.350×**

The original series mixed normalized, historical and differently defined issuer returns. These fixed assumptions now match [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/). A comparison price/B of 2.85× disagrees with the model; it does not uniquely identify NIM pressure, merger risk or a lower cost of equity.

**Bajaj-named scenario, aligned with Part 4:**
- Assumed forward RoE: **19.1%**, not a verified FY25 observation
- Stable Ke=6.70%+0.95×7.00%=**13.35%**
- Stable g=**10.0%**
- P/B=(19.1−10)/(13.35−10)=**2.716×**

A separate high-growth stage might assume book growth of 17% for a finite period. That can exceed Ke temporarily, but it cannot be put into the perpetual denominator. Growth also consumes retained equity; a growth rate above RoE would require external capital or another explicitly modeled adjustment.

For a multistage equity DCF:
1. Forecast annual net income, equity retention, payouts and any issuance over the explicit period.
2. Move to a stable terminal regime with Ke>g and a coherent payout/return assumption.
3. Discount both payouts and terminal equity value to today. Do not add a stable P/B to today's book without discounting the transition.

The price cannot tell us one unique growth duration. Several return, growth and risk paths can produce the same present value.

## DCF for Growth Capital Allocation

DCF is not only for valuing companies. It is the primary tool for deciding where to deploy capital within a company. This is where DCF becomes a management instrument rather than an investor instrument.

### NPV and IRR: The Two Decision Rules

**Net Present Value (NPV)** = PV of all future cash inflows from a project − initial investment required

```
NPV = Σ CFt/(1+r)^t − Initial Investment
```

Accept if NPV > 0; reject if NPV < 0. For comparable mutually exclusive projects with consistent risk, horizon and no binding capital constraint, choose the higher NPV. Capital rationing, timing and strategic dependencies require a fuller decision model.

**Internal Rate of Return (IRR)** = the discount rate at which NPV = 0 — the implied return from the project.

Accept if IRR > WACC; reject if IRR < WACC. This rule works in most cases but fails in important ones:

- **Scale problem:** with both returns arriving after one year and a common 8% discount rate, ₹100 crore returning ₹110 crore has NPV **₹1.852 crore**; ₹1 crore returning ₹1.25 crore has NPV **₹0.157 crore**. The smaller project has higher IRR but creates less absolute value under these assumptions.
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
- **Project IRR:** a scenario range of 10–13% crosses an assumed 11% WACC. For a conventional investment with one initial outflow, IRR above WACC implies positive NPV; equality implies zero NPV and a lower IRR implies negative NPV. This is not a verified issuer-wide project-return estimate.

The terminal value in a renewable project DCF is modest compared to a growth business because the asset has a defined 25-year life; there is no perpetual growth assumption after that. Most of the value is in the explicit 25-year cash flow stream.

The capital-allocation question is whether each project generates cash flows worth more than its investment at the appropriate discount rate. A project at 11% IRR against an 11% WACC does not create positive NPV merely because it is large. The capacity-cost and return ranges above are teaching assumptions; an issuer valuation requires dated project disclosures and cash-flow forecasts.

### Jio: The Most Important Indian Capital Allocation Decision of the Last Decade

Between 2012 and 2016, Reliance Industries committed approximately ₹2 lakh crore to build the Jio 4G network. At the time, the near-term DCF looked deeply unfavourable: enormous upfront capex, years of negative FCF before a single subscriber arrived, and no certainty that Jio's disruptive pricing (essentially free voice calls, ₹10/GB data) would produce a viable long-term business.

Three factors justified the commitment in DCF terms:

1. **Terminal state analysis.** At scale (200-400 million subscribers, dominant market share), Jio's steady-state FCF profile was compelling even at a 10%+ discount rate. The NPV was substantially positive if you believed scale could be achieved — which required a pricing war that only the Reliance balance sheet could sustain.

2. **Real option value.** Jio's infrastructure would also enable JioMart (retail e-commerce), Jio Financial Services (a new NBFC), JioCinema (OTT), and a platform ecosystem whose combined FCF potential was not captured in a simple telecom DCF. These are real options — the right but not the obligation to enter adjacent markets using existing infrastructure. Standard DCF systematically undervalues companies with real option portfolios.

3. **Competitive blocking.** The alternative — doing nothing and letting competitors build out 4G without Reliance — had negative NPV in the form of competitive erosion across Reliance's retail and consumer businesses. Framing the investment as "cost of not doing it" changes the NPV calculation entirely.

By FY25, Jio's estimated revenue had crossed ₹1 lakh crore annually. The Reliance stock re-rating from ~₹400 (2016) to ~₹1,478 (2025) reflects this DCF playing out in reality. Capital allocation at scale, done with disciplined DCF thinking and scenario analysis, is how conglomerates create multi-decade value.

## An Exchange Valuation: Separate the Model From the Filing

An exchange can be studied through transaction fees, recurring services, operating costs, reinvestment and regulatory scenarios. Network effects may strengthen its franchise, but competition and fee-rule changes still affect cash flows.

The original version quoted an NSE IPO size and analyst per-share targets without a linked filing or a reproducible forecast. Those figures are not used here as established facts. IPO status requires a dated issuer/exchange or regulatory disclosure; fair value requires the underlying model and share count.

For an illustrative mature exchange with year-10 FCFF of ₹100 crore, WACC=12% and terminal g=4%, year-10 terminal enterprise value is ₹1,300 crore. Its present value is **₹418.57 crore**, before adding explicit-period cash flows and reconciling net debt or other claims. This is a calculation on assumed inputs, not an NSE valuation.

Peer multiples can be a cross-check only when forecast periods, share counts and enterprise/equity claims match. A DCF and a multiple agreeing does not independently prove that their shared assumptions are correct.

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

In the fictional 18%-yield/8%-funding example, the 10-point spread must cover losses, operating costs and tax before it can support shareholder distributions. Convert all ratios to the same average-balance denominator. Underwriting and collections matter because the contractual yield is not the same as realized cash return.

### For Investors

DCF translates a market price into an implied thesis. This is perhaps the most underused application.

When a stock is "expensive" on trailing multiples, the right question is not "is it expensive?" but "what growth rate and discount rate does the current price assume?" If the price implies 20% FCF growth for 15 years and you believe 15% for 10 years, the stock is genuinely expensive. If you believe 25% for 15 years, it is cheap — and the same price, the same "expensive-looking" multiple, is in fact a buy.

This reverse-engineering of implied assumptions — sometimes called "implied growth duration" analysis — is what separates investors who have a thesis from investors who have an opinion. DCF is the tool that enables that translation.

## Conclusion

The mathematics stays the same: cash flows discounted consistently with the claim being valued. It appears in the ₹40,280 rounded monthly EMI, in a lender's spread and capital-retention decisions, and in a multistage valuation with an explicit stable end state. The useful discipline is to keep assumptions visible and source actual metrics separately.

DCF does not tell you what will happen. It tells you what must be true for a price to be justified — and that is the more useful skill. India is entering a decade of large, complex capital market transactions: renewable energy platforms, financial services unicorns, infrastructure trusts, and technology IPOs at unprecedented scale. The operators, lenders, founders, and investors who understand the present value mathematics beneath these decisions will see what others miss — not because the numbers are secret, but because the framework forces the right questions to be asked at the right time.

---

**Sources and references:**
- [RBI government-securities primer](https://m.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=711), §§23–24 and 29, for yield and holding-period distinctions used in Part 1.
- [Damodaran, *Valuing Financial Service Firms*](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf), equity cash-flow and excess-return sections.
- [Part 4’s reproducible P/B scenarios](/blog/bank-nbfc-valuation-pbv-excess-returns/) for the common HDFC/Bajaj assumptions. They are pedagogical inputs, not sourced issuer FY25 metrics.

The EMI, P/B and exchange examples were recalculated on 2 October 2026. Corporate-history illustrations elsewhere in the post are not current price targets; verify issuer filings before using their estimates for investment work.

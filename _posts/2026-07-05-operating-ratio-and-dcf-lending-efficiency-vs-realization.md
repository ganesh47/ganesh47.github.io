---
title: "The Two-Number Truth: Operating Ratio, Credit Cost, and Why They Tell Opposite Sides of the Same DCF Story"
date: 2026-07-05 00:00:00 UTC
categories: [finance, investing]
tags: [dcf, banking, operating-ratio, credit-cost, indian-markets, valuation]
excerpt: "A lender's Cost-to-Income Ratio tells you how efficiently the machine runs. It says nothing about whether the machine's output actually arrives as cash. This post connects operating efficiency to DCF valuation through the lens of Indian banks and NBFCs."
header:
  overlay_color: "#0f766e"
  overlay_filter: 0.55
toc: true
toc_sticky: true
---

*This is Part 3 of a series on Discounted Cash Flow analysis applied to Indian markets.
[Part 1](/blog/discounted-cash-flows-the-math-part-1/) covers the mathematics of DCF.
[Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) covers how Indian banks price loans and why lending institutions require a different valuation framework.
This post builds the bridge between operational efficiency and long-run cash realization.*

---

## The Machine That Leaks in Two Places

A manufacturing company's operating ratio is straightforward: operating expenses divided by revenue. Every rupee that does not go to running the business stays as profit. The lower the ratio, the better.

A bank's Cost-to-Income Ratio (CIR) looks similar — operating expenses divided by operating income — but it measures only one of the two ways a bank can fail to convert revenue into cash. The second leak is credit quality: loans that are extended, income that is accrued, but cash that never actually arrives.

This distinction matters enormously for DCF analysis. In a standard business, accrual income and cash income diverge only because of working capital timing. In a bank, they can diverge permanently — because a loan classified as an NPA does not just delay cash flow, it destroys it.

**The complete picture of a bank's profitability requires exactly two numbers, not one:**

**RoA = NIM − Operating Cost Ratio − Credit Cost Ratio**
{: .notice--info}

Where:
- **NIM** (Net Interest Margin) = interest earned minus interest paid, as a percentage of average assets
- **Operating Cost Ratio** = operating expenses as a percentage of average assets (captured by CIR)
- **Credit Cost Ratio** = provisions for bad loans as a percentage of average advances

CIR captures the first drain. Credit cost captures the second. Ignore either and you are reading half the story.

---

## What CIR Actually Measures

The Cost-to-Income Ratio is the banking equivalent of the industrial operating ratio, but defined over a different base:

**CIR = Operating Expenses / Operating Income**
{: .notice--info}

Where operating income for a bank = net interest income + non-interest income (fees, trading, forex).

A few things make CIR behave differently from an industrial operating ratio:

**The numerator is sticky; the denominator is rate-sensitive.** Salaries, branch costs, and technology investments do not move with interest rates. But net interest income does — when RBI cuts rates (as it did by 125 basis points between February and June 2026), NIM compresses and the same fixed cost base looks worse on CIR even if the bank ran its operations identically. This is why CIR deteriorated across the system in 2019–2021 even for well-managed banks: NIM fell, costs did not.

**Scale produces dramatic operating leverage.** A large private bank with ₹25 lakh crore in assets spreads its technology and compliance costs over a vastly larger income base than a small finance bank at ₹50,000 crore. This structural advantage compounds over time and largely explains why HDFC Bank's CIR (around 40%) is 25 percentage points better than IDFC First Bank's (~74%), even though both operate in Indian retail lending.

**Benchmarks vary by segment:**

| Segment | CIR range (typical) | Why |
|---------|-------------------|-----|
| Large private banks (HDFC, ICICI, Kotak) | 38–47% | Scale, CASA funding, digital efficiency |
| Public sector banks | 50–60% | Higher employee costs, legacy branch networks |
| Small finance banks | 60–75% | Building franchise, high branch density needed |
| Established NBFCs (Bajaj Finance, Muthoot) | 22–40% | No branch-based deposit gathering; leaner cost base |
| Housing finance companies (Aavas, Can Fin) | 25–35% | Asset-heavy business with low servicing complexity |

The NBFC advantage is structural: without the obligation to accept deposits, NBFCs skip branch networks and their costs entirely. They pay more for funds on the liability side, but their operating cost base can be dramatically leaner.

---

## The Accrual Trap: Why CIR Can Look Great Before a Crisis

Here is the mechanism by which CIR flatters a lender in the lead-up to a credit cycle:

1. A bank extends ₹1,000 crore in loans in FY23 at 11% yield. It immediately books ₹110 crore in annual interest income. Its operating costs are fixed at, say, ₹45 crore. CIR = 41%. Looks excellent.

2. By Q3 FY24, borrowers begin to stress. But under RBI's 90-day NPA recognition rule, the loan is not classified as NPA until three consecutive EMIs are missed. The bank keeps accruing interest income.

3. By Q1 FY25, the loan is classified Substandard (GNPA). Now the bank must reverse all accrued interest and begin provisioning: 15% of the outstanding in year one, stepping up to 100% if it reaches the Loss category.

4. Credit cost hits the P&L in FY25 — two years after the loan was booked and CIR looked fine.

**The crucial insight: CIR and credit cost are not contemporaneous measures.** CIR is a measure of the current period's machine efficiency. Credit cost reflects decisions made 1–3 years earlier, surfacing now through the NPA classification and provisioning cycle.

This timing gap is why analysts who looked at Yes Bank's ~50% CIR in FY2018 and called it an efficiently-run bank were measuring the wrong thing. The credit book was quietly deteriorating — loans to stressed real estate developers, infrastructure companies, and media conglomerates that would surface as NPAs in FY2019 and FY2020. CIR offered no warning. GNPA ratios (which rose from 1.7% in FY17 to 16.8% by March 2020) and the divergence between stated profit and operating cash flow were the actual signals.

A more robust early-warning diagnostic is the **cash-adjusted efficiency ratio**:

**Adjusted CIR = (Operating Expenses + Credit Costs) / Net Interest Income**
{: .notice--info}

This blends both leaks into one number and is harder to game through provisioning choices in the short run.

---

## The RoA Decomposition: Three Levers, One Number

Return on Assets is the cleanest single-number summary of a bank's business model, and it decomposes cleanly into the three-lever identity:

**RoA ≈ NIM − (OpEx / Avg Assets) − (Provisions / Avg Advances)**
{: .notice--info}

Let us work through two illustrative banks with identical CIR to see how dramatically credit cost changes the outcome.

### Illustrative Example: Precision Bank vs Efficiency Bank

Both banks, FY2025:
- NIM: 3.5% of assets
- CIR: 42% (identical)
- Operating cost as % of assets: 3.5% × 42% = **1.47%** (identical)

**Precision Bank:** credit cost ratio = 0.5% → **RoA = 3.5 − 1.47 − 0.5 = 1.53%**

**Efficiency Bank:** credit cost ratio = 1.5% → **RoA = 3.5 − 1.47 − 1.5 = 0.53%**

With 10:1 leverage (typical for Indian banks under Basel III capital requirements):
- Precision Bank RoE = 1.53% × 10 = **~15.3%**
- Efficiency Bank RoE = 0.53% × 10 = **~5.3%**

Same CIR. Three times the RoE difference. And because terminal value in a bank's dividend discount model is approximately `RoE × BV / (CoE − g)`, the P/B multiples these two banks deserve are fundamentally different — even though a CIR-only view would call them equally well-run.

---

## From RoA to DCF: Why Banks Are Valued Differently

The standard DCF uses Free Cash Flow to the Firm (FCFF): operating cash flows available to all capital providers. For a bank, this is almost meaningless — the "operations" of a bank are its liabilities (deposits) as much as its assets (loans). The balance sheet is the business model.

The correct framework for banks is **Free Cash Flow to Equity (FCFE)** or, in its most common applied form, the **Dividend Discount Model (DDM)**:

**Intrinsic Value = DPS₁ / (CoE − g)**
{: .notice--info}

Where DPS₁ is next year's expected dividend per share, CoE is cost of equity (from CAPM), and g is the sustainable long-run growth rate.

This simplifies to:

**P/B = (RoE − g) / (CoE − g)**
{: .notice--info}

This is the single most important formula in bank valuation. It says:

- If RoE = CoE, the bank is worth exactly book value (P/B = 1×)
- If RoE > CoE, the bank trades above book — it is creating value
- If RoE < CoE, the bank trades below book — it is destroying value in real terms

And since RoE = f(NIM, CIR, credit cost), the chain from operational ratios to intrinsic valuation is direct:

**NIM → CIR → Credit cost → RoA → RoE → P/B multiple**
{: .notice--info}

A bank that improves credit cost ratio by 100 basis points — through better underwriting, collections, or a shift toward lower-risk segments — can lift RoA from 1.2% to 2.2%, RoE from 12% to 22%, and justify a P/B re-rating from ~1× to ~3×. That is a 3× stock price move from a single operational improvement, which is why credit quality is so much more value-accretive than efficiency gains for most Indian banks.

---

## The Operating Leverage Asymmetry

Operating leverage in banking works differently from industrial companies. In manufacturing, high operating leverage means high fixed costs → profits amplify when revenue rises but collapse when it falls. Banks have a subtler version:

**Upside leverage:** When credit costs are low (which happens during economic expansion and when provisioning from a prior cycle has run off), a bank with a fixed cost base sees most of its incremental NIM flow straight through to profit. HDFC Bank's 5-year CAGR in PAT was consistently 18–22% through 2015–2020 partly because its fixed cost base was growing at 15% while its NIM was growing at 22%.

**Downside asymmetry:** When credit costs spike, the fixed cost base becomes an anchor. A bank with CIR of 45% and credit cost of 3% has essentially zero RoA before capital return requirements. This is the situation Bandhan Bank found itself in post-COVID when its microfinance book experienced severe stress: high NIM (7%+) but credit costs that at times exceeded NIM in stressed quarters.

**The NBFC structural advantage (and disadvantage):** NBFCs typically have CIRs 15–20 percentage points below equivalent banks. Bajaj Finance operates at ~35% CIR; a peer bank would be at 42–48%. This advantage comes from the absence of a deposit-gathering branch network. But NBFCs have no CASA funding — they borrow from markets at wholesale rates, which are higher and more volatile than deposit rates. When wholesale credit markets freeze (as they did after the IL&FS default in September 2018), NBFC cost of funds spikes precisely when they can least afford it. Their structural efficiency advantage is matched by a structural liquidity vulnerability.

---

## Delayed Cash Flow: The Core Tension in Lending DCF

When you build a DCF for a non-financial company, the timing of cash flows is driven by working capital and capital expenditure. The accrual gap is usually a few months.

When you build a DCF for a bank, the timing gap between accrued income and actual cash receipt can be 2–5 years — because loan tenures are long, NPA classification takes 90 days after the first default, and provisioning builds up over multiple quarters. This is structurally different from any other business.

The practical implication: **a bank's reported profit is a lagged indicator of its actual cash generation.** A lender growing its loan book rapidly will look highly profitable on accrual metrics for several years, because the credit cost of new loans will not surface until those loans season (usually 12–24 months for retail, longer for infrastructure and real estate). This is why rapidly-growing lenders often trade at high P/B multiples — the market is pricing in the optimistic scenario where growth continues and the new book seasons cleanly.

The risk premium embedded in a bank's cost of equity (its CoE in the DDM) should reflect this uncertainty. A bank with high loan book growth, a young average loan age, and limited credit cycle history should command a higher CoE than an established lender with stable asset quality through multiple cycles. India's lending history from 2014–2022 offers multiple case studies of what happens when this risk premium is priced too low.

---

## What Good Looks Like: The Indian Private Bank Standard

The sustainable RoA for a well-run Indian private bank converges on **1.5–2.5%**, driven by:

- NIM of 3.5–5.0% (higher for consumer/MSME focused lenders; lower for wholesale banks)
- Operating cost ratio of 1.5–2.5% (CIR of 40–50%)
- Credit cost ratio of 0.4–0.8% (GNPA < 2%, well-provided)

At 10–12× leverage, this produces **RoE of 15–22%** against a cost of equity of 13–15% — the spread that justifies P/B multiples of 2–4×.

Lenders that structurally cannot reach this equilibrium — either because their cost base is too high (small banks still building franchise) or their credit culture produces persistent credit costs above 2% — will trade below book value until one of those two inputs changes.

The Efficiency Lab tool accompanying this post makes this decomposition interactive across 15 Indian banks and NBFCs. Select any entity to see its NIM broken down into operating drain, credit drain, and surviving RoA — and whether its current RoE earns above or below cost of equity.

---

## The Two Questions to Ask Before Any Bank Investment

Every bank analysis ultimately reduces to two questions:

1. **How efficiently does the machine run?** (CIR — but remember this is cyclically sensitive and does not capture credit quality)

2. **How much of the machine's output actually arrives as cash?** (Credit cost ratio, GNPA trend, Provision Coverage Ratio)

A bank with excellent CIR but rising GNPA is running a clean engine on a leaking fuel line. A bank with mediocre CIR but pristine credit quality is leaving efficiency gains on the table — but its cash flows are real.

The DCF terminal value for a bank is determined by which of these two factors drives its long-run RoE. Operational efficiency can be improved through technology, consolidation, and scale. Credit quality, once lost through a cycle of aggressive growth into risky segments, can take a decade to rebuild — as the PSB sector demonstrated between 2015 and 2022.

**Both ratios together, not either alone, tell the truth.**

---

*Tools referenced in this post:*
- *[Efficiency Lab](https://ganesh47.github.io/india-dcf-explorer/#/efficiency-lab) — interactive NIM decomposition, CIR vs RoA scatter, two-number truth grid for 15 Indian lenders*
- *[WACC Lab](https://ganesh47.github.io/india-dcf-explorer/#/wacc-lab) — cost of equity across sectors*
- *[DCF Builder](https://ganesh47.github.io/india-dcf-explorer/#/dcf-builder) — build a full DCF for any NIFTY 100 company*

*Data sources: FY25 annual reports, Q4 FY25 earnings presentations (HDFC Bank, ICICI Bank, Kotak Mahindra Bank, Axis Bank, SBI, IndusInd Bank, Bandhan Bank, IDFC First Bank, Bajaj Finance, Shriram Finance, Mahindra Finance, L&T Finance, Muthoot Finance, AU Small Finance Bank, Aavas Financiers). RBI DBIE for system-level data. Damodaran (NYU Stern) for cost-of-equity benchmarks. All analysis is educational — not investment advice.*

---
title: "Discounted Cash Flows: The Math Behind Every Indian Valuation"
date: 2026-06-28 00:00:00
last_modified_at: 2026-10-02
categories: [blog]
author: Ganesh Raman
tags: [Finance, DCF, Valuation, India, Investing, WACC]
toc: true
author_profile: true
classes: wide
excerpt: "A first-principles walkthrough of cash-flow discounting, CAPM, WACC, terminal value and sensitivity analysis, with explicit illustrative inputs and reproducible arithmetic."
permalink: /blog/discounted-cash-flows-the-math-part-1/
---

*Revised 2 October 2026: Corrected bond-yield versus holding-return language, rounded arithmetic and terminal-value interpretation. Rate inputs are explicitly illustrative; the unlinked issuer price target is replaced by a reproducible fictional example. Original publication date retained.*


Series: Discounted Cash Flows: The Complete Indian Guide

Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/) \| [Liquidity risk](/blog/nbfc-liquidity-risk-ilfs-indusind/)

Part 1 of the series. Next: [DCF in Action: Lending, Growth, and Capital Allocation in India](/blog/discounted-cash-flows-india-lending-and-growth-part-2/)

## Summary

Every financial decision you make already uses discounted cash flow logic, even if you have never heard the term.

When a bank quotes you an EMI for a home loan, it is computing the present value of your future repayments and checking that they are worth more than the principal it hands you today. When a mutual fund analyst says a stock is "fairly valued at 45 times earnings," she has compressed a DCF model into a shorthand multiple. When the board of Reliance Industries approves a ₹2 lakh crore green energy programme on the promise of returns arriving in 2030 and 2035, they are (or should be) evaluating those future cash flows against what the money could earn today if deployed elsewhere.

The central insight is simple: a rupee today is worth more than a rupee in the future, because today's rupee can be invested and grow. The question DCF answers precisely is: *how much more?* That depends on two things — how certain you are that the future cash flows will actually arrive, and what your best alternative use of capital earns. An FD at 7% sets a floor. Equity in a cyclical business must clear a much higher bar. DCF is the framework that makes this trade-off explicit and auditable, rather than absorbed unconsciously into "feels like a quality franchise at a reasonable price."

This post builds the DCF model in four steps. Its rate inputs are fixed illustrations; obtain a dated source before substituting them into a current valuation:

1. **Free Cash Flow (FCF)** — What cash does the business actually generate, stripped of accounting choices? It is not profit, not EBITDA, and not reported EPS. Understanding why these differ is the single most important concept in valuation.
2. **The Discount Rate (WACC)** — At what rate should future cash flows be discounted? The examples assume a 6.84% risk-free benchmark and 7.08% equity risk premium. These are model inputs here, not a verified current quote or a claim about a particular dated Damodaran dataset.
3. **Terminal Value** — Businesses are not valued only for the next 5–10 years. Beyond the explicit forecast window, a terminal value formula captures everything else. This section shows how terminal value can dominate a model, and why its weight must be computed for the actual forecast rather than assumed universally.
4. **Sensitivity Analysis** — A single-number DCF is almost always wrong. The honest approach is a range, with the two most sensitive inputs — the discount rate and the long-run growth rate — stressed against each other. This section builds that table and explains what it reveals about the limits of precision in valuation.

Numbers throughout are explicit teaching assumptions. This revision replaces the unlinked Reliance analyst target with a fully specified fictional-company example; it does not make a current Reliance valuation claim. Part 2 of this series applies the same toolkit to the institutions that make money by explicitly pricing the time value of money: India's banks and NBFCs.

## Why Time Has a Price

Start with the simplest possible question: would you rather receive ₹1 lakh today or ₹1 lakh exactly one year from now?

The answer is obviously today — not because of impatience, but because of what you can do with the money in between. If you deposit ₹1 lakh in a fixed deposit at 7%, you will have ₹1,07,000 in a year. The person who waits gets ₹1,00,000. The difference is the price of time.

This observation — that a rupee today is worth more than a rupee in the future — is the entire foundation of DCF analysis. The rate at which you exchange present rupees for future rupees depends on your next best alternative. In financial markets, the closest thing to a risk-free next best alternative is the Indian government bond.

Suppose a one-year instrument promises ₹106.84 at maturity for ₹100 invested today, with no default. Its contractual one-year return is 6.84%. That is a simple time-value illustration.

A **ten-year G-Sec yield to maturity** of 6.84% is different: it depends on the bond price, coupon and maturity cash flows, and the realized return can depend on coupon reinvestment. Selling after one year exposes the holder to market-price changes. Sovereign credit risk and interest-rate risk are separate. The [RBI government-securities primer](https://m.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=711), §§23–24 and 29, distinguishes yields and holding-period risks. Here 6.84% is a chosen long-horizon discount-rate benchmark, not a guaranteed one-year cash return or an October market quote.

Most investments, however, are not Government bonds. They carry risk: the possibility that expected cash flows will not arrive, or will arrive diminished. Investors demand extra return to accept that risk. How much extra? That is the job of the discount rate.

## The DCF Formula

The present value of any stream of future cash flows is:

**PV = CF₁/(1+r)¹ + CF₂/(1+r)² + CF₃/(1+r)³ + ... + CFₙ/(1+r)ⁿ + TV/(1+r)ⁿ**
{: .notice--info}

Where:
- **CF₁, CF₂ … CFₙ** = free cash flows in years 1 through n
- **r** = discount rate (WACC), reflecting the riskiness of those cash flows
- **n** = explicit forecast period (typically 5–10 years)
- **TV** = terminal value, representing all cash flows beyond year n

Let us work through a clean 3-year example before introducing real Indian numbers. A company generates free cash flows of ₹10 crore, ₹12 crore, and ₹15 crore in years 1, 2, and 3, and is sold at a terminal value of ₹120 crore at the end of year 3. The appropriate discount rate is 12%.

| Year | Cash Flow (₹ cr) | Discount Factor (12%) | Present Value (₹ cr) |
|------|-----------------|----------------------|----------------------|
| 1    | 10.0            | 0.893                | 8.93                 |
| 2    | 12.0            | 0.797                | 9.57                 |
| 3    | 15.0            | 0.712                | 10.68                |
| 3 (TV) | 120.0        | 0.712                | 85.41                |
| **Total PV** |            |                      | **₹114.59 crore**    |

Two things are immediately apparent. First, the terminal value dominates: ₹85 crore of the ₹115 crore total is the present value of everything beyond year 3. Its share here is about 74.5%; other forecasts can produce quite different shares. Second, the discount factor does meaningful work: ₹120 crore three years from now is only worth ₹85 crore today at a 12% rate. Raise that rate to 15% and the same ₹120 crore is worth only ₹78.9 crore. The discount rate is not a detail — it is a decision.

## Input 1 — Free Cash Flow

The number in the numerator of every DCF term is **free cash flow to the firm (FCFF)**, not profit.

**FCF = EBIT × (1 − Tax Rate) + D&A − ΔNWC − Capex**
{: .notice--info}

Breaking this apart:

- **EBIT × (1 − t)** = net operating profit after tax (NOPAT). This is the cash the business generates from operations before financing costs are considered. Use the company’s applicable tax regime and expected effective cash tax rate; the worked example below assumes 25%.
- **+ Depreciation and Amortisation** — added back because it reduced EBIT but is non-cash. The cash left the business years ago when the asset was acquired; D&A is simply the accounting recognition of that spend spread over time.
- **− Change in Net Working Capital (ΔNWC)** — when a business grows, it typically needs more debtors outstanding and more inventory on the shelf. That growth in NWC consumes cash even though it does not appear in the profit statement.
- **− Capital Expenditure** — cash spent to buy, maintain, or expand the asset base. A telecom company building 5G towers, a steel plant adding capacity, a logistics company buying trucks: all of this is capex, and all of it reduces FCF even though it is not an expense on the income statement (it is capitalised and then depreciated).

**FCF is not PAT.** A company can show healthy net profit while generating deeply negative free cash flow if it is investing aggressively in capex or working capital. Conversely, a mature business with minimal growth needs may generate FCF well above its stated profit. Indian promoters routinely cite EBITDA margins in earnings calls; investors who do not translate to FCF often overpay.

**FCF is not EBITDA.** EBITDA ignores taxes, working capital movements, and capex entirely. It is a useful proxy for operating cash generation at the business level, but not a substitute for FCF in a valuation.

An illustration: a company reports EBIT of ₹100 crore, pays 25% tax, has D&A of ₹15 crore, grows its working capital by ₹20 crore (scaling fast), and spends ₹30 crore on capex.

```
FCF = 100 × (1 − 0.25) + 15 − 20 − 30
    = 75 + 15 − 20 − 30
    = ₹40 crore
```

The EBITDA for the same company is ₹115 crore. The gap between ₹115 crore EBITDA and ₹40 crore FCF is the cost of growth — and it is entirely invisible unless you build from operating cash flow upward.

## Input 2 — The Discount Rate (WACC)

The discount rate is the blended rate of return required by all providers of capital — equity shareholders and debt holders — weighted by their share of the total capital structure.

**WACC = (E/V) × Ke + (D/V) × Kd × (1 − t)**
{: .notice--info}

Where:
- **E/V** = equity as a fraction of total enterprise value
- **D/V** = debt as a fraction of total enterprise value
- **Ke** = cost of equity
- **Kd** = pre-tax cost of debt
- **t** = applicable tax rate (25% in the WACC examples)

### Cost of Equity: CAPM in India

The Capital Asset Pricing Model (CAPM) is the standard approach:

**Ke = Rf + β × ERP**
{: .notice--info}

**Rf — Risk-Free Rate: 6.84%**

A fixed illustrative benchmark in this article. For a live model, identify the security, price/yield observation date and cash-flow horizon. A sovereign bond still carries market-price risk before maturity.

**ERP — Equity Risk Premium: 7.08% (illustrative)**

This is the assumed incremental equity return over Rf. Do not attribute an undated input to a current dataset. [Damodaran's country-risk data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) provide a source for a separately dated estimate; retain the dataset date and avoid mixing country-risk adjustments twice.

**β — Beta**

Beta measures return sensitivity to a specified benchmark: covariance with benchmark returns divided by the variance of benchmark returns. It is not standalone volatility and does not guarantee a 1.5× response on every trading day. Specify the observation window, benchmark and estimation method.

Putting it together for illustrative sector cost-of-equity estimates:

| Sector | Illustrative β | Ke = 6.84% + β × 7.08% |
|--------|---------------|------------------------|
| FMCG / Consumer Staples | 0.50 | ~10.4% |
| Infrastructure / Utilities | 0.80 | ~12.5% |
| IT / Technology | 1.00 | ~13.9% |
| Real Estate / Construction | 1.20 | ~15.3% |
| NBFCs / Consumer Finance | 1.10 | ~14.6% |

The sector betas in the table are assumptions, not estimates fitted to those sectors. A dated market survey can be a cross-check, but matching a survey median does not validate a particular company’s CAPM inputs.

### Cost of Debt: Indian Rates

A company's cost of debt is its marginal borrowing rate for the relevant currency and maturity. The policy rate, sovereign curve, credit spread, fees and refinancing terms matter; repo plus a fixed spread is not a universal pricing identity.

As an arithmetic illustration, 8% pre-tax borrowing cost with an assumed tax rate of 25.168% gives 8%×(1−0.25168)=**5.99%** after tax, assuming the interest deduction is usable. This tax rate is an input to that calculation, not a universal company rate.

### Assembling WACC: Two Indian Examples

**Example 1: A debt-light FMCG company**
Capital structure: 80% equity, 20% debt. Ke 10.4%, Kd (pre-tax) 7%.

```
WACC = 0.80 × 10.4% + 0.20 × 7% × (1 − 0.25)
     = 8.32% + 1.05%
     = 9.37%
```

**Example 2: A leveraged real estate developer**
Capital structure: 40% equity, 60% debt. Ke 15.3%, Kd (pre-tax) 11%.

```
WACC = 0.40 × 15.3% + 0.60 × 11% × (1 − 0.25)
     = 6.12% + 4.95%
     = 11.07%
```

These WACCs use the explicitly stated capital weights and rounded Ke assumptions. They are illustrations, not calibrated company estimates. Market-value weights, currency, tax treatment and financing risk must be consistent before comparing with a survey.

The difference between a 9.4% WACC (FMCG) and an 11.1% WACC (real estate) might look modest in isolation. In a DCF it affects every discounted cash flow. The percentage effect depends on the chosen forecast and terminal growth; compute it rather than assuming a fixed 30–40% change.

## Input 3 — Terminal Value

No business is valued only for the next 5 or 10 years. Beyond the explicit forecast period, the **terminal value** (TV) captures all remaining value.

The standard approach in Indian practice is the **Gordon Growth Model**:

**TV = FCFₙ × (1 + g) / (WACC − g)**
{: .notice--info}

Where **g** is the perpetual growth rate of free cash flow beyond year n.

Long-run growth must be coherent with the business’s mature scale, currency, reinvestment and returns on capital. It is not simply a chosen GDP number: cash-flow growth requires reinvestment, which must also appear in terminal cash flows. The discounting formula requires WACC>g.

**Why the denominator is dangerous**

Suppose Year 10 FCF is ₹100 crore, WACC is 12%, and g is 4%:

```
TV = 100 × 1.04 / (0.12 − 0.04) = 104 / 0.08 = ₹1,300 crore
```

Now change g from 4% to 5%:

```
TV = 100 × 1.05 / (0.12 − 0.05) = 105 / 0.07 = ₹1,500 crore
```

The change adds ₹200 crore to terminal value **at the end of year 10**, not ₹200 crore to today’s value. At 12%, its present value is about ₹64.39 crore. The explicit ten-year cash-flow stream has not been specified here, so no comparison with its total is justified. Convergence requires g<WACC; a business growing faster than its addressable economy forever is an additional economic-consistency concern.

The **exit multiple method** serves as a sanity check. Multiply the terminal year EBITDA by a sector-appropriate EV/EBITDA multiple (observable from public comparables) to get an alternative TV. If the Gordon Growth Model gives ₹1,300 crore and the exit multiple gives ₹800 crore, the difference demands an explanation.

## Worked Example: A Fully Specified Fictional Company

Use annual FCFF of ₹10, ₹12 and ₹15 crore over the next three years. After year 3, cash flow grows at g forever. All figures are ₹crore; each cash flow arrives at year-end.

| Scenario | WACC | g | Year-3 terminal value | Present enterprise value |
|---|---:|---:|---:|---:|
| Bear | 15% | 2% | 117.69 | **105.02** |
| Base | 12% | 3% | 171.67 | **151.36** |
| Bull | 10% | 4% | 260.00 | **225.62** |

The cash-flow forecast is identical across these scenarios; only WACC and g change. The base terminal value is 15×1.03/(0.12−0.03)=₹171.67 crore. Enterprise value still needs a debt/cash and other-claim reconciliation before it becomes equity value.

If a comparison enterprise price were ₹200 crore, it would disagree with the base assumptions. A different expected cash-flow path, growth rate, discount rate or a combination could explain the difference. The price does not identify a unique market belief, and this fictional case supplies no Reliance price target.

## Sensitivity Analysis

A point-estimate DCF is almost always wrong. The honest way to present a DCF is as a range. The two most sensitive inputs are WACC and terminal growth rate. The table below shows the **present value of terminal value only** (₹ crore), assuming Year 10 FCF = ₹100 crore. Its share of total value must be computed from the actual explicit-period forecast.

**PV(TV) = FCF₁₀ × (1+g) / (WACC−g) / (1+WACC)^10**
{: .notice--info}

| WACC \ TGR   | g = 2% | g = 3% | g = 4% |
|--------------|--------|--------|--------|
| **WACC = 8%** | 787    | 954    | 1,204  |
| **WACC = 9%** | 616    | 725    | 879    |
| **WACC = 10%**| 492    | 567    | 668    |

The spread from the most pessimistic case (WACC 10%, g 2%) at ₹492 crore to the most optimistic (WACC 8%, g 4%) at ₹1,204 crore is about 2.45×. The range between a plausible bear and bull scenario is often large enough that DCF is better described as a framework for making assumptions explicit than as a precise valuation tool. This is not a deficiency — it is honesty. A P/E multiple of 25x gives a false sense of precision while hiding all the same assumptions in implicit form.

The key sensitivities to stress:

- At g=3% in this table, moving WACC from 9% to 10% reduces **PV(TV)** from about ₹725 crore to ₹567 crore, approximately 21.8%. This is a result of these inputs, not a universal percentage.
- At WACC=9%, moving g from 2% to 3% raises PV(TV) from about ₹616 crore to ₹725 crore, approximately 17.8%. Sensitivity rises as g approaches WACC.
- Shortening the explicit horizon shifts more of the model into its terminal assumptions. There is no universal doubling rule; calculate the resulting share for the full cash-flow path.

## Common Mistakes

**Using PAT as a proxy for cash flow.** Net profit includes non-cash items (depreciation), is distorted by the choice of depreciation method and accounting policy, and completely omits the capex needed to sustain the business. Build from EBIT, subtract taxes, add back D&A, subtract changes in NWC and capex.

**Setting WACC from intuition.** "12% feels right for an Indian mid-cap" is not a WACC. Start from the G-Sec rate (6.84%), add a beta-scaled equity risk premium (ERP 7.08%), adjust for the capital structure, and cross-check against a dated and appropriately comparable cost-of-capital source. The arithmetic is quick; defensibility depends on evidence for the inputs and consistency with the cash flows.

**Choosing terminal growth without a mature-business model.** Specify the relevant market, currency, reinvestment and return on capital. An indefinitely increasing share of a finite addressable economy is not a coherent end state. Mathematical convergence requires g<WACC; that condition alone does not establish economically sustainable growth. A dated practitioner survey can describe practice, but cannot supply a universal ceiling.

**Adding risk premiums without a distinct rationale.** CAPM is not limited by definition to large-cap stocks. If an analyst adds a size, liquidity or other adjustment, explain its evidence and avoid charging twice for risk already reflected in beta or the forecast. There is no universal 1–3% add-on for every smaller company.

**Letting terminal value exceed 85% of enterprise value without question.** When TV dominates this heavily, the explicit 5–10 year forecast is window dressing. You are, in effect, doing one calculation (what is the terminal state worth?) and dressing it in DCF notation. The honest fix is either extending the explicit forecast period to where the business reaches steady state, or doing more rigorous terminal state analysis — not adjusting g upward until the numbers look right.

---

Part 2 of this series applies the same toolkit to the institutions that make money by explicitly pricing the time value of money: India's banks and NBFCs. The next installment connects home-loan EMIs, lender spreads, capital retention and valuation scenarios without treating an unsourced price target as a verified transaction fact.


Primary references: [RBI government-securities primer](https://m.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=711), §§23–24 and 29; [Damodaran country-risk data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) for separately dated inputs; and [financial-firm valuation](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf) for the lender distinction developed in the series. All worked arithmetic was recomputed from the stated inputs on 2 October 2026.

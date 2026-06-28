---
title: "Discounted Cash Flows: The Math Behind Every Indian Valuation"
date: 2026-06-28 09:00:00
categories: [blog]
author: Ganesh Raman
tags: [Finance, DCF, Valuation, India, Investing, WACC]
toc: true
author_profile: true
classes: wide
excerpt: "A first-principles walkthrough of DCF mathematics using current Indian market parameters — 6.84% G-Sec yields, Damodaran's 7.08% equity risk premium for India, sector WACCs, and a live Reliance Industries example."
permalink: /blog/discounted-cash-flows-the-math-part-1/
---

Series: Discounted Cash Flows: The Complete Indian Guide

Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) | [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/)

Part 1 of 2. Next: [DCF in Action: Lending, Growth, and Capital Allocation in India](/blog/discounted-cash-flows-india-lending-and-growth-part-2/)

## Summary

Discounted Cash Flow (DCF) valuation is not a formula you memorize for an interview. It is a way of thinking about money, time, and risk that underpins every serious financial decision — from setting a home loan rate to pricing a ₹30,000 crore exchange IPO. This post builds the DCF model from scratch using current Indian market parameters: a 6.84% G-Sec risk-free rate (June 2026), Damodaran's 7.08% total equity risk premium for India (January 2026), and sector WACC benchmarks from the EY-NSE Cost of Capital Survey 2024. Part 2 of this series applies the same toolkit to lending businesses, NBFCs, and the NSE IPO valuation.

## Why Time Has a Price

Start with the simplest possible question: would you rather receive ₹1 lakh today or ₹1 lakh exactly one year from now?

The answer is obviously today — not because of impatience, but because of what you can do with the money in between. If you deposit ₹1 lakh in a fixed deposit at 7%, you will have ₹1,07,000 in a year. The person who waits gets ₹1,00,000. The difference is the price of time.

This observation — that a rupee today is worth more than a rupee in the future — is the entire foundation of DCF analysis. The rate at which you exchange present rupees for future rupees depends on your next best alternative. In financial markets, the closest thing to a risk-free next best alternative is the Indian government bond.

The 10-year Government of India bond (G-Sec) currently yields **6.84%** (June 2026). This is the baseline: if you hand the Government of India ₹100 today, it will return ₹106.84 in one year. Any investment that offers less than this, at the same level of risk, is a worse choice. This yield is what finance calls the **risk-free rate** (Rf). It has declined from ~7.1% in early 2024 as the RBI executed 125 basis points of rate cuts — bringing the repo rate from 6.50% down to 5.25% across 2025 and into 2026.

Most investments, however, are not Government bonds. They carry risk: the possibility that expected cash flows will not arrive, or will arrive diminished. Investors demand extra return to accept that risk. How much extra? That is the job of the discount rate.

## The DCF Formula

The present value of any stream of future cash flows is:

```
PV = CF₁/(1+r)¹ + CF₂/(1+r)² + CF₃/(1+r)³ + ... + CFₙ/(1+r)ⁿ + TV/(1+r)ⁿ
```

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
| 3 (TV) | 120.0        | 0.712                | 85.44                |
| **Total PV** |            |                      | **₹114.62 crore**    |

Two things are immediately apparent. First, the terminal value dominates: ₹85 crore of the ₹115 crore total is the present value of everything beyond year 3. In most real DCF models, terminal value accounts for 60–80% of total enterprise value. Second, the discount factor does meaningful work: ₹120 crore three years from now is only worth ₹85 crore today at a 12% rate. Raise that rate to 15% and the same ₹120 crore is worth only ₹78.9 crore. The discount rate is not a detail — it is a decision.

## Input 1 — Free Cash Flow

The number in the numerator of every DCF term is **free cash flow to the firm (FCFF)**, not profit.

```
FCF = EBIT × (1 − Tax Rate) + D&A − ΔNWC − Capex
```

Breaking this apart:

- **EBIT × (1 − t)** = net operating profit after tax (NOPAT). This is the cash the business generates from operations before financing costs are considered. India's standard corporate tax rate is 25.168% for domestic companies.
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

```
WACC = (E/V) × Ke + (D/V) × Kd × (1 − t)
```

Where:
- **E/V** = equity as a fraction of total enterprise value
- **D/V** = debt as a fraction of total enterprise value
- **Ke** = cost of equity
- **Kd** = pre-tax cost of debt
- **t** = corporate tax rate (25.168% for India)

### Cost of Equity: CAPM in India

The Capital Asset Pricing Model (CAPM) is the standard approach:

```
Ke = Rf + β × ERP
```

**Rf — Risk-Free Rate: 6.84%**

The India 10-year G-Sec yield as of June 2026. This rate establishes the floor: the government will guarantee this return with no credit risk. After the RBI's 125bps easing cycle (February 2025 to the current 5.25% repo rate), this yield has come down materially from its 7.1% level in early 2024.

**ERP — Equity Risk Premium: 7.08%**

The additional return equity investors require over the risk-free rate, to compensate for equity's uncertainty. Prof. Aswath Damodaran (NYU Stern) estimates India's total ERP at **7.08%** as of January 2026. This comprises a mature market ERP of ~4.23% plus a country risk premium (CRP) of **2.85%**, which reflects India's Baa3 sovereign rating from Moody's and an associated default spread of 1.87%. The Damodaran dataset is updated annually and is the most widely used public reference for India's ERP in institutional valuations.

**β — Beta**

Beta measures a company's return volatility relative to the broader market (Nifty 50). A β of 1.0 means the stock moves in line with the index; β of 1.5 means it amplifies moves by 50%; β of 0.5 means it is half as volatile. Beta varies meaningfully by sector — a defensive staples company is structurally less sensitive to market cycles than a real estate developer.

Putting it together for illustrative sector cost-of-equity estimates:

| Sector | Illustrative β | Ke = 6.84% + β × 7.08% |
|--------|---------------|------------------------|
| FMCG / Consumer Staples | 0.50 | ~10.4% |
| Infrastructure / Utilities | 0.80 | ~12.5% |
| IT / Technology | 1.00 | ~13.9% |
| Real Estate / Construction | 1.20 | ~15.3% |
| NBFCs / Consumer Finance | 1.10 | ~14.6% |

The **EY-NSE Cost of Capital Survey 2024** found that the median cost of equity across Indian companies is **14.2%**, up 40 basis points from 2021. FMCG sits at the lower end (~10–11%), real estate at the higher end (~15–16%). These numbers are consistent with CAPM at current G-Sec rates and Damodaran's ERP.

### Cost of Debt: Indian Rates

A company's cost of debt (Kd) is its pre-tax borrowing rate, anchored to:

- The RBI repo rate (5.25%) plus a credit spread based on the borrower's rating
- AAA-rated Indian corporates borrow at approximately repo + 150–200bps ≈ 6.75–7.25%
- A-rated corporates at repo + 250–300bps ≈ 7.75–8.25%
- Lower-rated or leveraged borrowers at 10%+

Post-tax cost of debt = Kd × (1 − tax rate). At a pre-tax rate of 8% and Indian corporate tax of 25.168%: 8% × (1 − 0.25168) = **5.99%** post-tax.

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

The RBSA Cost of Capital in India 6th Edition (2023) reports sector median WACCs: FMCG ~10.4%, IT ~13–14%, real estate ~15.3%. These benchmarks confirm that the CAPM-anchored WACCs above are calibrated correctly for Indian markets.

The difference between a 9.4% WACC (FMCG) and an 11.1% WACC (real estate) might look modest in isolation. In a DCF, it is not: over a 10-year horizon, it changes terminal value by 30–40% even with identical FCF projections.

## Input 3 — Terminal Value

No business is valued only for the next 5 or 10 years. Beyond the explicit forecast period, the **terminal value** (TV) captures all remaining value.

The standard approach in Indian practice is the **Gordon Growth Model**:

```
TV = FCFₙ × (1 + g) / (WACC − g)
```

Where **g** is the perpetual growth rate of free cash flow beyond year n.

The EY-NSE 2024 survey found that Indian corporate finance teams use an average terminal growth rate of **4.4%** and equity analysts use **4.7%**. These are not arbitrary — they approximate India's long-run nominal GDP growth (real GDP ~6.5–7% less a haircut for the divergence between aggregate GDP growth and per-firm FCF growth in a competitive economy).

**Why the denominator is dangerous**

Suppose Year 10 FCF is ₹100 crore, WACC is 12%, and g is 4%:

```
TV = 100 × 1.04 / (0.12 − 0.04) = 104 / 0.08 = ₹1,300 crore
```

Now change g from 4% to 5%:

```
TV = 100 × 1.05 / (0.12 − 0.05) = 105 / 0.07 = ₹1,500 crore
```

A single percentage point increase in terminal growth rate added ₹200 crore to the valuation — more than the entire 10-year FCF stream. And if g approaches WACC, the formula produces infinitely large values. A company cannot grow faster than the economy in perpetuity; this is a mathematical identity, not a philosophical position.

The **exit multiple method** serves as a sanity check. Multiply the terminal year EBITDA by a sector-appropriate EV/EBITDA multiple (observable from public comparables) to get an alternative TV. If the Gordon Growth Model gives ₹1,300 crore and the exit multiple gives ₹800 crore, the difference demands an explanation.

## Worked Example: Reliance Industries

A November 2025 analyst DCF for Reliance Industries (RIL) provides a public reference with unusually explicit parameters for Indian markets.

| Scenario | WACC   | Terminal Growth Rate | DCF Fair Value |
|----------|--------|---------------------|----------------|
| Bear     | 10.50% | 1.50%               | Below ₹876     |
| Base     | 9.07%  | 2.50%               | **₹876**       |
| Bull     | 8.00%  | 3.50%               | Above ₹876     |

At the time of the model, Reliance traded at approximately ₹1,478 — meaningfully above the analyst's base case DCF of ₹876.

This gap does not automatically mean the stock is overvalued. It reflects the market's collective belief that Reliance's future FCFs will be substantially higher than the analyst's assumptions, drawing on optionality across Jio's digital services, JioMart's retail scale, and the green energy buildout. The base case WACC of 9.07% is plausible given Reliance's diversified revenue, strong balance sheet, and strategic government relationships that reduce tail risk.

What the model makes explicit is the *implied* assumption at market price: the market must be pricing in a terminal growth rate materially above 2.5%, a WACC closer to 8% than 9%, substantially higher FCF than the analyst projects, or some combination of all three. DCF does not eliminate this uncertainty — it forces you to state it precisely, so it can be evaluated and argued rather than absorbed unconsciously into a "feels like a quality franchise at a reasonable price" judgement.

## Sensitivity Analysis

A point-estimate DCF is almost always wrong. The honest way to present a DCF is as a range. The two most sensitive inputs are WACC and terminal growth rate. The table below shows the **present value of terminal value only** (₹ crore), assuming Year 10 FCF = ₹100 crore. In practice, TV represents 60–80% of total enterprise value.

```
PV(TV) = FCF₁₀ × (1+g) / (WACC−g) / (1+WACC)^10
```

| WACC \ TGR   | g = 2% | g = 3% | g = 4% |
|--------------|--------|--------|--------|
| **WACC = 8%** | 787    | 954    | 1,204  |
| **WACC = 9%** | 615    | 725    | 879    |
| **WACC = 10%**| 491    | 567    | 668    |

The spread from the most pessimistic case (WACC 10%, g 2%) at ₹491 crore to the most optimistic (WACC 8%, g 4%) at ₹1,204 crore is 2.5×. The range between a plausible bear and bull scenario is often large enough that DCF is better described as a framework for making assumptions explicit than as a precise valuation tool. This is not a deficiency — it is honesty. A P/E multiple of 25x gives a false sense of precision while hiding all the same assumptions in implicit form.

The key sensitivities to stress:

- A **100bps increase in WACC** reduces terminal value by roughly 15–25% across most parameter combinations
- A **100bps increase in terminal growth rate** increases terminal value by a similar 15–25%, but the effect is non-linear — it grows larger as g approaches WACC
- Reducing the forecast horizon from 10 years to 5 years roughly doubles the weight of the terminal value, amplifying both sensitivity and uncertainty

## Common Mistakes

**Using PAT as a proxy for cash flow.** Net profit includes non-cash items (depreciation), is distorted by the choice of depreciation method and accounting policy, and completely omits the capex needed to sustain the business. Build from EBIT, subtract taxes, add back D&A, subtract changes in NWC and capex.

**Setting WACC from intuition.** "12% feels right for an Indian mid-cap" is not a WACC. Start from the G-Sec rate (6.84%), add a beta-scaled equity risk premium (ERP 7.08%), adjust for the capital structure, and check against the EY-NSE benchmark median of 14.2% for cost of equity. The process takes 30 minutes and produces a defensible number.

**Pushing terminal growth above nominal GDP.** India's nominal GDP grows at approximately 10–11% (real 6.5–7% plus inflation 3–4%). A company cannot indefinitely grow faster than the economy in which it operates. The EY-NSE average of 4.4% for Indian DCF practitioners reflects this ceiling with a reasonable discount for competitive erosion.

**Ignoring the size premium for small and mid-cap companies.** The CAPM gives you the cost of equity for a liquid, large-cap stock. For less liquid or smaller Indian companies, add 1–3% for illiquidity and execution risk. A Tier-2 city food delivery startup is not priced like HDFC Bank equity.

**Letting terminal value exceed 85% of enterprise value without question.** When TV dominates this heavily, the explicit 5–10 year forecast is window dressing. You are, in effect, doing one calculation (what is the terminal state worth?) and dressing it in DCF notation. The honest fix is either extending the explicit forecast period to where the business reaches steady state, or doing more rigorous terminal state analysis — not adjusting g upward until the numbers look right.

---

Part 2 of this series applies the same toolkit to the institutions that make money by explicitly pricing the time value of money: India's banks and NBFCs. Every home loan EMI, Bajaj Finance's 10.1% NIM, HDFC Bank's 3.46% net interest margin, and the ₹30,000 crore NSE IPO valuation are all DCF at work — just with different variables in the equation.

---
title: "What Is a Bank Worth? P/BV, Excess Returns, and Equity DCF for Financials"
date: 2026-07-26 12:00:00 UTC
last_modified_at: 2026-10-02
categories: [blog]
author: Ganesh Raman
tags: [Finance, Banking, NBFC, Valuation, P/BV, Excess-Returns, DCF, India, Investing, HDFC-Bank, ICICI-Bank, IndusInd, Bajaj-Finance]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "A reproducible P/BV and excess-returns framework for lenders: perpetual growth, finite fade, recovery assumptions, and the difference between creditor recovery and equity value."
header:
  overlay_color: "#1e3a5f"
  overlay_filter: 0.65
permalink: /blog/bank-nbfc-valuation-pbv-excess-returns/
---

*Revised 2 October 2026: Corrected Gordon versus finite-fade assumptions, P/B arithmetic, recovery interpretation and source definitions. Unreconciled issuer/price figures are now explicitly scenario inputs; reported SBI RoE and the HDFC merger date have primary citations. Original publication date retained.*


*Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| [Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) \| **Part 4 (this post)***

*Related: [Bank & NBFC Valuation Lab](https://ganesh47.github.io/india-dcf-explorer/#/valuation-lab). Check its displayed data dates and inputs before comparing it with this article's fixed scenarios.*

## Why Enterprise DCF Is Awkward for Banks

DCF does not stop working when the company is a bank. The difficulty is choosing the cash flow and the capital claim being valued.

For a manufacturer, free cash flow to the firm is before payments to lenders. Discount it at WACC to obtain operating enterprise value, then reconcile debt, cash and other claims to equity. Do not subtract debt service from FCFF and then apply WACC again.

For a lender, deposits and borrowings are central to producing income. Separating operating reinvestment from financing becomes difficult; conventional working-capital and net-debt adjustments can obscure the economics. The practical alternative is to value **equity cash flows** or **residual income** directly. [Damodaran's financial-firm valuation paper](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf), particularly the equity cash-flow and excess-return sections, sets out this distinction.

A bank's distributable cash is constrained by the equity needed to support its risk-weighted assets. Loan growth and profit are separate inputs. A simplified equity DCF deducts incremental required equity from net income and discounts the result at the cost of equity, Ke.

## The P/BV Framework—and Its Conditions

Under a constant-growth dividend model with clean-surplus accounting:

```
Fair P/BV = (RoE − g) / (Ke − g)
```

Here RoE means next-period earnings divided by **opening** book equity, g is perpetual growth of book equity, and Ke is the required equity return. Retained earnings must fund the assumed growth consistently. The model needs Ke > g; without external equity issuance, g cannot exceed RoE indefinitely while also paying non-negative dividends.

If RoE = Ke, the ratio is 1×. If RoE exceeds Ke, the franchise creates value above book. If RoE is below Ke, the model can value it below book. But a negative algebraic output when RoE < g is a warning that the assumed payout/growth regime is infeasible—not a meaningful negative price for limited-liability common equity.

For the scenario matrix below, use **Rf=6.70% and ERP=7.00% as fixed illustrative assumptions**, so Ke=6.70%+β×7.00%. These are not October market quotes, nor an independently estimated beta series.

## The Excess Returns Model

The same value can be expressed as book equity plus discounted economic profit:

```
Equity value = B₀ + Σ [(RoE_t − Ke) × B_(t−1)] / (1 + Ke)^t
```

The timing matters: year t earnings and the equity charge use opening book B_(t−1). With RoE and growth g constant forever, first-year residual income is (RoE−Ke)×B₀ and grows at g. Its present value gives the same Gordon ratio.

If the excess-return spread instead lasts **n years**, after which RoE becomes Ke, the finite-fade result is different:

```
V/B₀ = 1 + [(RoE − Ke)/(Ke − g)] × [1 − ((1+g)/(1+Ke))^n]
```

This expression assumes constant RoE and book growth during those n years and no excess returns afterwards. For illustrative RoE 14.4%, Ke 13%, g 9%, the P/B ratios are 1.058× after five years, 1.106× after ten, and 1.180× after twenty. The perpetual limit is 1.350×. Extending duration approaches that limit; it does not by itself justify a price above the same perpetual benchmark.

## Worked HDFC Scenario: What a Premium Does—and Does Not—Tell Us

This is a teaching scenario carrying fixed inputs, **not HDFC Bank's verified FY25 balance sheet or a current price target**. It also supplies the common HDFC assumptions used in Part 2.

| Input or result | Value |
|---|---:|
| Assumed opening book equity | ₹3,50,000 crore |
| Assumed forward RoE | 14.4% |
| Ke (β=0.90) | 13.00% |
| Perpetual g | 9.00% |
| First-year residual income | (14.4%−13%)×₹3,50,000 = ₹4,900 crore |
| PV of growing residual income | ₹4,900/(13%−9%) = ₹1,22,500 crore |
| Equity value | ₹3,50,000+₹1,22,500 = ₹4,72,500 crore |
| Model P/B | 1.350× |
| Comparison price/B input | 2.85× |
| Gap to model value | +111.1% |

The gap identifies disagreement with the input set. It cannot uniquely reveal the market's cost of equity, expected return or growth rate.

Holding RoE=14.4% and g=9%, a 2.85× ratio implies Ke of **10.895%**. At Ke=10.5%, the model gives **3.60×**, not 2.85×. Holding Ke=13% and g=9% instead, 2.85× requires RoE=20.4%. These are conditional calculations, not evidence that either forecast is correct.

For factual context, the HDFC Ltd merger became effective on **1 July 2023**, as recorded in [HDFC Bank's exchange disclosure](https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/personal-banking/about-us/stakeholders-information/disclosures/other-stock-exchange-disclosure/21-reg30.pdf), page 1. Comparing pre- and post-merger returns requires consistent consolidation, averaging periods and treatment of exceptional items. This article does not infer a specific NIM recovery from the scenario price.

## A Reproducible Input Matrix

The names make the scenarios easier to follow, but **the RoE, beta, growth and comparison-price inputs are illustrative, not a verified FY25 peer ranking**. Historical price/B figures from the original post lacked reproducible price dates and denominator definitions; they are retained only as comparison inputs. An issuer investment analysis needs a separate source table before those labels can be treated as actual financial observations.

The exception explicitly sourced here is SBI's **reported FY25 RoE of 19.87%** in its [FY2024–25 chairman's message](https://sbi.bank.in/corporate/SBIAR2425/chairmans-message.html), “Operating Performance.” It is not replaced with an arbitrary “normalised” 14% merely because leverage contributes to RoE. Its beta, g and price/B remain assumptions like the other scenarios.

Ke is displayed to two decimals and every model result is calculated from unrounded inputs. “Gap” means comparison price/model minus one; it is not proof of mispricing.

| Named scenario | RoE input | β input | Ke | g input | Algebraic P/B | Price/B input | Gap |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Bajaj Finance** | 19.10% | 0.95 | 13.35% | 10.00% | 2.716× | 6.11× | +124.9% |
| **AU Small Finance** | 12.00% | 1.05 | 14.05% | 8.00% | 0.661× | 2.84× | +329.6% |
| **Muthoot Finance** | 18.20% | 0.90 | 13.00% | 9.00% | 2.300× | 2.90× | +26.1% |
| **Kotak Mahindra** | 13.10% | 0.80 | 12.30% | 8.00% | 1.186× | 2.56× | +115.8% |
| **ICICI Bank** | 16.30% | 1.00 | 13.70% | 9.00% | 1.553× | 2.66× | +71.3% |
| **Shriram Finance** | 16.70% | 1.00 | 13.70% | 8.00% | 1.526× | 2.87× | +88.0% |
| **HDFC Bank** | 14.40% | 0.90 | 13.00% | 9.00% | 1.350× | 2.85× | +111.1% |
| **Axis Bank** | 15.10% | 1.00 | 13.70% | 8.00% | 1.246× | 2.02× | +62.2% |
| **SBI** | 19.87% | 1.15 | 14.75% | 6.00% | 1.585× | 1.50× | -5.4% |
| **Bandhan Bank** | 11.60% | 1.30 | 15.80% | 7.00% | 0.523× | 0.97× | +85.6% |
| **Yes Bank** | 5.10% | 1.50 | 17.20% | 5.00% | 0.008× | 1.33× | Near-zero baseline |
| **IndusInd Bank** | 4.00% | 1.40 | 16.50% | 6.00% | -0.190× | 1.03× | Invalid stable case |
| **IDFC First Bank** | 3.90% | 1.25 | 15.45% | 8.00% | -0.550× | 0.85× | Invalid stable case |

For IndusInd and IDFC First, the negative output is displayed only to diagnose invalid perpetual assumptions. Yes Bank's tiny positive result is highly sensitive because RoE barely exceeds g; a percentage “premium” against that near-zero denominator is not a useful investment verdict.

## Four Questions Hidden Inside the Multiple

**Franchise or forward-return hypothesis.** The Bajaj scenario gives 2.716× from RoE=19.1%, Ke=13.35%, g=10%. Its comparison input 6.11× is 124.9% higher. Gordon already assumes the stated spread persists forever. Explaining this gap needs different forward returns, growth, risk, accounting or a multistage path—not merely “fifteen more years” at identical assumptions.

**Source and definition hypothesis.** Does a higher ratio actually compare like with like? Standalone versus consolidated equity, average versus closing book, exceptional gains, accounting losses and price dates can all move the apparent comparison. A model cannot repair mismatched source data.

**Recovery hypothesis.** A weak current RoE can be a poor terminal assumption. The recovery path must be forecast explicitly, including provisions, retained capital and possible dilution. A stable end-state ratio is a cross-check, not the present value of the transition by itself.

**Risk hypothesis.** Funding concentration, maturity mismatch and governance uncertainty can affect cash flows and required returns. They do not allow us to identify a unique market motive from a P/B gap. Stress assumptions should be stated and tested separately.

## IndusInd: Two Different Input Sets, Two Different Conclusions

Under the **entity-specific** inputs Ke=16.5%, g=6%, a comparison price/B of 1.03× implies:

```
RoE = g + (P/B) × (Ke − g)
    = 6% + 1.03 × (16.5% − 6%)
    = 16.815%
```

At a recovered RoE of 14%, that input set gives 0.762×. The 1.03× comparison price is 35.2% above it. This does not establish that the market expects that exact recovery: changing Ke or g changes the implied return.

Under the **common sliders** Ke=13.7%, g=9%, HDFC's assumed 14.4% RoE gives **1.149×**. IndusInd's 4% current-return input produces an infeasible algebraic −1.064×. A recovered RoE=16% produces **1.489×**. Against that stable recovery scenario, 1.03× is about a **31% discount**.

Neither conclusion can be carried from one input set to the other. The −0.190× in the matrix comes from Ke=16.5%, g=6%; it is not the common-slider result. A proper recovery DCF also values the years before the end state and includes any capital needed to reach it.

## Yes Bank: A Stress Test, Not an Equity Backstop

With the illustrative comparison ratio 1.33×, Ke=17.2% and g=5%, implied stable RoE is **21.226%**. This is demanding relative to the 5.1% input, but it is one conditional endpoint calculation. It does not prove irrational pricing or establish an achievable operating plan.

A reconstruction, a shareholder's sponsorship or recovery by creditors is not a guaranteed equity floor. Common equity is the residual after prior claims; recapitalisation can dilute it substantially. The [liquidity-risk article](/blog/nbfc-liquidity-risk-ilfs-indusind/) now separates creditor recovery from residual equity. Legal outcomes for instruments such as AT1 bonds also require their own dated orders; this calculation does not decide them.

## The RoE Decomposition: Keep Denominators Consistent

The operating chain remains useful, provided it is defined correctly:

```
Revenue/assets = NII/average assets + non-interest income/average assets
Operating costs/assets = CIR × revenue/assets
Pre-tax RoA = revenue/assets − operating costs/assets − provisions/assets
After-tax RoA = net income/average assets
RoE = after-tax RoA × (average assets/average equity)
```

An issuer's published NIM may use average earning assets, while credit cost may use average advances. Convert both to a common denominator before subtraction; include non-interest income and tax. NIM×(1−CIR) minus a loan-based credit-cost percentage is not automatically after-tax RoA.

Part 3's two fictional banks make this explicit. With revenue/assets=4.2%, CIR=42%, asset-based credit cost=0.5% versus 1.5%, tax=25% and leverage=12×, RoE is **17.424% versus 8.424%**. Part 3 explicitly converts those **average-equity** returns to opening-equity returns of 18.03384% and 8.59248%, assuming linear within-year book growth. At Ke=12% and g=7% versus 4%, P/B is **2.207× versus 0.574×**, using unrounded inputs. These are model outcomes, not guaranteed market prices.

## What the P/B Multiple Is Really Pricing

Under the clean-surplus residual-income identity, paying 2.85× book means requiring PV of excess returns equal to 1.85× current book. In the ₹3,50,000 crore scenario, that is **₹6,47,500 crore**.

Our original RoE=14.4%, Ke=13%, g=9% scenario supplies only ₹1,22,500 crore of residual-income PV. Adding longer duration to an already perpetual model cannot fill the gap. A higher-return path, different stable growth, lower required return or other adjustments must be modeled explicitly. A capitalized value is a stock of rupees; it must not be labelled “rupees per year.”

## Putting the Series Together

Parts 1 and 2 introduce discounting and equity cash flows. Part 3 connects revenue, operating costs, credit provisions, tax and capital retention. Liquidity risk adds refinancing and stress scenarios. This post separates finite excess-return duration from perpetual growth.

The most useful questions are practical: Which numbers are issuer observations? Which are assumptions? Do their dates and denominators agree? Is growth financed? What does common equity receive in the stress case?

The formula is short. The hard work is choosing an evidence-backed return path and a coherent set of assumptions—and knowing when a simple stable-growth model cannot answer the question.

## Sources and Reproduction

- [Damodaran, *Valuing Financial Service Firms* (2009)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf), printed pages 15 and 22–25: dividend and excess-return models.
- [SBI FY2024–25 chairman's message](https://sbi.bank.in/corporate/SBIAR2425/chairmans-message.html), “Operating Performance”: reported RoE 19.87%, RoA 1.10% and CIR 51.64%. These are different from scenario assumptions.
- [HDFC Bank exchange disclosure, 21 September 2023](https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/personal-banking/about-us/stakeholders-information/disclosures/other-stock-exchange-disclosure/21-reg30.pdf), page 1: merger effective date.

All displayed model values were recalculated on 2 October 2026 from unrounded inputs. The local review bundle includes the standard-library calculation script and its output. No current investment price target is asserted.

*Previous: [Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) · [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/)*

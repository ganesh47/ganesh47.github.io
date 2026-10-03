---
title: "The Two-Number Truth: Operating Ratio, Credit Cost, and Why They Tell Opposite Sides of the Same DCF Story"
date: 2026-07-05 00:00:00 UTC
last_modified_at: 2026-10-02
categories: [blog]
author: Ganesh Raman
tags: [Finance, Banking, DCF, Operating-Ratio, Credit-Cost, India, Investing]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "A lender's Cost-to-Income Ratio tells you how efficiently the machine runs. It says nothing about whether the machine's output actually arrives as cash. This post connects operating efficiency to DCF valuation through the lens of Indian banks and NBFCs — with worked examples and the specific data from cases where the ratio looked fine right before things went wrong."
header:
  overlay_color: "#0f766e"
  overlay_filter: 0.55
permalink: /blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/
---

*Revised 2 October 2026: Corrected net-income versus advance-growth arithmetic, fictional versus issuer RoE, denominator and accrual timing explanations, and the Alpha/Beta calculation. Added the Part 4 link and a primary SBI reference. Original publication date retained.*


Series: Discounted Cash Flows: The Complete Indian Guide

Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| [Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) \| [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/) \| [Liquidity risk](/blog/nbfc-liquidity-risk-ilfs-indusind/)

Part 3 of the series. Previous: [Discounted Cash Flows in Action: Lending, Growth, and Capital Allocation in India](/blog/discounted-cash-flows-india-lending-and-growth-part-2/)

Extended reading: [Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) · [Part 4: P/BV and Excess Returns](/blog/bank-nbfc-valuation-pbv-excess-returns/)

## Summary

Part 1 built the DCF toolkit from scratch. Part 2 applied it to Indian lending institutions and showed why banks cannot be valued with standard FCFF. This post completes the picture: once you can value a bank, you need to know which of its operational metrics are leading indicators of cash realization and which are structural illusions. The answer comes down to two numbers — Cost-to-Income Ratio and Credit Cost Ratio — and why they must always be read together.

## The Machine That Leaks in Two Places

Consider a sugarcane crusher. The Cost-to-Income Ratio (CIR) tells you how efficiently the machine runs — what fraction of every rupee of juice revenue goes to operating the press. A machine running at 40% CIR is efficient: 60 paise remains before provisions, tax and any costs outside the defined operating ratio. For a bank, funding interest is already netted into net interest income.

But CIR says nothing about one crucial variable: what percentage of the sugarcane entering the machine is actually fresh? A machine running at 40% efficiency but fed 20% spoiled sugarcane will yield less juice than a 55%-efficient machine fed entirely fresh stock. The machine's efficiency metric told you nothing about the input quality.

A lender's balance sheet works the same way. CIR measures how efficiently the machine runs. **Credit cost measures recognized loss provisions relative to a specified loan or asset base. It is not itself a cash-collection ratio.** Ignore either number and you are reading half the story.

**CIR and credit cost are useful starting points; profitability also needs revenue, denominators and tax:**

**Pre-tax RoA = NII/assets + Non-interest income/assets − Operating costs/assets − Provisions/assets**
{: .notice--info}

Where:
- Issuer NIM may use average earning assets; convert it to average total assets before using this identity.
- **Operating cost ratio** is operating expenses divided by average total assets. CIR uses income, so it is not the same ratio.
- Published credit cost commonly uses average advances; multiply it by advances/assets to obtain provisions/assets. Include non-credit provisions where relevant, then deduct tax to obtain after-tax RoA.

CIR captures the first drain. Credit cost captures the second. A bank that optimises only on CIR is like a shopkeeper who counts receivables as income: her books look profitable for months, right up until the moment her customers stop paying.

## What CIR Actually Measures

The Cost-to-Income Ratio is the banking equivalent of an industrial operating ratio, but applied to a different base:

**CIR = Operating Expenses / (Net Interest Income + Non-Interest Income)**
{: .notice--info}

**The numerator includes:** staff costs (salaries, provident fund, ESOPs, pension), technology (core banking, ATMs, digital infrastructure), branch costs (rent, utilities), administration, and depreciation.

**The numerator explicitly excludes:** interest paid on deposits (already netted in the denominator as part of NIM) and provisions for NPAs (tracked separately as credit cost). This is what makes banking CIR non-comparable with an industrial operating ratio — the cost of "raw material" (deposit interest) is already stripped out before the ratio is calculated.

### Indian Benchmarks by Segment

| Segment | Typical CIR | Reason |
|---------|------------|--------|
| Large private banks (HDFC, ICICI) | 38–42% | Scale, CASA funding, digital efficiency |
| Mid-size private banks (Axis, Kotak) | 42–48% | Good franchise but less CASA advantage |
| Public sector banks (SBI standalone) | ~52–56% | Higher employee costs, legacy branch networks |
| Small finance banks | ~65–75% | Building franchise, high branch density |
| Established NBFCs (Bajaj Finance) | 25–40% | No deposit branch network; structurally leaner |
| Housing finance companies | 25–35% | Asset-heavy, low servicing complexity |

One verified FY25 reference is [SBI's chairman's message](https://sbi.bank.in/corporate/SBIAR2425/chairmans-message.html), “Operating Performance”: standalone CIR **51.64%**, RoA **1.10%** and RoE **19.87%**. These definitions belong to that issuer and reporting period; a peer comparison needs equally sourced, consistent figures.

Do not mix standalone bank income with consolidated insurance or asset-management operations. The broad segment ranges above are rough analytical orientation, not a sourced current peer ranking.

### Operating Leverage: Why Scale Is the Moat

A core banking platform built for five million customers costs almost the same to run for customer number five million and one. Compliance infrastructure, risk management teams, and leadership are largely fixed costs. This creates powerful operating leverage at scale.

A bank growing from ₹1 lakh crore to ₹2 lakh crore in advances does NOT double its operating cost — the cost base might grow 15–20% while NII doubles. This structural advantage compounds across decades. HDFC Bank's ability to run at 40% CIR while a small finance bank runs at 70% CIR does not mean HDFC manages every rupee better — it means HDFC's fixed cost base is amortised over a vastly larger franchise.

The practical implication: **low CIR can be the product of genuine efficiency or merely scale.** An analyst must distinguish the two. A smaller bank can reduce CIR as revenue grows faster than operating costs, but revenue growth alone cannot establish that it will overtake another bank's CIR. Forecast both numerator and denominator. The valuation question is whether the credit quality of that rapid growth will hold.

## The Accrual Trap: Why CIR Looks Good Before the Crisis

The most important limitation of CIR is timing. Here is the mechanism, step by step.

### The 90-Day Clock

Under RBI's Income Recognition, Asset Classification and Provisioning (IRACP) norms, interest income on performing (standard) assets is recognised on an accrual basis — the bank books the income when it is *due*, not when it is *received*.

For timing intuition, take a hypothetical ₹100 crore loan at 10% annually: one quarter's simple interest is ₹2.5 crore. If that quarter's interest remains unpaid for more than 90 days, the asset can become non-performing under the applicable rule; reverse uncollected accrued interest when required and recognize the relevant provision.

Do not stretch 30, 60 and 90 days past due across three whole quarters. A missed payment ages in calendar days. The exact income reversal depends on accrued and uncollected amounts, not a generic assumption that two quarters always reverse together. Provisioning also depends on security, asset category and the applicable regulatory regime.

### Provisioning Requires a Dated Rule

Non-performing classification and the required provision are separate questions. Asset category, time in the relevant category, secured and unsecured portions, recoverable collateral and the applicable RBI regime affect the calculation. Time **as doubtful** must not be confused with total time since first becoming NPA; the original table did so.

This revision removes that misleading ladder rather than treating a simplified percentage table as current regulatory guidance. Use the applicable dated RBI instruction for the institution and loan category. A provision coverage ratio is a diagnostic alongside collateral and asset quality, not a universal cash-recovery percentage or a blanket present-day 70% requirement.

### Yes Bank: The Canonical Indian Case

Yes Bank's collapse is the cleanest documented case of CIR-as-illusion in Indian banking. The cited data:

- **FY18:** RoA 1.78% — comparable to private sector peers. Gross NPA: ₹2,627 crore (1.52% of advances). On these numbers, Yes Bank looked like a well-run mid-size private bank.
- **The hidden stress:** RBI's Asset Quality Review (AQR) found a GNPA divergence of approximately ₹6,355 crore — Yes Bank was under-reporting its bad loans by this amount. Loans to IL&FS, DHFL, Jet Airways, Café Coffee Day, and Essel Group had been kept standard when they should have been classified as stressed.
- **FY19 cliff:** RoA crashed to 0.52%. New CEO Ravneet Gill could not raise capital against worsening asset quality. GNPA doubled to ₹17,134 crore by September 2019.
- **The provisioning gap:** Provision Coverage Ratio in FY19 was **43.1%** — the lowest among comparable banks, and far below the RBI's desirable 70%. For every ₹100 of bad loans on the books, only ₹43 of provisions had been set aside. The remaining ₹57 would hit future quarters.
- **FY20:** Net loss of ₹16,433 crore. RBI moratorium in March 2020.

What was Yes Bank's CIR doing during FY17–FY18? The available evidence is that the ratio appeared reasonable — the accrued interest from stressed borrowers was inflating NII (the denominator), making operating costs look proportionally small. The signal was not in the efficiency ratio. It was in the divergence between PCR and GNPA, the concentration of loans to stressed sectors, and the operating cash flow vs stated profit gap.

A **credit-cost-adjusted expense ratio** can put operating expenses and provisions on the same revenue base:

**Adjusted ratio = (Operating Expenses + Provisions) / Operating Income**
{: .notice--info}

It is not a cash-collection ratio: provisions are accounting charges, and the denominator can still include accrual income. Convert a published credit-cost percentage to rupees or to the same denominator before adding it to operating expenses. In the fictional example below, (1.764+0.500)/4.200=53.905% for Alpha and (1.764+1.500)/4.200=77.714% for Beta. Adding a loan-based 2% directly to a revenue-based CIR would mix denominators.

## The RoA Decomposition: Three Levers, One Number

Return on Assets is the cleanest single-number summary of a bank's business model:

**RoA = NIM + Non-Interest Income − Operating Cost Ratio − Credit Cost Ratio − Tax Effect**
{: .notice--info}

All terms must be converted to average total assets. Published NIM and credit-cost denominators can differ; the identity applies only after conversion.

The relationship between CIR and the operating cost ratio:

**Operating Cost Ratio = CIR × (NIM + Non-Interest Income Ratio)**
{: .notice--info}

So a low CIR is good only if the revenue ratio (NIM + fees) is also meaningful. An NBFC with CIR of 35% and NIM of 4% has an operating cost ratio of ~1.4%. A bank with the same 35% CIR but NIM of 8% has an operating cost ratio of ~2.8%. Same CIR; very different cost burden relative to assets.

### Worked Example: Same CIR, Very Different DCF

Two banks, identical in size (₹1,00,000 crore average assets) and efficiency (CIR = 42%):

| | Bank Alpha | Bank Beta |
|---|---|---|
| NIM | 3.50% | 3.50% |
| Non-Interest Income | 0.70% | 0.70% |
| Total Operating Revenue | 4.20% | 4.20% |
| Operating Expenses (CIR = 42%) | 1.764% | 1.764% |
| Pre-Provision Operating Profit | 2.436% | 2.436% |
| **Provisions / average assets** | **0.500%** | **1.500%** |
| Pre-Tax RoA | 1.936% | 0.936% |
| Tax (25%) | 0.484% | 0.234% |
| **RoA** | **1.452%** | **0.702%** |
| Equity multiplier (12×) | 12× | 12× |
| **RoE on average equity** | **17.424%** | **8.424%** |
| Cost of Equity (Ke) | 12% | 12% |
| Sustainable growth (g) | 7% | 4% |
| Opening-equity RoE, with linear within-year book growth | 18.03384% | 8.59248% |
| **Model P/B = (opening-equity RoE − g)/(Ke − g)** | **2.207×** | **0.574×** |

For this teaching model, assume average equity equals opening equity×(1+g/2), as if book grew linearly within the year. Therefore opening-equity RoE equals average-equity RoE×(1+g/2). An actual bank needs its reported averages and book changes reconciled; this conversion is not universal.

With that explicit convention, the assumptions produce about a **3.84× difference in model P/B**. Both provisions and g differ here, so it is not a pure estimate of credit cost alone. These are fictional modeled values, not observed market prices. The calculation uses unrounded inputs.

*(Illustrative example; leverage, g, and Ke are simplified for pedagogical clarity.)*

### NIM Compression: Read the Repricing Schedule

When policy rates fall, floating-rate loans and deposits need not reprice at the same speed. External-benchmark loans, MCLR-linked loans and fixed-rate loans have different reset terms; an MCLR loan does not necessarily reprice immediately. Fixed deposits often retain their contracted rate until renewal.

Near-term NIM can compress if asset yields fall before funding costs do. The size and timing depend on the lender's actual repricing buckets and funding mix. Do not carry an undated FY26 forecast forward as an October 2026 outcome. Compare dated disclosures and keep standalone, consolidated and average-balance definitions consistent.

## From RoA to DCF: Why Banks Are Valued Differently

The standard DCF uses Free Cash Flow to the Firm (FCFF). For banks, this framework breaks down: the "operations" of a bank are inseparable from its liabilities (deposits are simultaneously the raw material and the funding). Leverage is the business model, not a financing choice.

The correct framework is **Free Cash Flow to Equity (FCFE)**, which for a bank requires accounting for regulatory capital retention:

**FCFE = Net Income − (ΔAdvances × Risk Weight × Target CET1 Ratio)**
{: .notice--info}

Assume incremental advances of ₹100 crore, a 100% risk weight, a 13% target CET1 ratio **and net income of ₹100 crore**. Incremental required equity is ₹13 crore, leaving illustrative FCFE of ₹87 crore. Without the separate net income assumption, advance growth minus retained capital cannot determine distributable earnings. Actual capacity also depends on existing buffers, other risk-weighted assets and payout restrictions.

This is why rapidly growing banks with thin capital ratios often show strong profits but pay minimal dividends. The growth is consuming capital faster than it is being generated.

Indian capital requirements (Basel III):
- Minimum CET1: 5.5% + 2.5% Capital Conservation Buffer = 8.0%
- D-SIBs (SBI, HDFC Bank, ICICI Bank): additional surcharge of 0.2–0.8%
- In practice, top private banks target 16–18% CRAR for rating and confidence reasons

### The Dividend Discount Model: Bank Valuation Reduced to Two Numbers

In its simplest applicable form, bank valuation reduces to:

**Intrinsic P/B = (RoE − g) / (Ke − g)**
{: .notice--info}

Where:
- **RoE** = return on equity (end product of the NIM → CIR → credit cost chain)
- **Ke** = cost of equity (from CAPM: Rf + β × ERP; for Indian banks, typically 13–15%)
- **g** = sustainable long-run growth rate of book value

This formula encodes the entire value creation logic of banking:

- If RoE = Ke: the bank is worth exactly book value (P/B = 1×)
- If RoE > Ke: the bank trades above book — it is creating value
- If RoE < Ke: the bank trades below book — it is destroying value in real terms

As a **fictional** example, after-tax RoA=2.23% and average assets/equity=11× give RoE=24.53%. If 24.53% is separately assumed to be the **opening-equity** valuation return, Ke=13.8% and g=8% give P/B=(24.53−8)/(13.8−8)=**2.850×**. Do not automatically substitute a reported average-equity return into this opening-book model. This is not ICICI Bank’s verified FY25 RoE. The separate ICICI-named scenario in [Part 4](/blog/bank-nbfc-valuation-pbv-excess-returns/) uses an explicitly assumed 16.3% return; the two cases must not be presented as one issuer observation.

Many Indian PSU banks traded below 0.5× book in 2014–2018 for the opposite reason: gross NPA peaked at **14.6% of advances in March 2018**, representing ₹8.96 lakh crore in bad loans, pushing credit costs above 3%, destroying RoA, and driving RoE well below Ke. The Government of India injected ₹3.10 lakh crore in capital into PSU banks between FY17 and FY21 — through "recap bonds" — to restore solvency. But recapitalisation addressed the capital hole; it did not fix the structural CIR gap (PSU banks still run 12–15 percentage points above private banks on CIR) or the underlying credit culture that created the problem.

### The Full Value Chain

**NIM → CIR → Credit Cost → RoA → RoE → P/B multiple**
{: .notice--info}

A lower provision burden can raise returns, holding other inputs constant. An asset-based 100-basis-point reduction raises pre-tax RoA by one point; at 25% tax, after-tax RoA rises by 0.75 points. Its effect on RoE depends on average leverage, and its P/B effect depends on Ke and g. A modeled re-rating is not a guaranteed stock-price change.

## The Operating Leverage Asymmetry

Operating leverage in banking creates an asymmetric risk profile that the efficiency ratio alone does not capture.

**Upside:** When credit costs are low (economic expansion, provisioning from a prior cycle has run off), a bank with a fixed cost base sees most of its incremental NIM flow through to profit. HDFC Bank's 5-year PAT CAGR of 18–22% through 2015–2020 was driven partly by this: the fixed cost base was growing at ~15% while NIM was growing faster.

**Downside asymmetry:** When credit costs spike, the fixed cost base becomes an anchor. Bandhan Bank's experience illustrates this: NIM above 7% was structurally attractive, but when its microfinance book experienced severe post-COVID stress, credit costs in some quarters effectively consumed the entire NIM. CIR looked reasonable because the cost base was appropriate for a bank of its size — but the credit drain wiped out what the operating machine had generated.

### The NBFC Structural Position

NBFCs have no CASA deposit access. They borrow from banks, issue NCDs and commercial paper, and their blended cost of funds is typically 7–9% for investment-grade entities — versus a large bank's 4–5%. This structural funding cost disadvantage should translate into a lower CIR to compensate.

And it often does: Bajaj Finance runs at ~35% CIR; Muthoot Finance at ~22%. These lean operations are what allow high-NIM NBFCs to maintain competitive returns despite expensive liabilities.

But the structural advantage disappears in a funding stress. When wholesale credit markets froze after the IL&FS default in September 2018, NBFC cost of funds spiked by 100–200 basis points precisely when their loan books were most stressed. The operating efficiency that appeared in normal times provided no buffer against liquidity risk — because CIR, however low, says nothing about the structure of liabilities.

## Delayed Cash Flow: The Core Tension in Lending DCF

In a standard business, the accrual-to-cash timing gap is driven by working capital — receivables, payables, inventory — measured in weeks or months.

In a bank, the timing gap between accrued income and actual cash receipt can be **2–5 years** — because loan tenures are long, NPA classification takes 90 days after first default, provisioning builds up over multiple quarters, and resolution (through IBC or restructuring) can take 2–4 years beyond that.

The practical implication for DCF analysis: **a bank's reported profit is a lagged indicator of its actual cash generation.** A lender growing its loan book rapidly will appear highly profitable for several years, because the credit cost of new loans will not surface until those loans season (typically 12–24 months for retail, longer for infrastructure and real estate).

This is the fundamental reason why banks must be valued using through-cycle assumptions rather than current-year metrics. A bank reporting 0.4% credit cost in a benign year (as the Indian system is currently doing) is not a bank that has a 0.4% credit cost business model — it is a bank in a benign part of the cycle. The through-cycle credit cost for most retail banks is 0.6–1.2%, and for microfinance or unsecured consumer lenders, 2–4%.

The risk premium embedded in a bank's cost of equity (Ke) should reflect the uncertainty of credit cost being higher than current levels. A bank with high loan book growth, a young average loan tenure, and no tested credit cycle history should command a higher Ke than an established lender. India's lending history from 2014–2022 — encompassing the PSB NPA cycle, the NBFC liquidity crisis, the microfinance stress waves — provides multiple case studies of what happens when this premium is priced too low.

## What a Sustainable Model Needs

A sustainable model reconciles revenue, operating costs, credit provisions and tax on common asset denominators, then reconciles average equity returns to the opening-book convention used in the valuation. It also budgets the capital retained to support growth.

The fictional Alpha/Beta example shows why a low CIR alone cannot justify a particular P/B multiple. A range of NIM, cost and credit inputs without fees, tax, leverage, Ke and g does not establish a universal 15–24% RoE or a 2–4× valuation range. Use an explicit through-cycle scenario and a separate recovery path where current returns are temporarily weak.

## The Two Questions to Ask Before Any Bank Investment

Every bank analysis ultimately reduces to two questions:

**1. How efficiently does the machine run?** CIR — but read it carefully. Is low CIR from genuine efficiency or from scale? Is it being maintained by underinvesting in risk infrastructure? Is NIM compression changing the ratio even as costs are flat?

**2. How much of the machine's output actually arrives as cash?** Credit cost ratio, GNPA trend, Provision Coverage Ratio, and the age distribution of the loan book. Read PCR alongside collateral, write-offs, GNPA movements and the applicable requirements. A low ratio with worsening asset quality can signal further provision needs; a high ratio alone does not establish collectible cash.

A bank with excellent CIR but rising GNPA is running a clean engine on a leaking fuel line. A bank with mediocre CIR but pristine credit quality is leaving efficiency gains on the table — but its cash flows are real and its terminal value is not at risk.

**Read efficiency and credit quality together.** The kirana store owner who counts receivables as income looks profitable right up until the moment her customers stop paying. The lender whose CIR looks fine while credit costs are building looks well-run until required interest reversals and credit provisions reduce the reported return. The amounts and recognition dates depend on the actual loans and applicable rules.

The Efficiency Lab tool linked below makes this decomposition interactive across 15 Indian banks and NBFCs. Select any entity to see its NIM broken down into operating drain, credit drain, and surviving RoA — and whether its current RoE earns above or below its cost of equity.

*Tools referenced in this post:*
- *[Efficiency Lab](https://ganesh47.github.io/india-dcf-explorer/#/efficiency-lab) — NIM decomposition, CIR vs RoA scatter, two-number truth grid for 15 Indian lenders*
- *[WACC Lab](https://ganesh47.github.io/india-dcf-explorer/#/wacc-lab) — cost of equity and WACC across Indian sectors*
- *[DCF Builder](https://ganesh47.github.io/india-dcf-explorer/#/dcf-builder) — full DCF model for any NIFTY 100 company*

*Data sources: FY25 annual reports and Q4FY25 earnings presentations (HDFC Bank, ICICI Bank, SBI, Kotak Mahindra Bank, Axis Bank, IndusInd Bank, Bandhan Bank, IDFC First Bank, Bajaj Finance, Shriram Finance, Mahindra Finance, L&T Finance, Muthoot Finance, AU Small Finance Bank, Aavas Financiers). S&P/Business Standard for SBI CIR. RBI Master Circular on IRACP for provisioning norms. RBI DBIE for system-level NPA data. Crisil for RoA and credit cost forecasts. Damodaran (NYU Stern) for cost-of-equity benchmarks. All data for educational purposes — not investment advice.*


Revision references: [SBI FY2024–25 chairman’s message](https://sbi.bank.in/corporate/SBIAR2425/chairmans-message.html), “Operating Performance”; [Damodaran’s lender valuation framework](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf), equity cash-flow and stable-growth sections. Historical regulatory examples need their own dated rule and issuer evidence; this revision does not silently treat them as October forecasts.

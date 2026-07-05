---
title: "The Two-Number Truth: Operating Ratio, Credit Cost, and Why They Tell Opposite Sides of the Same DCF Story"
date: 2026-07-05 00:00:00 UTC
categories: [finance, investing]
tags: [dcf, banking, operating-ratio, credit-cost, indian-markets, valuation]
excerpt: "A lender's Cost-to-Income Ratio tells you how efficiently the machine runs. It says nothing about whether the machine's output actually arrives as cash. This post connects operating efficiency to DCF valuation through the lens of Indian banks and NBFCs — with worked examples and the specific data from cases where the ratio looked fine right before things went wrong."
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

Consider a sugarcane crusher. The Cost-to-Income Ratio (CIR) tells you how efficiently the machine runs — what fraction of every rupee of juice revenue goes to operating the press. A machine running at 40% CIR is efficient: 60 paise of every rupee of juice stays as profit before financing costs.

But CIR says nothing about one crucial variable: what percentage of the sugarcane entering the machine is actually fresh? A machine running at 40% efficiency but fed 20% spoiled sugarcane will yield less juice than a 55%-efficient machine fed entirely fresh stock. The machine's efficiency metric told you nothing about the input quality.

A lender's balance sheet works the same way. CIR measures how efficiently the machine runs. **Credit cost measures how much of the machine's output — interest income accrued — actually arrives as cash.** Ignore either number and you are reading half the story.

**The complete picture of a bank's profitability requires exactly two numbers:**

**RoA = NIM − Operating Cost Ratio − Credit Cost Ratio**
{: .notice--info}

Where:
- **NIM** = net interest margin (interest earned minus interest paid, as % of average assets)
- **Operating Cost Ratio** = operating expenses as % of average assets — what CIR captures
- **Credit Cost Ratio** = provisions for bad loans as % of average advances — what CIR ignores

CIR captures the first drain. Credit cost captures the second. A bank that optimises only on CIR is like a shopkeeper who counts receivables as income: her books look profitable for months, right up until the moment her customers stop paying.

---

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

Specific cited data for FY25:
- **HDFC Bank Q3FY25:** 40.6% (Q4FY24: ~38%)
- **ICICI Bank FY25:** ~39% (derived from ₹42,372 cr opex / ₹107,768 cr revenue)
- **SBI standalone FY25:** ~51.6% (cited from S&P/Business Standard)
- **SBI consolidated:** ~65–66% (inflated by SBI Life and SBI Mutual Fund subsidiaries)

The SBI standalone vs consolidated gap is a useful reminder: always use standalone CIR when comparing bank operating efficiency. Subsidiaries — insurance, mutual funds, wealth management — have entirely different cost structures and should not be blended in.

### Operating Leverage: Why Scale Is the Moat

A core banking platform built for five million customers costs almost the same to run for customer number five million and one. Compliance infrastructure, risk management teams, and leadership are largely fixed costs. This creates powerful operating leverage at scale.

A bank growing from ₹1 lakh crore to ₹2 lakh crore in advances does NOT double its operating cost — the cost base might grow 15–20% while NII doubles. This structural advantage compounds across decades. HDFC Bank's ability to run at 40% CIR while a small finance bank runs at 70% CIR does not mean HDFC manages every rupee better — it means HDFC's fixed cost base is amortised over a vastly larger franchise.

The practical implication: **low CIR can be the product of genuine efficiency or merely scale.** An analyst must distinguish the two. A small bank at 55% CIR growing at 25% per year will reach a lower CIR than a large bank at 42% growing at 8% — in five years, the denominator (NII) of the small bank will have grown enough to compress its CIR structurally. The valuation question is whether the credit quality of that rapid growth will hold.

---

## The Accrual Trap: Why CIR Looks Good Before the Crisis

The most important limitation of CIR is timing. Here is the mechanism, step by step.

### The 90-Day Clock

Under RBI's Income Recognition, Asset Classification and Provisioning (IRACP) norms, interest income on performing (standard) assets is recognised on an accrual basis — the bank books the income when it is *due*, not when it is *received*.

Consider a ₹100 crore loan at 10% per annum (₹2.5 crore interest per quarter):

| Quarter | Event | Accrued income | Cash received |
|---------|-------|---------------|---------------|
| Q1 | Borrower current | ₹2.5 cr booked | ₹2.5 cr received ✓ |
| Q2 | Borrower misses payment (30 DPD) | ₹2.5 cr booked | ₹0 received ✗ |
| Q3 | 60–89 days past due | ₹2.5 cr booked | ₹0 received ✗ |
| Q4 | Crosses 90 days → classified NPA | Income *reversed*: −₹5 cr | ₹0 received ✗ |
| Q4 | Provision: 15% of ₹100 cr | −₹15 cr charge | |

**Net P&L swing at NPA classification:** −₹5 cr (income reversal) + −₹15 cr (provision) = **−₹20 crore in a single quarter** — from a loan that had been showing as ₹2.5 crore income per quarter for three quarters before that.

CIR was fine throughout. The operating expenses didn't change. The accrued (but uncollected) interest was *inflating* the denominator of CIR, making the efficiency ratio look *better* than reality in the three quarters before the NPA classification. The efficiency metric was lying — not because anyone was dishonest, but because accrual accounting is structurally blind to collection risk.

### RBI's Provisioning Ladder

Once classified as NPA, the minimum provisioning requirements escalate over time:

| Category | Trigger | Minimum provisioning |
|----------|---------|---------------------|
| Sub-standard | 90+ days overdue, up to 12 months as NPA | 15% (secured); 25% (unsecured) |
| Doubtful ≤ 1 year | NPA for 12–24 months | 25% secured + 100% unsecured |
| Doubtful 1–3 years | NPA for 24–36 months | 40% secured + 100% unsecured |
| Doubtful > 3 years | NPA > 36 months | 100% |
| Loss | Identified by auditor or RBI inspection | 100% |

*Source: RBI Master Circular on IRACP norms.*

The RBI has indicated that a Provision Coverage Ratio (PCR = total provisions / gross NPA) of 70% is desirable — a PCR below this signals that under-provisioning risk remains.

### Yes Bank: The Canonical Indian Case

Yes Bank's collapse is the cleanest documented case of CIR-as-illusion in Indian banking. The cited data:

- **FY18:** RoA 1.78% — comparable to private sector peers. Gross NPA: ₹2,627 crore (1.52% of advances). On these numbers, Yes Bank looked like a well-run mid-size private bank.
- **The hidden stress:** RBI's Asset Quality Review (AQR) found a GNPA divergence of approximately ₹6,355 crore — Yes Bank was under-reporting its bad loans by this amount. Loans to IL&FS, DHFL, Jet Airways, Café Coffee Day, and Essel Group had been kept standard when they should have been classified as stressed.
- **FY19 cliff:** RoA crashed to 0.52%. New CEO Ravneet Gill could not raise capital against worsening asset quality. GNPA doubled to ₹17,134 crore by September 2019.
- **The provisioning gap:** Provision Coverage Ratio in FY19 was **43.1%** — the lowest among comparable banks, and far below the RBI's desirable 70%. For every ₹100 of bad loans on the books, only ₹43 of provisions had been set aside. The remaining ₹57 would hit future quarters.
- **FY20:** Net loss of ₹16,433 crore. RBI moratorium in March 2020.

What was Yes Bank's CIR doing during FY17–FY18? The available evidence is that the ratio appeared reasonable — the accrued interest from stressed borrowers was inflating NII (the denominator), making operating costs look proportionally small. The signal was not in the efficiency ratio. It was in the divergence between PCR and GNPA, the concentration of loans to stressed sectors, and the operating cash flow vs stated profit gap.

**The cash-adjusted CIR** captures what the standard ratio hides:

**Adjusted CIR = (Operating Expenses + Credit Costs) / Operating Income**
{: .notice--info}

This adds provisions back into the numerator. It answers: "If the bank had recognised credit losses in the same period as the income, what would efficiency look like?" A bank with 42% standard CIR and 2% credit cost added to the numerator will show a very different adjusted ratio than one with 42% CIR and 0.4% credit cost.

---

## The RoA Decomposition: Three Levers, One Number

Return on Assets is the cleanest single-number summary of a bank's business model:

**RoA = NIM + Non-Interest Income − Operating Cost Ratio − Credit Cost Ratio − Tax Effect**
{: .notice--info}

All terms expressed as a percentage of average total assets.

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
| Operating Expenses (CIR = 42%) | 1.76% | 1.76% |
| Pre-Provision Operating Profit | 2.44% | 2.44% |
| **Credit Cost Ratio** | **0.50%** | **1.50%** |
| Pre-Tax RoA | 1.94% | 0.94% |
| Tax (25%) | 0.49% | 0.24% |
| **RoA** | **1.45%** | **0.71%** |
| Equity multiplier (12×) | 12× | 12× |
| **RoE** | **17.4%** | **8.5%** |
| Cost of Equity (Ke) | 12% | 12% |
| Sustainable growth (g) | 7% | 4% |
| **Justified P/B = (RoE − g)/(Ke − g)** | **(17.4 − 7)/(12 − 7) = 2.08×** | **(8.5 − 4)/(12 − 4) = 0.56×** |

Identical CIR. Identical NIM. A one percentage point difference in credit cost ratio produces a **3.7× difference in justified P/B multiple** — Bank Alpha is a 2× book value compounder; Bank Beta is trading at half book, destroying shareholder value with every passing year.

*(Illustrative example; leverage, g, and Ke are simplified for pedagogical clarity.)*

### NIM Compression: The 2025–2026 Context

RBI cut the repo rate by a cumulative 125 basis points in the 2025 easing cycle. NIM is being compressed across the system:

- When rates fall, floating-rate loans (MCLR-linked, home loans) reprice immediately
- Fixed deposits reprice only when they mature — a 6–24 month lag
- Near-term effect: lending yields fall faster than deposit costs → NIM compresses

System-level NIM fell ~20 basis points in FY25 vs FY24. HDFC Bank's NIM has already compressed from 4.3% in FY23 to 3.6% in FY24 due to the merger with HDFC Ltd (the parent had a higher cost of funds).

System RoA trajectory:
- **FY25:** ~1.3% (above the 20-year average of 0.8%)
- **FY26 forecast:** ~1.1–1.2% (NIM headwind, normalisation of treasury gains)
- System credit cost FY25: **~0.4%** — a decade low, driven by clean post-pandemic books
- Credit cost FY26 forecast: remains below 0.5% unless MFI/unsecured stress broadens

This creates an important current-year context: the system is in a rare period where both CIR (scale + digital efficiency) and credit cost (clean books after a decade of NPA resolution) are favourable simultaneously. The next cycle will test which banks have genuinely durable advantages vs which benefited from benign credit conditions.

---

## From RoA to DCF: Why Banks Are Valued Differently

The standard DCF uses Free Cash Flow to the Firm (FCFF). For banks, this framework breaks down: the "operations" of a bank are inseparable from its liabilities (deposits are simultaneously the raw material and the funding). Leverage is the business model, not a financing choice.

The correct framework is **Free Cash Flow to Equity (FCFE)**, which for a bank requires accounting for regulatory capital retention:

**FCFE = Net Income − (ΔAdvances × Risk Weight × Target CET1 Ratio)**
{: .notice--info}

If a bank grows its advances by ₹100 crore, with average 100% risk weight and a target Common Equity Tier 1 ratio of 13%, it must retain ₹13 crore of the current year's earnings as capital. The remaining ₹87 crore is freely distributable as dividend or buyback.

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

ICICI Bank's RoA of 2.23% in FY25, at ~11× leverage, produces RoE of ~24.5%. Against a Ke of ~13.8%, with g = 8%, the justified P/B = (24.5 − 8) / (13.8 − 8) = 2.84×. The market valuation around 3.5× book reflects the market pricing in a sustained above-WACC spread.

Many Indian PSU banks traded below 0.5× book in 2014–2018 for the opposite reason: gross NPA peaked at **14.6% of advances in March 2018**, representing ₹8.96 lakh crore in bad loans, pushing credit costs above 3%, destroying RoA, and driving RoE well below Ke. The Government of India injected ₹3.10 lakh crore in capital into PSU banks between FY17 and FY21 — through "recap bonds" — to restore solvency. But recapitalisation addressed the capital hole; it did not fix the structural CIR gap (PSU banks still run 12–15 percentage points above private banks on CIR) or the underlying credit culture that created the problem.

### The Full Value Chain

**NIM → CIR → Credit Cost → RoA → RoE → P/B multiple**
{: .notice--info}

A bank that improves its credit cost ratio by 100 basis points — through better underwriting, early warning systems, or a shift toward lower-risk segments — can lift RoA from 1.2% to 2.2%, RoE from ~14% to ~26%, and justify a P/B re-rating from ~1× to ~3×. That is a 3× stock price change from a single operational improvement, achieved without touching the CIR at all. This is why credit quality is more value-accretive than pure efficiency gains for most Indian banks.

---

## The Operating Leverage Asymmetry

Operating leverage in banking creates an asymmetric risk profile that the efficiency ratio alone does not capture.

**Upside:** When credit costs are low (economic expansion, provisioning from a prior cycle has run off), a bank with a fixed cost base sees most of its incremental NIM flow through to profit. HDFC Bank's 5-year PAT CAGR of 18–22% through 2015–2020 was driven partly by this: the fixed cost base was growing at ~15% while NIM was growing faster.

**Downside asymmetry:** When credit costs spike, the fixed cost base becomes an anchor. Bandhan Bank's experience illustrates this: NIM above 7% was structurally attractive, but when its microfinance book experienced severe post-COVID stress, credit costs in some quarters effectively consumed the entire NIM. CIR looked reasonable because the cost base was appropriate for a bank of its size — but the credit drain wiped out what the operating machine had generated.

### The NBFC Structural Position

NBFCs have no CASA deposit access. They borrow from banks, issue NCDs and commercial paper, and their blended cost of funds is typically 7–9% for investment-grade entities — versus a large bank's 4–5%. This structural funding cost disadvantage should translate into a lower CIR to compensate.

And it often does: Bajaj Finance runs at ~35% CIR; Muthoot Finance at ~22%. These lean operations are what allow high-NIM NBFCs to maintain competitive returns despite expensive liabilities.

But the structural advantage disappears in a funding stress. When wholesale credit markets froze after the IL&FS default in September 2018, NBFC cost of funds spiked by 100–200 basis points precisely when their loan books were most stressed. The operating efficiency that appeared in normal times provided no buffer against liquidity risk — because CIR, however low, says nothing about the structure of liabilities.

---

## Delayed Cash Flow: The Core Tension in Lending DCF

In a standard business, the accrual-to-cash timing gap is driven by working capital — receivables, payables, inventory — measured in weeks or months.

In a bank, the timing gap between accrued income and actual cash receipt can be **2–5 years** — because loan tenures are long, NPA classification takes 90 days after first default, provisioning builds up over multiple quarters, and resolution (through IBC or restructuring) can take 2–4 years beyond that.

The practical implication for DCF analysis: **a bank's reported profit is a lagged indicator of its actual cash generation.** A lender growing its loan book rapidly will appear highly profitable for several years, because the credit cost of new loans will not surface until those loans season (typically 12–24 months for retail, longer for infrastructure and real estate).

This is the fundamental reason why banks must be valued using through-cycle assumptions rather than current-year metrics. A bank reporting 0.4% credit cost in a benign year (as the Indian system is currently doing) is not a bank that has a 0.4% credit cost business model — it is a bank in a benign part of the cycle. The through-cycle credit cost for most retail banks is 0.6–1.2%, and for microfinance or unsecured consumer lenders, 2–4%.

The risk premium embedded in a bank's cost of equity (Ke) should reflect the uncertainty of credit cost being higher than current levels. A bank with high loan book growth, a young average loan tenure, and no tested credit cycle history should command a higher Ke than an established lender. India's lending history from 2014–2022 — encompassing the PSB NPA cycle, the NBFC liquidity crisis, the microfinance stress waves — provides multiple case studies of what happens when this premium is priced too low.

---

## What Good Looks Like: The Private Bank Equilibrium

The sustainable RoA for a well-run Indian private bank converges on **1.5–2.5%**, driven by:

- NIM of 3.5–5.0% (higher for consumer or MSME-focused lenders; lower for wholesale)
- Operating cost ratio of 1.5–2.5% (CIR of 40–50% depending on NIM level)
- Credit cost ratio of 0.4–0.8% in normal conditions (GNPA < 2%, PCR > 70%)

At 10–12× leverage, this produces **RoE of 15–24%** against a Ke of 13–15% — the spread that justifies P/B multiples of 2–4×.

Lenders that structurally cannot reach this equilibrium — because their cost base is too high (building franchise) or their credit culture produces persistent credit costs above 2% — will trade below book value until one of those inputs changes. The PSU sector has demonstrated how long that can take: GNPA peaked at 14.6% in March 2018; by FY24, system-level credit costs had normalised and PSU bank profits had recovered to ₹1.41 lakh crore — but the CIR gap vs private banks remains, and so does the P/B discount.

---

## The Two Questions to Ask Before Any Bank Investment

Every bank analysis ultimately reduces to two questions:

**1. How efficiently does the machine run?** CIR — but read it carefully. Is low CIR from genuine efficiency or from scale? Is it being maintained by underinvesting in risk infrastructure? Is NIM compression changing the ratio even as costs are flat?

**2. How much of the machine's output actually arrives as cash?** Credit cost ratio, GNPA trend, Provision Coverage Ratio, and the age distribution of the loan book. A high PCR (above 70%) with declining GNPA is a forward-looking positive signal. A low PCR with rising GNPA is a signal of future provisions yet to hit the P&L.

A bank with excellent CIR but rising GNPA is running a clean engine on a leaking fuel line. A bank with mediocre CIR but pristine credit quality is leaving efficiency gains on the table — but its cash flows are real and its terminal value is not at risk.

**Both ratios together, not either alone, tell the truth.** The kirana store owner who counts receivables as income looks profitable right up until the moment her customers stop paying. The lender whose CIR looks fine while credit costs are building looks well-run right up until the quarter when 90 days of accrued income reverses and provisions hit simultaneously.

The Efficiency Lab tool linked below makes this decomposition interactive across 15 Indian banks and NBFCs. Select any entity to see its NIM broken down into operating drain, credit drain, and surviving RoA — and whether its current RoE earns above or below its cost of equity.

---

*Tools referenced in this post:*
- *[Efficiency Lab](https://ganesh47.github.io/india-dcf-explorer/#/efficiency-lab) — NIM decomposition, CIR vs RoA scatter, two-number truth grid for 15 Indian lenders*
- *[WACC Lab](https://ganesh47.github.io/india-dcf-explorer/#/wacc-lab) — cost of equity and WACC across Indian sectors*
- *[DCF Builder](https://ganesh47.github.io/india-dcf-explorer/#/dcf-builder) — full DCF model for any NIFTY 100 company*

*Data sources: FY25 annual reports and Q4FY25 earnings presentations (HDFC Bank, ICICI Bank, SBI, Kotak Mahindra Bank, Axis Bank, IndusInd Bank, Bandhan Bank, IDFC First Bank, Bajaj Finance, Shriram Finance, Mahindra Finance, L&T Finance, Muthoot Finance, AU Small Finance Bank, Aavas Financiers). S&P/Business Standard for SBI CIR. RBI Master Circular on IRACP for provisioning norms. RBI DBIE for system-level NPA data. Crisil for RoA and credit cost forecasts. Damodaran (NYU Stern) for cost-of-equity benchmarks. All data for educational purposes — not investment advice.*

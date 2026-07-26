---
title: "What Is a Bank Worth? P/BV, Excess Returns, and Why DCF Fails for Financials"
date: 2026-07-26 12:00:00 UTC
categories: [blog]
author: Ganesh Raman
tags: [Finance, Banking, NBFC, Valuation, P/BV, Excess-Returns, DCF, India, Investing, HDFC-Bank, ICICI-Bank, IndusInd, Bajaj-Finance]
toc: true
toc_sticky: true
author_profile: true
classes: wide
excerpt: "Standard DCF breaks for banks: you can't separate 'financing' from 'operations' because deposits are the raw material, not just funding. The right framework uses Price-to-Book vs RoE and the Excess Returns Model — and when you apply them to India's banking sector, the data tells a precise story about which franchises the market trusts and why."
header:
  overlay_color: "#1e3a5f"
  overlay_filter: 0.65
permalink: /blog/bank-nbfc-valuation-pbv-excess-returns/
---

*Series map: [Part 1](/blog/discounted-cash-flows-the-math-part-1/) \| [Part 2](/blog/discounted-cash-flows-india-lending-and-growth-part-2/) \| [Part 3](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/) \| [Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) \| **Part 4 (this post)***

*Related: [Bank & NBFC Valuation Lab](https://ganesh47.github.io/india-dcf-explorer/#/valuation-lab) — interactive P/BV vs RoE scatter with live Gordon fair-value line, adjustable Ke/g sliders, and excess returns decomposition for 13 Indian banks and NBFCs.*

---

## Why DCF Breaks for Banks

The standard Discounted Cash Flow model — take free cash flow to the firm, subtract debt service, discount at WACC, add terminal value — hits a fundamental problem with banks. The problem is definitional: what is a bank's "debt"?

In a manufacturing company, debt is financing. It sits on the right side of the balance sheet alongside equity and is distinct from the business's operating activities. The free cash flow to the firm is the pre-debt cash flow; you discount it and subtract the market value of debt to get equity value.

A bank's deposits are not financing in this sense. They are the raw material. A bank takes in deposits (typically 4–7% cost), uses them to make loans (10–18% yield), and earns the spread. If you tried to apply the standard DCF logic — separate "financing cash flows" from "operating cash flows" — you would have to treat all deposit inflows and outflows as financing. That's the entire business. The FCFF would be meaningless.

Damodaran states the problem directly in his 2009 paper on valuing financial service firms: "Debt is more like raw material itself" for banks. The interest paid on deposits is an operating cost, not a financing cost — conceptually similar to cost of goods sold for a retailer.

Three additional complications make FCFF worse:

**Regulatory capital constraints.** A bank's minimum capital is set by regulation. Under Basel III / RBI guidelines, banks must maintain a minimum Capital Adequacy Ratio of 11.5% (including capital conservation buffer). Banks cannot simply retain all profits and compound equity freely — they must maintain the regulatory buffer as they grow. "Free cash flow" from a bank's perspective is always constrained by the equity needed to support loan book growth at the mandated capital ratio.

**Leverage is intrinsic, not a choice.** A manufacturing company chooses its D/E ratio. A bank's leverage is driven by its loan book growth, deposit inflows, and regulatory capital — all three interact. You cannot "unlever" a bank to isolate the unlevered firm value.

**Working capital is the business itself.** The standard DCF adjustment — subtract increase in working capital — becomes nonsense when 90%+ of a bank's balance sheet consists of loans (current in the accounting sense) and deposits repayable on demand.

The right valuation models for banks use equity directly. Two models dominate: the **Dividend Discount Model (DDM)** and the **Excess Returns Model**. They are mathematically equivalent under the same assumptions. The Excess Returns Model is more useful because it shows *why* a franchise deserves a premium above book.

---

## The P/BV Framework

For a bank, book value (equity = assets − liabilities) represents the accounting cushion between loans outstanding and amounts owed to depositors. A bank at 1× book means the market values its equity at exactly what the accountants say. A bank at 3× book means the market believes the franchise can generate returns significantly above the cost of equity — persistently.

The Gordon Growth Model gives us the fair P/BV ratio:

```
Fair P/BV = (RoE − g) / (Ke − g)
```

where:
- **RoE** = Return on Equity
- **g** = sustainable long-run growth rate (nominal)
- **Ke** = Cost of Equity = Rf + β × ERP

For India in mid-2026:
- Rf = 6.7% (10-year G-Sec yield)
- ERP = 7.0% (India equity risk premium; IncWert / Damodaran-methodology estimate, April 2025)
- Ke = 6.7% + β × 7.0%

A bank with RoE = Ke earns exactly its cost of capital. The Gordon formula gives P/BV = 1× — the franchise is worth exactly book, no more. A bank with RoE > Ke earns excess returns; the market pays above book. A bank with RoE < Ke destroys value and should trade below book.

The formula immediately clarifies something that confuses many investors: **a bank can have growing earnings and still deserve a below-book valuation.** If RoE < Ke, every rupee of retained earnings creates less than a rupee of value. Growth destroys value when returns earned are below the cost of capital.

---

## The Excess Returns Model

The Excess Returns approach says a franchise is worth its current book value plus the present value of all future economic profits above the cost of equity:

```
Value of Equity = Book Value of Equity + PV(Excess Returns)

Excess Return in year t = (RoE_t − Ke) × BV_t
```

If RoE = Ke every year, PV(excess returns) = 0 and equity = book. The more above Ke the bank earns — and the longer it sustains that edge — the more it's worth above book.

Under the simplifying assumption that excess returns are earned at RoE for `n` years and then decay to Ke (no more franchise edge), the Gordon Growth formula emerges as the closed-form solution. The two models are the same.

**Worked example — HDFC Bank FY25:**

| Item | Value |
|---|---|
| Book equity | ~₹3.5 lakh crore |
| RoE (FY25) | 14.4% |
| Ke (β = 0.90) | 6.7 + 0.90 × 7.0 = **13.0%** |
| Excess return spread | 14.4% − 13.0% = **+1.4%** |
| Annual value creation | 1.4% × ₹3.5L cr = **₹4,900 crore/yr** |
| Gordon implied P/BV (g = 9%) | (14.4 − 9) / (13.0 − 9) = **1.35×** |
| Actual P/BV (Mar 2025) | **2.85×** |
| Premium to implied | **+111%** |

The 111% premium is the market's franchise quality premium. At a raw Ke of 13%, the Gordon model gives 1.35×. But HDFC Bank's 30-year track record, GNPA of 1.33%, credit cost of 0.42%, and the demonstrated ability to earn above the cost of capital through multiple credit cycles tells the market: this franchise's *effective* Ke is closer to 10.5%. At Ke = 10.5%, the model gives 2.85× — exactly matching the market price. The franchise quality premium is a discount to the effective cost of capital, not a deviation from rational pricing.

Note: HDFC Bank's current RoE of 14.4% is below its pre-merger average of 16–17%. The HDFC Ltd merger (April 2023) absorbed a large low-yield mortgage book, compressing NIM from 4.3% (FY23) to 3.46% (FY25). The market is paying 2.85× book on the expectation that NIM normalises to 3.6–3.8% as legacy HDFC Ltd bonds roll off, driving RoE back toward 16%+.

---

## The Indian Banking P/BV Landscape

Here is the FY25 snapshot for 13 Indian banks and NBFCs, using Ke from CAPM (Rf 6.7%, ERP 7.0%) and entity-specific betas:

| Entity | RoE | β | Ke | g | **Implied P/BV** | **Actual P/BV** | Premium |
|---|---|---|---|---|---|---|---|
| **Bajaj Finance** | 19.1% | 0.95 | 13.4% | 10.0% | 2.72× | 6.11× | +125% |
| **AU Small Finance** | 12.0% | 1.05 | 14.1% | 8.0% | 0.66× | 2.84× | +330% |
| **Muthoot Finance** | 18.2% | 0.90 | 13.0% | 9.0% | 2.30× | 2.90× | +26% |
| **Kotak Mahindra** | 13.1% | 0.80 | 12.3% | 8.0% | 1.19× | 2.56× | +115% |
| **ICICI Bank** | 16.3% | 1.00 | 13.7% | 9.0% | 1.55× | 2.66× | +72% |
| **Shriram Finance** | 16.7% | 1.00 | 13.7% | 8.0% | 1.53× | 2.87× | +88% |
| **HDFC Bank** | 14.4% | 0.90 | 13.0% | 9.0% | 1.35× | 2.85× | +111% |
| **Axis Bank** | 15.1% | 1.00 | 13.7% | 8.0% | 1.25× | 2.02× | +62% |
| **SBI** | 14.0%* | 1.15 | 14.75% | 6.0% | 0.91× | 1.50× | +65% |
| **Bandhan Bank** | 11.6% | 1.30 | 15.8% | 7.0% | 0.52× | 0.97× | +87% |
| **Yes Bank** | 5.1% | 1.50 | 17.2% | 5.0% | ~0.01× | 1.33× | Recovery |
| **IndusInd Bank** | 4.0% | 1.40 | 16.5% | 6.0% | −0.19× | 1.03× | Recovery |
| **IDFC First Bank** | 3.9% | 1.25 | 15.5% | 8.0% | −0.55× | 0.85× | Recovery |

*SBI's reported FY25 RoE is 19.87% but this is leverage-inflated (equity base thin, RoA is 1.10%). Normalised RoE = RoA × leverage ≈ 14%. Using 14% gives a more meaningful P/BV comparison.*

### The Four Archetypes

**1. Franchise quality premium (Bajaj Finance, AU SFB, Kotak, HDFC)**

These trade at large multiples above their Gordon-model implied P/BV. AU Small Finance Bank at 2.84× with implied 0.66× (330% premium) is the most extreme — entirely a growth franchise bet. The current RoE of 12% (below Ke of 14.1%) means the basic model says the bank creates no value at current returns, yet the market pays almost 3× book. The bet: CIR will fall from 63% to ~50% as the deposit franchise matures, driving RoE to 18–20%. If that happens, 2.84× will look cheap retroactively.

Bajaj Finance at 6.11× (125% above implied 2.72×) encodes the market's belief that 19%+ RoE will persist for 15+ years on a growing asset base. No other Indian financial has delivered this duration of consistent above-Ke returns.

Interestingly, Muthoot Finance (RoE 18.2%, highest sustained RoE in our universe except Bajaj) trades at only a 26% premium to its Gordon implied value. Gold lending is a single-product concentration — the market applies a higher effective risk premium to regulatory and concentration risk, even with exemplary current returns.

**2. Moderate premiums with demonstrated earnings (ICICI, Shriram, HDFC, Axis)**

These trade at 60–90% above their Gordon-implied P/BV. The premiums are defensible and declining as the market re-prices each against its track record. ICICI Bank's 72% premium reflects the demonstrated transformation from a corporate-heavy NPA machine (GNPA 9.97% in FY18) to best-in-class retail underwriting (GNPA 1.67% in FY25, PCR 76%). Shriram Finance at 88% premium reflects its unique retail deposit franchise (26% of borrowings in retail public deposits — no CP issuance) that differentiates it structurally from the IL&FS and DHFL model.

Axis Bank's smaller premium (62%) vs ICICI at comparable RoE reflects a shorter proven track record post-transformation and the ongoing Citi India integration costs.

**3. Recovery thesis (IndusInd, Yes Bank, IDFC First)**

When RoE < g, the Gordon model gives a negative or zero implied P/BV. Yet these banks trade at real, positive prices — because they are not valued on current returns. They are valued on normalised future returns.

IndusInd at 1.03× book with RoE 4.0% is a bet on recovery to ~14% RoE. Yes Bank at 1.33× with RoE 5.1% is a bet on NIM rebuilding past 4% and CIR falling below 60%. IDFC First at 0.85× (below book) with RoE 3.9% reflects the market pricing the trajectory, not current destruction.

What RoE does IndusInd's 1.03× P/BV imply? Rearranging the formula:
```
1.03 = (RoE − 6) / (16.5 − 6)
RoE − 6 = 1.03 × 10.5 = 10.82
RoE implied = ~16.8%
```

So the market at 1.03× is pricing recovery all the way to pre-stress RoE (~16–17%). Any shortfall in that recovery would push the price below 1× book. The 1.03× is an optimistic recovery bet, not a depressed valuation.

**4. PSU and MFI-concentration discounts (SBI, Bandhan)**

SBI at 1.50× and Bandhan at 0.97× both reflect structural or cyclical risk discounts:

SBI's 65% premium to its Gordon implied (0.91×) looks large until you realise the implied P/BV of 0.91× already prices in the PSU drag — a normalised RoE of 14% vs Ke of 14.75%, giving almost no excess return. SBI's market price is partly a scale premium (largest bank in India, government backing) and partly the market pricing the ongoing NPA recovery (GNPA fell from 14.6% in FY18 to 1.82% in FY25 — a 12-percentage-point improvement).

Bandhan at 0.97× below book: the Gordon model (at 11.6% RoE, Ke 15.8%) gives an implied of only 0.52×. The 0.97× market price is actually a 87% premium above even that depressed model value — the market is pricing recovery of credit cost from 4% toward 2%, which would lift RoE to 14–16%.

---

## Why the PSU P/BV Discount Is Structural

SBI trades at 1.50×. HDFC Bank trades at 2.85×. The gap is not explained by current metrics alone — SBI's credit cost (0.42%) is now comparable to HDFC's. The structural PSU discount has three permanent components:

**Priority Sector Lending (PSL).** Banks must lend 40% of Adjusted Net Bank Credit to priority sectors — agriculture (18%), small farmers (8%), micro enterprises (7.5%), weaker sections (12%). These carry regulated rates, often 150–200 bps below MCLR. For SBI with its massive ANBC base, this is a structural 30–50 bps drag on NIM vs a private bank that can optimise its book composition.

**CRR + SLR cost.** As of mid-2026, the Cash Reserve Ratio is 3.0% of NDTL (earning zero; RBI cut it from 4.5% in phases through November 2025) and the Statutory Liquidity Ratio is 18% of NDTL (earning G-sec yields of ~6.5–7%). The CRR dead-weight and SLR low-yield effect create ~80–100 bps structural floor cost that cannot be eliminated. On SBI's ₹70+ lakh crore deposit base, the CRR alone locks up ₹2.1 lakh crore at 0% return.

**Employee cost and governance.** SBI's 2.3 lakh employees, defined-benefit pension commitments, and 22,000 branches create a fixed cost structure that cannot be restructured quickly. The CIR gap (SBI 55% vs HDFC 40%) is 15 percentage points — on India's largest bank balance sheet, that's enormous persistent drag on RoE.

The P/BV discount is the market pricing these as permanent structural features. The SBI trade is: do you believe the credit cycle stays benign AND the government allows capital efficiency improvements? If yes, 1.5× book is cheap. If the credit cycle turns and structural drag compounds, 1.5× may not be.

---

## The IndusInd Case: Valuing Recovery

IndusInd Bank is the clearest example of why you must use *normalised* RoE, not *current-year* RoE, when valuing stressed banks.

FY25 facts:
- Q4FY25 net loss: ₹2,329 crore (largest quarterly loss in the bank's history)
- Full-year FY25 RoE: 4.0% (collapsed from 14.2% in FY24)
- GNPA: 3.13% (+88 bps QoQ in Q4FY25)
- NIM: 3.93% (falling from 4.26% in early FY25)
- Derivatives mis-marking disclosed: PwC forensic audit found ₹1,979 crore of incorrectly recorded derivative gains, plus ₹674 crore MFI income mis-recording and ₹595 crore in questionable "other assets" — total overstatement of ~₹3,248 crore
- P/BV (March 2025): 1.03×

At 4.0% RoE and Ke of 16.5%, the Gordon formula gives a *negative* implied P/BV. The franchise is destroying value at current returns. Yet the market paid 1.03× book — almost exactly book value.

The Gordon formula rearranged tells us what RoE the market is pricing at 1.03×:
```
1.03 = (RoE − 6) / (16.5 − 6)
RoE implied ≈ 16.8%
```

The market is pricing recovery almost all the way back to FY24 levels (14.2% RoE). The recovery evidence by Q1FY27 supports this: net profit ₹1,037 crore, CRAR 17.15%, new CEO Rajiv Anand (ex-Axis Bank Deputy MD, appointed August 2025). But the implied 16.8% RoE recovery embedded in the 1.03× price is ambitious — at 14% recovered RoE (Ke 16.5%, g 6%), the Gordon implied is only (14−6)/(16.5−6) = 0.76×. The market at 1.03× is paying a 35% premium even to the recovery case fair value.

This is not irrational — it's pricing execution risk + governance repair + franchise option value. But it illustrates the precision with which the P/BV framework reveals what the market is betting on.

---

## Bajaj Finance: The Duration of Excess Returns

The opposite extreme: Bajaj Finance at 6.11× book with RoE 19.1%.

Gordon implied P/BV at g = 10% and Ke = 13.4%: **(19.1 − 10) / (13.4 − 10) = 9.1 / 3.4 = 2.72×**. The actual P/BV of 6.11× represents a 125% premium above the already-elevated implied value.

The 125% premium encodes three specific market beliefs:
1. **Duration**: the market expects Bajaj to earn 19%+ RoE not for 5 years but for 15–20 years. The Gordon formula assumes a single-period estimate; Bajaj's AUM growth (₹4.16 lakh crore, +26% YoY in FY25) and 100M+ customer base suggest the moat has not peaked.
2. **Platform scalability**: 300+ product categories, proprietary credit bureau scoring, 60M+ active EMI relationships — the marginal cost of adding a new product is near zero. This is a technology-infrastructure story inside a lending business.
3. **Credit discipline through cycles**: GNPA 0.96%, credit cost 1.80%, CIR 33% — delivered consistently through demonetisation (2016), COVID (2020–21), and the NBFC stress (2018–19). Each cycle validated the underwriting model.

The risk embedded in the premium: Bajaj's wholesale CP funding (17% of borrowings). In an IL&FS-style market freeze, CoF would spike 100–150 bps while the consumer book reprices slowly. The NIM 11% provides a buffer — a 150 bps CoF shock is survivable. But a simultaneous credit event (as happened in COVID) would compress NIM and expand credit costs at the same time. That tail scenario is why the market does not price Bajaj at 10× book even with 19%+ RoE.

---

## Yes Bank: From 4× to 0.03× to 1.33×

**Timeline:** Yes Bank peaked at ~4× P/BV in August 2018 (stock price ₹404). The bank's NPA situation was misrepresented — GNPA reported at ~3% while the actual level was closer to 14–17%. Provisioning in Q3FY20 alone was ₹24,765 crore (vs ₹550 crore a year prior — a 45× surge).

RBI imposed a moratorium in March 2020. The stock fell to ₹5.55. AT1 bonds were written off: **₹8,415 crore** — a total loss for AT1 holders, later confirmed by the Supreme Court (AT1s rank below deposits in the capital stack and can be written down by the regulator in a reconstruction). The SBI-led consortium infused ₹10,000 crore equity; authorised capital was raised from ₹1,100 crore to ₹6,200 crore — massive dilution.

FY25 recovery: GNPA 1.60%, NIM 2.70% (thin but rebuilding), RoE 5.1%, P/BV 1.33×.

What does 1.33× imply? At Ke 17.2%, g 5%:
```
1.33 = (RoE − 5) / (17.2 − 5)
RoE − 5 = 1.33 × 12.2 = 16.2
RoE implied ≈ 21.2%
```

The market is pricing Yes Bank recovering to 21% RoE — which would require NIM to rebuild past 5% (from current 2.7%) and CIR to fall from 74% to under 50%. That is highly ambitious. The 1.33× P/BV looks like option value pricing, not a rational fundamental case. The P/BV 1.33× survives because the floor is the reconstruction scheme backstop (SBI + consortium), not any genuine franchise recovery.

The IL&FS / DHFL comparison: both resolved at 43–50 paise per rupee for *senior secured creditors*. For Yes Bank AT1 holders, recovery was 0 paise. For Yes Bank equity holders at the 2020 trough price (₹5.55), recovery has been partial but real — the stock now trades at ₹21 (3.8× from the trough). That is the risk-reward of buying genuinely distressed bank equity: catastrophic downside (0 paise) vs. lotto-ticket upside if reconstruction succeeds.

---

## The RoE Decomposition

Every bank valuation ultimately traces back to three numbers in the P&L:

```
RoA ≈ NIM − Credit Cost − (CIR × NIM)
RoE ≈ RoA × Leverage (Assets/Equity)
Fair P/BV ≈ (RoE − g) / (Ke − g)
```

| Entity | NIM | Credit Cost | CIR | RoA | Leverage | **RoE** |
|---|---|---|---|---|---|---|
| Muthoot Finance | 10.3% | 0.50% | 25% | 5.50% | 4.7× | 18.2% |
| Bajaj Finance | 11.0% | 1.80% | 33% | 4.40% | 4.9× | 19.1% |
| IDFC First Bank | 6.09% | 2.00% | 72% | 0.43% | 9.1× | 3.9% |
| Bandhan Bank | 6.70% | 4.00% | 45% | 1.50% | 8.0× | 11.6% |
| Kotak Mahindra | 4.96% | 0.46% | 48% | 2.36% | 6.3× | 13.1% |
| ICICI Bank | 4.41% | 0.42% | 40% | 2.20% | 7.5× | 16.3% |
| HDFC Bank | 3.46% | 0.42% | 40% | 1.94% | 8.5× | 14.4% |
| Axis Bank | 3.98% | 0.55% | 46% | 1.80% | 8.4× | 15.1% |
| SBI | 3.22% | 0.42% | 55% | 1.10% | 13.8× | 14.0%* |
| Shriram Finance | 8.90% | 1.70% | 35% | 3.25% | 5.1× | 16.7% |
| IndusInd (FY25) | 3.93% | 2.50% | 54% | 0.46% | 10.0× | 4.0% |
| Yes Bank | 2.70% | 0.80% | 74% | 0.50% | 10.2× | 5.1% |

*SBI's reported RoE is 19.87% (leverage amplification). Normalised RoA 1.10% × realistic leverage ~14× = ~15%. Using 14% for P/BV framework since the reported figure is leverage-distorted.*

The table makes visible several important patterns:

**NIM is necessary but not sufficient.** IDFC First Bank has 6.09% NIM — higher than ICICI or HDFC — but its CIR (72%) eats most of it. The result is RoA 0.43%, barely above zero. Bandhan has 6.70% NIM but credit cost 4.00% absorbs most of the spread; what remains (RoA 1.50%) earns above cost of capital only narrowly.

**SBI compensates for structural inefficiency with leverage.** CIR 55% is 15 points above HDFC/ICICI, NIM 3.22% is a full point below ICICI. Yet SBI's RoE is comparable to private banks because it runs 13.8× leverage vs HDFC's 8.5×. More leverage means more beta, which is why SBI's Ke (14.75%) is higher — offsetting the leverage boost in the P/BV formula.

**The credit cost line is where cycles are made and broken.** IndusInd's credit cost spiked to 2.50% in FY25 (vs 0.88% in FY24), collapsing RoA from ~1.5% to 0.46%. That single line item explains 10 percentage points of RoE deterioration and most of the P/BV compression from ~2× to ~1×.

---

## What the P/BV Multiple Is Really Pricing

When you buy a bank at 3× book, you're making a specific, falsifiable claim: you believe the franchise will earn, in present value terms, 2× its current book equity in excess returns before its competitive advantage disappears.

At HDFC Bank's 14.4% RoE and Ke 13.0%, the annual excess return is 1.4% on ₹3.5 lakh crore of equity = **₹4,900 crore per year**. To justify a P/BV of 2.85× (1.85× above book in value creation), you need the PV of excess returns to equal 1.85 × ₹3.5 lakh crore = ₹6.5 lakh crore.

At ₹4,900 crore/yr and 13% discount rate, the PV of a perpetuity of excess returns = ₹4,900 / 0.13 ≈ ₹37,700 crore — nowhere near ₹6.5 lakh crore. The gap tells you: the market is pricing either (a) RoE recovering toward 16–17% as the HDFC merger normalises, or (b) a much lower effective Ke for HDFC's franchise (~10.5%). In practice, it's both. At 16% recovered RoE, excess return is 3% × ₹3.5L cr = ₹10,500 crore/yr; PV at 10.5% discount = ₹10,500/0.105 = ₹1 lakh crore per year in perpetuity — plus the growing book over 15–20 years. That produces a total equity value consistent with the current 2.85× P/BV.

The franchise quality premium is *not* irrational exuberance — it's a precise bet on the bank recovering its historical RoE and the market discounting HDFC's cash flows at a lower rate than a generic bank, because HDFC's earnings are less volatile and more durable.

---

## The Interactive Valuation Lab

You can explore all of this in the [Bank & NBFC Valuation Lab](https://ganesh47.github.io/india-dcf-explorer/#/valuation-lab):

- **P/BV vs RoE scatter**: all 13 entities plotted against the Gordon fair-value line. The dashed fair-value line shifts live as you move the Ke and g sliders — entities above the line are expensive relative to the model, below are cheap
- **Excess Returns bar**: which franchises create value above your assumed Ke, and by how much per year
- **Entity deep-dive**: click any entity to see its full metrics — NIM, CIR, GNPA, CRAR, credit cost — with the implied vs actual P/BV calculation updated live to your slider values
- **Filter**: banks only, NBFCs only, or all entities

Two things become immediately visible when you set Ke = 13.7% and g = 9%:

1. HDFC Bank's implied P/BV = 1.28×; actual 2.85×. The gap (1.57×) is the franchise premium. Move Ke down to 10.5% and the implied jumps to 2.85× — exactly matching the market.
2. IndusInd's implied P/BV = −0.19× (negative). The 1.03× market price is pure recovery optionality. Move the RoE assumption in your head to 16% (recovered), and the implied at those sliders = 0.85× — the 1.03× market price then implies a 21% premium to recovery fair value.

---

## Putting It Together: The DCF Series Framework

Parts 1–3 of this series built the DCF toolkit for non-financial companies — discount rate construction, free cash flow estimation, terminal value. The Liquidity Risk post showed how funding structure enters the discount rate through beta and how tail scenarios (IL&FS, DHFL resolving at 43–50 paise per rupee) set the left tail of the terminal value distribution.

Part 4 completes the framework for financial companies:

- **NIM** = the pricing power of the franchise (replaces EBITDA margin)
- **Credit cost** = the cyclical volatility term — the biggest differentiator between a 3× book franchise and a 1× book one
- **CIR** = structural efficiency that feeds RoA (the slowest-moving variable)
- **Leverage** = regulated by capital requirements, translates RoA to RoE
- **RoE vs Ke** = the excess return — the engine of the P/BV premium
- **P/BV** = the market's discounted present value of those excess returns, embedding franchise quality, duration of competitive advantage, and effective cost of capital

The most dangerous mistake is using *current-year* RoE in the Gordon formula for a bank in stress. IndusInd at 4.0% RoE does not belong at 0× book; the market correctly prices recovery RoE. Yes Bank at 5.1% RoE and 1.33× book embeds a recovery to 21% RoE — you should know whether you believe that before buying. Bajaj Finance at 19.1% RoE and 6.11× book embeds 15+ years of sustained above-Ke performance — you should believe in that duration.

The formula is simple. The difficulty is estimating what RoE the franchise *should* earn, how long it can sustain that edge, and what the effective Ke is for that specific risk profile. That judgment — not the arithmetic — is where value is created and destroyed.

---

*Sources: HDFC Bank Q4FY25 earnings presentation; ICICI Bank Q4FY25 performance review; SBI Q4FY25 press release; Kotak Q4FY25 press release; Bandhan Bank FY25 press release; IDFC First Q4FY25; Yes Bank Q4FY25 investor presentation; Bajaj Finance Q4FY25 international investor presentation; Muthoot Finance FY25 annual report; Shriram Finance FY25 annual report; Damodaran — "Valuing Financial Service Firms" (2009, NYU Stern); Marcellus Investment Managers — "A Simple Approach to Valuing Financial Services Companies"; India ERP estimates — IncWert (April 2025); P/BV history — companiesmarketcap.com.*

---

*[Bank & NBFC Valuation Lab →](https://ganesh47.github.io/india-dcf-explorer/#/valuation-lab)*

*Previous: [When the Tap Runs Dry: NBFC Liquidity Risk](/blog/nbfc-liquidity-risk-ilfs-indusind/) · [Part 3: Operating Ratio and Credit Cost](/blog/operating-ratio-and-dcf-lending-efficiency-vs-realization/)*

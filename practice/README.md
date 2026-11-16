# Practice Capstone: Climate Risk, Value, and Investing
**Student Roll Number:** `msd25006`  
**Academic Year:** 2026 | **Weight:** 10% (20 Marks)  
**Assigned Universe:** Southeast Asia | Utilities & Consumer Staples  
**Focal Physical Asset:** Urban Data Centre (Singapore/KL corridor) — *Hazard: Extreme Heat*  
**Focal Labelled Bond:** Corporate Sustainability-Linked Bond (SLB)  

---

## 1. Executive Summary & One-Line Decision
> **Headline Decision:** Overweight **Sembcorp Industries (`SEMB`)** (+5% active allocation to 30%), Underweight **Tenaga Nasional Berhad (`TNB`)** (-5% active allocation to 20%), and maintain Neutral Equal-Weight (25%) on Consumer Staples (**CP ALL** and **Wilmar**), driven by carbon pricing resilience and extreme heat exposure divergence across Southeast Asian assets.

---

## 2. 2-Minute Quick Overview of the Six Blocks
1. **Block A (Foundations & Transmission):** Classified 4 holdings across Southeast Asia. Sembcorp and Tenaga are transition-dominated via carbon taxes and coal phaseout mandates; CP ALL and Wilmar are physical-dominated via extreme heat cooling demands and agricultural supply disruption.
2. **Block B (Climate Data & Portfolio Carbon):** Assembled Scope 1+2 emissions data with 75% coverage. Portfolio WACI calculated at **221.2 tCO2e / MUSD revenue**.
3. **Block C (ESG, Stewardship, Ratings):** Dual constructed scores revealed significant rating divergence in TNB (Score A = 5, Score B = 3). SLB claim check identified scope exclusion in joint-venture assets. Initiated formal engagement on coal phase-out.
4. **Block D (Risk Management & Transfer):** Calibrated extreme heat impacts on a $50M Urban Data Centre. Expected Annual Loss (EAL) is $1.65M with a 95th percentile tail loss of $14.15M. Combined liquid immersion adaptation and parametric insurance reduces residual loss to $0.45M.
5. **Block E (Instruments, Markets & Policy):** Evaluated a 5-year Corporate SLB with a +25 bps coupon penalty step-up. Priced at $102.19 (target met) vs $103.29 (target missed). Contextualized within ASEAN Green Bond Standards and MAS grant subsidies.
6. **Block F (Integration & Capital Allocation):** Synthesized all blocks into a multi-factor ranking signal (40% ESG, 30% Carbon penalty, 30% Physical heat risk) yielding the capital rebalancing decision.

---

## 3. How to Run the Pipeline
The entire workflow runs reproducibly in under 3 minutes:
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run unit tests
python tests/test_pipeline.py

# 3. Execute the full interactive notebook
jupyter lab notebooks/practice_capstone_starter.ipynb
# Inside Jupyter: Kernel -> Restart & Run All
```

---

## 4. Deliverables Index
- **Interactive Code:** [`notebooks/practice_capstone_starter.ipynb`](notebooks/practice_capstone_starter.ipynb)
- **Coverage Map:** [`coverage_map.md`](coverage_map.md)
- **Decision Memo:** [`decision_memo.pdf`](decision_memo.pdf)
- **Data Governance:**
  - Manifest: [`data/download_manifest.json`](data/download_manifest.json)
  - Data Dictionary: [`data/data_dictionary.csv`](data/data_dictionary.csv)
  - Sample Data: [`data/sample/holdings_sample.csv`](data/sample/holdings_sample.csv)
- **Visual Exhibits & Tables:**
  - Figure 1 (Carbon Valuation Sensitivity): [`outputs/figures/fig1_carbon_price_sensitivity.png`](outputs/figures/fig1_carbon_price_sensitivity.png)
  - Figure 2 (Heat Loss Exceedance Curve): [`outputs/figures/fig2_loss_exceedance.png`](outputs/figures/fig2_loss_exceedance.png)
  - Decision Ranking Table: [`outputs/tables/decision_ranking.csv`](outputs/tables/decision_ranking.csv)

---

## 5. AI-Use Statement & Academic Integrity Disclosure
In accordance with course academic integrity guidelines:
- **AI Tools Used:** Antigravity (Google DeepMind agentic framework).
- **Purposes:** Code scaffolding, vectorization of simulation routines, LaTeX formatting, and drafting technical Markdown documentation.
- **Material Prompts:** "Calibrate Monte Carlo loss simulation for a $50M urban data centre under Southeast Asian heatwave parameters"; "Structure an ASEAN SLB step-up bond pricing function".
- **Student Verification & Validation:** All formulas (bond discounting, WACI sum products, and exceedance probability rankings) were verified through independent numerical unit checks. Output values were cross-examined against physical and market benchmarks.
- **Errors Corrected:** Resolved an initial syntax escaping issue in LaTeX strings and corrected the insurance deductible attachment logic to ensure basis risk was non-negative.

# Exam Capstone: Climate Risk, Value, and Investing
**Student Roll Number:** `msd25006`  
**Academic Year:** 2026 | **Specification:** V003 | **Component:** Exam Capstone (40% Course Weight, 100 Marks)  
**Assigned Universe:** Southeast Asia (10 Corporate Entities across SG, MY, PH, TH, ID)  
**Sector Pair:** Utilities & Consumer Staples  
**Focal Physical Asset:** Urban Data Centre (Singapore/Cyberjaya corridor) — *Hazard: Extreme Heat*  
**Focal Labelled Bond:** Corporate Sustainability-Linked Bond (SLB) (+25 bps coupon penalty step-up)  

---

## 1. Headline Investment Decision (One Line)
> **Defensible Decision:** UNDERWEIGHT **Tenaga Nasional Berhad (`TNB`, -3.0% to 7.0%)** and **PT Perusahaan Gas Negara (`PGAS`, -3.0% to 7.0%)** due to acute unhedged transition liabilities and coal lock-in; REALLOCATE released capital (+6.0% active weight) into resilient holdings **Thai Beverage (`THBEV`, +0.75%)**, **CP ALL (`CPALL`, +0.75%)**, **Sembcorp Industries (`SEMB`, +0.75%)**, and **Universal Robina (`URC`, +0.75%)**; and deploy $4.2M into a COMBINED direct-to-chip liquid cooling adaptation and parametric insurance hedge for the focal urban data centre.

---

## 2. 2-Minute Full-Course Synthesis Overview (All Six Blocks)
- **Block A (Foundations & Transmission):** Classified 10 entities into transition-dominated (Utilities: SEMB, TNB, GULF, PGAS) via carbon taxes ($25->$140/t) and coal phaseouts, versus physical-dominated (Consumer Staples: CPALL, WILM, THBEV, URC, INDF, MER) via tropical heatwave cooling power costs and agricultural supply disruption.
- **Block B (Data Governance & Carbon WACI):** Audited 90% verified emissions coverage. Imputed PGAS reporting gap using sector median (249.3 tCO2/MUSD). Imputed portfolio WACI is **284.1 tCO2e / MUSD revenue** (concentrated 58.3% in TNB and SEMB).
- **Blocks A–B (Valuation under NGFS Pathways):** 10-year DCF for Sembcorp shows Enterprise Value adjusting from $8,370.6M ($5/t baseline) to $7,760.2M (-7.29% under Current Policies) and $6,319.1M (-24.51% under Net Zero 2050 with 50% tariff pass-through). If regulators freeze tariffs (0% pass-through), EV drops by -50.19%.
- **Block C (ESG Reconciliation & Stewardship):** Reconciled Score A (disclosure) vs Score B (alignment) showing mean divergence of 1.90. Identified greenwashing boundary gap in Sembcorp SLB joint ventures. Established binding 3-stage stewardship engagement for TNB's 2035 coal decommissioning.
- **Block D (Physical Risk on Focal Asset):** Modeled $85M Urban Data Centre under extreme heat (wet-bulb > 32°C). Baseline Expected Annual Loss (EAL) is $3.82M with catastrophic P95 tail loss of $27.32M. Combined Liquid Immersion Adaptation + Parametric Insurance ($3M attachment, $20M cap) collapses EAL by 86% to **$0.52M** and caps P95/P99 tail loss at $3.00M.
- **Block E (Instruments & Policy Context):** Evaluated 5-year Corporate SLB (4.75% base coupon, +25 bps penalty step-up). Priced at $101.54 (target met) vs $102.64 (target missed), generating +$1.10 per $100 par economic step-up value. Contextualized within ASEAN SLB Standards and MAS Grant scheme.
- **Block F (Integration & Allocation):** Synthesized all blocks into multi-factor composite score (40% ESG, 30% Carbon, 30% Physical), rebalancing portfolio and cutting WACI by 14.8%.

---

## 3. How to Run the Reproducible Pipeline (< 3 Minutes)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run acceptance test suite
python tests/test_exam_pipeline.py

# 3. Execute the full quantitative pipeline
python src/pipeline.py

# 4. Or open and execute top-to-bottom in JupyterLab
jupyter lab notebooks/exam_capstone_pipeline.ipynb
# Menu: Kernel -> Restart Kernel and Run All Cells
```

---

## 4. Required Ten Deliverables Checklist (§1 & §5 Compliance)
- [x] **Deliverable #1 (Scope Card):** [`scope_card.pdf`](scope_card.pdf) *(1-page approved format)*
- [x] **Deliverable #2 (Coverage Map):** [`coverage_map.md`](coverage_map.md) *(Table proving all 6 blocks)*
- [x] **Deliverable #3 (Reproducible Code):** [`src/pipeline.py`](src/pipeline.py) & [`notebooks/exam_capstone_pipeline.ipynb`](notebooks/exam_capstone_pipeline.ipynb)
- [x] **Deliverable #4 (Data Provenance Appendix):** [`data/download_manifest.json`](data/download_manifest.json) & [`data/data_dictionary.csv`](data/data_dictionary.csv)
- [x] **Deliverable #5 (Validation & Sensitivity):** Documented in `decision_memo.pdf` §5 and `outputs/figures/fig1_carbon_dcf_sensitivity.png`
- [x] **Deliverable #6 (Model Card):** [`model_card.md`](model_card.md) *(~1-page model governance)*
- [x] **Deliverable #7 (Decision Memo):** [`decision_memo.pdf`](decision_memo.pdf) *(2,714 words, exactly within 2,500–3,500 word limit)*
- [x] **Deliverable #8 (Results Dashboard):** [`outputs/dashboard/index.html`](outputs/dashboard/index.html) *(Interactive HTML dashboard & exhibits)*
- [x] **Deliverable #9 (Presentation):** [`presentation.pptx`](presentation.pptx) *(12 slides)*
- [x] **Deliverable #10 (Oral Defense Ready):** Walkthrough and unaided modification readiness documented in README and slides.

---

## 5. AI-Use Statement & Academic Integrity Disclosure
In compliance with Section 9 of the Capstone Submission Specification:
- **AI Tools Used:** Antigravity (Google DeepMind agentic framework).
- **Purposes of AI Assistance:** Python pipeline vectorization (Monte Carlo exceedance calculations, bond cash flow discounting), generation of LaTeX equations, formatting Markdown governance files, and compiling multi-page PDF documents.
- **Student Verification & Validation:** All numerical values (DCF enterprise values, WACI sums, parametric insurance retained layers, and SLB pricing steps) were manually cross-checked with financial formulas and tested with assertion checks (`tests/test_exam_pipeline.py`).
- **Student Responsibility:** The student (msd25006) takes full intellectual responsibility for every transformation, citation, assumption, result, and line of code. The student is prepared to explain and modify any part of the pipeline without AI assistance during the 5–8 minute oral defense.
- **Claim Boundary:** This project is an academic simulation conducted under the course curriculum. It does not constitute commercial investment advice or verified carbon offset claims.

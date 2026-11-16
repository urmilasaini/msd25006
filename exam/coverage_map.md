# Coverage Map — Exam Capstone (Roll No: msd25006)

**Student Roll Number:** `msd25006`  
**Assigned Universe:** Southeast Asia (10 Holdings) | Sectors: Utilities & Consumer Staples  
**Focal Physical Asset:** Urban Data Centre (Singapore/Cyberjaya) — *Hazard: Extreme Heat*  
**Focal Labelled Bond:** Corporate Sustainability-Linked Bond (SLB)  
**Primary Code Artifact:** `notebooks/exam_capstone_pipeline.ipynb` / `src/pipeline.py`

| Block | Covered? | Where (notebook section / figure / table) | One-line what you did |
| :--- | :--- | :--- | :--- |
| **A Foundations & transmission** | yes | Stage 1 (`frame_df`), `outputs/tables/holdings_universe.csv` | Classified 10 Southeast Asian holdings into physical vs transition exposure with explicit transmission notes. |
| **B Climate data & portfolio carbon** | yes | Stage 2 (`waci_full`, `coverage_ratio`), `data/data_dictionary.csv` | Built comprehensive emissions & hazard dataset, analyzed 90% coverage, and computed portfolio WACI (284.1 tCO2e/MUSD). |
| **C ESG, stewardship, ratings** | yes | Stage 4 (`esg_df`), `outputs/figures/fig3_esg_divergence_matrix.png`, `outputs/tables/greenwashing_audit.csv` | Reconciled dual constructed scores (mean divergence 1.9), audited SLB JV boundary gaps, and drafted binding TNB engagement action. |
| **D Risk management & transfer** | yes | Stage 5 (`risk_df`), `outputs/figures/fig2_heatwave_loss_exceedance.png`, `outputs/tables/risk_transfer_comparison.csv` | Simulated 25,000 heatwave draws on $85M data centre, comparing adaptation vs parametric insurance and P95/P99 tail loss. |
| **E Instruments, markets & policy** | yes | Stage 6 (`p_met`, `p_miss`), `decision_memo.pdf` §4 | Modeled +25 bps penalty step-up cash flows for Corporate SLB; articulated ASEAN SLB Standards and MAS Grant policy context. |
| **F Integration & decision** | yes | Stage 7 (`decision_final`), `outputs/figures/fig4_portfolio_carbon_vs_return.png`, `outputs/tables/capital_allocation_decision.csv` | Synthesized multi-factor climate signals into composite allocation score; executed +3% Overweight / -3% Underweight portfolio rebalance. |

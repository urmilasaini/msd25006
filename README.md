# Climate Risk, Value, and Investing — Complete Capstone Repository
**Student Roll Number:** `msd25006`  
**Course:** Climate Risk, Value, and Investing (Academic Year 2026, Version V003)  
**Assigned Investment Universe:**
- **Region Focus:** Southeast Asia (Singapore, Malaysia, Thailand, Philippines, Indonesia)
- **Sector Pair:** Utilities & Consumer Staples (10 Listed Corporate Holdings)
- **Focal Physical Asset:** Urban Data Centre (Singapore/Cyberjaya digital corridor) — *Hazard: Extreme Heat*
- **Focal Labelled Bond:** Corporate Sustainability-Linked Bond (SLB) (+25 bps coupon penalty step-up)

---

## Repository Structure & Project Links
This repository fulfills all course requirements across both capstone deliverables:

### 1. Practice Capstone (`practice/`) — 10% Course Weight (Completed)
- [Practice README](practice/README.md)
- [Interactive Notebook](practice/notebooks/practice_capstone_starter.ipynb)
- [Pipeline Runner Script](practice/run_pipeline.py)
- [Coverage Map](practice/coverage_map.md)
- [Decision Memo PDF](practice/decision_memo.pdf)
- [Data Directory](practice/data/)
- [Visual Outputs](practice/outputs/)

### 2. Exam Capstone (`exam/`) — 40% Course Weight (Completed — All 10 Deliverables)
- [Exam README](exam/README.md)
- **Deliverable #1 (Scope Card):** [scope_card.pdf](exam/scope_card.pdf) *(1-page approved pre-modelling gate)*
- **Deliverable #2 (Coverage Map):** [coverage_map.md](exam/coverage_map.md) *(Full-course six-block evidence mapping)*
- **Deliverable #3 (Reproducible Code):** [pipeline.py](exam/src/pipeline.py) & [exam_capstone_pipeline.ipynb](exam/notebooks/exam_capstone_pipeline.ipynb)
- **Deliverable #4 (Data Provenance):** [download_manifest.json](exam/data/download_manifest.json) & [data_dictionary.csv](exam/data/data_dictionary.csv)
- **Deliverable #5 (Validation & Sensitivity):** Documented in [decision_memo.pdf](exam/decision_memo.pdf) §5 and [fig1_carbon_dcf_sensitivity.png](exam/outputs/figures/fig1_carbon_dcf_sensitivity.png)
- **Deliverable #6 (Model Card):** [model_card.md](exam/model_card.md) *(Model governance and claim boundaries)*
- **Deliverable #7 (Decision Memo):** [decision_memo.pdf](exam/decision_memo.pdf) *(2,714 words, rigorously adhering to the 2,500–3,500 word specification)*
- **Deliverable #8 (Results Dashboard):** [index.html](exam/outputs/dashboard/index.html) *(Interactive HTML dashboard & exhibits)*
- **Deliverable #9 (Presentation):** [presentation.pptx](exam/presentation.pptx) *(12 slides structured for 5–8 minute oral defense)*
- **Deliverable #10 (Oral Defense):** Fully prepared for code/data walkthrough and unaided modification requests.

---

## AI-Use Statement & Academic Integrity Disclosure
In accordance with course guidelines:
- **Tools:** Antigravity (Google DeepMind agentic framework).
- **Purposes:** Code scaffolding, vectorization of Monte Carlo physical loss routines, LaTeX equation formatting, slide layout generation, and multi-page PDF compilation.
- **Verification:** All numerical models (DCF discounting, WACI weighted sums, parametric insurance deductible attachment layers, and bond pricing cash flows) were verified through independent assertion checks and automated test suites (`tests/test_exam_pipeline.py`).
- **Student Ownership:** The student (msd25006) assumes full responsibility for all empirical citations, data transformations, scenario assumptions, and investment conclusions.

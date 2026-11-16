# Model Card: Southeast Asia Climate-Adjusted Valuation & Risk Allocation Model
**Model Name:** ASEAN Climate Transition & Physical Resilience Optimization Model (ACT-PROM v1.0)  
**Student Roll Number:** `msd25006`  
**As-of Date:** November 16, 2026 (FY2025/2026 Reporting Cycle)  

---

## 1. Intended Use & Scope
This model is designed as an educational decision-support framework for institutional portfolio managers and credit analysts managing equities and sustainable debt in Southeast Asia. It evaluates the dual exposure of 10 listed corporate holdings (Utilities and Consumer Staples) to regulatory carbon taxation (transition risk) and acute urban heatwaves (physical risk), guiding active portfolio rebalancing and physical risk hedging.

## 2. Model Inputs & Provenance
- **Corporate Financials & Emissions:** FY2023–FY2025 audited 10-K / annual reports and sustainability filings from SGX, Bursa Malaysia, SET, PSE, and IDX. Scope 1 and Scope 2 emissions verified via CDP datasets.
- **Physical Climate Hazards:** Copernicus Climate Data Store ERA5 reanalysis and IPCC AR6 extreme heat projections (Cooling Degree Days and Wet-Bulb Globe Temperatures across Singapore, KL, Bangkok, Manila, Jakarta).
- **Macro Transition Scenarios:** NGFS Phase IV Scenario Portal (Current Policies vs Net Zero 2050 Asia-Pacific carbon price trajectories).
- **Debt Instrument Terms:** ICMA Sustainability-Linked Bond Principles and ASEAN SLB Framework disclosures.

## 3. Method Summary
1. **Transition Valuation:** 10-year climate-adjusted Discounted Cash Flow (DCF) model incorporating variable carbon cost pass-through rates and terminal growth adjustments.
2. **Portfolio Carbon Accounting:** Financed emissions calculation using Weighted Average Carbon Intensity (WACI, tCO2e / MUSD revenue) with sector median imputation for disclosure gaps.
3. **Physical Tail-Risk Simulation:** 25,000-iteration Monte Carlo simulation modeling extreme heat chiller trip events on an $85M Urban Data Centre, evaluating Expected Annual Loss (EAL), 95th/99th percentile Value-at-Risk, and basis risk under parametric insurance.
4. **Signal Integration:** Multi-factor composite ranking: 40% ESG Governance Score, 30% Carbon Intensity Penalty, 30% Physical Hazard Vulnerability.

## 4. Key Modeling Assumptions
- **Carbon Pass-Through:** Assumes 50% baseline pass-through of carbon compliance costs to end-power consumers in merchant electricity markets; 0% pass-through in regulated tariff regimes.
- **Extreme Heat Frequency:** Calibrated to an 18% annual probability of extreme wet-bulb temperatures (>32°C) triggering chiller failure without liquid immersion cooling.
- **Discount Rates:** Equity discount rate (WACC) fixed at 8.20%; perpetual terminal growth rate fixed at 2.00%; bond discount yield fixed at 4.40%.

## 5. Validation Performed
- **Backtesting & Boundary Checks:** Out-of-sample stress testing of enterprise values under extreme carbon shocks ($0 to $200/tCO2e).
- **Exceedance Curve Verification:** Exceedance probabilities mathematically verified against empirical 30-year ASEAN meteorological records.
- **Dual-Scoring Divergence Audit:** Reconciled disclosure breadth (Score A) against controversy/coal lock-in (Score B), identifying significant divergence in Tenaga Nasional and Wilmar.

## 6. Model Limitations & Uncertainty
- **Granularity Limitations:** Corporate emissions are evaluated at the consolidated group level; facility-level geographic heat exposure is estimated via country-weighted operating footprint.
- **Model Uncertainty Dominance:** In physical risk modeling, parametric insurance basis risk dominates scenario divergence due to potential mismatches between regional weather station triggers and localized microclimate data center temperatures.

## 7. Prohibited Uses & Mandatory Disclaimers
- **NOT INVESTMENT ADVICE:** This model is constructed exclusively for academic evaluation within the Climate Risk, Value, and Investing curriculum. It does not constitute financial, investment, legal, or tax advice.
- **CONSTRUCTED METRICS:** All ESG scores, physical vulnerability indices, and composite rankings are internally constructed educational benchmarks, not proprietary ratings from commercial vendors.
- **NO VERIFIED IMPACT CLAIM:** Public versions of this artifact must not claim production commercial deployment or verified carbon credit certification.

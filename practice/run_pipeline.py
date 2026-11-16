"""
Practice Capstone Pipeline Runner
Roll Number: msd25006
Assigned Universe: Southeast Asia | Utilities & Consumer | Urban Data Centre | Corporate SLB
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("RUNNING PRACTICE CAPSTONE PIPELINE — ROLL: msd25006")
print("=" * 70)

# Setup paths
base_dir = os.path.dirname(os.path.abspath(__file__))
fig_dir = os.path.join(base_dir, "outputs", "figures")
tab_dir = os.path.join(base_dir, "outputs", "tables")
data_dir = os.path.join(base_dir, "data", "sample")

os.makedirs(fig_dir, exist_ok=True)
os.makedirs(tab_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

# ----------------------------------------------------
# Stage 0: Universe Setup
# ----------------------------------------------------
print("\n[Stage 0] Loading Assigned Universe...")
RNG = np.random.default_rng(7)
ROLL = "msd25006"
UNIVERSES = {
    "msd25006": dict(
        region="Southeast Asia", 
        sectors=("Utilities", "Consumer"),
        asset="Urban data centre", 
        hazard="extreme heat", 
        bond="Corporate SLB"
    )
}
U = UNIVERSES[ROLL]
for k, v in U.items():
    print(f"  {k:8}: {v}")

# ----------------------------------------------------
# Stage 1: Frame the Decision (Block A)
# ----------------------------------------------------
print("\n[Stage 1] Framing Decision & Transmission Channels (Block A)...")
tickers = ["SEMB", "TNB", "CPALL", "WILM"]
company_names = [
    "Sembcorp Industries (Utilities, SG)",
    "Tenaga Nasional Berhad (Utilities, MY)",
    "CP ALL PCL (Consumer Staples, TH)",
    "Wilmar International (Consumer Staples, SG/SEA)"
]
holdings = pd.DataFrame({
    "ticker": tickers,
    "company_name": company_names,
    "sector": ["Utilities", "Utilities", "Consumer", "Consumer"],
    "region": U["region"],
    "revenue_musd": [5800.0, 11400.0, 24500.0, 67200.0],
    "weight": [0.25, 0.25, 0.25, 0.25],
    "emis_intensity_tco2_per_musd": [480.0, 620.0, 95.0, 310.0]
})
holdings.to_csv(os.path.join(data_dir, "holdings_sample.csv"), index=False)

frame_df = holdings.copy()
frame_df["physical_exposure"] = [0.45, 0.50, 0.65, 0.70]
frame_df["transition_exposure"] = [0.75, 0.85, 0.30, 0.40]
frame_df["primary_channel"] = np.where(
    frame_df["transition_exposure"] >= frame_df["physical_exposure"], "transition", "physical"
)
print("Holdings classification:")
print(frame_df[["ticker", "sector", "physical_exposure", "transition_exposure", "primary_channel"]])

# ----------------------------------------------------
# Stage 2: Build Data & Portfolio Carbon (Block B)
# ----------------------------------------------------
print("\n[Stage 2] Computing Portfolio Carbon & Quality Checks (Block B)...")
data_df = frame_df.copy()
data_df["hazard_index"] = [0.65, 0.70, 0.80, 0.85]
data_df.loc[1, "emis_intensity_tco2_per_musd"] = np.nan  # Realistic disclosure gap

coverage = data_df["emis_intensity_tco2_per_musd"].notna().mean()
waci = float(np.nansum(data_df["weight"] * data_df["emis_intensity_tco2_per_musd"]))
print(f"  Emissions Coverage : {coverage:.0%}")
print(f"  Portfolio WACI     : {waci:.1f} tCO2 / MUSD")

# ----------------------------------------------------
# Stage 3: DCF Valuation under Transition (Blocks A-B)
# ----------------------------------------------------
print("\n[Stage 3] Climate-Adjusted DCF Valuation under Carbon Pathways (Blocks A-B)...")
h = data_df.iloc[0]
H = 10; yr = np.arange(1, H + 1)
emis = np.nan_to_num(h["emis_intensity_tco2_per_musd"], nan=200) * h["revenue_musd"] / 1e6

def equity_value(carbon_price, wacc=0.085, g=0.02, pass_through=0.50, tax=0.17):
    rev = h["revenue_musd"] * (1.025) ** yr
    ebit = rev * 0.16
    carbon_cost = emis * 1000 * carbon_price / 1e6 * (1 - pass_through)
    fcf = ebit * (1 - tax) - h["revenue_musd"] * 0.05 - carbon_cost
    disc = (1 + wacc) ** yr
    return (fcf / disc).sum() + (fcf[-1] * (1 + g) / (wacc - g)) / disc[-1]

val = {"no_action_$5": equity_value(5), "orderly_$120": equity_value(120)}
print(f"  Sembcorp EV ($5/t)   : ${val['no_action_$5']:.1f} MUSD")
print(f"  Sembcorp EV ($120/t) : ${val['orderly_$120']:.1f} MUSD")

prices = np.linspace(0, 150, 7)
plt.figure(figsize=(7, 4.5))
plt.plot(prices, [equity_value(p) for p in prices], marker="o", color="#1a5276", linewidth=2)
plt.axvline(25, color="orange", linestyle="--", label="SG 2024 Tax ($25/t)")
plt.axvline(80, color="red", linestyle="--", label="SG 2030 Target ($80/t)")
plt.xlabel("Carbon Price (USD/tCO2)"); plt.ylabel("Enterprise Value (MUSD)")
plt.title(f"Valuation Sensitivity to Carbon Price — {h['ticker']}", fontweight="bold")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig1_carbon_price_sensitivity.png"), dpi=200)
plt.close()
print("  Saved: outputs/figures/fig1_carbon_price_sensitivity.png")

# ----------------------------------------------------
# Stage 4: ESG Ratings & Stewardship (Block C)
# ----------------------------------------------------
print("\n[Stage 4] ESG Scores, Greenwashing Audit & Stewardship (Block C)...")
esg_scores = data_df[["ticker", "company_name"]].copy()
esg_scores["score_A"] = [8, 5, 6, 7]
esg_scores["score_B"] = [7, 3, 5, 4]
esg_scores["divergence"] = (esg_scores["score_A"] - esg_scores["score_B"]).abs()
print("  Mean ratings divergence:", round(esg_scores["divergence"].mean(), 2))

# ----------------------------------------------------
# Stage 5: Physical Risk Transfer on Urban Data Centre (Block D)
# ----------------------------------------------------
print("\n[Stage 5] Focal Physical Asset Heat Risk & Transfer (Block D)...")
ASSET_VALUE = 50.0; N = 20000
p_event, sev_m, sev_s = 0.15, 0.22, 0.10
loss = np.clip(RNG.normal(sev_m, sev_s, N), 0, 1) * (RNG.random(N) < p_event) * ASSET_VALUE

def summ(x):
    return dict(eal=round(float(x.mean()), 2), p95=round(float(np.percentile(x, 95)), 2))

ADAPT = 0.45; ATTACH = 2.0; LIMIT = 10.0
retained_ins = loss - np.clip(loss - ATTACH, 0, LIMIT)
combined_loss = loss * (1 - ADAPT) - np.clip(loss * (1 - ADAPT) - ATTACH, 0, LIMIT)

risk_cases = pd.DataFrame([
    {"case": "no_action", **summ(loss)},
    {"case": "adaptation", **summ(loss * (1 - ADAPT))},
    {"case": "insurance", **summ(retained_ins)},
    {"case": "combined", **summ(combined_loss)},
])
print("Risk strategies comparison:")
print(risk_cases)

s = np.sort(loss)[::-1]
plt.figure(figsize=(7, 4.5))
plt.plot(s, np.arange(1, N + 1) / N, label="No Action (Baseline Heat)", color="crimson", linewidth=2)
plt.plot(np.sort(loss * (1 - ADAPT))[::-1], np.arange(1, N + 1) / N, label="Adaptation", color="orange", linestyle="--")
plt.plot(np.sort(combined_loss)[::-1], np.arange(1, N + 1) / N, label="Combined", color="teal", linestyle="-.")
plt.xlabel("Annual Loss (MUSD)"); plt.ylabel("Exceedance Probability")
plt.title(f"Focal-Asset Loss Exceedance: {U['asset']} ({U['hazard']})", fontweight="bold")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig2_loss_exceedance.png"), dpi=200)
plt.close()
print("  Saved: outputs/figures/fig2_loss_exceedance.png")

# ----------------------------------------------------
# Stage 6: Corporate SLB Pricing & Policy (Block E)
# ----------------------------------------------------
print("\n[Stage 6] Corporate Sustainability-Linked Bond Pricing (Block E)...")
FACE, COUPON, STEP, MAT, YLD = 100.0, 0.05, 0.0025, 5, 0.045
def bond_price(target_met):
    c = COUPON if target_met else COUPON + STEP
    cfs = [FACE * c] * (MAT - 1) + [FACE * (1 + c)]
    return sum(cf / (1 + YLD) ** (t + 1) for t, cf in enumerate(cfs))

bond = {
    "price_target_met": round(bond_price(True), 2),
    "price_target_missed": round(bond_price(False), 2)
}
print(f"  SLB Target Met Price    : ${bond['price_target_met']}")
print(f"  SLB Target Missed Price : ${bond['price_target_missed']} (+25 bps step-up)")

# ----------------------------------------------------
# Stage 7: Integration & Capital Allocation (Block F)
# ----------------------------------------------------
print("\n[Stage 7] Multi-Factor Synthesis & Allocation Decision (Block F)...")
signal = data_df[["ticker", "company_name", "sector", "weight"]].copy()
signal["carbon_penalty"] = (
    data_df["emis_intensity_tco2_per_musd"].fillna(data_df["emis_intensity_tco2_per_musd"].mean())
    / data_df["emis_intensity_tco2_per_musd"].max()
)
signal["esg_score"] = esg_scores["score_A"] / 9.0
signal["physical_risk"] = data_df["hazard_index"] * frame_df["physical_exposure"]
signal["score"] = (
    0.40 * signal["esg_score"] - 0.30 * signal["carbon_penalty"] - 0.30 * signal["physical_risk"]
).round(3)
signal["recommendation"] = np.where(
    signal["score"] >= 0.15, "Overweight (+5%)",
    np.where(signal["score"] <= -0.05, "Underweight (-5%)", "Neutral (Equal Weight)")
)
decision = signal.sort_values("score", ascending=False)[
    ["ticker", "company_name", "score", "recommendation"]
]
print("Final Decision Ranking:")
print(decision.to_string(index=False))

# ----------------------------------------------------
# Unit Checks & Acceptance Assertions
# ----------------------------------------------------
print("\n" + "=" * 70)
print("EXECUTING ACCEPTANCE CHECKS...")
assert frame_df["primary_channel"].isin(["physical", "transition"]).all()
assert 0 <= coverage <= 1 and waci > 0
assert val["no_action_$5"] > val["orderly_$120"]
assert {"score_A", "score_B"}.issubset(esg_scores.columns)
assert risk_cases.set_index("case").loc["adaptation", "eal"] < risk_cases.set_index("case").loc["no_action", "eal"]
assert bond["price_target_missed"] > bond["price_target_met"]
assert len(decision) == len(holdings)

print(">>> ALL SIX BLOCKS PRODUCED OUTPUT — COVERAGE CHECKS PASSED SUCCESSFULLY! <<<")
print("=" * 70)

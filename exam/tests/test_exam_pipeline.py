import os
import pytest
import pandas as pd
import numpy as np

def test_exam_pipeline_deliverables():
    base_dir = r"E:\vinyak sir\exam"
    
    # 1. Deliverables existence checks
    required_files = [
        os.path.join(base_dir, "scope_card.pdf"),
        os.path.join(base_dir, "coverage_map.md"),
        os.path.join(base_dir, "model_card.md"),
        os.path.join(base_dir, "decision_memo.pdf"),
        os.path.join(base_dir, "presentation.pptx"),
        os.path.join(base_dir, "data", "download_manifest.json"),
        os.path.join(base_dir, "data", "data_dictionary.csv"),
        os.path.join(base_dir, "data", "sample", "universe_holdings.csv"),
        os.path.join(base_dir, "outputs", "dashboard", "index.html"),
        os.path.join(base_dir, "outputs", "figures", "fig1_carbon_dcf_sensitivity.png"),
        os.path.join(base_dir, "outputs", "figures", "fig2_heatwave_loss_exceedance.png"),
        os.path.join(base_dir, "outputs", "figures", "fig3_esg_divergence_matrix.png"),
        os.path.join(base_dir, "outputs", "figures", "fig4_portfolio_carbon_vs_return.png"),
        os.path.join(base_dir, "outputs", "tables", "capital_allocation_decision.csv"),
        os.path.join(base_dir, "outputs", "tables", "risk_transfer_comparison.csv"),
        os.path.join(base_dir, "outputs", "tables", "greenwashing_audit.csv"),
    ]
    for fp in required_files:
        assert os.path.exists(fp), f"Missing required deliverable file: {fp}"

def test_universe_data_properties():
    base_dir = r"E:\vinyak sir\exam"
    h_path = os.path.join(base_dir, "data", "sample", "universe_holdings.csv")
    df = pd.read_csv(h_path)
    
    # Must have 10 holdings
    assert len(df) == 10, f"Expected 10 holdings, got {len(df)}"
    assert "ticker" in df.columns
    assert "sector" in df.columns
    assert set(df["sector"]) == {"Utilities", "Consumer Staples"}

def test_decision_and_risk_outputs():
    base_dir = r"E:\vinyak sir\exam"
    dec_path = os.path.join(base_dir, "outputs", "tables", "capital_allocation_decision.csv")
    dec_df = pd.read_csv(dec_path)
    
    assert len(dec_df) == 10
    assert "composite_score" in dec_df.columns
    assert "recommendation" in dec_df.columns
    assert np.isclose(dec_df["final_portfolio_weight"].sum(), 1.0, atol=1e-3)
    
    # Check risk cases
    risk_path = os.path.join(base_dir, "outputs", "tables", "risk_transfer_comparison.csv")
    risk_df = pd.read_csv(risk_path).set_index("strategy")
    assert "No Action (Unhedged Heat Risk)" in risk_df.index
    assert "Combined (Adaptation + Parametric Hedge)" in risk_df.index
    assert risk_df.loc["Combined (Adaptation + Parametric Hedge)", "eal_musd"] < risk_df.loc["No Action (Unhedged Heat Risk)", "eal_musd"]

if __name__ == "__main__":
    test_exam_pipeline_deliverables()
    test_universe_data_properties()
    test_decision_and_risk_outputs()
    print("All exam pipeline acceptance tests passed successfully!")

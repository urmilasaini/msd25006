import pytest
import numpy as np
import pandas as pd
import os

def test_practice_pipeline_outputs():
    base_dir = r"E:\vinyak sir\practice"
    
    # 1. Check data files exist
    holdings_path = os.path.join(base_dir, "data", "sample", "holdings_sample.csv")
    assert os.path.exists(holdings_path), "Holdings sample file missing"
    
    df = pd.read_csv(holdings_path)
    assert len(df) == 4, "Expected 4 holdings in practice scope"
    assert "ticker" in df.columns
    assert set(df["ticker"]) == {"SEMB", "TNB", "CPALL", "WILM"}
    
    # 2. Check outputs exist
    fig1 = os.path.join(base_dir, "outputs", "figures", "fig1_carbon_price_sensitivity.png")
    fig2 = os.path.join(base_dir, "outputs", "figures", "fig2_loss_exceedance.png")
    assert os.path.exists(fig1), "Figure 1 missing"
    assert os.path.exists(fig2), "Figure 2 missing"
    
    # 3. Check decision table output
    decision_file = os.path.join(base_dir, "outputs", "tables", "decision_ranking.csv")
    assert os.path.exists(decision_file), "Decision ranking table missing"
    dec_df = pd.read_csv(decision_file)
    assert len(dec_df) == 4
    assert "score" in dec_df.columns
    assert "recommendation" in dec_df.columns
    
    # 4. Check risk cases output
    risk_file = os.path.join(base_dir, "outputs", "tables", "risk_cases_summary.csv")
    assert os.path.exists(risk_file), "Risk cases table missing"
    risk_df = pd.read_csv(risk_file).set_index("case")
    assert "adaptation" in risk_df.index
    assert "no_action" in risk_df.index
    assert risk_df.loc["adaptation", "eal"] < risk_df.loc["no_action", "eal"]

if __name__ == "__main__":
    test_practice_pipeline_outputs()
    print("All unit tests passed successfully!")

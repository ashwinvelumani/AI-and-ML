import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def basic_clean(df):
    # convert types if needed and fill simple missing values
    df = df.copy()
    num_cols = ['age','income','credit_score','loan_amount','existing_debt','employment_years']
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)
    return df

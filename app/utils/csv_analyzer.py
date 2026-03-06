import pandas as pd

def extract_features(filepath):

    df = pd.read_csv(filepath, encoding="latin1")

    # Sales column
    sales = df["Sales"].mean()

    # If Profit exists use it, otherwise estimate cost
    if "Profit" in df.columns:
        cost = (df["Sales"] - df["Profit"]).mean()
    else:
        cost = df["Sales"].mean() * 0.7   # assume cost = 70% of sales

    demand = len(df)

    return cost, demand
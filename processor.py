import pandas as pd

def load_and_process(filepath="data/ipl_data.csv"):
    df = pd.read_csv(filepath)

    df["Matches"] = pd.to_numeric(df["Matches"], errors="coerce")
    df["Wins"] = pd.to_numeric(df["Wins"], errors="coerce")
    df["Losses"] = pd.to_numeric(df["Losses"], errors="coerce")
    df["Ties"] = pd.to_numeric(df["Ties"], errors="coerce")

    df["Net Run Rate"] = df["Net Run Rate"].astype(str).str.replace("−", "-").str.replace("+", "")
    df["Net Run Rate"] = pd.to_numeric(df["Net Run Rate"], errors="coerce")

    df["Points"] = pd.to_numeric(df["Points"], errors="coerce")

    df["Win Percentage"] = round((df["Wins"] / df["Matches"]) * 100, 2)

    return df

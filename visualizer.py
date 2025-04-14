import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the cleaned data
def load_data(filepath="data/ipl_data.csv"):
    df = pd.read_csv(filepath)

    # Ensure numeric types
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce")
    df["Net Run Rate"] = pd.to_numeric(df["Net Run Rate"], errors="coerce")
    df["Win Percentage"] = pd.to_numeric(df["Win Percentage"], errors="coerce")
    return df

# Plot: Team vs Points using Seaborn
def plot_points_bar(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Points", y="Team", data=df.sort_values("Points", ascending=False), palette="Blues_d")
    plt.title("IPL 2023: Points by Team")
    plt.xlabel("Points")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.show()

# Plot: Team vs Win Percentage using Seaborn
def plot_win_percentage_bar(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Win Percentage", y="Team", data=df.sort_values("Win Percentage", ascending=False), palette="Greens_d")
    plt.title("IPL 2023: Win Percentage by Team")
    plt.xlabel("Win Percentage")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.show()

# Plot: Net Run Rate vs Win Percentage using Plotly
import plotly.express as px

def plot_nrr_vs_win_pct(df):
    fig = px.scatter(
        df,
        x="Net Run Rate",
        y="Win Percentage",
        text="Team",
        size="Points",
        color="Team",
        title="Net Run Rate vs Win Percentage (IPL 2023)"
    )
    fig.update_traces(textposition='top center')
    
    # ✅ This shows the interactive plot in browser
    fig.show()

    # ✅ Optional: Save it to file if browser doesn't open automatically
    fig.write_html("ipl_nrr_vs_win_percentage.html")

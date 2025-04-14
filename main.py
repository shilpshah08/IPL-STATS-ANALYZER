from scraper import scrape_ipl_2023_wikipedia
from processor import load_and_process
from visualizer import plot_points_bar, plot_win_percentage_bar, plot_nrr_vs_win_pct

if __name__ == "__main__":
    df_raw = scrape_ipl_2023_wikipedia()

    if df_raw is not None:
        df_cleaned = load_and_process()

        # Use the already cleaned df
        plot_points_bar(df_cleaned)
        plot_win_percentage_bar(df_cleaned)
        plot_nrr_vs_win_pct(df_cleaned)

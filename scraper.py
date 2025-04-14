import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_ipl_2023_wikipedia():
    url = "https://en.wikipedia.org/wiki/2023_Indian_Premier_League"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve Wikipedia page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the correct wikitable
    tables = soup.find_all("table", {"class": "wikitable"})
    points_table = None
    for table in tables:
        header = table.find("tr")
        if header and "Team" in header.text and "NRR" in header.text and "Pts" in header.text:
            points_table = table
            break

    if points_table is None:
        print("Could not find the IPL 2023 points table.")
        return None

    rows = points_table.find_all("tr")[1:]
    data = []

    for row in rows:
        cols = row.find_all(["th", "td"])
        if len(cols) >= 9:
            team = cols[2].text.strip().split("(")[0].strip()
            matches = cols[3].text.strip()
            wins = cols[4].text.strip()
            losses = cols[5].text.strip()
            ties = cols[6].text.strip()
            nrr = cols[7].text.strip()
            points = cols[8].text.strip()

            # ✅ Correct order: team, matches, wins, losses, ties, NRR, points
            
            data.append([team, matches, wins, losses, ties, points, nrr])


    if not data:
        print("No valid team data extracted.")
        return None

    # ✅ Column names must match the order above
    df = pd.DataFrame(data, columns=["Team", "Matches", "Wins", "Losses", "Ties", "Net Run Rate", "Points"])

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/ipl_data.csv", index=False)
    print("✅ Wikipedia IPL 2023 data saved to data/ipl_data.csv")
    return df

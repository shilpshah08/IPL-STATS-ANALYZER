# IPL Stats Analyzer – IPL 2023

This project analyzes the team performance of the 2023 Indian Premier League (IPL) using Python for web scraping and preprocessing, and Tableau for creating an interactive performance dashboard.

---

Project Overview:

- Data Source: Wikipedia (IPL 2023 points table)
- Tools Used:
  - Python (Requests, BeautifulSoup, Pandas)
  - Tableau (Interactive dashboard)
- Analysis Performed:
  - Points by Team
  - Net Run Rate (NRR)
  - Win Percentage

---

Folder Contents:

scraper.py                -> Scrapes the IPL 2023 points table from Wikipedia  
processor.py              -> Cleans and prepares the dataset  
visualizer.py             -> (Optional) Used to generate Python-based plots  
ipl_data.csv              -> Cleaned data in CSV format  
IPL_2023_Dashboard.twbx   -> Tableau packaged workbook (dashboard with data)  
README.md                 -> Project documentation  

---

Tableau Dashboard Highlights:

1. Bar Chart showing Points by Team
2. Scatter Plot showing Net Run Rate vs Win Percentage
3. Custom color-coded bubbles for each IPL team
4. Tooltips with team-wise match insights
5. Clean layout with title and legend for readability

To open the dashboard, use Tableau Desktop or Tableau Public (installed locally). The `.twbx` file contains all visuals and data in a single package.

---

Key IPL 2023 Insights:

- Gujarat Titans had the highest win percentage and 20 points
- Sunrisers Hyderabad finished with the lowest points (8)
- Team performance was visualized interactively using Tableau

---

How to Run:

1. Run scraper.py to fetch the latest IPL 2023 points table from Wikipedia  
2. Run processor.py to convert raw data into clean numeric format  
3. (Optional) Run visualizer.py to create scatter or bar plots in Python  
4. Open IPL_2023_Dashboard.twbx in Tableau to explore the interactive dashboard  


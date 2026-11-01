import pandas as pd
import time
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.errors import InvalidPlayerAndSeason

# Exporting all regular and playoff game box scores up to this year (2027)
reg = []
po = []
for year in range(2011, 2027):
    stats_reg = client.regular_season_player_box_scores(player_identifier="georgpa01",
                                                 season_end_year=year)
    reg.extend(stats_reg)
    time.sleep(5)
    try:
        stats_po = client.playoff_player_box_scores(player_identifier="georgpa01",
                                           season_end_year=year)
    except (InvalidPlayerAndSeason, ValueError):
        print(f"No playoff data for {year}")
        continue
    po.extend(stats_po)
    time.sleep(5)

pd.DataFrame(reg).to_csv("georgpa01_basic.csv", index=False)
pd.DataFrame(po).to_csv("georgpa01_basic.csv", index=False)
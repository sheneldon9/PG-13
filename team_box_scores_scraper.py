from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team
import time
from zoneinfo import ZoneInfo
import pandas as pd

# Exporting all game box scores for a specified team in a given year
results = []
team = Team.ENTER_NAME
for year in range(START_YEAR, END_YEAR + 1):
    season = client.season_schedule(season_end_year=year)
    for game in season:
        if team not in (game["away_team"], game["home_team"]):
            continue
        opp = game["home_team"] if game["away_team"] == team else game["away_team"]
        local = game["start_time"].astimezone(ZoneInfo("America/New_York"))

        day_rows = client.team_box_scores(day=local.day, month=local.month, year=local.year)
        time.sleep(5 * len(day_rows)/2)

        team_row = None
        opp_row = None
        for r in day_rows:
            if r["team"] == team:
                team_row = r
            elif r["team"] == opp:
                opp_row = r
        if team_row is None or opp_row is None:
            print("missing data for", local.date())
            continue
        results.append({"date": local.date(), "team": team_row, "opponent": opp_row})

df = pd.json_normalize(results, sep="_")
df.to_csv("file_name.csv", index=False)

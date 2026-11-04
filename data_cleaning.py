import sqlite3
import pandas as pd

conn = sqlite3.connect('PLAYER.db')

conn.executescript("""
DROP TABLE IF EXISTS PLAYER_box_scores_clean_100;

CREATE TABLE PLAYER_box_scores_clean_100 (
season INTEGER,
game_type TEXT,
date TEXT,
points REAL,
assists REAL,
rebounds REAL,
steals REAL,
blocks REAL,
turnovers REAL,
game_score REAL
);
""")

player = "PLAYER"
reg_raw = pd.read_csv(f"./regular/{player}_basic.csv")
reg_raw.to_sql(f"{player}_box_reg_raw", conn, if_exists='replace', index=False)
po_raw = pd.read_csv(f"./playoffs/{player}_basic.csv")
po_raw.to_sql(f"{player}_box_po_raw", conn, if_exists='replace', index=False)

conn.executescript(f"""
WITH games AS (
    SELECT 'regular' AS game_type, date, points_scored, assists, offensive_rebounds, defensive_rebounds,
           steals, blocks, turnovers, game_score, seconds_played
    FROM {player}_box_reg_raw
    UNION ALL
    SELECT 'playoffs' AS game_type, date, points_scored, assists, offensive_rebounds, defensive_rebounds,
           steals, blocks, turnovers, game_score, seconds_played
    FROM {player}_box_po_raw
)
INSERT INTO {player}_box_scores_clean_100
    (season, game_type, date, points, assists, rebounds, steals, blocks, turnovers, game_score)
SELECT p.season,
       g.game_type,
       g.date,
       g.points_scored * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       g.assists * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       (g.offensive_rebounds + g.defensive_rebounds) * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       g.steals * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       g.blocks * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       g.turnovers * (48.0 / (g.seconds_played / 60.0)) * (100.0 / p.Pace),
       g.game_score
FROM games AS g
JOIN team_pace AS p
ON g.date = p.date
WHERE g.seconds_played > 0
""")

print(pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn))
print(pd.read_sql(f"SELECT * FROM {player}_box_scores_clean_100 LIMIT 5", conn))
conn.commit()
conn.close()

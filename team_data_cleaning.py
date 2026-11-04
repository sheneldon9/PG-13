import sqlite3
import pandas as pd

conn = sqlite3.connect('PLAYER.db')

conn.executescript("""
DROP TABLE IF EXISTS team_pace;

CREATE TABLE team_pace (
season INTEGER,
tm TEXT,
date TEXT,
TmMP REAL,
TMPoss REAL,
OppPoss REAL,
Poss REAL,
PACE REAL
);
""")

seasons = range(START_YEAR, END_YEAR + 1)
for year in seasons:
    raw = pd.read_csv(f"./team_box/{year}.csv")
    raw.to_sql(f"team_box_raw_{year}", conn, if_exists='replace', index=False)

    conn.executescript(f"""
    WITH clean AS (
        SELECT date,
           team_team as Tm,
           team_minutes_played as TmMP,
           team_made_field_goals as TmFG,
           team_attempted_field_goals AS TmFGA,
           team_attempted_free_throws AS TmFTA,
           team_defensive_rebounds AS TmDRB,
           team_offensive_rebounds AS TmORB,
           team_turnovers as TmTOV,
           opponent_made_field_goals as OppFG,
           opponent_attempted_field_goals AS OppFGA,
           opponent_attempted_free_throws AS OppFTA,
           opponent_defensive_rebounds AS OppDRB,
           opponent_offensive_rebounds AS OppORB,
           opponent_turnovers as OppTOV
        FROM team_box_raw_{year}
    ),
    poss AS (
        SELECT date,
           Tm,
           TmMP,
           TmFGA + 0.4 * TmFTA - 1.07 * (1.0 * TmORB / (TmORB + OppDRB)) * (TmFGA - TmFG) + TmTOV AS TmPoss,
           OppFGA + 0.4 * OppFTA - 1.07 * (1.0 * OppORB / (OppORB + TmDRB)) * (OppFGA - OppFG) + OppTOV AS OppPoss
        FROM clean
    )
    INSERT INTO team_pace
    SELECT {year} AS season,
           Tm,
           date,
           TmMP,
           TmPoss,
           OppPoss,
           0.5 * (TmPoss + OppPoss) AS Poss,
           48.0 * (TmPoss + OppPoss) / (2.0 * (TmMP / 5.0)) AS Pace
    FROM poss;
    """)

print(pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn))
print(pd.read_sql("SELECT * from team_pace LIMIT 5", conn))
conn.commit()
conn.close()

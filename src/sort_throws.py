import pandas as pd
from paths import DATA_CSV, QB_CPOE_CSV
# helper function to simplify sort function
# removes plays with no passes and plays like sacks, two point conversions, NA air yards, etc...
# create columns for each zone
def filter_throws(df):
    df = df[
        (df["pass_attempt"] == 1)
        & (df["sack"] == 0)
        & (df["qb_spike"] == 0)
        & (df["two_point_attempt"] == 0)
        & (df["air_yards"].notna())
        & (df["pass_location"].notna())
        & (df["cpoe"].notna())
    ]
    cols = ["air_yards", "pass_location", "passer_player_name", "passer_player_id", "cpoe"]
    df = df[cols]
    df["depth"] = pd.cut(df["air_yards"], bins=[0, 10, 20, 100], labels=["short", "middle", "deep"], right=False)
    return df
def sort():
    qb_df = pd.read_csv(DATA_CSV, low_memory=False) # low_memory=False to get rid of the warning every time it runs
    qb_df = filter_throws(qb_df)
    qb_df_grouped = qb_df.groupby(["passer_player_id", "passer_player_name", "depth", "pass_location"], observed=True)["cpoe"]
    qb_cpoe = qb_df_grouped.agg(cpoe="mean", throws="count").reset_index() # Get the average CPOE for each zone and the throw count per zone, then reset index to make the index cols normal cols again
    qb_cpoe.to_csv(QB_CPOE_CSV, index=False)
    
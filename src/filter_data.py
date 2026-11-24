import pandas as pd
from paths import QB_CPOE_CSV
def filter(name): # where name is a string name (first, space, last) of the qb
    separated = name.split()
    first = separated[0]
    last = separated[1]
    first_initial = first[0]
    selected_qb_name = first_initial + "." + last
    qb_df = pd.read_csv(QB_CPOE_CSV)
    selected_qb_df = qb_df[qb_df["passer_player_name"] == selected_qb_name]
    return selected_qb_df
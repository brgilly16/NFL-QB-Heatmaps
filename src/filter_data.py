import pandas as pd
from paths import QB_CPOE_CSV
def filter(name): # where name is a string name (first, space, last) of the qb
    # Try-except block fixes issues with user input not being in the proper format
    try:
        separated = name.lower().split()
        first = separated[0]
        last = separated[1]
    except IndexError: 
            print("Please give the full name (First space Last e.g. Josh Allen) of the qb")
            return
    first_initial = first[0]
    selected_qb_name = first_initial + "." + last # match the form of passer_player_name in the data
    qb_df = pd.read_csv(QB_CPOE_CSV)
    qb_df["passer_player_name"] = qb_df["passer_player_name"].str.lower()
    selected_qb_df = qb_df[qb_df["passer_player_name"] == selected_qb_name]
    # check for multiple qb's filtered for, because previously Jayden Daniels and Jalon Daniels would be the same.
    # Now if multiple qb's are selected, it will check the display name from nflreadpy to find the desired qb
    if selected_qb_df["passer_player_id"].nunique() > 1:
        selected_qb_df = qb_df[qb_df["display_name"].str.lower() == " ".join(separated)] # check against separated list to avoid whitespaces causing issues
    if selected_qb_df.empty: # if there is no qb by the name inputted print the error message and return
        print(f"Couldn't find an NFL QB named {name}. Ensure that the name is in first name then last name order and that the name is of a current NFL QB.")
        return
    return selected_qb_df
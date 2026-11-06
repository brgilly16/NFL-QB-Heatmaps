import nflreadpy as nfl
import pandas as pd
def load():
    # load this season's play by play data from 
    data = nfl.load_pbp()
    # nflreadpy uses Polars and not pandas. Convert to pandas because I am more familiar with that
    df = data.to_pandas()
    df.to_csv("data/data.csv")

import nflreadpy as nfl
import pandas as pd
from paths import DATA_DIR, DATA_CSV
def load():
    # load this season's play by play data from nflreadpy
    data = nfl.load_pbp()
    # nflreadpy uses Polars and not pandas. Convert to pandas because I am more familiar with that
    data = data.to_pandas()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(DATA_CSV, index=False)

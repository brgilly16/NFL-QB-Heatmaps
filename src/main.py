from download_data import load
from sort_throws import sort
import os
if not os.path.exists("data/data.csv"):
    load()
if not os.path.exists("qb_cpoe.csv"):
    sort()
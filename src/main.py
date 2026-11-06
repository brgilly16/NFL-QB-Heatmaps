from download_data import load
import os
if not os.path.exists("data/data.csv"):
    load()

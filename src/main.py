from download_data import load
from sort_throws import sort
from paths import DATA_CSV, QB_CPOE_CSV
if not DATA_CSV.exists():
    load()
if not QB_CPOE_CSV.exists():
    sort()
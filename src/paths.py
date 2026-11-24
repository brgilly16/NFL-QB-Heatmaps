from pathlib import Path
# Central file paths for the project
# Paths are built from this file location so that the scripts work no matter where they are run from
ROOT = Path(__file__).resolve().parent.parent 
DATA_DIR = ROOT / "data" 
DATA_CSV = DATA_DIR / "data.csv"
QB_CPOE_CSV = DATA_DIR / "qb_cpoe.csv"
import argparse
from download_data import load
from sort_throws import sort
from paths import DATA_CSV, QB_CPOE_CSV
from filter_data import filter
from visualize_heatmap import visualize
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("qb", nargs="+", help="QB name (First space Last) e.g. Josh Allen")
    return parser.parse_args()
def main():
    args = getArgs()
    chosen_qb = " ".join(args.qb)
    try:
        if not DATA_CSV.exists():
            load()
        if not QB_CPOE_CSV.exists():
            sort()
    except ConnectionError:
        print("Couldn't download NFL data. Check your internet connection and try again.")
        return
    visualize(filter(chosen_qb))
if __name__ == "__main__":
    main()
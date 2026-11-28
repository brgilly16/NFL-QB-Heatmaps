import argparse
from download_data import load
from sort_throws import sort
from paths import DATA_CSV, QB_CPOE_CSV
from filter_data import filter
from visualize_heatmap import visualize
import matplotlib.pyplot as plt
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("qb", nargs="+", help="QB name (First space Last) e.g. Josh Allen")
    parser.add_argument("--compare", nargs="+", help="Second QB to compare, e.g. python main.py Patrick Mahomes --compare Josh Allen")
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
    if args.compare:
        chosen_comparison = " ".join(args.compare)
        if chosen_comparison.upper() == chosen_qb.upper(): # check for user putting the same QB twice and guard against it.
            print("Please choose two different QBs to compare.") 
            return
        visualize(filter(chosen_comparison))
    plt.show() # display both heatmaps at the same time.
if __name__ == "__main__":
    main()
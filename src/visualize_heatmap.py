import matplotlib.pyplot as plt
def visualize(df):
    # sometimes filter may return None if the input is wrong or something. In that case execution should be stopped.
    if df is None:
        return
    # adjustment for the compare feature. another way to implement the compare feature would have been to put both heatmaps on the same plot using plt.subplots and all the related tools that comes with that.
    # however, I am the main user for this project and I preferred the version of the feature that uses two separate plots, so that is the one I chose.
    plt.figure() 
    depths = ["short", "intermediate", "deep"]
    sides = ["left", "middle", "right"]
    # create the grid tables that are used to create the heatmap
    cpoe_table = df.pivot_table(index="depth", columns="pass_location", values="cpoe")
    throws_table = df.pivot_table(index="depth", columns="pass_location", values="throws", fill_value=0) 
    cpoe_table = cpoe_table.reindex(index=depths, columns=sides)
    throws_table = throws_table.reindex(index=depths, columns=sides, fill_value=0).astype(int)
    plt.imshow(cpoe_table, cmap="RdBu", vmin=-30, vmax=30, origin="lower") # create the heatmap. Origin=lower puts the short throws at the bottom because it is most similar to the POV of a QB looking downfield.
    plt.colorbar(label="CPOE")
    # add the numerical values and the number of throws to each zone
    for row in range(3):
        for col in range(3):
            cpoe = cpoe_table.iloc[row, col]
            throws = throws_table.iloc[row, col]
            if abs(cpoe) > 19: # change text color to white on darker backgrounds to make it easier to see
                text_color = "white"
            else:
                text_color = "black"
            plt.text(col, row, f"{cpoe:.2f}\n{throws} throws", ha="center", va="center", color=text_color)
    plt.xticks([0, 1, 2], ["Left", "Middle", "Right"])
    plt.yticks([0, 1, 2], ["Short (0-10 yards)", "Intermediate (10-20 yards)", "Deep (20+ yards)"])
    plt.title(df["display_name"].iloc[0] + " CPOE by Zone")  
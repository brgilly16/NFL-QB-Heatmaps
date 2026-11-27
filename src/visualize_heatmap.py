import matplotlib.pyplot as plt
def visualize(df):
    if df is None:
        return  
    depths = ["short", "intermediate", "deep"]
    sides = ["left", "middle", "right"]
    cpoe_table = df.pivot_table(index="depth", columns="pass_location", values="cpoe")
    throws_table = df.pivot_table(index="depth", columns="pass_location", values="throws", fill_value=0)
    cpoe_table = cpoe_table.reindex(index=depths, columns=sides)
    throws_table = throws_table.reindex(index=depths, columns=sides, fill_value=0).astype(int)
    plt.imshow(cpoe_table, cmap="RdBu", vmin=-30, vmax=30, origin="lower")
    plt.colorbar(label="CPOE")
    for row in range(3):
        for col in range(3):
            cpoe = cpoe_table.iloc[row, col]
            throws = throws_table.iloc[row, col]
            if abs(cpoe) > 19:
                text_color = "white"
            else:
                text_color = "black"
            plt.text(col, row, f"{cpoe:.1f}\n{throws} throws", ha="center", va="center", color=text_color)
    plt.xticks([0, 1, 2], ["Left", "Middle", "Right"])
    plt.yticks([0, 1, 2], ["Short (0-10 yards)", "Intermediate (10-20 yards)", "Deep (20+ yards)"])
    plt.title(df["display_name"].iloc[0] + " CPOE by Zone")
    plt.show()  
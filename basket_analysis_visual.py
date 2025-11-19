from basket_analysis_functions import *
import matplotlib.pyplot as plt



shopping_carts = (
    pd.read_csv('basket_analysis.csv')
    .pipe(remove_index_column)
    .pipe(listwise_deletion)
)


#returns how many TRUE values are in each column.
# How many baskets each item appears in.
def item_freq_bar_chart(data):
    item_counts = data.sum(axis=0)
    item_counts.sort_values(ascending=False).plot(kind='bar', figsize=(16,10))
    plt.ylabel("Basket Count")
    plt.title("Frequency of Each Item Across Baskets")
    plt.savefig("item_frequency_barchart.png", dpi=300, bbox_inches="tight")
    plt.show()



# runs function and exports a png of the graph to project folder
item_freq_bar_chart(shopping_carts)

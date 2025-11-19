import pandas as pd
import numpy as np
from basket_analysis_functions import model, listwise_deletion, remove_index_column

#read in and prep for the model
#dataset n=999 rows and p=16 item parameters
shopping_carts = (
    pd.read_csv('basket_analysis.csv')
    .pipe(remove_index_column)
    .pipe(listwise_deletion)
)

#creates support and confidence values to put in the model to see what creates the most/best rules.
supports = np.arange(0.1, 0.21, 0.05)
confidences = np.arange(0.30, 0.81, 0.05)
#initialize output hashmap
rules_dict = {}

# generates the association rules based on the parameters above and loops them all into one dictionary.
# however, it's now a dictionary of dataframes so they have to be combined into one large dataframe to be
# output as a csv.
for s in supports:
    for c in confidences:
        rules = model(shopping_carts, s, c)
        if not rules.empty:
            rules["min support"] = s
            rules["min confidence"] = c
            rules["pair"] = rules.apply(
                lambda x: "-".join(sorted(list(x["antecedents"] | x["consequents"]))),
                axis=1)
            #stores keys as tuples so I can iterate over them when setting up the csv.
            #holds metadata for what each value contains
            key = (s, c)
            rules_dict[key] = rules



# removes double counted entries. for example, if milk and chocolate are a pair,
# it'll remove chocolate and milk. It keeps the highest confidence version of the pair.
# The confidences are almost identical to 3 decimal places. after refining support and confidence values,
# another copy will be made to include the reciprocal pairs (demonstrated in report and presentation).
for key, df in rules_dict.items():
    df_sorted = df.sort_values(by=["confidence", "support"], ascending=False)

    # Drop duplicates by 'pair', keeping the strongest (highest confidence/support)
    #copies in place to avoid errors and headaches
    df_cleaned = df_sorted.drop_duplicates(subset="pair", keep="first").copy()

    # Convert frozensets to strings for readability in output
    df_cleaned["antecedents"] = df_cleaned["antecedents"].apply(lambda x: ", ".join(sorted(x)))
    df_cleaned["consequents"] = df_cleaned["consequents"].apply(lambda x: ", ".join(sorted(x)))

    # Store cleaned version back into the dictionary
    rules_dict[key] = df_cleaned


#combines all dictionary items into one df that can be exported easier. 2 because it was my 2nd try :)
combined_df2 = pd.concat(
    [df for df in rules_dict.values()],
    ignore_index=True)

#exports the whole thing to the project directory.
#more analysis can be done via excel.
combined_df2.to_csv("good_rule_outputs.csv", index=False)
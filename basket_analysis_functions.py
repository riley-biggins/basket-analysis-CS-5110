import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#drops the index column then returns the dataset as booleans,
#since that's what's preferred for apriori.
def remove_index_column(data):
    data.drop(data.columns[[0]], axis=1, inplace=True)  # drops index column
    return data.astype(bool)


#Remove rows with any missing values. The data was clean, but just to make sure.
def listwise_deletion(data):
    return data.dropna()


#function to find interesting associations
#inputs are MINIMUM values for each metric for them to qualify as noteable.
def model(data, support, confidence):
    #finds candidate pairs, which are the items that appear in more than "support" by percentage
    frequent_itemsets = apriori(data, min_support=support, use_colnames=True, max_len=2)

    # Generating association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=confidence)


    #conf(i ->j) = support(i -> j) / support(i), prob of j given i. Can be high sometimes with
    #frequent items. That's why we test with interest to see if j given i is higher than just P(j) itself.
    #find interesting rules using interest(i->j) = conf(i->j) - Pr[j].
    #chapter 6 assoc rules slide 14

    #add interest metric column
    rules['interest'] = rules['confidence'] - rules['consequent support']

    #sort rules by interest and return to main function.
    interesting_rules = rules.sort_values(by='interest', ascending=False)
    return interesting_rules




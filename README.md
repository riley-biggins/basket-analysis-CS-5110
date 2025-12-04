Market Basket Analysis Project
Frequent Itemset Mining and Association Rule Generation in Python
Overview

This project performs a market basket analysis on transactional shopping cart data. It uses the Apriori algorithm to identify frequent item pairs and then generates association rules based on minimum support and confidence thresholds. The goal is to determine which items commonly appear together in customer baskets and to rank these associations using additional interest metrics.

The codebase is organized into three Python files:
basket_analysis_functions.py – data cleaning functions and the main model definition
basket_analysis_main.py – runs the mining process across multiple support and confidence thresholds, removes duplicate rules, and exports results
basket_analysis_visual.py – generates a bar chart for individual items and exports it to project folder.
All final rule outputs are exported as CSV files for further analysis or dashboard creation in tools like Power BI or Tableau.


Instructions for running: 
This repo includes all the files needed to execute this for yourself. By putting all of these files into the same project directory and running the
main function, it will reference what it needs from the function file. The bar chart needs to be run seperately, but it should be in the same code base. 
It will show the bar chart on the screen and also export it to the file location / project directory.

How It Works:
The dataset is cleaned by:
Removing an index column
Converting item indicators to boolean
Dropping any rows containing missing values


Frequent Itemset and Rule Mining:
The Apriori algorithm (from mlxtend) is used with a specified minimum support to find frequent item pairs. Association rules are then extracted with a minimum confidence threshold. The project also computes an interest score:

interest = confidence - consequent_support

Rules are sorted by interest to highlight associations that exceed what would be expected by chance.

Duplicate Rule Removal:
Since the project focuses on undirected co-occurrence (A & B appear together), symmetrical rules such as A → B and B → A are duplicates. Only the version with the higher confidence (and support) is kept. This makes the final dataset easier to interpret and avoids double-counting pairs.

Output:
For each support–confidence combination, results are stored in a dictionary keyed by (support, confidence). All rule data frames are cleaned, merged, and exported as a final CSV. Item frequencies are also visualized and saved as a PNG.

File Descriptions:
basket_analysis_functions.py

Contains:
remove_index_column()
listwise_deletion()
model() – generates frequent itemsets, rules, computes interest, and returns the sorted rules


basket_analysis_main.py

Handles:
Dataset loading and preprocessing
Iterating over support and confidence values
Storing rules in a dictionary
Removing reciprocal duplicates
Converting frozensets to readable strings
Consolidating all rule outputs and saving to CSV

basket_analysis_visual.py

Produces:
A bar chart showing how many baskets contain each item
Saves visualization as a PNG file

Author:
Created by Riley B. for CS 5110. The project demonstrates a complete pipeline for association rule mining, from data cleaning through rule generation, post-processing, and visualization.

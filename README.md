# Market Basket Analysis with Apriori Algorithm

This project implements association rule mining on a market basket dataset using the Apriori algorithm. The application is developed in Python and includes a user interface built with PyQt6.

## Overview

Market Basket Analysis is a powerful data mining technique used to discover associations between items frequently purchased together by customers. The Apriori algorithm is a classic approach that efficiently identifies frequent itemsets, enabling the generation of meaningful association rules.

## Features

1. **Apriori Algorithm:** The core of the project includes the implementation of the Apriori algorithm to find frequent itemsets.

2. **Association Rule Mining:** The algorithm generates association rules with metrics such as confidence, support, and lift to measure the significance of the rules.

3. **Market Basket Dataset:** The application supports the loading and analysis of market basket datasets in CSV or compatible formats.

4. **User Interface:** A user-friendly interface built with PyQt6 allows users to interact with the algorithm and visualize the results.

## How to Run

1. Clone the repository: `git clone https://github.com/Shalaby1022/Association-Rule.git`
2. Install the required dependencies: `pip install PyQt6 pandas`
3. Run the application: `python main.py`
4. Load your market basket dataset, set the parameters, and initiate the analysis.

## Usage

1. **Import Dataset:** Import your market basket data in CSV format or any other compatible format.

2. **Set Parameters:** Set the minimum support and confidence values for the association rule mining.

3. **Run Analysis:** Initiate the Apriori algorithm to discover frequent itemsets and association rules.

4. **View Results:** The application displays the discovered rules and their associated metrics for further analysis.

## Dependencies

- Python 3.9.6
- PyQt6 6.1.0
- pandas

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

class AssociationRuleAnalyzerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Association Rule Analyzer")
        self.create_widgets()

    def create_widgets(self):
        # Create the "Upload Dataset" button and text area
        self.upload_button = tk.Button(self.window, text="Upload Dataset", command=self.upload_dataset)
        self.upload_button.pack(pady=10)

        self.uploaded_file_text = tk.Text(self.window, height=1, width=50)
        self.uploaded_file_text.pack()

        # Create the "Analyze" button and text area
        self.analyze_button = tk.Button(self.window, text="Analyze", command=self.analyze_dataset)
        self.analyze_button.pack(pady=10)

        self.results_text = tk.Text(self.window, height=25, width=110)
        self.results_text.pack()


        # Make the GUI resizable
        self.window.resizable(True, True)

    def upload_dataset(self):
        file_path = filedialog.askopenfilename()

        # Load the dataset
        self.df = pd.read_csv(file_path)
        self.uploaded_file_text.delete(1.0, tk.END)
        self.uploaded_file_text.insert(tk.END, file_path)

    def preprocess_dataset(self):
        # Convert the dataset into a suitable format for association rule analysis
        self.basket = []

        for row in self.df.iterrows():
            transaction = [item for item in row[1] if pd.notnull(item)]
            self.basket.append(transaction)

    def analyze_dataset(self):
        # Perform association rule analysis
        self.preprocess_dataset()

        te = TransactionEncoder()
        te_ary = te.fit_transform(self.basket)
        df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

        frequent_itemsets = apriori(df_transformed, min_support=0.009, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

        # Build the output string
        output = "Most Frequent Items:\n"
        output += str(frequent_itemsets) + "\n\n"

        accepted_rules = rules[rules['confidence'] >= 0.3]

        output += f"Number of Accepted Rules (with confidence >= 0.9): {len(accepted_rules)}\n\n"

        for i, itemset in frequent_itemsets.iterrows():
            support = itemset['support']
            output += f"Accepted Rules for Itemset: {set(itemset['itemsets'])} (Support: {support:.2f})\n"

            itemset_rules = accepted_rules[accepted_rules['antecedents'] == itemset['itemsets']]

            for j, rule in itemset_rules.iterrows():
                output += f"{set(rule['antecedents'])} => {set(rule['consequents'])} (Confidence: {rule['confidence']:.2f})\n"

            output += "\n"

        # Clear the text area and update the output
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, output)

        # Create a vertical scroll bar for the text area
        scroll_bar = tk.Scrollbar(self.window)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the text area to use the scroll bar
        self.results_text.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.results_text.yview)

    def run(self):
        self.window.mainloop()

# Create an instance of the AssociationRuleAnalyzerGUI class and run the GUI
analyzer = AssociationRuleAnalyzerGUI()
analyzer.run()

# Import libraries
import os
import pandas as pd
 
# Path to CSV file
budget_pathway = os.path.join("Resources", "budget_data.csv")
 
# Put CSV file in pandas DataFrame
df = pd.read_csv(budget_pathway)

# Total number of months
total_months = len(df)
 
# Total "Profit/Losses"
net_total = df['Profit/Losses'].sum()
 
# "Profit/Losses" over entire period
df['Profit_Change'] = df['Profit/Losses'].diff()
 
# Average change
average_change = df['Profit_Change'].mean()
 
# Greatest increase in profits
greatest_increase = df.loc[df['Profit_Change'].idxmax()]
 
# Greatest decrease in profits
greatest_decrease = df.loc[df['Profit_Change'].idxmin()]
 
# Prepare the results
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit_Change']:.0f})
Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit_Change']:.0f})
"""
 
# Print results to console
print(results)
 
# Create output directory
output_dir = "Analysis"
os.makedirs(output_dir, exist_ok=True)
 
# Write results to text file
output_path = os.path.join(output_dir, "financial_analysis.txt")
with open(output_path, 'w') as output_file:
    output_file.write(results)
 
print(f"Results have been saved to {output_path}")
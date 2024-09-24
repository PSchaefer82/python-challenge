# Necessary libraries
import os
import pandas as pd
 
# Set the path to the CSV file
poll_pathway = os.path.join("Resources", "election_data.csv")
 
# Read CSV file to pandas DataFrame
df = pd.read_csv(poll_pathway)
 
# Total number of votes
total_votes = len(df)
 
# Count votes of each candidate
candidate_votes = df['Candidate'].value_counts()
 
# Calculate percentage of votes for each candidate
percentages = (candidate_votes / total_votes) * 100
 
# Find the winner
winner = candidate_votes.idxmax()
 
# Prepare the results string
results = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
 
for candidate, votes in candidate_votes.items():
    results += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"
 
results += f"""-------------------------
Winner: {winner}
-------------------------
"""
 
# Print results
print(results)
 
# Create output directory
output_dir = "Analysis"
os.makedirs(output_dir, exist_ok=True)
 
# Write results to text file
output_path = os.path.join(output_dir, "election_results.txt")
with open(output_path, 'w') as output_file:
    output_file.write(results)
 
print(f"Results have been saved to {output_path}")
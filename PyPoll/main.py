# Importing essential modules
import os 
import csv

# Specify the file path
election_data = os.path.join("Resources", "election_data.csv")


total_votes = 0
candidates = []
vote_percentage= []
candidate_votes = []


with open(election_data, encoding = "utf-8") as election_csv:
    csv_reader = csv.reader(election_csv, delimiter = ",")
    csv_header = next(election_csv)

    for row in csv_reader:
        
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
    
    for i in candidate_votes:
        percentage = (i / total_votes) * 100
        percentage = "%.3f%%" % percentage
        vote_percentage.append(percentage)

    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    election_winner = candidates[index]

# Print the analysis output
print(i)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for j in range(len(candidates)):
    print(f"{candidates[j]}: {str(vote_percentage[j])} ({str(candidate_votes[j])})")
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

# Export as teext file
analysis_results = os.path.join("Analysis", "analysis_results.txt")

with open(analysis_results, "w") as txt:
    txt.write("Election Results""\n")
    txt.write("-------------------------""\n")
    txt.write(f"Total Votes: {str(total_votes)}""\n")
    txt.write("-------------------------""\n")
    for j in range(len(candidates)):
        txt.write(f"{candidates[j]}: {str(vote_percentage[j])} ({str(candidate_votes[j])})""\n")
    txt.write("-------------------------""\n")
    txt.write(f"Winner: {election_winner}""\n")
    txt.write("-------------------------""\n")

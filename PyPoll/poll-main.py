## PyPoll

# ![Vote Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv 

file_path = 'Resources/election_data.csv'

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_votes +=1
        if row[2] == 'Khan':
            khan_votes +=1
        elif row[2] == 'Correy':
            correy_votes +=1
        elif row[2] == 'Li':
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

candidates = ["Khan","Correy","Li","O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

dict_candidates_and_votes = dict(zip(candidates, votes))
winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (otooley_votes/total_votes) *100

print(f'Election Results')
print(f'------------------------')
print(f'Total Votes: {total_votes}')
print(f'------------------------')
print(f'Khan: {khan_percent:.3f}% ({khan_votes})')
print(f'Correy: {correy_percent:.3f}% ({correy_votes})')
print(f'Li: {li_percent:.3f}% ({li_votes})')
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f'------------------------')
print(f'Winner: {winner}')
print(f'------------------------')

output_file = 'Analysis/Election_Results.txt'

with open(output_file,'w') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")

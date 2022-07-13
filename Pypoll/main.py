import math
import os
import csv


csvpath = os.path.join("Resources", "election.csv")
txtpath = os.path.join("Analysis", "analysis.txt")


id = []
votes = {}

with open (csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile, fieldnames=['id', 'county', 'candidate'], delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        id.append(row['id'])
        c = row['candidate']
        if c in votes.keys():
            votes[c] += 1
        else:
            votes[c] = 1

# The total number of votes cast
total_votes = sum(votes.values())
# A complete list of candidates who received votes
candidates = votes.keys()
# The percentage of votes each candidate won
percents = {}
for c in candidates:
    percents[c] = votes[c] / total_votes
# The total number of votes each candidate won
votes
# The winner of the election based on popular vote
winner = None
winner_votes = 0
for c in candidates:
    if votes[c] > winner_votes:
        winner  = c
        winner_votes = votes[c]

with open(txtpath, 'w') as txt:
    txt.write(f'Election Results\n')
    txt.write(f'----------------------------------------\n')
    txt.write(f'Total Votes: {total_votes}\n')
    txt.write(f'----------------------------------------\n')
    for c in candidates:
        txt.write(f'{c}: {percents[c] * 100  : 2.2f}% ({votes[c]})\n')
    txt.write(f'----------------------------------------\n')
    txt.write(f'Winner: {winner}\n')






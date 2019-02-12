# ## PyPoll

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#   (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't 
#   what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is 
#   composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes
#   the votes and calculates each of the following:

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

import csv

csv_path = (r"C:\Users\ryanz\Desktop\Data Analytics Bootcamp\Resources\RICH201901DATA3\03-Python\Homework\Instructions\PyPoll\Resources\election_data.csv")

pollData = []

with open(csv_path, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    pollData.append(csv_header)
    
    for row in csvreader:
        pollData.append(row)

# The total number of votes cast

print(f"Election Results:")
print("-----------------------------")

total_votes = 0

for row in pollData[1:]:
    total_votes += 1
print(f"Total Votes: {total_votes}")
print("-----------------------------")

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

cand_list = {}
for row in pollData[1:]:
    if row[2] not in cand_list:
        cand_list[row[2]] = {}
        cand_list[row[2]]["cand_votes"] = 1
        cand_list[row[2]]["perc_votes"] = cand_list[row[2]]["cand_votes"]/total_votes
    else:
        cand_list[row[2]]["cand_votes"] += 1
        cand_list[row[2]]["perc_votes"] = cand_list[row[2]]["cand_votes"]/total_votes

for key in cand_list:
    print(key + ": " + str(format(cand_list[key]["cand_votes"])) + " (" + str(format(cand_list[key]["perc_votes"],".3%")) + ") ")


# The winner of the election based on popular vote.
most_votes = 0
winner_name = ""

for name in cand_list:
    if cand_list[name]["cand_votes"] > most_votes:
        most_votes = cand_list[name]["cand_votes"]
        winner_name = name

print("-----------------------------")     
print(f"Winner: {winner_name}"
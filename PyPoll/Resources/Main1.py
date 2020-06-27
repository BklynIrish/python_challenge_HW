# ## PyPoll

# ![Vote Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes casted

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


csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Analysis","election_analysis.txt")
with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    print(header,"\n\n")
    
    #variables
    khan_votes = 0
    khan_percent = 0.00
    correy_votes = 0
    correy_percent = 0.00
    li_votes = 0
    li_percent = 0.00
    otooley_votes = 0
    otooley_percent = 0.00
    winner_votes = 0
    total_votes = 0
    winner = ""

    for row in csvreader:
        total_votes = total_votes + 1
        if(row[2] == "Khan"): 
            khan_votes = khan_votes + 1
        elif (row[2] == "Correy"): 
            correy_votes = correy_votes + 1
        elif (row[2] == "Li"): 
            li_votes = li_votes + 1
        elif (row[2] == "O'Tooley"): 
            otooley_votes = otooley_votes + 1

#Percentages of each person on ballot
khan_percent = khan_votes / total_votes * 100
correy_percent = correy_votes / total_votes * 100
li_percent = li_votes / total_votes * 100
otooley_percent = otooley_votes / total_votes * 100
# type out the winner
winner_votes = max(khan_votes, correy_votes, li_votes, otooley_votes)
if(winner_votes == khan_votes):
    winner = "Khan"
elif(winner_votes == correy_votes):
    winner = "Correy"
elif(winner_votes == li_votes):
    winner = "Li"
else:
    winner = "O'Tooley"

#print (total_votes)


print(f"Election Results")
print(f"---------------------------")
print(f"Total votes: {str(total_votes)}")
print(f"---------------------------")
print(f"Khan: {str(round(khan_percent,3))}% ({str(khan_votes)})")
print(f"Correy: {str(round(correy_percent,3))}% ({str(correy_votes)})")
print(f"Li: {str(round(li_percent,3))}% ({str(li_votes)})")
print(f"O'Tooley: {str(round(otooley_percent,3))}% ({str(otooley_votes)})")
print(f"---------------------------")
print(f"Winner: {str(winner)}")
print(f"\n---------------------------")
    
with open(pathout, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total votes: {str(total_votes)}\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Khan: {str(round(khan_percent,3))}% ({str(khan_votes)})\n")
    txt_file.write(f"Correy: {str(round(correy_percent,3))}% ({str(correy_votes)})\n")
    txt_file.write(f"Li: {str(round(li_percent,3))}% ({str(li_votes)}\n)")
    txt_file.write(f"O'Tooley: {str(round(otooley_percent,3))}% ({str(otooley_votes)})\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Winner: {str(winner)}\n")
    txt_file.write(f"\n---------------------------")

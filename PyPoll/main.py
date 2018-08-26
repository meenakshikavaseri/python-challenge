import os
import csv
csvpath= os.path.join(".","Resources","election_data.csv")
#You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
counter = 0
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   csv_header = next(reader)
   for Cols in reader:
       counter = counter+1
#print(counter)
   

# A complete list of candidates who received votes
# CandidateList=[]
# with open(csvpath, newline="") as csvfile:
#    reader = csv.reader(csvfile,delimiter=',')
#    csv_header = next(reader)
#    for Cols in reader:
#        Candidate=Cols[2]
#        if Candidate not in CandidateList:
#            CandidateList.append (Candidate)
# print(CandidateList)

# The percentage of votes each candidate won
CandidateList=[]
VotecountList=[]
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   csv_header = next(reader)
   for Cols in reader:
        Candidate=Cols[2]
        if Candidate not in CandidateList:
           CandidateList.append (Candidate)
           VotecountList.append (1)
        else:
            #increement corresponding value in 
            #votecount list
            candidateIndex = CandidateList.index(Candidate) 
            countValue = VotecountList[candidateIndex]
            countValue = countValue + 1

            VotecountList[candidateIndex] = countValue

#print(CandidateList)
#print(VotecountList)

# The percentage of votes each candidate won
# this would be the number of vote per candidate/tot count * 100
maxWinningPercent = 0
maxWinningIndex = -1

print("-------------------------")
print ("Election Results")
print("-------------------------")
print("Total Votes: "+ str(counter)) 
print("-------------------------")

for candName in CandidateList:
    
    candidateIndex = CandidateList.index(candName) 
    countValue = VotecountList [candidateIndex]
    votePercent = (countValue/counter) * 100
    print(candName + ":" + str(round(votePercent,2)) + "% (" + str(countValue) + ")")
    if ( votePercent > maxWinningPercent):
        maxWinningPercent = votePercent
        maxWinningIndex = candidateIndex


print("-------------------------")
print("Winner: " + CandidateList[maxWinningIndex])
print("-------------------------")

#write to text file
with open("Output.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("----------------------------\n")
    text_file.write("Total Votes: {0}\n".format(counter))
    text_file.write("----------------------------\n")
    for candName in CandidateList:
    
        candidateIndex = CandidateList.index(candName) 
        countValue = VotecountList [candidateIndex]
        votePercent = (countValue/counter) * 100
        text_file.write(candName + ":" + str(round(votePercent,2)) + "% (" + str(countValue) + ")\n")
        if ( votePercent > maxWinningPercent):
            maxWinningPercent = votePercent
            maxWinningIndex = candidateIndex

    text_file.write("----------------------------\n")
    text_file.write("Total Votes:" +  CandidateList[maxWinningIndex] + "\n")
    
 

# The total number of votes each candidate won

# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


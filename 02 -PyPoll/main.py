'''Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''
import os
import csv
import sys

#identify path to elecation csv file,read csv file
election_data =os.path.join("02 -PyPoll", "01 - Resouces", "election_data.csv")

#create list for columns in csv file
voterID = [] 
county = []
candidate = [] 


with open(election_data,'r',encoding ='utf-8') as input_file:
    csvreader = csv.reader(input_file)

    next(csvreader) #skip header

    #create list 
    for r in csvreader:
        voterID.append(r[0])
        county.append(r[1])
        candidate.append(r[2])



#find unique list of candidates 
candidatelist = list(set(candidate))

#print(candidatelist)

#create lists for total votes and % 
candidatevotes = []
percentage = [] 

#find values for total votes and % with for loop

for h in candidatelist:
    candidatevotes.append((candidate.count(h)))
    percentage.append((candidate.count(h))/(len(voterID))*100)

#candidate with most votes = winner
winner = max(set(candidate),key = candidate.count)


#print results in terminal 
print('Election Results')
print('-------------------------')
#total number of votes using len
print('Total Votes:', len(voterID))
print('-------------------------')
#print list of candiates,% and count 
for x in range(len(candidatelist)):
    candidate_name = str(candidatelist[x])
    candidate_percent =str(round(percentage[x],3))
    candiate_vote = str(​​candidatevotes[x])

    print(candidate_name + candidate_percent + candidate_votes)
#print(f"{​​​(candidatelist[x]:) + (​​​round(percentage[x],3)00%) + (​​candidatevotes[x])}")
#print winner
print("Winner:",winner)
print('-------------------------')
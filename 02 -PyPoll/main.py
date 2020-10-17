#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

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

#total number of votes using len
#totalvotes = 

print('Total Votes:', len(voterID))
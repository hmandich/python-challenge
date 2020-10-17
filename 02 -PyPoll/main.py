#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv
import sys


#identify path to elecation csv file,read csv file
election_data =os.path.join("01 - Resouces", "election_data.csv")
with open(election_data,'r',encoding ='utf-8') as input_file:
    csvreader = csv.reader(input_file)

    next(csvreader)
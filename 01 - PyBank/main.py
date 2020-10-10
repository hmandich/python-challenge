import os
import csv

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

net_amount = []
month_count = []
change =[]


budget_data =os.path.join("01 - PyBank","01 - Resouces", "budget_data.csv")
with open(budget_data,'r') as input_file:
    csvreader = csv.reader(input_file)

    next(csvreader)
#Count column 0 to get number of months, sum coloumn 1 to get revenue
    for r in csvreader:
        month_count.append(r[0])
        net_amount.append(float(r[1]))
        #net_amount += revenue
        
#Print script in terminal
print("Financial Analysis")
print("------------------------------")
print("Total Months:",len(month_count))
print("Total: $",sum(net_amount))
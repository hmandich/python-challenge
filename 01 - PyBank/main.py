import os
import csv

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

net_amount = []
month_year = []
change =[]

#identify path to budget csv file,read csv file
budget_data =os.path.join("01 - PyBank","01 - Resouces", "budget_data.csv")
with open(budget_data,'r') as input_file:
    csvreader = csv.reader(input_file)

    next(csvreader)#skip title row
#count column 0 to get number of months, sum coloumn 1 to get revenue
    for r in csvreader:
        month_year.append(r[0])
        net_amount.append(float(r[1]))
        
#calculated difference of net amount, found total change + min and max change 
    for h in range(1,len(net_amount)):
        change.append(net_amount[h] - net_amount[h-1])
        avg_change = sum(change)/len(change)
        max_change = max(change)
        min_change = min(change)

        max_change_wmonth = str(month_year[change.index(max(change))])
        min_change_wmonth = str(month_year[change.index(min(change))])


#Print script in terminal
print("Financial Analysis")
print("------------------------------")
print("Total Months:",len(month_year))
print("Total: $",sum(net_amount))
print("Average  Change: $",round(avg_change,2))
print("Greatest Increase in Profits:",max_change_wmonth,"($",round(max_change),")")
print("Greatest Decrease in Profits:",min_change_wmonth,"($",round(min_change),")")

#print(min_change)
#print(max_change)
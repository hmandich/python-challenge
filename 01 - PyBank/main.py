import os
import csv
import sys



#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#lists to store data
revenue = []
month_year = []
change =[]

#identify path to budget csv file,read csv file
budget_data =os.path.join("01 - PyBank","01 - Resouces", "budget_data.csv")

with open(budget_data,'r',encoding='utf-8') as input_file:
    csvreader = csv.reader(input_file,delimiter=",")
    next(csvreader,None)#skipheader
#count column 0 to get number of months, sum coloumn 1 to get revenue
    for r in csvreader:
        month_year.append(r[0])
        revenue.append(float(r[1]))


#calculated difference of net amount, found total change + min and max change 
    for h in range(1,len(revenue)):
        change.append(revenue[h] - revenue[h-1])
        avg_change = sum(change)/len(change)
        max_change = max(change)
        min_change = min(change)

        max_change_wmonth = str(month_year[change.index(max(change))])
        min_change_wmonth = str(month_year[change.index(min(change))])

#print(max_change_wmonth)
#print(avg_change)
#print(max_change)
#print(min_change)


#Print script in terminal
print("Financial Analysis")
print("------------------------------")
print("Total Months:",len(month_year))
print("Total: $",sum(revenue))
print("Average  Change: $",round(avg_change,2))
print("Greatest Increase in Profits:",max_change_wmonth,"($",round(max_change),")")
print("Greatest Decrease in Profits:",min_change_wmonth,"($",round(min_change),")")

#create txt file

stdoutOrigin=sys.stdout 
sys.stdout = open("PyBank_Analysis.txt", "w")

print("Financial Analysis")
print("------------------------------")
print("Total Months:",len(month_year))
print("Total: $",sum(revenue))
print("Average  Change: $",round(avg_change,2))
print("Greatest Increase in Profits:",max_change_wmonth,"($",round(max_change),")")
print("Greatest Decrease in Profits:",min_change_wmonth,"($",round(min_change),")")

sys.stdout.close()
sys.stdout=stdoutOrigin

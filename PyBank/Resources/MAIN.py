# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
# composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting 
# so the records are simple.)
#  * Your task is to create a Python script that analyzes the records to calculate each of the following:
#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * The average of the changes in "Profit/Losses" over the entire period
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
    #* As an example, your analysis should look similar to the one below:

# ```text
#  Financial Analysis

import os
import csv 

csvpath = os.path.join(".","Resources","budget_data.csv")
pathout = os.path.join("Analysis","budget_analysis.txt")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader) #in this case reads the first row header row, if there were more it would iterate through them 

    # make empty lists for the requested data listed above. The header line is also a list stating what each items 
    # separated by a comma is equal to such as dates, namely months, and profits.  We make more lists to procure other values
    # such as, the sum of all of the profits, the average of profits, greatest increase in profits (date and amount) over the 
    # entire period, and the greatest decrease in losses (date and amount) over the entire period

    month = []
    profit = []
    profit_change = []
    avg_change = []
    netprofit = 0
    print(f"Header: {csv_header}")               

# to add the first item in the 1st row so row[0] would be the date---> rows[0] as months, 
# and profit/losses is the 2nd item (row[1]) and print the length of row[0] or month to 
# get the total amount of months which happen to be 86      
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
        netprofit = netprofit + int(row[1])
    print(len(month))
    print(netprofit)
    
 # average change in profit. the reason for the range(len(profit)-1) is because the length of a row 
 # or column will always be 1 greater than data structure's total indices; as row[0] is the 1st item  
    
    i = 0
    for i in range(len(profit) - 1):
        profit_loss = int(profit[i+1]) - int(profit[i])
 # add the above profit_loss to list defined above 
        profit_change.append(profit_loss)
    Total = sum(profit_change)
    #print(Total)
    #print(profit_change)
    #print(len(profit_change)) and it said 85
    print(Total / len(profit_change))
        
# Greatest Increase over entire period and Date it occurred

profit_increase = max(profit_change)
print(profit_increase)
k = profit_change.index(profit_increase)  #i don't know if this is necessary
month_increase = month[k+1]
print(month_increase)
     
# Greatest Decrease over entire period and Date it occurred

profit_decrease = min(profit_change)
print(profit_decrease)    
j = profit_change.index(profit_decrease) #i don't know if this is necessary
month_decrease = month[j+1]
print(month_decrease)
print('\n\n')

#Print Statements as requested to appear via the instruction

print(f'Financial Analyses')
print(f'----------------------------'+'\n')
print("Total number of months: ",len(month))
print("Total Profit over Period: $",netprofit)
print("Total Avg. in Profits/Losses over period: $",Total / len(profit_change))
print("Greatest Profit Increase and Month and Year it occurrred: $",profit_increase, month_increase)
print("Greatest Decrease in Profit and Month and Year it occurred: $",profit_decrease, month_decrease)
print('\n\n\n')

with open(pathout, "w") as txt_file:
    txt_file.write(f"Brandon McDermott\n\n\n")
    txt_file.write(f"Financial Analyses")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total number of months: {len(month)}\n")
    txt_file.write(f"Total Profit over Period: ${netprofit}\n")
    txt_file.write(f"Total Avg. in Profits/Losses over period: ${Total} / {len(profit_change)}\n")
    txt_file.write(f"Greatest Profit Increase and Month and Year it occurrred: ${profit_increase} ({month_increase})\n")
    txt_file.write(f"Greatest Decrease in Profit and Month and Year it occurred: ${profit_decrease} ({month_decrease})\n")
    txt_file.write(f'\n\n\n')

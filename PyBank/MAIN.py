import os
import csv 
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
# composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting 
# so the records are simple.)

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset

# * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period

    #* As an example, your analysis should look similar to the one below:

# ```text
#  Financial Analysis

csvpath = os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

    # make empty lists for the requested data listed above. The header line is also a list stating what each items 
    # separated by a comma is equal to such as dates, namely months, and revenues.  We make more lists to procure other values
    # such as, the sum of all of the revenues, the average of revenues, greatest increase in profits (date and amount) over the 
    # entire period, and the greatest decrease in losses (date and amount) over the entire period

    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    avg_change = []
    
    print(f"Header: {csv_header}")               

# to add the first item in the 1st row---> rows[0] as months, and add revenue as the 2nd item (row[1]) and print the 
# length of row[0] or month to get the total amount of months which happen to be 86      
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 # set revenue as an integer now so it remains that way when we use change in revenue
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 # average change in revenue. the reason for the range(len(revenue)-1) is because the length of a row 
 # or column will always be 1 greater than data structure's total indices; as row[0] is the 1st item in
 # lines 20-21 so their are 
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    avg_change = Total / len(revenue_change)
    print(avg_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average change in Revenue : $" + str(avg_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
 
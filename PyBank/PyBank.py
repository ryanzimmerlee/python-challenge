# # Unit 3 | Assignment - Py Me Up, Charlie

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv

csv_path = (r"C:\Users\ryanz\Desktop\Data Analytics Bootcamp\Resources\RICH201901DATA3\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv")

myData = []

with open(csv_path, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    myData.append(csv_header)
    
    for row in csvreader:
        myData.append(row)

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period

total_month = 0
total_pl = 0

for row in myData[1:]:
    total_month += 1
    total_pl += int(row[1])

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_month}")
print(f"Total ${total_pl}")
        
# The average of the changes in "Profit/Losses" over the entire period

cum_chg = 0

# Extract the P/L values by themselves
pl_list = [int(b) for a, b in myData[1:]]

# List Comprehension
# Zip the list to itself with an offset of 1 in order to get an offset list
# In doing so, you create 1 new value list by subtracting the second value in the list to the first value
valchg_list = [x - y for x , y in zip(pl_list[1:],pl_list)]

# Divide the sum of the value change list by the length of the value change list - the value chg list will give you 85
# Length of a list will count the number of iterations...where as length of a text item will give you length of the object
avgchg = sum(valchg_list)/len(valchg_list)

print(f"Average Change: ${round(avgchg, 2)}")

month_list = [i for i, j in myData[1:]]
month_chg_list = [i for i in zip(month_list[1:], valchg_list)]

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
for row in month_chg_list:
    if row[1] == max(valchg_list):
        gr_incmonth = row[0]
        gr_incval = row[1]
    if row[1] == min(valchg_list):
        gr_decmonth = row[0]
        gr_decval = row[1]

    
print(f"Greatest Increase in Profits: {gr_incmonth} (${gr_incval})")
print(f"Greatest Decrease in Profits: {gr_decmonth} (${gr_decval})")


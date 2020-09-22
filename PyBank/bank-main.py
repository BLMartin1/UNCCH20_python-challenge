# PyBank
# ![Revenue](Images/revenue-per-lead.png)
# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
#  You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

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

import os
import csv

file_path = 'Resources/budget_data.csv'

print(f'Financial Analysis')
print(f'------------------------')

total_months = []
total_profit = []
average_change = []
average_change_result = 0
previous_pl = 0
running_max = 0
running_max_list = []
# Number of months
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        total_months.append(row[0])
# Total profit
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_profit.append(int(row[1]))

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        value = int(row[1])
        if previous_pl != 0:
            average_change.append(value-previous_pl)
        previous_pl = int(row[1])

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row[0] in csvreader:
        date = row[0]
        if str:
            running_max_list.append(date)
    for row[1] in running_max_list:
        values = float(row[1])
        running_max_list.append(values)

        

print(running_max_list)
# print(sum(average_change))
# print(len(total_months))   
# average_change_result = sum(average_change)/len(total_months)
# print(f'Total Months: {len(total_months)}')
# print(f'Total: ${sum(total_profit)}')
# print(f'Average Change: ${float(average_change_result)}')
# # print(f'Greatest Increase: {running_max_date} {running_max}')
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
running_max = float('-inf')
running_max_date = ''
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
        running_max = max(csvreader['Profits/Losses'])
        running_max_date = row[0]
    

print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(total_profit)}')
print(f'Average Change: ${int(sum(total_profit)/len(total_profit))}')
print(f'Greatest Increase: {running_max_date} {running_max}')
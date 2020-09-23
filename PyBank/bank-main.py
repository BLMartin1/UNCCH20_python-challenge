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

total_months = []
total_profit = []
monthly_profit_change = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(int(total_profit[i+1])-int(total_profit[i]))

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

print(sum(total_profit))
print('Finanical Analysis')
print('------------------------')
print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(total_profit)}')
print(f'Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')
print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${str(max_increase_value)})')
print(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${str(max_decrease_value)})')

output_file = "Analysis/Financial_Analysis_Summary.txt"

with open(output_file,"w") as file:
     file.write("Financial Analysis")
     file.write("\n")
     file.write("----------------------------")
     file.write("\n")
     file.write(f"Total Months: {len(total_months)}")
     file.write("\n")
     file.write(f"Total: ${sum(total_profit)}")
     file.write("\n")
     file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
     file.write("\n")
     file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
     file.write("\n")
     file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
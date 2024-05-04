# Importing essential modules
import os 
import csv

# Specify the file path
budget_data = os.path.join("Resources", "budget_data.csv")

total_months = []
total_profit_loss = []
change = []

# Read csv file
with open(budget_data, encoding = "utf-8") as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter = ",")
    csv_header = next(budget_csv)
    
    for row in csv_reader:
        total_months.append(row[0])
        total_profit_loss.append(int(row[1]))
    
    for i in range(len(total_profit_loss) - 1):
        change.append(total_profit_loss[i + 1] - total_profit_loss[i])


greatest_increase_date = change.index(max(change)) + 1
greatest_increase_amount = max(change)

greatest_decrease_date = change.index(min(change)) + 1
greatest_decrease_amount = min(change)

# Print the analysis output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: ${round(sum(change) / len(change), 2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_date]} (${str(greatest_increase_amount)})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_date]} (${str(greatest_decrease_amount)})")

# Export as teext file
analysis_results = os.path.join("Analysis", "analysis_results.txt")

with open(analysis_results, "w") as txt:
    txt.write("Financial Analysis""\n")
    txt.write("----------------------------""\n")
    txt.write(f"Total Months: {len(total_months)}""\n")
    txt.write(f"Total: ${sum(total_profit_loss)}""\n")
    txt.write(f"Average Change: ${round(sum(change) / len(change), 2)}""\n")
    txt.write(f"Greatest Increase in Profits: {total_months[greatest_increase_date]} (${str(greatest_increase_amount)})""\n")
    txt.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_date]} (${str(greatest_decrease_amount)})""\n")


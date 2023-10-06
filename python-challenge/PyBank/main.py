import csv

# Files to load
file_to_load = "C:/Users/purot/Desktop/Boot_Camp/python-challenge/PyBank/Resources/budget_data.csv"

# Files to save
file_to_save = ("C:/Users/purot/Desktop/Boot_Camp/python-challenge/PyBank/analysis/budget_data.txt")

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    # use of next to skip first title row in csv file
    next(reader) 

    # creating variables to store my information for the analysis
    budget = []
    month = []
    budget_change = []

    # we store the total of profit/looses and store the dates in month
    for row in reader:

        budget.append(int(row[1]))
        month.append(row[0])

with open(file_to_save, "w") as txt_file:

    # we calculate the average change of the profit/looses column and we also retrieve and store the max and min of profits/looses column 
    for i in range(1,len(budget)):

        budget_change.append(budget[i] - budget[i-1])   
        avg_budget_change = sum(budget_change)/len(budget_change)

        max_budget_change = max(budget_change)

        min_budget_change = min(budget_change)

        max_budget_change_month = str(month[budget_change.index(max(budget_change))])
        min_budget_change_month = str(month[budget_change.index(min(budget_change))])

    # we foramt and print the results 
    budget_results = (
        f"\nFinancial Analysis\n"
        f"-----------------------------------\n"
        f"Total Months: {len(month)}\n"
        f"Total: ${sum(budget)}\n"
        f"Total Change: ${avg_budget_change:.2f}\n"
        f"Greatest Increase in Profits: {max_budget_change_month} ({max_budget_change})\n"
        f"Greatest Decrease in Profits: {min_budget_change_month} ({min_budget_change})\n")
    print(budget_results)

    # write and store the data in a text file 
    txt_file.write(budget_results)
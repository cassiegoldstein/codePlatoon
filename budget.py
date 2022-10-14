import csv

class Budget:
    def __init__(self):
        pass

    def viewExpenses():
        with open("./budget.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print('{:<20}  {:<15} {:<15} {:<15} {:<15} {:<15}'.format(*row))
        file.close()
    
    def changeIncome(newIncome):
        rows = []
        with open("./budget.csv", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        #Edit the Data
        rows[1][0] = newIncome
        #Write the Data to File
        with open("./budget.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        with open("./budget.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print('{:<20}  {:<15} {:<15} {:<15} {:<15} {:<15}'.format(*row))
        file.close()

    def viewMonthlyCosts():
        rows = []
        costs = 0
        with open("./budget.csv", newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                rows.append(row)
        [rows] = rows
        for i in range(1, len(rows)):
            costs = costs + int(rows[i])
        print("Your Monthly costs are: " + str(costs))


    def createNewExpense(expenseCategory, expenseAmount):
        rows = []
        with open("./budget.csv", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        #Edit the Data
        rows[0].append(expenseCategory)
        rows[1].append(expenseAmount)
        #Write the Data to File
        with open("./budget.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        with open("./budget.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print('{:<20}  {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(*row))
        file.close()

    def percentIncome():
        rows = []
        costs = 0
        with open("./budget.csv", newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                rows.append(row)
        [rows] = rows
        for i in range(1, len(rows)):
            costs = costs + int(rows[i])
        income = rows[0]
        percent = int((int(costs)/int(income))*100)
        print("You have used up " + str(percent) + "% of your monthly income")
        
        
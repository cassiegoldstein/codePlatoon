from budget import Budget

mode = None
while (mode != '6'):
    mode = input("\nWhat would you like to do?\nOptions:\n1. View Expenses\n2. Update Monthly Income\n3. View Monthly Costs\n4. Create New Expenses\n5. View Percent of Monthly Income Spent\n6. Quit\n")
    if mode == '1':
        Budget.viewExpenses() 
    elif mode == '2':
        newIncome = input('What is your new monthly income? ')
        Budget.changeIncome(newIncome)
    elif mode == '3':
        Budget.viewMonthlyCosts()
    elif mode == '4':
        category =  input("What expense category would you like to add? ")
        amount = input("How much have you spent in this category so far? ")
        Budget.createNewExpense(category, amount)
    elif mode == '5':
        Budget.percentIncome()
    elif mode == '6':
        quit
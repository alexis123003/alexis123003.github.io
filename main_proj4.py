print("Welcome to your personal computer assistant. =)")

while True:
    print("Enter 1 to Generate a Design.")
    print("Enter 2 to Activate Budget Mode.")
    print("Enter 3 to Project Future Income.")
    print("Enter 4 to Calculate Doubling Salary.")
    print("Enter q to quit.")
    option = input("Please select an option: ")

    if option == "1":
        import random
        rows = random.randint(3, 7)
        for row in range(1, rows + 1):
            for column in range(1, row + 1):
                print("*", end="")
            print()
        print(f"Well, ain't that cute with {rows} rows!")

    elif option == "2":
        budget_month = float(input('How much did you budget for "this" month?: '))
        total_expenses = 0.0

        for expense_number in range(1, 7):
            expense = float(input(f"Amount of Expense #{expense_number}?(type -1 to skip): "))
            if expense != -1:
                total_expenses += expense

        remaining_budget = budget_month - total_expenses
        print(f"Your remaining budget is: ${remaining_budget:.2f}")

        if remaining_budget < 0:
            import random
            lottery_number = random.randint(0, 9999999)
            print(f"You are under budget! Your 7-digit lottery number is: {lottery_number:07d}")
        elif remaining_budget >= 0:
            print("You are not under budget, so no lottery number is awarded.")

    elif option == "3":
        day = int(input("How many days do you plan to work?: "))
        total_dollar = 0.0

        for days in range(1, day + 1):
            total_days = float(input(f"Day {days} out of {day}: "))
            total_dollar += total_days

        print(f"You made a total of ${total_dollar:.2f} in {day} days.")

    elif option == "4":
        days = int(input("How many days would you like to calculate? "))
        pennies = 1
        total_pennies = 0

        print("Day      Salary")
        print("----------------")

        for day in range(1, days + 1):
            total_pennies += pennies
            salary_dollars = pennies / 100
            print(f"{day:<5}   ${salary_dollars:.2f}")
            pennies *= 2

        total_dollars = total_pennies / 100
        print(f"You made a total of: ${total_dollars:.2f}")

    elif option == "q":
        print("You have quit the program. Goodbye!")
        break

    else:
        print("You have entered an invalid option. Please try again.")

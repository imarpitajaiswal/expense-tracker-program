# Expense Tracker - Chapter 6 Compliant
expenses = []
print("Welcome to Personal Finance Management Tool 🙏🏻")

while True:
    print("\n========== MENU =============")
    print("Choose 1: To add Expenses")
    print("Choose 2: To view all Expenses")
    print("Choose 3: To view total Expenses")
    print("Choose 4: EXIT")

    choice = input("Enter your choice: ") # Using input() as string to avoid errors

    # To add Expenses
    if choice == '1':
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }
        expenses.append(expense)
        print("\nYour expense added successfully! ✅")

    # To view all expenses
    elif choice == '2':
        if len(expenses) == 0:
            print("No expenses found. Please add an expense first.")
        else:
            print("\n--- YOUR EXPENSES ---")
            count = 1
            for item in expenses:
                # Cleaner display using f-strings
                print(f"{count}. {item['Date']} | {item['Category']} | {item['Description']} | ₹{item['Amount']}")
                count += 1

    # To view total expenses
    elif choice == '3':
        total = 0.0
        for item in expenses:
            total += item["Amount"]
        print(f"\nYour total spending is: ₹{total:.2f}")

    # To EXIT
    elif choice == '4':
        print("\nThank you for using the tool. Goodbye! 👋")
        break

    else:
        print("\nINVALID INPUT!! TRY AGAIN.")

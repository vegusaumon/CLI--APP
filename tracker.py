from datetime import datetime
import json

class Expense:
    def __init__(self,date,description,amount):
        try:
            self.date = datetime.strptime(date,"%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: '{date}'. Use YYYY-MM-DD.")
        self.description = description
        self.amount = float(amount)
        if self.amount <0:
            raise ValueError("Amount cannot be negative")
        
    def __str__(self):
        return f"{self.date.date()} | {self.description} | ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("---- Expenses ----")
        for exp in self.expenses:
            print(exp)
        print("-------------\n")

def get_valid_expense():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter Description: ")
        amount_input = input("Enter amount: ")

        try: 
            expense = Expense(date_input,description, amount_input)
            return expense
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")


tracker = ExpenseTracker()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        expense = get_valid_expense()
        tracker.add_expense(expense)
        print("expense added successfully!\n")
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        print("Thank you for using our app")
        break
    else:
        print('Invalid option. Please try again. \n')







# Test for negative integers

#exp = Expense("2026-03-21","Lunch",-12)

# Test for invalid format
#exp2 = Expense("21-03-2026","Dinner",15)

# Valid test 
#exp3 = Expense("2026-03-21","Lunch",12)
#print(exp3)
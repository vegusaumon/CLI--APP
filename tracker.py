from datetime import datetime
import os
import cbor2

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


    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "amount":self.amount
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(data["date"],data["description"],data["amount"])


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
        # Show total at the end
        print(F"Total Expenses: ${self.total_expenses():.2f}\n")

    def total_expenses(self):
        return sum(exp.amount for exp in self.expenses)

    def save_to_file(self,filename= "expenses.cbor"):
        data = [exp.to_dict() for exp in self.expenses]
        with open(filename,"wb") as file:
            cbor2.dump(data,file)

    def load_from_file(self, filename="expenses.cbor"):
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            # File does not exist or is empty, start with empty list
            self.expenses = []
            return
        
        with open(filename,"rb") as file:
                data = cbor2.load(file)
                self.expenses =[Expense.from_dict(item) for item in data]



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


def main():
    tracker = ExpenseTracker()
    tracker.load_from_file()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            expense = get_valid_expense()
            tracker.add_expense(expense)
            tracker.save_to_file()
            print("expense added successfully!\n")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            if not tracker.expenses:
                print("no expenses to delete.\n")
                continue

            print("---- Expenses -----")
            for idx,exp in enumerate(tracker.expenses):
                print(f"{idx}: {exp}")
            print("--------------------")

            try:
                del_index = int(input("Enter the index of the expense to delete: "))
                if (0<= del_index) and (del_index <len(tracker.expenses)):
                    deleted = tracker.expenses.pop(del_index)
                    tracker.save_to_file()
                    print(f"Deleted expense: {deleted}\n")
                else:
                    print('Invalid index. Please try again. \n')
            except ValueError:
                print("Invalid input. Please enter a number. \n")


        elif choice == "4":
            print("Thank you for using our app")
            break
        else:
            print('Invalid option. Please try again. \n')


if __name__ == "__main__":
    main()





# Test for negative integers

#exp = Expense("2026-03-21","Lunch",-12)

# Test for invalid format
#exp2 = Expense("21-03-2026","Dinner",15)

# Valid test 
#exp3 = Expense("2026-03-21","Lunch",12)
#print(exp3)
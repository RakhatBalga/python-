import os
import pandas as pd 

CSV_FILE = "expenses.csv"

print("Welcome to the Expense Tracker App")

def load_expenses():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=["date", "amount","category", "description"])
    else:
        return pd.read_csv(CSV_FILE)

def save_expenses(df):
    df.to_csv(CSV_FILE, index=False)

def add_expense(date, amount, category, description):
    df = load_expenses()

    amount = float(amount)

    new_expense=pd.DataFrame([{ "date": date,
                                "amount": amount,
                                "category": category,
                                "description": description}])
    df = pd.concat([df, new_expense], ignore_index=True)
    save_expenses(df)
    print("Expense added successfully!")

def view_expenses():
    df = load_expenses()

    if df.empty:
        print("No expenses found!")
        return
    display_df = df.copy()
    display_df.index += 1

    print("\nAll Expenses: ")
    print(display_df)

def delete_expense():
    df = load_expenses()

    if df.empty:
        print("No expenses found!")
        return

    try:
        index_to_delete = int(input("Enter the expense number to delete: "))

        if 1 <= index_to_delete <= len(df):
            df = df.drop(index=index_to_delete - 1).reset_index(drop=True)
            save_expenses(df)
            print("Expense deleted successfully!")
        else:
            print("Invalid index")

    except ValueError:
        print("Invalid input. Please enter a number.")

def show_summary():
    df = load_expenses()

    if df.empty:
        print("No expenses found!")
        return

    total_expenses = df["amount"].sum()
    by_category = df.groupby("category")["amount"].sum()

    print("\nExpense Summary: ")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("\nExpenses by Category: ")
    print(by_category)


def main():
    while True:
        print("\nMenu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter date (dd-mm-yyyy): ")
            amount = input("Enter amount of money: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
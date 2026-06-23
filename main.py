import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

# ==== Clear Screen =====
def clear_screen():
    """Clears the terminal screen for a cleaner UI."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ==== Display Menu =====
def displayMenu():
    """Displays the main meny options to the user."""
    print("\n--- TRACKIFY Menu ---")
    print('\n---- Welcome to Trackify - An Interactive CLI based Expense Tracker ----')
    print('1. Add Expense')
    print('2. View All Expenses')
    print('3. Edit Expense')
    print('4. Delete Expense')
    print('5. Monthly Summary')
    print('6. Category-wise Spending')
    print('7. Exit')
    print('----------------------------')


# ===== Get Valid Amount =====
def get_valid_amount():
    """Prompts the user until a valid positive number is entered."""
    while True:
        try:
            amount_input = input('Enter amount: ').strip()
            amount = float(amount_input)
            if amount <= 0:
                print('Amount must be greater than 0.')
                continue
            return amount
        except ValueError:
            print('Invalid input! Please enter a valid number.')


# ==== Get Current Date =====
def get_valid_date():
    """Prompts the user until a valid YYYY-MM-DD date is entered."""
    while True:
        date_str = input('Enter date (YYYY-MM-DD): ').strip()
        try:
            valid_date = datetime.strptime(date_str, '%Y-%m-%d')
            return valid_date.strftime('%Y-%m-%d')
        except:
            print('Invalid date format! Please use YYYY-MM-DD.')


# ===== Add Expense =====
def add_expense(expenses):
    """Prompts the user for expense details and adds it to the list."""
    print('\n--- Add a new Expense ---')
    amount = get_valid_amount()
    category = input('Enter category (e.g., Food, Transport): ').strip()
    description = input('Enter description: ').strip()
    date = get_valid_date()

    # Create a dictionary for the new expense
    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': date
    }

    # Add the dictionary to our list
    expenses.append(expense)
    save_expenses(expenses)
    print('Expense added successfully!')


# ===== View All Expenses =====
def view_expenses(expenses):
    """Displays all expenses currently in the list"""
    print('\n--- All Expenses ---')

    if len(expenses) == 0:
        print('No expenses recoreded yet.')
        return
    
    for index, expense in enumerate(expenses):
        print(f'Expense #{index + 1}')
        print(f'  Date:          {expense["date"]}')
        print(f'  Category:      {expense["category"]}')
        amount = expense.get("amount")
        if amount is None:
            print("  Amount:        N/A")
        else:
            print(f'  Amount:        ₹{amount:.2f}')
        print(f'  Description:   {expense["description"]}')
        print('-' * 20)
    

# ===== Delete Expenses =====
def delete_expenses(expenses):
    """Deletes an expense from the list by its index"""
    if len(expenses) == 0:
        print('\nNo expenses to delete.')
        return
    
    view_expenses(expenses)

    try:
        index_input = input('Enter the expense number to delete (or 0 to cancel): ')
        index = int(index_input)

        if index == 0:
            print('Deletion cancelled.')
            return
        
        if 1 <= index <= len(expenses):
            # Show the user what they are about to delete
            expense_to_delete = expenses[index - 1]
            confirm = input(f'Are you sure you want to delete "{expense_to_delete["description"]}"? (y/n): ')

            if confirm.lower() == 'y':
                deleted_expense = expenses.pop(index - 1)
                save_expenses(expenses)
                print(f'Successfully deleted expense: {deleted_expense}')
            else:
                print('Deletion cancelled.')
        else:
            print('Invalid expense number.')
    except ValueError:
        print('Invalid input! Please enter a valid number.')


# ===== Edit Expense =====
def edit_expense(expenses):
    """Allows the user to modify an existing expense's details."""
    if len(expenses) == 0:
        print('\nNo expenses to edit.')
        return

    view_expenses(expenses)

    try:
        index_input = input('Enter the expense number to edit (or 0 to cancel): ')
        index = int(index_input)

        if index == 0:
            print('Edit cancelled.')
            return

        if 1 <= index <= len(expenses):
            expense = expenses[index - 1]
            print(f'\nEditing Expense #{index}:')
            print('(Press Enter to keep the current value)\n')

            # Edit amount
            amount_input = input(f'  Amount [₹{expense["amount"]:.2f}]: ').strip()
            if amount_input:
                try:
                    new_amount = float(amount_input)
                    if new_amount > 0:
                        expense['amount'] = new_amount
                    else:
                        print('  Amount must be positive. Keeping current value.')
                except ValueError:
                    print('  Invalid number. Keeping current value.')

            # Edit category
            category_input = input(f'  Category [{expense["category"]}]: ').strip()
            if category_input:
                expense['category'] = category_input

            # Edit description
            desc_input = input(f'  Description [{expense["description"]}]: ').strip()
            if desc_input:
                expense['description'] = desc_input

            # Edit date
            date_input = input(f'  Date [{expense["date"]}]: ').strip()
            if date_input:
                try:
                    valid_date = datetime.strptime(date_input, '%Y-%m-%d')
                    expense['date'] = valid_date.strftime('%Y-%m-%d')
                except ValueError:
                    print('  Invalid date format. Keeping current value.')

            save_expenses(expenses)
            print('\nExpense updated successfully!')
        else:
            print('Invalid expense number.')
    except ValueError:
        print('Invalid input! Please enter a valid number.')


# ===== Initialize Storage =====
def init_storage():
    """Creates the JSON file with an empty list if it doesn't exist."""
    if not os.path.exists(EXPENSES_FILE):
        save_expenses([])   # Reuse our existing save function


# ===== Save Expenses =====
def save_expenses(expenses):
    """Saves the current list of expenses to the JSON file."""
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent = 4)


# ==== Load Expenses =====
def load_expenses():
    """Loads thhe list of expenses from the JSON file. Handles errors if file is missing or corrupt."""
    try:
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Storage file not found. Starting with an empty list.')
        return []
    except json.JSONDecodeError:
        print('Warning: Storage file is corrupted. Starting with an empty list.')
        return []


# ===== Get Monthly Total =====
def get_monthly_total(expenses, year_month):
    """Calculates the total expenses for a specific YYYY-MM period."""
    total = 0.0
    for expense in expenses:
        if expense['date'].startswith(year_month):
            total += expense['amount']
    return total


# ===== Monthly Summary =====
def display_monthly_summary(expenses):
    """Displays the total spending for a specific month."""
    print('\n--- Monthly Summary ---')
    year_month = input('Enter the month to summarize (YYYY-MM): ')

    total = get_monthly_total(expenses, year_month)
    print(f'\nTotal spent in {year_month}: ₹{total:.2f}')


# ===== Get Category Spendings Total =====
def get_category_totals(expenses):
    """Calculates total expenses grouped by category."""
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals        


# ===== Category-wise Spending =====
def display_category_report(expenses):
    """Displays a breakdown of total spending by category."""
    print('\n--- Category-wise Spending Report ---')
    if len(expenses) == 0:
        print('No expenses recorded yet.')
        return
    
    category_totals = get_category_totals(expenses)

    for category, total in category_totals.items():
        print(f' {category}: ₹{total:.2f}')


# ===== Main Program =====
def main():
    """Main entry point for the TRACKIFY"""
    
    # Ensure our JSON storage file exists
    init_storage()

    # Load existing expenses from the file into memory
    expenses = load_expenses()

    while True:
        clear_screen()
        displayMenu()
        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            edit_expense(expenses)
        elif choice == '4':
            delete_expenses(expenses)
        elif choice == '5':
            display_monthly_summary(expenses)
        elif choice == '6':
            display_category_report(expenses)
        elif choice == '7':
            print('Exiting Trackify. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number from 1 to 7.')

        input('\nPress Enter to continue...')
if __name__ == '__main__':
    main()
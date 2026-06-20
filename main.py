def displayMenu():
    """Displays the main meny options to the user."""
    print("\n--- TRACKIFY Menu ---")
    print('1. Add Expense')
    print('2.View All Expenese')
    print('3. Delete Expense')
    print('4. Monthly Summary')
    print('5. Category-wise Spending')
    print('6. Exit')
    print('----------------------------')


# ===== Add Expense =====
def add_expense(expenses):
    """Prompts the user for expense details and adds it to the list."""
    print('\n--- Add a new Expense ---')
    
    while True:
        try:
            amount_input = input('Enter amount: ')
            amount = float(amount_input)
            if amount <= 0:
                print('Amount must be greater than 0.')
                continue
            break
        except ValueError:
            print('Invalid input! Please enter a valid number.')

    category = input('Enter category (e.g., Food, Transport): ')
    description = input('Enter description: ')
    date = input('Enter date (YYYY-MM-DD): ')

    # Create a dictionary for the new expense
    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': date
    }

    # Add the dictionary to our list
    expenses.append(expense)
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
        print(f' Date:          {expense['date']}')
        print(f' Category:      {expense['category']}')
        print(f' Amount:        ₹{expense['amount']:.2f}')
        print(f' Description:   {expense['description']}')
        print('-' * 20)
    

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
            deleted_expense = expenses.pop(index - 1)
            print(f'Successfully deleted expense: {deleted_expense}')
        else:
            print('Invalid expense number.')
    except ValueError:
        print('Invalid input! Please enter a valid number.')


# ===== Main Program =====
def main():
    """Main entry point for the TRACKIFY"""
    print('Welcome to TRACKIFY')

    # List to store all our expenses dictionaries in memory
    expenses = []

    while True:
        displayMenu()
        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print('DeleteExpenses selected (Coming soon!).')
        elif choice == '4':
            print('Monthly Summaryselected (Coming soon!).')
        elif choice == '5':
            print('Category-wise Spending selected (Coming soon!).')
        elif choice == '6':
            print('Exiting Trackify. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number from 1 to 6.')

if __name__ == '__main__':
    main()
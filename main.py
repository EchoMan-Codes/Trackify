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

def main():
    """Main entry point for the TRACKIFY"""
    print('Welcome to TRACKIFY')

    while True:
        displayMenu()
        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            print('Add Expense selected (Coming soon!).')
        elif choice == '2':
            print('View All Expenses selected (Coming soon!).')
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
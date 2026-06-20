# Python CLI Expense Tracker

A robust command-line expense tracking application built entirely in Python. This project was developed to practice and demonstrate core Python concepts including File I/O (JSON), data structures (lists and dictionaries), modular programming, loop control, and input validation.

## Features

* **Add Expense**: Record new expenses with strict validation for amounts (positive floats) and dates (YYYY-MM-DD).
* **View All Expenses**: Display a cleanly formatted, enumerated list of all recorded expenses.
* **Delete Expense**: Safely remove an expense using its index number, complete with a `y/n` confirmation prompt.
* **Monthly Summary**: Calculate total spending for a specific `YYYY-MM` period.
* **Category-wise Spending**: View an aggregated summary of total expenses grouped by category using a dictionary.
* **Data Persistence**: Automatically saves and loads data to a local `expenses.json` file.

## How to Run

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt in the project directory.
3. Run the application:
   ```bash
   python main.py
   ```

---

## Sample Output Demonstration

Here is a detailed walkthrough demonstrating all the features of the application in action.

### 1. Starting the Application
```text
Welcome to Expense Tracker!

--- Expense Tracker Menu ---
1. Add Expense
2. View All Expenses
3. Delete Expense
4. Monthly Summary
5. Category-wise Spending
6. Exit
----------------------------
Enter your choice (1-6): 1
```

### 2. Adding an Expense (With Validation)
```text
--- Add a New Expense ---
Enter amount: apple
Invalid input! Please enter a valid number for the amount.
Enter amount: 15.50
Enter category (e.g., Food, Transport): Food
Enter description: Lunch at cafe
Enter date (YYYY-MM-DD): 2026-06-19
Expense added successfully!

Press Enter to continue...
```

### 3. Adding Another Expense
```text
--- Add a New Expense ---
Enter amount: 40.00
Enter category (e.g., Food, Transport): Transport
Enter description: Gas station
Enter date (YYYY-MM-DD): 2026-06-19
Expense added successfully!

Press Enter to continue...
```

### 4. Viewing All Expenses
```text
Enter your choice (1-6): 2

--- All Expenses ---
Expense #1
  Date:        2026-06-19
  Category:    Food
  Amount:      $15.50
  Description: Lunch at cafe
--------------------
Expense #2
  Date:        2026-06-19
  Category:    Transport
  Amount:      $40.00
  Description: Gas station
--------------------

Press Enter to continue...
```

### 5. Category-wise Spending
```text
Enter your choice (1-6): 5

--- Category-wise Spending ---
  Food: $15.50
  Transport: $40.00

Press Enter to continue...
```

### 6. Monthly Summary
```text
Enter your choice (1-6): 4

--- Monthly Summary ---
Enter the month to summarize (YYYY-MM): 2026-06

Total spent in 2026-06: $55.50

Press Enter to continue...
```

### 7. Deleting an Expense (With Confirmation)
```text
Enter your choice (1-6): 3

--- All Expenses ---
Expense #1
  Date:        2026-06-19
  Category:    Food
  Amount:      $15.50
  Description: Lunch at cafe
--------------------
Expense #2
  Date:        2026-06-19
  Category:    Transport
  Amount:      $40.00
  Description: Gas station
--------------------
Enter the expense number to delete (or 0 to cancel): 1
Are you sure you want to delete 'Lunch at cafe'? (y/n): y
Successfully deleted expense: Lunch at cafe ($15.50)

Press Enter to continue...
```

### 8. Exiting the App
```text
Enter your choice (1-6): 6
Exiting Expense Tracker. Goodbye!
```

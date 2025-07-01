'''
Purpose: Entry point of the app. Handles the user menu and navigation.

Includes:
    Main menu with options: Add Expense, View, Analyze, Show Charts, Exit

    Calls appropriate functions from other modules (expenses.py, analyzer.py, etc.)

    Basic loop for continuous user interaction

'''

def start_app():
    '''Main Application start point'''

    try:
        print("\n==== Personal Expense Tracker ====")

        while True:
            # Show the menu only once per loop
            print("\n=== Main Menu ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Summarize Expenses")
            print("4. Display Charts")
            print("5. Exit")

            # Get user input
            option = input("\nChoose an option (1-5): ")

            # Menu logic
            if option == '1':
                print("\n Adding expense...")
            elif option == '2':
                print("\n Listing expenses...")
            elif option == '3':
                print("\n Summarizing expenses...")
            elif option == '4':
                print("\n Displaying charts...")
            elif option == '5':
                print("\n Exiting... Goodbye!")
                break
            else:
                print("\n Invalid option. Please choose between 1–5.")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    start_app()

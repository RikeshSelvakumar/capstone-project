# Main program
#TODO: When category is asked a string input breaks the code - change to try int() and create exception ValueError if a string or float is inputted
#TODO: For category the dictionary should be filled with actual category names rather than numbers
#TODO: Investigate if there is any way to accidentally wipe the csv file without producing a new one with the removed transaction
#TODO: Add new function that allows to view all transactions and able to see transactions for certain dates 
from Functions.add_transactions import add_transaction
from Functions.remove_transaction import remove_transaction
from Functions.csv_handler import add_transaction_to_csv,load_csv

transactions_list = load_csv()

while True:
    selection = int(input("Please select if you want to add a transaction (1) or remove a transaction(2): "))
    if selection == 1:
        new_transaction = add_transaction()
        print(new_transaction)
        add_transaction_to_csv(new_transaction)
        repeat = input("Would you like to add or remove another transaction (Y/N): ").lower().strip()
        if repeat == "n":
            break
    elif selection == 2:
        transactions_list = load_csv()
        remove_transaction(transactions_list)
        repeat = input("Would you like to add or remove another transaction (Y/N): ").lower().strip()
        if repeat == "n":
            break
    else: 
        print("Please enter 1 or 2")


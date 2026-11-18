# Main program
from Functions.transactions import add_transaction
from Functions.csv_handler import add_transaction_to_csv
stored_transactions = []

selection = int(input("Please select if you want to add a transaction (1) or remove a transaction(2): "))
if selection == 1:
    new_transaction = add_transaction()
    print(new_transaction)
    add_transaction_to_csv(new_transaction)

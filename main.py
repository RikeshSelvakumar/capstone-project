# Main program
from Functions.transactions import add_transaction
stored_transactions = []

selection = int(input("Please select if you want to add a transaction (1) or remove a transaction(2): "))
if selection == 1:
    stored_transactions.append(add_transaction())
print(stored_transactions)
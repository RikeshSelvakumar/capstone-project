from Functions.csv_handler import load_csv, delete_csv, add_transaction_to_csv
#List containing dictionaries of each transaction
transactions_list = load_csv()

# Prints out the id description and amount 
def print_transactions(transaction_list):
    for i in transactions_list:
        id = i["id"]
        description = i["description"]
        category = i["category"]
        transaction_type = i["transaction_type"]
        amount = i["amount"]
        print(f"{id} | {category} | {description} | {transaction_type} £{amount}")

# Prints out the transaction clean to confirm if this is what they want to remove
def print_transaction(transaction):
    id = transaction["id"]
    description = transaction["description"]
    amount = transaction["amount"]
    transaction_type = transaction["transaction_type"]
    category = transaction["category"]
    date = transaction["date"]
    print(f"""
    Id: {id}
    Description: {description}
    Category: {category}
    Amount: {transaction_type} £{amount}
    Date: {date}
    """)



# Select transaction - Takes an input from the user and returns the id of the transaction if it exists
def select_transaction(transaction_list):
    while True:
        print_transactions(transaction_list)
        selected_id = input("Please copy and past the id of the transaction you would like to remove: ").strip()
        for transaction in transactions_list:
            if transaction["id"] == selected_id:
                while True:
                    print_transaction(transaction)
                    confirm = input(f"Is this the transaction you would like to remove (Y/N): ").lower().strip()
                    if confirm == "y":
                        break
                    elif confirm == "n":
                        selected_id = None
                        break
                    else:
                        print("Please enter Y or N")
                        continue
            else:
                continue
        if selected_id == None:
            continue
        else:
            return selected_id

def remove_transaction(transactions_list):
    selected_id = select_transaction(transactions_list)
    new_transaction_list = []
    for transaction in transactions_list:
        if selected_id == transaction["id"]:
            continue
        else:
            new_transaction_list.append(transaction)
    if new_transaction_list == []:
        print("There has been an error")
    else:
        delete_csv()
        for transaction in new_transaction_list:
            print(transaction)
            add_transaction_to_csv(transaction)


#Function of generating unique id, add transaction and remove transaction 
#TODO: When category is asked a string input breaks the code - change to try int()
#TODO: Complete remove_transaction function as well as find a way to create a permanent save - ends up meaning finding a way to load and alter a csv file - research loading and modifying csv files
import uuid
from Functions.validators import amount_validator, description_validator, type_validator, category_validator, date_selection
from Data.categories import INCOME_CATEGORIES, EXPENSE_CATEGORIES
# Generate unique id for transation
def generate_id():
    return str(uuid.uuid4()) # uuid4 ensures theres no duplicate id that is made.

# Adding function - Collects inputted values from user and returns a dictionary of the transaction
def add_transaction():
    print("Please enter your details here")
    # Description section
    while True:
        description = description_validator(input("Description(optional): ").strip())
        if description is not None:
            break

    # Amount section
    while True:
        amount = amount_validator(input("Amount(£): ").strip())
        if amount is not None:
            break
    # Transaction type section
    while True:
        transaction_type = type_validator(input("Income (I) or Expense (E): ").lower().strip())
        if transaction_type is not None:
            break

    # Category section
    # Print categories based on transaction type 
    if transaction_type == "+":
        for number, category in enumerate(INCOME_CATEGORIES, start=1):
            print(f"{number}. {category}")
    elif transaction_type == "-":
        for number, category in enumerate(EXPENSE_CATEGORIES, start=1):
            print(f"{number}. {category}")
    else:
        print("Something went wrong with the transaction type logic")
    # Category validation
    while True:
        category = category_validator(transaction_type, int(input("Please enter the number of the category the transaction relates to: ")))
        if category is not None:
            break

    #Date section
    while True:
        input_date = date_selection(input("Was the transaction done today (Y/N): ").lower().strip())
        if input_date is not None:
            break
    # Transaction dict format
    transaction = {
    "id": generate_id(),
    "description": description,
    "amount": amount,
    "transaction_type": transaction_type,
    "category": category,
    "date": input_date,
    }
    return transaction

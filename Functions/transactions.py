#Function of generating unique id, add transaction, remove transaction, date validator
import uuid
from datetime import datetime, date
from Functions.validators import date_validator, amount_validator, description_validator, type_validator, category_validator
from Data.categories import INCOME_CATEGORIES, EXPENSE_CATEGORIES
def generate_id():
    return str(uuid.uuid4()) # uuid4 ensures theres no duplicate id that is made.

def enter_values():
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
        today = input("Was the transaction done today (Y/N): ").lower().strip()
        if today == "y":
            input_date = datetime.now().strftime("%Y-%m-%d")
            break
        elif today == "n":
            input_date = date_validator()
            break
        else:
            print("Please enter Y/N")
            continue
    return description, amount, transaction_type, category, input_date



description, amount, transaction_type, category, input_date = enter_values()

transaction = {"id": generate_id(),
"description": description,
"amount": amount,
"transaction_type": transaction_type,
"category": category,
"date": input_date
}
print(transaction)
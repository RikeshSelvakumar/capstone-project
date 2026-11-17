#Contains all the value validating functions in one place 
from datetime import datetime, date
from Data.categories import INCOME_CATEGORIES, EXPENSE_CATEGORIES

#Date validator
def date_validator():
    while True:
        entered = input("Please enter date of transaction (dd-mm-yyyy):").strip()
        current = date.today()
        try:
            entered_date = datetime.strptime(entered, "%d-%m-%Y").date() #Checking for valid date in the correct format
        except ValueError:
            print("Thats not a valid date or format - please use the format dd-mm-yyyy")
            continue
        if entered_date > current:
            print("That is a future date - please try again")
            continue
        break
    return entered_date

#Amount validator - checks if integer or float and checks if the amount starts with a currency symbol
def amount_validator(entered_amount):
    entered_amount = entered_amount.removeprefix("£").strip()
    try:
        amount = float(entered_amount)
    except ValueError:
        print("That is not a valid amount - please only enter numbers")
        return None
    if amount <= 0:
        print("Amount has to be more than zero - please try again")
        return None
    return round(amount, 2)

#Description validator - checks if it its too long
def description_validator(entered):
    if len(entered) > 50:
        print("Description is too long keep it to under 50 characters")
        return None
    return entered

#Transaction type validator
def type_validator(entered):
    if entered == "i":
        entered_type = "+"
    elif entered == "e":
        entered_type = "-"
    else:
        return None
    return entered_type
        

#Category validator - check if the number inputted is exists within the list
def category_validator(transaction_type, entered):
    if transaction_type == "+":
        length = len(INCOME_CATEGORIES)
        if entered > length or entered <= 0:
            print("Please enter a number related to a category")
            return None
    elif transaction_type == "-":
        length = len(EXPENSE_CATEGORIES)
        if entered > length or entered <= 0:
            print("Please enter a number related to a category")
            return None
    else:
        print("Something is wrong with the transaction type function")
        return entered
    return entered
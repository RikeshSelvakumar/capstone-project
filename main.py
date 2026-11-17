# Main program
from Functions.transactions import enter_values, generate_id

description, amount, transaction_type, category, input_date = enter_values()

transaction = {
    "id": generate_id(),
    "description": description,
    "amount": amount,
    "transaction_type": transaction_type,
    "category": category,
    "date": input_date,
}

print(transaction)
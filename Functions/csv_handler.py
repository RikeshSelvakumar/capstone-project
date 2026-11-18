# File containing functions that handle the save in csv, load in csv and modify in csv
import csv
import os
#File paths defined
FUNCTIONS_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the path to the folder containing this python file specifically
PROJECT_DIR = os.path.dirname(FUNCTIONS_DIR) # Cuts off the function folder from the path so its now on the main folder of the repo
DATA_FILE = os.path.join(PROJECT_DIR,"Data","transactions.csv") # Creates the path for the transactions.csv folder - This is where transactions.csv will be made if its not already made

def add_transaction_to_csv(transaction):
    field_list = []
    exists = os.path.isfile(DATA_FILE) #Boolean return if transaction.csv exists

    # Extracting field names for the csv file 
    for i in transaction:
        field_list.append(i)
        continue

    with open(DATA_FILE,"a", newline="") as f:
        writer = csv.DictWriter(f,fieldnames=field_list)
        if not exists:
            writer.writeheader()
        writer.writerow(transaction)

def load_csv():
    with open(DATA_FILE, "r", newline="") as f:
        read = csv.DictReader(f)
        transactions = list(read)
    return transactions

def delete_csv():
    if os.path.isfile(DATA_FILE):
        os.remove(DATA_FILE)


# Testing + notes

# print(FUNCTIONS_DIR) #c:\Users\rikes\OneDrive\Desktop\Main\Projects\capstone-project\Functions
# print(PROJECT_DIR) #c:\Users\rikes\OneDrive\Desktop\Main\Projects\capstone-project
# print(DATA_FILE) #c:\Users\rikes\OneDrive\Desktop\Main\Projects\capstone-project\Data\transactions.csv

#dirname is the directory name essentially it cuts off te last part of the path making it a path to the folder containing the file

# open(DATA_FILE,"a", newline="") as f
# There are 3 modes for open 
# a = append - new data added to the end
# r = read - only reads + produce error if it doesnt exist
# w = write - wipes the file making it empty
# newline="" - stops python from touching the line endings letting the csv module handle it instead

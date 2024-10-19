from models import users, expenses
import csv
from services import split_expense
def generate_balance_sheet():
    balance_sheet = []
    for expense in expenses:
        split_data = split_expense(expense)
        for user_email in expense.participants:
            balance_sheet.append({
                'user': user_email,
                'description': expense.description,
                'amount': split_data[user_email],
                'created_by': expense.created_by
            })

    return balance_sheet

def download_balance_sheet():
    balance_sheet = generate_balance_sheet()
    
    with open('balance_sheet.csv', 'w', newline='') as csvfile:
        fieldnames = ['user', 'description', 'amount', 'created_by']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in balance_sheet:
            writer.writerow(row)
    
    return 'balance_sheet.csv'

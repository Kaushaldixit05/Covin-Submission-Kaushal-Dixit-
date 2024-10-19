from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd

app = Flask(__name__)

# A simple in-memory store for users and expenses
users = {}
expenses = {}

# Home route (Landing page)
@app.route('/')
def index():
    return render_template('index.html', users=users)

# Route to create a new user
@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        mobile = request.form['mobile']
        # Add user to the in-memory store
        users[email] = {'name': name, 'mobile': mobile}
        expenses[email] = []  # Initialize an empty expense list for the user
        return redirect(url_for('index'))
    return render_template('create_user.html')

# Route to add a new expense
@app.route('/expenses/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        user_email = request.form['user_email']
        total_amount = float(request.form['amount'])  # Total expense amount
        split_method = request.form['split_method']  # Get the split method
        num_people = int(request.form['num_people'])  # Number of participants

        user_spent = 0
        owed_amount = 0
        split_amount = 0
        
        # Process the expense based on the chosen split method
        if split_method == "Equal":
            split_amount = total_amount / num_people
            user_spent = split_amount  # User spends their share
            owed_amount = total_amount - user_spent  # Remaining owed amount

        elif split_method == "Exact":
            user_spent = float(request.form['user_spent'])  # User's exact spend
            owed_amount = total_amount - user_spent  # Remaining owed amount

        elif split_method == "Percentage":
            user_percentage = float(request.form['user_percentage'])
            user_spent = (user_percentage / 100) * total_amount  # User's spent amount
            owed_amount = total_amount - user_spent  # Remaining owed amount

        # Append the expense to the user's list
        expenses[user_email].append({
            'amount': total_amount,
            'user_spent': user_spent,
            'owed_amount': owed_amount,
            'split_method': split_method
        })
        
        return redirect(url_for('index'))
    
    return render_template('add_expense.html', users=users)

# Route to download user expenses as an Excel file
@app.route('/download/<email>')
def download_expenses(email):
    if email in expenses:
        user_expenses = expenses[email]
        
        # Calculate total spending and total owed amounts
        total_spent = sum(expense['user_spent'] for expense in user_expenses)
        total_owed = sum(expense['owed_amount'] for expense in user_expenses)
        
        # Convert user's expenses to a DataFrame
        df = pd.DataFrame(user_expenses)
        
        # Add total spent and total owed as new rows in the DataFrame
        totals = pd.DataFrame({
            'amount': ['Total Spending', 'Total Owed'],
            'user_spent': [total_spent, ''],
            'owed_amount': ['', total_owed],
            'split_method': ['', '']
        })
        
        # Append totals to the DataFrame
        df = pd.concat([df, totals], ignore_index=True)
        
        # Define the file path
        file_path = f"{email}_expenses.xlsx"
        # Save the DataFrame to an Excel file
        df.to_excel(file_path, index=False)
        return send_file(file_path, as_attachment=True)  # Send the file for download
    return "User not found!"

# Route to download overall expenses as an Excel file
# Route to download overall expenses as an Excel file
@app.route('/download/balance_sheet')
def download_balance_sheet():
    overall_expenses = []

    for email, user_expenses in expenses.items():
        total_spent = sum(expense['user_spent'] for expense in user_expenses)
        total_owed = sum(expense['owed_amount'] for expense in user_expenses)

        for expense in user_expenses:
            overall_expenses.append({
                'User Email': email,
                'Total Amount': expense['amount'],
                'User Spent': expense['user_spent'],
                'Owed Amount': expense['owed_amount'],
                'Split Method': expense['split_method']
            })

        overall_expenses.append({
            'User Email': email,
            'Total Amount': 'Total Spending',
            'User Spent': total_spent,
            'Owed Amount': '',
            'Split Method': ''
        })

        overall_expenses.append({
            'User Email': email,
            'Total Amount': 'Total Owed',
            'User Spent': '',
            'Owed Amount': total_owed,
            'Split Method': ''
        })

    # Convert overall expenses to a DataFrame
    df = pd.DataFrame(overall_expenses)
    # Define the file path
    file_path = "overall_expenses.xlsx"
    # Save the DataFrame to an Excel file
    df.to_excel(file_path, index=False)
    return send_file(file_path, as_attachment=True)  # Send the file for download


if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, request, jsonify
from models import users, expenses, User, Expense
from services import split_expense, validate_percentage_split

user_routes = Blueprint('user_routes', __name__)
expense_routes = Blueprint('expense_routes', __name__)

# Create user
@user_routes.route('/create', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')
    name = data.get('name')
    mobile = data.get('mobile')

    if email in users:
        return jsonify({'error': 'User already exists'}), 400

    users[email] = User(email, name, mobile)
    return jsonify({'message': 'User created successfully'}), 201

# Add expense
@expense_routes.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    amount = data.get('amount')
    description = data.get('description')
    created_by = data.get('created_by')
    participants = data.get('participants')  # List of participant emails
    split_type = data.get('split_type')  # 'equal', 'exact', or 'percentage'
    split_details = data.get('split_details')  # Exact amounts or percentages

    if split_type == 'percentage' and not validate_percentage_split(split_details):
        return jsonify({'error': 'Percentages do not add up to 100'}), 400

    expense = Expense(amount, description, created_by, participants, split_type, split_details)
    expenses.append(expense)

    return jsonify({'message': 'Expense added successfully'}), 201

users = {}
expenses = []

class User:
    def __init__(self, email, name, mobile):
        self.email = email
        self.name = name
        self.mobile = mobile
        self.expenses = []

class Expense:
    def __init__(self, amount, description, created_by, participants, split_type, split_details):
        self.amount = amount
        self.description = description
        self.created_by = created_by
        self.participants = participants
        self.split_type = split_type
        self.split_details = split_details  # Can store either exact amounts or percentages

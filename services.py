def split_expense(expense):
    if expense.split_type == 'equal':
        return equal_split(expense.amount, len(expense.participants))
    elif expense.split_type == 'exact':
        return exact_split(expense.split_details)
    elif expense.split_type == 'percentage':
        return percentage_split(expense.amount, expense.split_details)

def equal_split(amount, num_people):
    share = amount / num_people
    return {i: share for i in range(num_people)}

def exact_split(split_details):
    return split_details

def percentage_split(amount, split_details):
    return {i: (amount * (split_details[i] / 100)) for i in range(len(split_details))}

def validate_percentage_split(split_details):
    return sum(split_details.values()) == 100

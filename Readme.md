# Daily Expenses Sharing Application

## Overview

This application allows users to manage their daily expenses, split bills among participants, and generate downloadable balance sheets in Excel format. Users can add expenses, specify split methods (equal, exact, percentage), and track their spending and owed amounts.

## Features

- User Management:
  - Create users with email, name, and mobile number.
  - Retrieve user details.

- Expense Management:
  - Add expenses with specified amounts.
  - Split expenses using:
    1. Equal: Split equally among all participants.
    2. Exact: Specify the exact amount each participant owes.
    3. Percentage: Specify the percentage each participant owes (ensuring percentages add up to 100%).

- Balance Sheet:
  - Show individual expenses.
  - Show overall expenses for all users.
  - Download balance sheets as Excel files with total spending and owed amounts.

## Getting Started

## Prerequisites

- Python 3.11.0 (64-bit)
- pip (Python package installer)

Note: The application is developed and tested with Python 3.11.0 (64-bit). If you are using a different version of Python, it may lead to compatibility issues.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Kaushaldixit05/Covin-Submission-Kaushal-Dixit-.git
   cd <repository_name>

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3. Install the required packages
    ```bash
    pip install -r requirements.txt

### Running the Application
1. Run the Flask application
    ```bash
    python app.py


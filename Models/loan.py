# Models/loan.py

from config import get_connection

# ========== Database Operations ==========

def create_loan(loan_id, customer_id, principal, rate, period, interest, total_amount, emi, start_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO loan (
            loan_id, customer_id, principal, interest_rate,
            loan_period_years, interest, total_amount,
            emi_amount, start_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (loan_id, customer_id, principal, rate, period, interest, total_amount, emi, start_date))
    conn.commit()
    conn.close()

def get_loan_by_id(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM loan WHERE loan_id = ?', (loan_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Loan(*row)
    return None

def get_loans_by_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM loan WHERE customer_id = ?', (customer_id,))
    rows = cursor.fetchall()
    conn.close()
    return [Loan(*row) for row in rows]

# ========== Loan Data Model ==========

class Loan:
    def __init__(self, loan_id, customer_id, principal, interest_rate, loan_period_years,
                 interest, total_amount, emi_amount, start_date):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal = principal
        self.interest_rate = interest_rate
        self.loan_period_years = loan_period_years
        self.interest = interest
        self.total_amount = total_amount
        self.emi_amount = emi_amount
        self.start_date = start_date

    def to_dict(self):
        return self.__dict__

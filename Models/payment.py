# bank_loan_system/models/payment.py

from config import get_connection

#  Database Operations

def add_payment(payment_id, loan_id, amount_paid, payment_type, payment_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payment (
            payment_id, loan_id, amount_paid, payment_type, payment_date
        ) VALUES (?, ?, ?, ?, ?)
    ''', (payment_id, loan_id, amount_paid, payment_type, payment_date))
    conn.commit()
    conn.close()

def get_payments_by_loan(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM payment WHERE loan_id = ?', (loan_id,))
    rows = cursor.fetchall()
    conn.close()
    return [Payment(*row) for row in rows]

def get_total_paid(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount_paid) FROM payment WHERE loan_id = ?', (loan_id,))
    total_paid = cursor.fetchone()[0] or 0
    conn.close()
    return total_paid

#  Payment Data Model

class Payment:
    def __init__(self, payment_id, loan_id, amount_paid, payment_type, payment_date):
        self.payment_id = payment_id
        self.loan_id = loan_id
        self.amount_paid = amount_paid
        self.payment_type = payment_type
        self.payment_date = payment_date

    def to_dict(self):
        return self.__dict__

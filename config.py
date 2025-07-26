# config.py

import sqlite3
import os

DB_PATH = 'data/bank.db'

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create Customer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')

    # Create Loan table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loan (
            loan_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            principal REAL,
            interest_rate REAL,
            loan_period_years INTEGER,
            interest REAL,
            total_amount REAL,
            emi_amount REAL,
            start_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        )
    ''')

    # Create Payment table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payment (
            payment_id TEXT PRIMARY KEY,
            loan_id TEXT NOT NULL,
            amount_paid REAL,
            payment_type TEXT,
            payment_date TEXT,
            FOREIGN KEY (loan_id) REFERENCES loan(loan_id)
        )
    ''')

    conn.commit()
    conn.close()

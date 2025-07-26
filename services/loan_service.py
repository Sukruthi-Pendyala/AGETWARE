# bank_loan_system/services/loan_service.py

import uuid
from datetime import date
from utils.calculations import (
    calculate_interest, calculate_total_amount, calculate_emi
)
from models.loan import create_loan

def lend_money(customer_id, principal, rate, period):
    loan_id = str(uuid.uuid4())
    interest = calculate_interest(principal, rate, period)
    total_amount = calculate_total_amount(principal, interest)
    emi = calculate_emi(total_amount, period)
    start_date = date.today().isoformat()

    create_loan(
        loan_id, customer_id, principal, rate, period,
        interest, total_amount, emi, start_date
    )

    return {
        "loan_id": loan_id,
        "total_amount": total_amount,
        "monthly_emi": emi
    }

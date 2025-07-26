# bank_loan_system/services/payment_service.py

import uuid
from datetime import date
from models.payment import add_payment, get_total_paid
from models.loan import get_loan_by_id
from utils.calculations import calculate_remaining_emis

def make_payment(loan_id, amount, payment_type):
    payment_id = str(uuid.uuid4())
    payment_date = date.today().isoformat()
    add_payment(payment_id, loan_id, amount, payment_type, payment_date)

    loan = get_loan_by_id(loan_id)
    if not loan:
        return {"error": "Loan not found"}

    total_amount = loan[6]
    emi_amount = loan[7]
    total_paid = get_total_paid(loan_id)
    remaining = total_amount - total_paid
    emis_left = calculate_remaining_emis(remaining, emi_amount)

    return {
        "status": "success",
        "total_paid": total_paid,
        "remaining_amount": remaining,
        "remaining_emis": emis_left
    }

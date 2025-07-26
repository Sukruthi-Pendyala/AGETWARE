# bank_loan_system/services/ledger_service.py

from models.loan import get_loan_by_id
from models.payment import get_payments_by_loan, get_total_paid
from utils.calculations import calculate_remaining_emis

def get_ledger(loan_id):
    loan = get_loan_by_id(loan_id)
    if not loan:
        return {"error": "Loan not found"}

    payments = get_payments_by_loan(loan_id)
    total_paid = get_total_paid(loan_id)
    balance = loan[6] - total_paid
    emis_left = calculate_remaining_emis(balance, loan[7])

    return {
        "loan_id": loan_id,
        "total_amount": loan[6],
        "emi_amount": loan[7],
        "payments": [
            {
                "date": p[4],
                "type": p[3],
                "amount": p[2]
            } for p in payments
        ],
        "total_paid": total_paid,
        "balance_amount": balance,
        "remaining_emis": emis_left
    }

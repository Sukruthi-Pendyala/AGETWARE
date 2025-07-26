# bank_loan_system/services/overview_service.py

from models.loan import get_loans_by_customer
from models.payment import get_total_paid
from utils.calculations import calculate_remaining_emis

def get_account_overview(customer_id):
    loans = get_loans_by_customer(customer_id)
    overview = []

    for loan in loans:
        total_paid = get_total_paid(loan[0])
        remaining = loan[6] - total_paid
        emis_left = calculate_remaining_emis(remaining, loan[7])

        overview.append({
            "loan_id": loan[0],
            "principal": loan[2],
            "interest": loan[5],
            "total_amount": loan[6],
            "emi_amount": loan[7],
            "total_paid": total_paid,
            "remaining_emis": emis_left
        })

    return overview

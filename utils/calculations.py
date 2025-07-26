# bank_loan_system/utils/calculations.py

import math

def calculate_interest(principal, rate, years):
    return round((principal * rate * years) / 100, 2)

def calculate_total_amount(principal, interest):
    return round(principal + interest, 2)

def calculate_emi(total_amount, loan_period_years):
    months = loan_period_years * 12
    return round(total_amount / months, 2)

def calculate_remaining_emis(balance, emi_amount):
    return math.ceil(balance / emi_amount)

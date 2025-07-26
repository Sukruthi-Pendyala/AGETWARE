# routes/loan_routes.py

from flask import Blueprint, request, jsonify
from Models.loan import Loan, get_loan_by_id
from config import get_connection

# Attempt to import loan calculation service
try:
    from services.loan_service import lend_money
except ImportError:
    lend_money = None  # fallback for development

loan_bp = Blueprint('loan_bp', __name__)

# ========== Route: Issue a New Loan ==========
@loan_bp.route('/', methods=['POST'])
def lend():
    data = request.get_json()

    customer_id = data.get('customer_id')
    principal = data.get('principal')
    interest_rate = data.get('interest_rate')
    loan_period_years = data.get('loan_period_years')

    if not all([customer_id, principal, interest_rate, loan_period_years]):
        return jsonify({'error': 'Missing required fields'}), 400

    if lend_money:
        # If service is available, use it
        result = lend_money(customer_id, principal, interest_rate, loan_period_years)
        return jsonify(result), 201
    else:
        return jsonify({
            "error": "Lending service not implemented",
            "tip": "Add 'services/loan_service.py' with 'lend_money' function"
        }), 501

# ========== Route: Get All Loans ==========
@loan_bp.route('/', methods=['GET'])
def get_loans():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loan")
    rows = cursor.fetchall()
    conn.close()

    loans = [Loan(*row).to_dict() for row in rows]
    return jsonify(loans)

# ========== Route: Get Loan by ID ==========
@loan_bp.route('/<loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = get_loan_by_id(loan_id)
    if loan:
        return jsonify(loan.to_dict())
    return jsonify({"error": "Loan not found"}), 404

# routes/payment_routes.py

from flask import Blueprint, request, jsonify
from Models.payment import Payment
from config import get_connection

# Try to import optional service
try:
    from services.payment_service import make_payment
except ImportError:
    make_payment = None

payment_bp = Blueprint('payment_bp', __name__)

# ========== Route: Add Payment (Service Logic or Manual) ==========
@payment_bp.route('/', methods=['POST'])
def pay():
    data = request.get_json()

    # Case 1: Use service if available
    if make_payment:
        loan_id = data.get('loan_id')
        amount = data.get('amount_paid')
        payment_type = data.get('payment_type')

        if not all([loan_id, amount, payment_type]):
            return jsonify({'error': 'Missing required fields'}), 400

        result = make_payment(loan_id, amount, payment_type)
        return jsonify(result), 201

    # Case 2: Use manual insert if full data is provided
    required = ['payment_id', 'loan_id', 'amount_paid', 'payment_type', 'payment_date']
    if not all(k in data for k in required):
        return jsonify({
            'error': 'Missing required fields and payment service is not available'
        }), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payment VALUES (?, ?, ?, ?, ?)
    ''', (
        data['payment_id'], data['loan_id'], data['amount_paid'],
        data['payment_type'], data['payment_date']
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Payment added successfully (manual insert)"}), 201

# ========== Route: Get All Payments ==========
@payment_bp.route('/', methods=['GET'])
def get_payments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment")
    rows = cursor.fetchall()
    conn.close()

    payments = [Payment(*row).to_dict() for row in rows]
    return jsonify(payments)

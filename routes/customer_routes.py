# routes/customer_routes.py

from flask import Blueprint, request, jsonify
from Models.customer import Customer, create_customer
from config import get_connection

# Optional service imports if implemented
try:
    from services.ledger_service import get_ledger
    from services.overview_service import get_account_overview
except ImportError:
    # Fallback if service files don't exist yet
    get_ledger = lambda loan_id: {"ledger": f"Not implemented for {loan_id}"}
    get_account_overview = lambda customer_id: {"overview": f"Not implemented for {customer_id}"}

customer_bp = Blueprint('customer_bp', __name__)

# Route: Add a New Customer 
@customer_bp.route('/', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer_id = data.get('customer_id')
    name = data.get('name')
    email = data.get('email', '')

    if not all([customer_id, name]):
        return jsonify({'error': 'Missing required fields'}), 400

    create_customer(customer_id, name, email)
    return jsonify({'status': 'Customer created successfully'}), 201

#  Route: Get All Customers 
@customer_bp.route('/', methods=['GET'])
def get_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    conn.close()

    customers = [Customer(*row).to_dict() for row in rows]
    return jsonify(customers)

# Route: Account Overview
@customer_bp.route('/<customer_id>/loans', methods=['GET'])
def overview(customer_id):
    result = get_account_overview(customer_id)
    return jsonify(result)

# Route: Ledger View
@customer_bp.route('/ledger/<loan_id>', methods=['GET'])
def ledger(loan_id):
    result = get_ledger(loan_id)
    return jsonify(result)

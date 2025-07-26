# Models/customer.py

from config import get_connection

# Database interaction functions
def create_customer(customer_id, name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO customer (customer_id, name, email) VALUES (?, ?, ?)',
        (customer_id, name, email)
    )
    conn.commit()
    conn.close()

def get_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM customer WHERE customer_id = ?', (customer_id,)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return Customer(*row)
    return None

# Model class
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

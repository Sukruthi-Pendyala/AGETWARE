from flask import Flask
from routes.loan_routes import loan_bp
from routes.payment_routes import payment_bp
from routes.customer_routes import customer_bp
from config import init_db

app = Flask(__name__)

@app.before_request
def initialize():
    if not hasattr(app, 'db_initialized'):
        init_db()
        app.db_initialized = True

app.register_blueprint(loan_bp, url_prefix='/loans')
app.register_blueprint(payment_bp, url_prefix='/payments')
app.register_blueprint(customer_bp, url_prefix='/customers')

if __name__ == '__main__':
    app.run(debug=True)

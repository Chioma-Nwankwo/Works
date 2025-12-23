from flask import Blueprint

customer_bp=Blueprint('customer', __name__, template_folder='templates', static_folder='static')


from app.customer import views

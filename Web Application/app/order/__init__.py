from flask import Blueprint

order_bp=Blueprint('order', __name__, template_folder='templates', static_folder='static')


from app.order import views
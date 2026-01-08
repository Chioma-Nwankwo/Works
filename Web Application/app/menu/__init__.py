from flask import Blueprint

menu_bp=Blueprint('menu', __name__, template_folder='templates', static_folder='static')


from app.menu import views

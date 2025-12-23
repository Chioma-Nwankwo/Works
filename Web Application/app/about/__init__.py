from flask import Blueprint

about_bp=Blueprint('about', __name__, template_folder='templates', static_folder='static')


from app.about import views

from flask import *
from app.home import home_bp


@home_bp.route('/home_list')
def get_home_list():
    return render_template ('home.html')
from flask import *
from app.about import about_bp


@about_bp.route('/about_list')
def get_about_list():
    return render_template ('about.html')
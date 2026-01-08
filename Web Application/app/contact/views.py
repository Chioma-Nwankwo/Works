from flask import *
from app.contact import contact_bp


@contact_bp.route('/contact_list')
def get_contact_list():
    return render_template ('contact.html')
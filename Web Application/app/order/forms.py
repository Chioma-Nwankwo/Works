from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.menu.models import *

class OrderForm(FlaskForm):
    id=HiddenField('id')
    menu_id=SelectField('Select Menu')
    name=StringField('Order Name:', validators=[DataRequired()])
    code=StringField('Order Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.menu_id.choices=[(menu.id, menu.name)for menu in Menu.query.all()]
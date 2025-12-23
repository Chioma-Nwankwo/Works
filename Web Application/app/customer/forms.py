from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.order.models import Order

class CustomerForm(FlaskForm):
    id=HiddenField('id')
    order_id=SelectField('Select Order')
    name=StringField('Customer Name:', validators=[DataRequired()])
    code=StringField('Customer Code:', validators=[DataRequired()])
    price=FloatField('Total Price:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.order_id.choices=[(order.id)for order in Order.query.all()]
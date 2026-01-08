from flask_wtf import *
from wtforms import *
from wtforms.validators import *



class MenuForm(FlaskForm):
    id=HiddenField('id')
    name=StringField('Menu Name:', validators=[DataRequired()])
    code=StringField('Menu Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')
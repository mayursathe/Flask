from wtforms import StringField, PasswordField, validators
from flask_wtf import FlaskForm

class login_check(FlaskForm):
    username = StringField(validators=[validators.DataRequired(),validators.Length(min=1, max=35)])
    password = PasswordField(validators=[validators.DataRequired(),validators.Length(min=8, max=35)])
    email = StringField(validators=[validators.Optional()])


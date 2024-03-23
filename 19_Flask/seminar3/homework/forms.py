from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from .validators import validate_len_80


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), validate_len_80])
    surname = StringField("Surname", validators=[InputRequired(), validate_len_80])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        "New Password",
        [
            InputRequired(),
            EqualTo("confirm", message="Passwords must match"),
            Length(min=6),
        ],
    )
    confirm = PasswordField("Repeat Password")

from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD, PasswordField as PASSWORD_FIELD

class Formularz_Usuwanie_Konta(FLASK_FORM):
    Pole_Hasło_1 = PASSWORD_FIELD("Hasło Hasło", [VALIDATORS.DataRequired(), VALIDATORS.EqualTo("Pole_Hasło_2"), VALIDATORS.length(min=8, max=100)])
    Pole_Hasło_2 = PASSWORD_FIELD("Powtórz Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)])
    Pole_Submit = SUBMIT_FIELD("Wyślij")
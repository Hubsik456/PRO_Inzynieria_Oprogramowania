from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD, StringField as STRING_FIELD, EmailField as EMAIL_FIELD, TextAreaField as TEXTAREA_FIELD

class Formularz_Edycja_Konta(FLASK_FORM):
    Pole_Login = STRING_FIELD("Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)])
    Pole_Email = EMAIL_FIELD("E-Mail", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)])
    Pole_Opis = TEXTAREA_FIELD("Opis")
    Pole_Submit = SUBMIT_FIELD("Wyślij")
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD,  StringField as STRING_FIELD, TextAreaField as TEXTAREA_FIELD

class Nowa_Wiadomość(FLASK_FORM):
    Pole_Treść = TEXTAREA_FIELD("Treść", [VALIDATORS.DataRequired(), VALIDATORS.length(min=3, max=100)])
    Pole_Submit = SUBMIT_FIELD("Wyślij")
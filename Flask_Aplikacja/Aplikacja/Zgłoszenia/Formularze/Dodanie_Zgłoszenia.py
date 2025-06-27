from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD,  StringField as STRING_FIELD, SelectField as SELECT_FIELD

class Dodanie_Zgłoszenia(FLASK_FORM):
    Pole_Tytuł = STRING_FIELD("Tytuł", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)])
    Pole_Kategoria = SELECT_FIELD("Kategoria", [VALIDATORS.DataRequired()])
    Pole_Priorytet = SELECT_FIELD("Priorytet", [VALIDATORS.DataRequired()])
    Pole_Status = SELECT_FIELD("Status", [VALIDATORS.DataRequired()])
    Pole_Submit = SUBMIT_FIELD("Wyślij")
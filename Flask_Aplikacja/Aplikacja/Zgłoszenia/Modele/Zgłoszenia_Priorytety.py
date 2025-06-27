from Aplikacja.Baza_Danych import DB
from sqlalchemy.sql import func as FUNC

class Zgłoszenia_Priorytety(DB.Model):
    __tablename__ = "Zgłoszenia_Priorytety"

    ID = DB.Column(DB.Integer, primary_key=True)
    Nazwa = DB.Column(DB.String(100), nullable=False)
    Opis = DB.Column(DB.Text)

    Zgłoszenie = DB.relationship("Zgłoszenia", back_populates="Priorytet")

    def __repr__(self):
        return f"Zgłoszenie Priorytet --> ID: '{self.ID}'"
from Aplikacja.Baza_Danych import DB
from sqlalchemy.sql import func as FUNC

class Zgłoszenia_Statusy(DB.Model):
    __tablename__ = "Zgłoszenia_Statusy"

    ID = DB.Column(DB.Integer, primary_key=True)
    Nazwa = DB.Column(DB.String(100), nullable=False)
    Opis = DB.Column(DB.Text)

    Zgłoszenie = DB.relationship("Zgłoszenia", back_populates="Status")

    def __repr__(self):
        return f"Zgłoszenie Status --> ID: '{self.ID}'"
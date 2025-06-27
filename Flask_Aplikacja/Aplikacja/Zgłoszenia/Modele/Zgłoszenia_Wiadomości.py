from Aplikacja.Baza_Danych import DB
from sqlalchemy.sql import func as FUNC

class Zgłoszenia_Wiadomości(DB.Model):
    __tablename__ = "Zgłoszenia_Wiadomości"

    ID = DB.Column(DB.Integer, primary_key= True)
    ID_Autor = DB.Column(DB.Integer, DB.ForeignKey("Użytkownicy.ID"), nullable=False)
    ID_Zgłoszenia = DB.Column(DB.Integer, DB.ForeignKey("Zgłoszenia.ID"), nullable=False)
    Treść = DB.Column(DB.Text)
    Data_Utworzenia = DB.Column(DB.DateTime, server_default=FUNC.now(), nullable=False)

    Zgłoszenie = DB.relationship("Zgłoszenia", back_populates="Wiadomość")

    def __repr__(self):
        return f"Zgłoszenie Wiadomość --> ID: {self.ID}"
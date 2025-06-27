from Aplikacja.Baza_Danych import DB
from sqlalchemy.sql import func as FUNC

class Zgłoszenia(DB.Model):
    __tablename__ = "Zgłoszenia"

    ID = DB.Column(DB.Integer, primary_key=True)
    Tytuł = DB.Column(DB.String(250), nullable=False)
    ID_Autor = DB.Column(DB.Integer, DB.ForeignKey("Użytkownicy.ID"), nullable=False)
    Data_Utworzenia = DB.Column(DB.DateTime, server_default=FUNC.now(), nullable=False)
    ID_Kategoria = DB.Column(DB.Integer, DB.ForeignKey("Zgłoszenia_Kategorie.ID"), nullable=False)
    ID_Priorytet = DB.Column(DB.Integer, DB.ForeignKey("Zgłoszenia_Priorytety.ID"), nullable=False)
    ID_Status = DB.Column(DB.Integer, DB.ForeignKey("Zgłoszenia_Statusy.ID"), nullable=False)

    Autor = DB.relationship("Użytkownicy", back_populates="Zgłoszenie")
    Kategoria = DB.relationship("Zgłoszenia_Kategorie", back_populates="Zgłoszenie")
    Priorytet = DB.relationship("Zgłoszenia_Priorytety", back_populates="Zgłoszenie")
    Status = DB.relationship("Zgłoszenia_Statusy", back_populates="Zgłoszenie")
    Wiadomość = DB.relationship("Zgłoszenia_Wiadomości", back_populates="Zgłoszenie")

    def __repr__(self):
        return f"Zgłoszenie --> ID: '{self.ID}'"

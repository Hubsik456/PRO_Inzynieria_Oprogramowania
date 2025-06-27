from Aplikacja.Baza_Danych import DB
from flask_login import UserMixin as USER_MIXIN
from sqlalchemy.sql import func as FUNC

class Użytkownicy(USER_MIXIN, DB.Model):
    __tablename__ = "Użytkownicy"

    ID = DB.Column(DB.Integer, primary_key=True)
    Login = DB.Column(DB.String(100), unique=True, nullable=False)
    Hasło = DB.Column(DB.String(100), nullable=False)
    Email = DB.Column(DB.String(100), unique=True, nullable=False)
    Dodano = DB.Column(DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False)
    ID_Rola = DB.Column(DB.Integer, DB.ForeignKey("Użytkownicy_Role.ID"), server_default="1", nullable=False)
    Opis = DB.Column(DB.Text)

    Zgłoszenie = DB.relationship("Zgłoszenia", back_populates="Autor")
    Rola = DB.relationship("Użytkownicy_Role", back_populates="Użytkownik")

    def get_id(self):
        return self.ID

    def __repr__(self):
        return f"Użytkownik --> ID: '{self.ID}'"
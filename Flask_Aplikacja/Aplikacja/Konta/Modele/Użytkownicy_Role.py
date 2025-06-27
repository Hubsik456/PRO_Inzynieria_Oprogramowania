from Aplikacja.Baza_Danych import DB

class Użytkownicy_Role(DB.Model):
    __tablename__ = "Użytkownicy_Role"

    ID = DB.Column(DB.Integer, primary_key=True)
    Nazwa = DB.Column(DB.String(100), nullable=False)
    Opis = DB.Column(DB.Text)

    Użytkownik = DB.relationship("Użytkownicy", back_populates="Rola")

    def __repr__(self):
        return f"Użytkownik Rola --> ID: '{self.ID}'"
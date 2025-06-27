# Aplication Factory

#! Zewnętrzne Biblioteki
from flask import Flask as FLASK, flash as FLASH, render_template as RENDER_TEMPLATE, request as REQUEST, abort as ABORT
from flask_login import LoginManager as LOGIN_MANAGER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED

#! Lokalne
from Konfiguracja import Konfiguracja
from Aplikacja.Baza_Danych import DB
#from Aplikacja.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Konta.Modele.Użytkownicy import Użytkownicy

#! Funkcje
def create_app(Konfiguracja = Konfiguracja):
    Aplikacja = FLASK(__name__, template_folder="Szablony", static_folder="Statyczne")
    Aplikacja.config.from_object(Konfiguracja)

    #! Baza Danych
    DB.init_app(Aplikacja)

    #! Konta Użytkowników
    #TODO:
    Login_Manager = LOGIN_MANAGER()
    Login_Manager.login_view = "Blueprint_2.Widok_Konta_Logowanie"
    Login_Manager.login_message = "Ta strona jest dostępna tylko dla zalogowanych użytkowników"
    Login_Manager.init_app(Aplikacja)

    @Login_Manager.user_loader
    def load_user(user_id):
        return Użytkownicy.query.get(int(user_id))

    #! BluePrints
    from Aplikacja.Main import Blueprint_1 as Blueprint_Main
    Aplikacja.register_blueprint(Blueprint_Main)

    from Aplikacja.Konta import Blueprint_2 as Blueprint_Konta
    Aplikacja.register_blueprint(Blueprint_Konta)

    from Aplikacja.Zgłoszenia import Blueprint_3 as Blueprint_Zgłoszenia
    Aplikacja.register_blueprint(Blueprint_Zgłoszenia)

    #! Obsługa Błędów
    @Aplikacja.errorhandler(404)
    def Błąd_404(Błąd):
        return RENDER_TEMPLATE("Błąd.html", Komunikat = "404")

    @Aplikacja.errorhandler(500)
    def Błąd_500(Błąd):
        return RENDER_TEMPLATE("Błąd.html", Komunikat = "500")

    return Aplikacja
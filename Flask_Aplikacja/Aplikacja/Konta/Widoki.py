# Ogólne URL'e

#! Zewnętrzne
from flask import render_template as RENDER_TEMPLATE, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, request as REQUEST
from werkzeug.security import check_password_hash as CHECK_PASSWORD_HASH, generate_password_hash as GENERATE_PASSWORD_HASH
from flask_login import login_user as LOGIN_USER, logout_user as LOGOUT_USER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED, current_user as CURRENT_USER

#! Własne
from Aplikacja.Baza_Danych import DB
from Aplikacja.Konta import Blueprint_2
from Aplikacja.Konta.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Konta.Modele.Użytkownicy_Role import Użytkownicy_Role
from Aplikacja.Konta.Formularze.Logowanie import Formularz_Logowanie
from Aplikacja.Konta.Formularze.Rejestracja import Formularz_Rejestracja
from Aplikacja.Konta.Formularze.Usuwanie_Konta import Formularz_Usuwanie_Konta
from Aplikacja.Konta.Formularze.Zmiana_Hasła import Formularz_Zmiana_Hasła
from Aplikacja.Konta.Formularze.Edycja_Konta import Formularz_Edycja_Konta

@Blueprint_2.route("/")
def Widok_Konta():
    return RENDER_TEMPLATE("Konta/index.html")

@Blueprint_2.route("/logowanie/", methods=["POST", "GET"])
def Widok_Konta_Logowanie():
    # TODO: Zrobić redirect jeśli ktoś się już zalogował

    Formularz = Formularz_Logowanie()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Login = Formularz.Pole_Login.data
            _Hasło = Formularz.Pole_Hasło.data

            _Użytkownik = Użytkownicy.query.filter_by(Login = _Login).first()

            if not _Użytkownik or not CHECK_PASSWORD_HASH(_Użytkownik.Hasło, _Hasło):
                FLASH("Taki użytkownik nie istnieje lub podano niepoprawne hasło.")
                return RENDER_TEMPLATE("Konta/Logowanie.html", Formularz = Formularz)

            FLASH(f"Zalogowano jako: {_Użytkownik.Login}")

            LOGIN_USER(_Użytkownik)

            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konta"))

        FLASH("Podano niepoprawne dane.")

    return RENDER_TEMPLATE("Konta/Logowanie.html", Formularz = Formularz)

@Blueprint_2.route("/rejestracja/", methods=["POST", "GET"])
def Widok_Konta_Rejestracja():
    Formularz = Formularz_Rejestracja()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Login = Formularz.Pole_Login.data
            _Hasło = Formularz.Pole_Hasło_1.data
            _Email = Formularz.Pole_Email.data

            _Użytkownik = Użytkownicy.query.filter_by(Login = _Login).first()

            if _Użytkownik: # Jeśli takie kontu już istnieje
                FLASH("Takie konto już istnieje.")
                return RENDER_TEMPLATE("Konta/Rejestracja.html", Formularz = Formularz)

            __Użytkownik = Użytkownicy(Login = _Login, Hasło = GENERATE_PASSWORD_HASH(_Hasło), Email = _Email)
            DB.session.add(__Użytkownik)
            DB.session.commit()

            FLASH("Rejestracja zakończona pomyślnie.")

            LOGIN_USER(__Użytkownik)

            return RENDER_TEMPLATE("Konta/Konto.html")

        FLASH("Podano niepoprawne dane.")

    return RENDER_TEMPLATE("Konta/Rejestracja.html", Formularz = Formularz)

@Blueprint_2.route("/zmiana-hasla/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konta_Zmiana_Hasła():
    Formularz = Formularz_Zmiana_Hasła()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()
            _Stare_Hasło = Formularz.Pole_Stare_Hasło.data
            _Nowe_Hasło = Formularz.Pole_Nowe_Hasło_1.data

            if not _Użytkownik or not CHECK_PASSWORD_HASH(_Użytkownik.Hasło, _Stare_Hasło):
                FLASH("Podano niepoprawne dane.")
                return RENDER_TEMPLATE("Konta/Zmiana_Hasła.html", Formularz = Formularz)

            _Użytkownik.Hasło = GENERATE_PASSWORD_HASH(_Nowe_Hasło)
            DB.session.commit()

            FLASH("Hasło zostało zmienione.")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konta"))

        FLASH("Podano niepoprawne dane.")

    return RENDER_TEMPLATE("Konta/Zmiana_Hasła.html", Formularz = Formularz)

@Blueprint_2.route("/edytuj-konto/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konta_Edycja():
    Formularz = Formularz_Edycja_Konta()
    _Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Użytkownik.Login = Formularz.Pole_Login.data
            _Użytkownik.Email = Formularz.Pole_Email.data
            _Użytkownik.Opis = Formularz.Pole_Opis.data
            DB.session.commit()

            FLASH("Zapisano zmiany konta")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konta"))

        FLASH("Podano niepoprawne dane.")

    Formularz.Pole_Login.data = _Użytkownik.Login
    Formularz.Pole_Email.data = _Użytkownik.Email
    Formularz.Pole_Opis.data = _Użytkownik.Opis

    return RENDER_TEMPLATE("Konta/Edycja.html", Formularz = Formularz)

@Blueprint_2.route("/usun-konto/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konta_Usuń_Konto():
    Formularz = Formularz_Usuwanie_Konta()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()
            _Hasło = Formularz.Pole_Hasło_1.data

            if not _Użytkownik or not CHECK_PASSWORD_HASH(_Użytkownik.Hasło, _Hasło):
                FLASH("Podano niepoprawne hasło.")
                return RENDER_TEMPLATE("Konta/Usuń_Konto.html", Formularz = Formularz)

            Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).delete()
            DB.session.commit()

            FLASH("Twoje konto zostało usunięte.")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konta"))

        FLASH("Podano niepoprawne hasło.")

    return RENDER_TEMPLATE("Konta/Usuń_Konto.html", Formularz = Formularz)

@Blueprint_2.route("/wyloguj/")
@LOGIN_REQUIRED
def Widok_Konta_Wyloguj():
    FLASH("Wylogowano.")
    LOGOUT_USER()

    return REDIRECT(URL_FOR("Blueprint_2.Widok_Konta"))
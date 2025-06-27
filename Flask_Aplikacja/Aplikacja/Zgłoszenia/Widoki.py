# Ogólne URL'e

#! Zewnętrzne
from flask import render_template as RENDER_TEMPLATE, redirect as REDIRECT, url_for as URL_FOR, flash as FLASH, request as REQUEST
from flask_login import login_required as LOGIN_REQUIRED, current_user as CURRENT_USER

#! Własne
from Aplikacja.Baza_Danych import DB
from Aplikacja.Zgłoszenia import Blueprint_3
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia import Zgłoszenia
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Kategorie import Zgłoszenia_Kategorie
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Priorytety import Zgłoszenia_Priorytety
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Statusy import Zgłoszenia_Statusy
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Wiadomości import Zgłoszenia_Wiadomości

from Aplikacja.Zgłoszenia.Formularze.Dodanie_Zgłoszenia import Dodanie_Zgłoszenia
from Aplikacja.Zgłoszenia.Formularze.Nowa_Wiadomość import Nowa_Wiadomość
from Aplikacja.Zgłoszenia.Formularze.Edycja_Zgłoszenia import Edycja_Zgłoszenia

@Blueprint_3.route("/")
def Widok_Zgłoszenia():
    try:
        Dostępne_Zgłoszenia = DB.session.execute(DB.select(Zgłoszenia).order_by(Zgłoszenia.Tytuł)).scalars()

    except Exception as Błąd:
        FLASH(f"Błąd: '{Błąd}'.", "danger")

    return RENDER_TEMPLATE("Zgłoszenia/index.html", Dostępne_Zgłoszenia = Dostępne_Zgłoszenia)

@Blueprint_3.route("/dodaj/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Zgłoszenia_Dodaj_Zgłoszenie():
    Formularz = Dodanie_Zgłoszenia()

    WIP_Kategorie = DB.session.execute(DB.select(Zgłoszenia_Kategorie)).scalars().all()
    Formularz.Pole_Kategoria.choices = [(x.ID, x.Nazwa) for x in WIP_Kategorie]

    WIP_Priorytety = DB.session.execute(DB.select(Zgłoszenia_Priorytety)).scalars().all()
    Formularz.Pole_Priorytet.choices = [(x.ID, x.Nazwa) for x in WIP_Priorytety]

    WIP_Statusy = DB.session.execute(DB.select(Zgłoszenia_Statusy)).scalars().all()
    Formularz.Pole_Status.choices = [(x.ID, x.Nazwa) for x in WIP_Statusy]

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            _Tytuł = Formularz.Pole_Tytuł.data
            _Kategoria = Formularz.Pole_Kategoria.data
            _Priorytet = Formularz.Pole_Priorytet.data
            _Status = Formularz.Pole_Status.data
            _ID_Autora = CURRENT_USER.ID

            Nowe_Zgłoszenie = Zgłoszenia(Tytuł = _Tytuł, ID_Autor = _ID_Autora, ID_Kategoria = _Kategoria, ID_Priorytet = _Priorytet, ID_Status = _Status)

            DB.session.add(Nowe_Zgłoszenie)
            DB.session.commit()

            FLASH("Dodano nowe zgłoszenie", "success")

            return REDIRECT(URL_FOR("Blueprint_3.Widok_Zgłoszenia"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Zgłoszenia/Dodanie_Zgłoszenia.html", Formularz = Formularz)

@Blueprint_3.route("/<int:ID>/")
def Widok_Zgłoszenia_Wyświetl_Zgłoszenie(ID):
    Zgłoszenie = DB.one_or_404(DB.select(Zgłoszenia).filter_by(ID = ID))

    return RENDER_TEMPLATE("Zgłoszenia/Wyświetlenie_Zgłoszenia.html", Zgłoszenie = Zgłoszenie, ID = ID)

@Blueprint_3.route("/<int:ID>/edytuj", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Zgłoszenia_Edytuj(ID):
    Zgłoszenie = DB.one_or_404(DB.select(Zgłoszenia).filter_by(ID = ID))

    Edytowane_Zgłoszenie = Edycja_Zgłoszenia()

    WIP_Kategorie = DB.session.execute(DB.select(Zgłoszenia_Kategorie)).scalars().all()
    Edytowane_Zgłoszenie.Pole_Kategoria.choices = [(x.ID, x.Nazwa) for x in WIP_Kategorie]

    WIP_Priorytety = DB.session.execute(DB.select(Zgłoszenia_Priorytety)).scalars().all()
    Edytowane_Zgłoszenie.Pole_Priorytet.choices = [(x.ID, x.Nazwa) for x in WIP_Priorytety]

    WIP_Statusy = DB.session.execute(DB.select(Zgłoszenia_Statusy)).scalars().all()
    Edytowane_Zgłoszenie.Pole_Status.choices = [(x.ID, x.Nazwa) for x in WIP_Statusy]

    print(f"{Edytowane_Zgłoszenie.Pole_Kategoria=}")
    print(f"{Edytowane_Zgłoszenie.Pole_Kategoria.choices=}")
    print(f"{Edytowane_Zgłoszenie.Pole_Kategoria.default=}")
    print(f"{Edytowane_Zgłoszenie.Pole_Kategoria.data=}")

    if REQUEST.method == "GET":
        Edytowane_Zgłoszenie.Pole_Kategoria.default = str(Zgłoszenie.ID_Kategoria)
        Edytowane_Zgłoszenie.Pole_Kategoria.data = str(Zgłoszenie.ID_Kategoria)

        Edytowane_Zgłoszenie.Pole_Priorytet.default = str(Zgłoszenie.ID_Priorytet)
        Edytowane_Zgłoszenie.Pole_Priorytet.data = str(Zgłoszenie.ID_Priorytet)

        Edytowane_Zgłoszenie.Pole_Status.default = str(Zgłoszenie.ID_Status)
        Edytowane_Zgłoszenie.Pole_Status.data = str(Zgłoszenie.ID_Status)

    if REQUEST.method == "POST":

        if Edytowane_Zgłoszenie.validate_on_submit():
            _Kategoria = Edytowane_Zgłoszenie.Pole_Kategoria.data
            _Priorytet = Edytowane_Zgłoszenie.Pole_Priorytet.data
            _Status = Edytowane_Zgłoszenie.Pole_Status.data

            print(f"{Zgłoszenie=}")

            print(f"{_Kategoria=}")
            print(f"{_Priorytet=}")
            print(f"{_Status=}")

            Zgłoszenie.ID_Kategoria = _Kategoria
            Zgłoszenie.ID_Priorytet = _Priorytet
            Zgłoszenie.ID_Status = _Status

            _Wiadomość = Zgłoszenia_Wiadomości(ID_Autor = CURRENT_USER.ID, ID_Zgłoszenia = ID, Treść = f"Zmodyfikowano zgłoszenie, nowe dane to: {Zgłoszenie.Kategoria.Nazwa}, {Zgłoszenie.Priorytet.Nazwa}, {Zgłoszenie.Status.Nazwa}.")
            DB.session.add(_Wiadomość)

            DB.session.commit()

            FLASH("Zgłoszenie zostało zaktualizowane", "success")

            return REDIRECT(URL_FOR("Blueprint_3.Widok_Zgłoszenia_Wyświetl_Zgłoszenie", ID = ID))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Zgłoszenia/Edytuj_Zgłoszenie.html", Formularz = Edytowane_Zgłoszenie)

@Blueprint_3.route("/<int:ID>/dodaj-wiadomosc/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Zgłoszenia_Nowa_Wiadomość(ID):
    DB.one_or_404(DB.select(Zgłoszenia).filter_by(ID = ID))

    Wiadomość = Nowa_Wiadomość()

    if REQUEST.method == "POST":
        if Wiadomość.validate_on_submit():
            _Treść = Wiadomość.Pole_Treść.data

            _Wiadomość = Zgłoszenia_Wiadomości(ID_Autor = CURRENT_USER.ID, ID_Zgłoszenia = ID, Treść = _Treść)

            DB.session.add(_Wiadomość)
            DB.session.commit()

            FLASH("Dodano nową wiadomość.", "success")

            return REDIRECT(URL_FOR("Blueprint_3.Widok_Zgłoszenia", ID = ID))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Zgłoszenia/Nowa_Wiadomość.html", Formularz = Wiadomość)
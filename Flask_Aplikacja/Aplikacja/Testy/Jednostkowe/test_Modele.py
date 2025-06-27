
#! Zewnętrzne
from werkzeug.security import check_password_hash as CHECK_PASSWORD_HASH, generate_password_hash as GENERATE_PASSWORD_HASH

#! Własne
from Aplikacja.Konta.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Konta.Modele.Użytkownicy_Role import Użytkownicy_Role

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia import Zgłoszenia
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Kategorie import Zgłoszenia_Kategorie
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Priorytety import Zgłoszenia_Priorytety
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Statusy import Zgłoszenia_Statusy
from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Wiadomości import Zgłoszenia_Wiadomości

#! Testy
    #? Użytkownicy
def test_Użytkownicy():
    Użytkownik = Użytkownicy(Login="Login_99999", Hasło=GENERATE_PASSWORD_HASH("Hasło#123"), Email="wip_99999@wip.wip", Opis="Lorem Ipsum")

    assert Użytkownik.ID == None
    assert Użytkownik.Login == "Login_99999"
    assert Użytkownik.Hasło != "Hasło#123"
    assert Użytkownik.Email == "wip_99999@wip.wip"
    assert Użytkownik.ID_Rola == None
    assert Użytkownik.Opis == "Lorem Ipsum"

    assert Użytkownik.Zgłoszenie == []
    assert Użytkownik.Rola == None

def test_Użytkownicy_Role():
    Rola = Użytkownicy_Role(Nazwa="WIP_1", Opis="WIP_2")

    assert Rola.ID == None
    assert Rola.Nazwa == "WIP_1"
    assert Rola.Opis == "WIP_2"

    assert Rola.Użytkownik == []

    #? Zgłoszenia
def test_Zgłoszenia():
    Zgłoszenie = Zgłoszenia(Tytuł="WIP_1")

    assert Zgłoszenie.ID == None
    assert Zgłoszenie.Tytuł == "WIP_1"
    assert Zgłoszenie.ID_Autor == None
    assert Zgłoszenie.ID_Kategoria == None
    assert Zgłoszenie.ID_Priorytet == None
    assert Zgłoszenie.ID_Status == None

    assert Zgłoszenie.Autor == None
    assert Zgłoszenie.Kategoria == None
    assert Zgłoszenie.Priorytet == None
    assert Zgłoszenie.Status == None
    assert Zgłoszenie.Wiadomość == []

def test_Zgłoszenia_Kategorie():
    Kategoria = Zgłoszenia_Kategorie(Nazwa="WIP_1", Opis="WIP_2")

    assert Kategoria.ID == None
    assert Kategoria.Nazwa == "WIP_1"
    assert Kategoria.Opis == "WIP_2"

    assert Kategoria.Zgłoszenie == []


def test_Zgłoszenia_Priorytety():
    Kategoria = Zgłoszenia_Priorytety(Nazwa="WIP_1", Opis="WIP_2")

    assert Kategoria.ID == None
    assert Kategoria.Nazwa == "WIP_1"
    assert Kategoria.Opis == "WIP_2"

    assert Kategoria.Zgłoszenie == []

def test_Zgłoszenia_Statusy():
    Kategoria = Zgłoszenia_Statusy(Nazwa="WIP_1", Opis="WIP_2")

    assert Kategoria.ID == None
    assert Kategoria.Nazwa == "WIP_1"
    assert Kategoria.Opis == "WIP_2"

    assert Kategoria.Zgłoszenie == []

def test_Zgłoszenia_Wiadomości():
    Kategoria = Zgłoszenia_Wiadomości(Treść="WIP_1")

    assert Kategoria.ID == None
    assert Kategoria.Treść == "WIP_1"

    assert Kategoria.Zgłoszenie == None
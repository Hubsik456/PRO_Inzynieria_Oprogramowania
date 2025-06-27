# Blueprint - Konta

Blueprint_Prefix = "/konto"

# ! Index
def test_Widok_Konta_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/")

    assert Odpowiedź.status_code == 200

#! Logowanie
def test_Widok_Konta_Logowanie_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/logowanie/")

    assert Odpowiedź.status_code == 200

def test_Widok_Konta_Logowanie_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/logowanie/")

    assert Odpowiedź.status_code == 200

#! Rejestracja
def test_Widok_Konta_Rejestracja_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/rejestracja/")

    assert Odpowiedź.status_code == 200

def test_Widok_Konta_Rejestracja_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/rejestracja/")

    assert Odpowiedź.status_code == 200

#! Zmiana hasła
def test_Widok_Konta_Zmiana_Hasła_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/zmiana-hasla/")

    assert Odpowiedź.status_code == 302

def test_Widok_Konta_Zmiana_Hasła_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/zmiana-hasla/")

    assert Odpowiedź.status_code == 302

#! Edycja konta
def test_Widok_Konta_Edycja_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/edytuj-konto/")

    assert Odpowiedź.status_code == 302

def test_Widok_Konta_Edycja_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/edytuj-konto/")

    assert Odpowiedź.status_code == 302

#! Usuń konto
def test_Widok_Konta_Usuń_Konto_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/usun-konto/")

    assert Odpowiedź.status_code == 302

def test_Widok_Konta_Usuń_Konto_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/usun-konto/")

    assert Odpowiedź.status_code == 302

#! Wyloguj
def test_Widok_Konta_Wyloguj_Konto_GET(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/usun-konto/")

    assert Odpowiedź.status_code == 302
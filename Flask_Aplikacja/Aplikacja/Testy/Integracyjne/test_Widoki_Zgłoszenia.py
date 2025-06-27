# Blueprint - Testy

Blueprint_Prefix = "/zgloszenia"

# ! Index
def test_Widok_Zgłoszenia_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/")

    assert Odpowiedź.status_code == 200

#! Dodanie zgłoszenia
def test_Widok_Zgłoszenia_Dodaj_Zgłoszenie_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/dodaj/")

    assert Odpowiedź.status_code == 302

def test_Widok_Zgłoszenia_Dodaj_Zgłoszenie_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/dodaj/")

    assert Odpowiedź.status_code == 302

#! Wyświetlenie zgłoszenia
def test_Widok_Zgłoszenia_Wyświetl_Zgłoszenie_GET(Klient):
    Odpowiedź_1 = Klient.get(f"{Blueprint_Prefix}/1")
    Odpowiedź_2 = Klient.get(f"{Blueprint_Prefix}/999")

    assert Odpowiedź_1.status_code == 308
    assert Odpowiedź_2.status_code == 308

#! Edycja Zgłoszenia
def test_Widok_Zgłoszenia_Edytuj_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/1/edytuj/")

    assert Odpowiedź.status_code == 200

def test_Widok_Zgłoszenia_Edytuj_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/1/edytuj/")

    assert Odpowiedź.status_code == 200

#! Dodanie Wiadomości
def test_Widok_Zgłoszenia_Nowa_Wiadomość_GET(Klient):
    Odpowiedź = Klient.get(f"{Blueprint_Prefix}/1/dodaj-wiadomosc/")

    assert Odpowiedź.status_code == 302

def test_Widok_Zgłoszenia_Nowa_Wiadomość_POST(Klient):
    Odpowiedź = Klient.post(f"{Blueprint_Prefix}/1/dodaj-wiadomosc/")

    assert Odpowiedź.status_code == 302
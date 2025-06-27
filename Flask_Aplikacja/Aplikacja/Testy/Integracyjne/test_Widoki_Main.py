# Blueprint - Main

def test_Widok_Index_GET(Klient):
    Odpowiedź = Klient.get("/")

    assert Odpowiedź.status_code == 200

def test_Widok_O_Programie_GET(Klient):
    Odpowiedź = Klient.get("/o-programie/")

    assert Odpowiedź.status_code == 200

def test_Widok_Polityka_Prywatności_GET(Klient):
    Odpowiedź = Klient.get("/polityka-prywatnosci/")

    assert Odpowiedź.status_code == 200
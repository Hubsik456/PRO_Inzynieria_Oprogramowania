from Aplikacja.Baza_Danych import DB

from Aplikacja.Konta.Modele import Użytkownicy
from Aplikacja.Konta.Modele import Użytkownicy_Role

from Aplikacja.Zgłoszenia.Modele import Zgłoszenia
from Aplikacja.Zgłoszenia.Modele import Zgłoszenia_Kategorie
from Aplikacja.Zgłoszenia.Modele import Zgłoszenia_Priorytety
from Aplikacja.Zgłoszenia.Modele import Zgłoszenia_Statusy
from Aplikacja.Zgłoszenia.Modele import Zgłoszenia_Wiadomości

DB.drop_all()
DB.create_all()

from Aplikacja.Konta.Modele.Użytkownicy_Role import Użytkownicy_Role as Rola
Rola_1 = Rola(ID=1, Nazwa="Zgłaszający", Opis="Uprawnienia przeznaczone dla zwykłych użytkowników. Może składać i udzielać się w zgłoszeniach.")
#Rola_2 = Rola(ID=2, Nazwa="Administrator", Opis="Uprawnienia przeznaczone dla administratorów.")
DB.session.add(Rola_1)
#DB.session.add(Rola_2)
DB.session.commit()

from Aplikacja.Konta.Modele.Użytkownicy import Użytkownicy as Użytkownik
Użytkownik_1 = Użytkownik(ID=1, Login="Login_1", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_1@wip.wip")
Użytkownik_2 = Użytkownik(ID=2, Login="Login_2", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_2@wip.wip")
Użytkownik_3 = Użytkownik(ID=3, Login="Login_3", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_3@wip.wip")
DB.session.add(Użytkownik_1)
DB.session.add(Użytkownik_2)
DB.session.add(Użytkownik_3)
DB.session.commit()

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Kategorie import Zgłoszenia_Kategorie as Kategoria
Kategoria_1 = Kategoria(ID=1, Nazwa="Ogólne")
Kategoria_2 = Kategoria(ID=2, Nazwa="Strony Internetowe")
Kategoria_3 = Kategoria(ID=3, Nazwa="Sprzęt")
Kategoria_4 = Kategoria(ID=4, Nazwa="Oprogramowanie")
Kategoria_5 = Kategoria(ID=5, Nazwa="Licencje")
Kategoria_6 = Kategoria(ID=6, Nazwa="Inne")
DB.session.add(Kategoria_1)
DB.session.add(Kategoria_2)
DB.session.add(Kategoria_3)
DB.session.add(Kategoria_4)
DB.session.add(Kategoria_5)
DB.session.add(Kategoria_6)
DB.session.commit()

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Priorytety import Zgłoszenia_Priorytety as Priorytet
Priorytet_1 = Priorytet(ID=1, Nazwa="Natychmiastowy")
Priorytet_2 = Priorytet(ID=2, Nazwa="Wysoki")
Priorytet_3 = Priorytet(ID=3, Nazwa="Średni")
Priorytet_4 = Priorytet(ID=4, Nazwa="Niski")
Priorytet_5 = Priorytet(ID=5, Nazwa="Bardzo Niski")
DB.session.add(Priorytet_1)
DB.session.add(Priorytet_2)
DB.session.add(Priorytet_3)
DB.session.add(Priorytet_4)
DB.session.add(Priorytet_5)
DB.session.commit()

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Statusy import Zgłoszenia_Statusy as Status
Status_1 = Status(ID=1, Nazwa="Nowe")
Status_2 = Status(ID=2, Nazwa="W trakcie")
Status_3 = Status(ID=3, Nazwa="Zakończone")
Status_4 = Status(ID=4, Nazwa="Archiwum")
DB.session.add(Status_1)
DB.session.add(Status_2)
DB.session.add(Status_3)
DB.session.add(Status_4)
DB.session.commit()

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia import Zgłoszenia as Zgłoszenie
Zgłoszenie_1 = Zgłoszenie(ID=1, Tytuł="Zgłoszenie #1", ID_Autor=1, ID_Kategoria=1, ID_Priorytet=1, ID_Status=1)
Zgłoszenie_2 = Zgłoszenie(ID=2, Tytuł="Zgłoszenie #2", ID_Autor=3, ID_Kategoria=1, ID_Priorytet=2, ID_Status=1)
Zgłoszenie_3 = Zgłoszenie(ID=3, Tytuł="Zgłoszenie #3", ID_Autor=2, ID_Kategoria=2, ID_Priorytet=3, ID_Status=1)
Zgłoszenie_4 = Zgłoszenie(ID=4, Tytuł="Zgłoszenie #4", ID_Autor=3, ID_Kategoria=3, ID_Priorytet=1, ID_Status=1)
Zgłoszenie_5 = Zgłoszenie(ID=5, Tytuł="Zgłoszenie #5", ID_Autor=1, ID_Kategoria=3, ID_Priorytet=4, ID_Status=3)
Zgłoszenie_6 = Zgłoszenie(ID=6, Tytuł="Zgłoszenie #6", ID_Autor=1, ID_Kategoria=1, ID_Priorytet=5, ID_Status=2)
Zgłoszenie_7 = Zgłoszenie(ID=7, Tytuł="Zgłoszenie #7", ID_Autor=2, ID_Kategoria=2, ID_Priorytet=1, ID_Status=4)
Zgłoszenie_8 = Zgłoszenie(ID=8, Tytuł="Zgłoszenie #8", ID_Autor=1, ID_Kategoria=1, ID_Priorytet=1, ID_Status=1)
DB.session.add(Zgłoszenie_1)
DB.session.add(Zgłoszenie_2)
DB.session.add(Zgłoszenie_3)
DB.session.add(Zgłoszenie_4)
DB.session.add(Zgłoszenie_5)
DB.session.add(Zgłoszenie_6)
DB.session.add(Zgłoszenie_7)
DB.session.add(Zgłoszenie_8)
DB.session.commit()

from Aplikacja.Zgłoszenia.Modele.Zgłoszenia_Wiadomości import Zgłoszenia_Wiadomości as Wiadomość
Wiadomość_1 = Wiadomość(ID=1, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #1")
Wiadomość_2 = Wiadomość(ID=2, ID_Autor=2, ID_Zgłoszenia=1, Treść="Wiadomość #2")
Wiadomość_3 = Wiadomość(ID=3, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #3")
Wiadomość_4 = Wiadomość(ID=4, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #4")
Wiadomość_5 = Wiadomość(ID=5, ID_Autor=3, ID_Zgłoszenia=2, Treść="Wiadomość #5")
Wiadomość_6 = Wiadomość(ID=6, ID_Autor=1, ID_Zgłoszenia=2, Treść="Wiadomość #6")
Wiadomość_7 = Wiadomość(ID=7, ID_Autor=2, ID_Zgłoszenia=2, Treść="Wiadomość #7")
Wiadomość_8 = Wiadomość(ID=8, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #8")
Wiadomość_9 = Wiadomość(ID=9, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #9")
Wiadomość_10 = Wiadomość(ID=10, ID_Autor=3, ID_Zgłoszenia=3, Treść="Wiadomość #10")
Wiadomość_11 = Wiadomość(ID=11, ID_Autor=1, ID_Zgłoszenia=3, Treść="Wiadomość #11")
Wiadomość_12 = Wiadomość(ID=12, ID_Autor=1, ID_Zgłoszenia=3, Treść="Wiadomość #12")
Wiadomość_13 = Wiadomość(ID=13, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #13")
Wiadomość_14 = Wiadomość(ID=14, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #14")
Wiadomość_15 = Wiadomość(ID=15, ID_Autor=1, ID_Zgłoszenia=1, Treść="Wiadomość #15")
DB.session.add(Wiadomość_1)
DB.session.add(Wiadomość_2)
DB.session.add(Wiadomość_3)
DB.session.add(Wiadomość_4)
DB.session.add(Wiadomość_5)
DB.session.add(Wiadomość_6)
DB.session.add(Wiadomość_7)
DB.session.add(Wiadomość_8)
DB.session.add(Wiadomość_9)
DB.session.add(Wiadomość_10)
DB.session.add(Wiadomość_11)
DB.session.add(Wiadomość_12)
DB.session.add(Wiadomość_13)
DB.session.add(Wiadomość_14)
DB.session.add(Wiadomość_15)
DB.session.commit()

exit()

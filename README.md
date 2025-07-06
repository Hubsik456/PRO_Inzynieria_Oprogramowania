# PRO Inżynieria Oprogramowania

Hubert Michna, w67259

## Jak uruchomić tę aplikacje?

1. Upewnić się że na komputerze jest zainstalowany Python, najlepiej w wersji 3.13.
2. Pobrać to repozytorium, i wypakować do jakiegoś folderu.
3. Wejść do tego wypakowanego folderu. Wykonać polecenie `python -m venv "ŚCIEŻKA"`.
4. Teraz w tym folderze powinny się znajdować następujące foldery/pliki `Flask_Aplikacja`, `requirements.txt`, `Include`, `Lib`, `Scripts`, `pyvenv.cfg`
5. Wykonać polecenie `.\Scripts\activate` aby aktywować venv.
6. Zainstalować niezbędne biblioteki poleceniem `pip install -r requirements.txt`.
7. Uruchomienie aplikacji `cd .\Flask_Aplikacja\ | flask run`.
8. Otworzyć w przeglądarce stronę `http://127.0.0.1:5004`.


#! Zewnętrzne
import pytest as PYTEST
from Konfiguracja import Konfiguracja

#! Własne
from Aplikacja import create_app

@PYTEST.fixture(scope="module")
def Klient():
    Aplikacja = create_app()
    Aplikacja.config.from_object(Konfiguracja)

    with Aplikacja.test_client() as Test_Klient:
        with Aplikacja.app_context():
            yield Test_Klient
#! BluePrint #2 - Zgłoszenia

#! Zewnętrzne Biblioteki
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_3 = BLUEPRINT("Blueprint_3", __name__, url_prefix="/zgloszenia")

from Aplikacja.Zgłoszenia import Widoki
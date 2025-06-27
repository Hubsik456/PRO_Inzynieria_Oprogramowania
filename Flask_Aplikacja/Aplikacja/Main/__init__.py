# Blueprint #1 - Main

#! Zewnętrzne Biblioteki
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_1 = BLUEPRINT("Blueprint_1", __name__)

from Aplikacja.Main import Widoki
from Aplikacja.Main import Filtry
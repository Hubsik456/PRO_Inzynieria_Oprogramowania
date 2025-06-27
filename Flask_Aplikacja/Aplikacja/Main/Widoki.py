# Ogólne URL'e

#! Zewnętrzne
from flask import render_template as RENDER_TEMPLATE

#! Własne
from Aplikacja.Main import Blueprint_1

@Blueprint_1.route("/")
def Widok_Index():
    return RENDER_TEMPLATE("Main/index.html")

@Blueprint_1.route("/o-programie/")
def Widok_O_Programie():
    return RENDER_TEMPLATE("Main/O_Programie.html")

@Blueprint_1.route("/polityka-prywatnosci/")
def Widok_Polityka_Prywatności():
    return RENDER_TEMPLATE("Main/Polityka_Prywatności.html")
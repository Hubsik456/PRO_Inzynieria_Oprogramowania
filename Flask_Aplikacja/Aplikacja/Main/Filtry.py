# Filtry do wykorzystania w szablonach Jinja2
#! Zewnętrzne
from datetime import datetime as DATETIME # https://strftime.org/

#! Własne
from Aplikacja.Main import Blueprint_1

@Blueprint_1.app_template_filter("Filtr_Null")
def Filtr_Null(Input):
    Input = str(Input)

    if Input == "None":
        return "Brak"
    else:
        return Input

@Blueprint_1.app_template_filter("Filtr_Data_Godzina")
def Filtr_Data_Godzina(Input):
    Input = DATETIME.strftime(Input, "%d.%m.%Y, %H:%M:%S")

    return Input
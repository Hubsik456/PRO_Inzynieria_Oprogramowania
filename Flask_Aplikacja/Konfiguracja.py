# Plik z konfiguracją

#! Zewnętrzne Biblioteki
import os as OS
from dotenv import load_dotenv as LOAD_DOTENV

#! Main
LOAD_DOTENV()

Ścieżka = OS.path.abspath(OS.path.dirname(__file__))

class Konfiguracja():
    SECRET_KEY = OS.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = OS.environ.get('DATABASE_URI') or 'sqlite:///' + OS.path.join(Ścieżka, 'Baza_Danych.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = OS.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
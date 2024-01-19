"""Aufgabe 2: Eingebaute Module

    Python kommt mit vielen eingebauten Modulen. Wir können diese
    jederzeit zum programmieren nutzen! Hier ein paar Beispiele:

        math     -> Komplexere mathematische Funktionen
        datetime -> Uhrzeit, Kalender, Zeitzonen usw
        platform -> Alles zum Betriebssystem

    Um diese sogenannten Built-In Module zu importieren, müssen wir
    weder eine Datei erstellen noch wissen wo sich die dazugehörige
    Python-Datei befindet. Einfach importieren und fertig:

        import math

    Ist der Name des Moduls zu lang, können wir einen Alias benutzen:

        import platform as p

    Nun können wir Variablen und Funktionen mit dem Alias aufrufen:

        p.system()

    In dieser Aufgabe nutzen wir das Modul random
    um ein kleines Spiel zu programmieren!
"""

# random ist ein Built-In Modul von Python um Zufallszahlen zu erzeugen.
import random as r

print("Zahlen raten")
print("------------")

# Hier speichern wir eine zufällige Zahl zwischen 1 und 10 ab.
zahl = r.randint(1, 10)

vermutung = int(input("Welche Zahl zwischen 1 und 10 wurde gewählt? "))

# TODO Prüfe ob deine Vermutung gleich der zufälligen Zahl ist
# Falls ja: Gib die Nachricht "Treffer!" aus.
# Falls nein: Gib die Nachricht "Kein Treffer!" aus.

# TODO Frage jetzt den Spieler ob er weiterspielen will.
# Falls ja: Spiele eine weitere Runde.
# Falls nein: Beende das Spiel.

# TODO Erstelle ein Modul mit dem Namen zahlen_raten und
# kopiere dein Spiel in die Funktion spielen().
# Importiere dann dein Modul und rufe es hier auf!

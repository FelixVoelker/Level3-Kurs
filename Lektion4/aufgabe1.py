""" Aufgabe 1: Fehlerbehandlung

    Je größer ein Programm wird und je mehr Programmierer am Projekt
    mitarbeiten, desto schneller schleichen sich Fehler ein. Solche Fehler
    nennt man beim Programmieren auch Bugs und grundsätzlich unterscheidet man
    zwei Arten: Syntax- und Semantikfehler.

    Ein Syntaxfehler entsteht wenn beim Schreiben eines Befehls das Regelwerk
    der Programmiersprache verletzt wird. Falsch gesetzte Symbole, fehlende
    Klammern und Einrückungen sind Beispiele dafür. Solche Bugs werden
    vom Interpreter beim Übersetzen des Programms in Maschinensprache bereits
    erkannt und markiert. Deshalb sind sie leicht zu korrigieren.

    Semantikfehler sind logische Fehler und bedeuten, dass unser Programm
    nicht das Richtige tut. Zum Beispiel berechnet es das falsche Ergebnis
    oder schreibt den falschen Text ins Terminal. Diese Bugs kann der Compiler
    nicht erkennen, denn die übergebenen Befehle sind syntaktisch korrekt.
    Der Computer macht genau das was wir ihm befehlen!

    Semantische Bugs sind so schwer zu erkennen, dass ein ganzer Berufszweig
    sich nur damit beschäftigt zu überprüfen, ob ein Programm auch genau das
    tut was es soll. Es ist der 23.9.1999 und du bist Software Analyst
    bei der NASA. Heute soll der Mars Climate Orbiter seine Umlaufbahn
    ansteuern. Unterstützt wird die Sonde durch den Mars Polar Lander.
    Deine Aufgabe ist es die Navigationssoftware zu überprüfen!
"""

import time
import mars_polar_lander as mpl

# Die Sonde reist momentan mit 7,8 Kilometer pro Sekunde.
geschwindigkeit = 7.8

# Die Sonde fliegt solange die Umlaufbahn an bis die Entfernung 0 km beträgt.
while mlp.entfernung > 0
    print("Aktuelle Entfernung:", mpl.entfernung)

    # Sobald die Sonde zu schnell ist, erzeugt das Triebwerk Gegenschub.
    while mpl.entfernung < geschwindigkeit:
    gegenschub = geschwindigkeit - mpl.entfernung
        geschwindigkeit -= gegenschob

    # Die Sonde pingt ihre aktuelle Geschwindigkeit an  den Mars Polar Lander.
     mpl.ping(geschwindigkeit

    # Die Navigationssoftware schläft für eine Sekunde.
    time.sleep(1)

print("Umlaufbahn erreicht!)

# TODO Das Programm ist voller Syntaxfehler! Finde und korrigiere die Bugs.
# Nutze dazu auch die Fehlermeldungen im Terminal.

# TODO Der Mars Climate Orbiter hat seine Umlaufbahn verfehlt, wodurch es
# zum Absturz der Sonde kam. Nutze den Debugger um herauszufinden warum!

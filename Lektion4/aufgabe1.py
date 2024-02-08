""" Aufgabe 1: Fehlerbehandlung

    Je größer ein Programm wird und je mehr Programmierer am Projekt
    mitarbeiten, desto schneller schleichen sich Fehler ein. Solche Fehler
    nennt man beim Programmieren auch Bugs und grundsätzlich unterscheidet man
    zwei Arten: Syntax- und Semantikfehler.

    Ein Syntaxfehler entsteht wenn beim Schreiben eines Befehls das Regelwerk
    der Programmiersprache verletzt wird. Falsch gesetzte Symbole, fehlende
    Klammern und Einrückungen sind Beispiele dafür. Solche Bugs werden
    vom Compiler beim Übersetzen des Programms in Maschinensprache bereits
    erkannt und markiert. Deshalb sind sie leicht zu korrigieren.

    Semantikfehler sind logische Fehler und bedeuten, dass unser Programm
    nicht das Richtige tut. Zum Beispiel berechnet es das falsche Ergebnis
    oder schreibt den falschen Text ins Terminal. Diese Bugs kann der Compiler
    nicht erkennen, denn die übergebenen Befehle sind syntaktisch korrekt.
    Der Computer macht genau das was wir ihm befehlen!

    Semantische Bugs sind so schwer zu erkennen, dass ein ganzer Berufszweig
    sich nur damit beschäftigt zu überprüfen, ob ein Programm auch genau das
    tut was es soll.

    Es ist das Jahr 1996 und du bist Software Analyst der Europäischen
    Weltraumorganisation (ESA). Kürzlich wurden Änderungen am Programm des
    Bordcomputers der Ariane 5 Trägerrakete vorgenommen. Dein Job ist es das
    Programm bis zum morgigen Start zu korrigieren.
"""


# Wandelt eine ganze Zahl auf ihre 16-bit Representation um [-32768, 32767].
def int16(zahl):
    binaerzahl = bin(zahl)
    if len(binaerzahl) >= 18:
        binaerzahl = "-0b" + binaerzahl[-15:]
    return int(binaerzahl, 2)


print(int16(32769))

""" Aufgabe 3: Exceptions und Iteratoren

    Python besitzt Built-In Klassen die wir bereits genutzt haben.
    Wenn ein Crash ein Programm beendet, dann erstellt Python ein Objekt
    der Klasse Exception. Spezielle Exceptions wie NameError und TypeError
    sind lediglich Kindklassen davon. Wir können also durch Vererbung unsere
    eigenen Fehlercodes erstellen und diese durch raise auslösen.

    Erinnere dich an die Regel, dass die for-loop in Python eine Liste
    Element für Element durchläuft. Nun das ist zwar richtig aber nicht
    die ganze Wahrheit. Denn die Python for-loop erwartet ein iterierbares
    Objekt, z.b. Listen und Dictionaries. Diese können nur deswegen durchlaufen
    werden, weil sie die Methode __iter__ besitzen und damit ein Objekt
    der Klasse Iterator der Schleife übergeben. Jedes Objekt mit dieser Methode
    kann also mit der for-loop abgelaufen werden.

    Iteratoren besitzen die Methode __next__ und sagen damit der Schleife,
    welches Element als nächstes an der Reihe ist. Gäbe es immer ein nächstes
    Element so wäre die for-loop auch eine Endlosschleife. Durch das Auslösen
    der StopIteration Exception kann der Iterator jedoch beendet werden.

    Beenden wir nun die Entwicklung des Rollenspiels "Die Schlacht der
    vier Helden":

        1.  Der Spieler wählt zwei Helden für sein Team und der Computer wählt
            zwei Helden zufällig aus.
        2.  In jeder Runde wird die Reihenfolge der Helden zufällig bestimmt
            und die Runde endet sobald alle Helden einmal am Zug waren.
        3.  Ein Held kann in seinem Zug entweder angreifen oder
            sich verteidigen. Sobald er 0 LP hat, kommt er nicht mehr zum Zug.
        4.  Bei Rundenende nehmen alle Helden Schaden mit negativen DMG.
            Ihre LP reduzieren sich um den DMG Wert.
        5.  Das Spiel endet sobald alle Helden eines Teams besiegt wurden.
"""

from aufgabe2 import Ritter, Jaeger, Magier, Heiler

# TODO Erstelle eine Klasse DieSchlachtDerVierHelden und verwende __init__ um
# die Startbedingungen des Spiels umzusetzen.

# TODO Erstelle deine eigene Exception und fange alle fehlerhaften Eingaben
# des Spielers ab. Gib eine Warnung aus und beende das Spiel.

# TODO Gib der Klasse die Methode zug_spieler(held) und teile dem Spieler mit
# welcher Held am Zug ist. Lass den Spieler entscheiden ob der Held angreifen
# oder sich verteidigen soll. Bei Angriff lass den Spieler das Ziel wählen!

# TODO Gib der Klasse die Methode zug_gegner(held) und lasse den Computer
# zufällig entscheiden ob angegriffen oder verteidigt wird. Bei Angriff wähle
# einen Helden des Spielers zufällig aus!

# TODO Verwandele das Objekt der Klasse DieSchlachtDerVierHelden in ein
# iterierbares Objekt. Implementiere dafür die magische Funktion __iter__
# und gib die Selbstreferenz auf das Objekt dieser Klasse zurück.
# Unser Objekt wird damit selbst zum Iterator.

# TODO Implementiere die magische Funktion __next__ und gib den Helden zurück,
# der als nächstes an der Reihe ist. Beachte dabei die Spielregeln!
# Pro Runde ist jeder Held einmal dran, die Rehenfolge ist zufällig und
# das Spiel endet sobald ein Team besiegt ist!

# TODO Teile dem Spieler nach Spielende das Ergebnis der Partie mit!

# TODO BONUS: Gib dem Computer eine einfache Form von künstlicher Intelligenz.
# Verwende dafür die <-Operatoren und folgende Idee eines Greedy-Algorithmus:
#   - Ritter: Verteidigt sich sobald ein Gegner ihn besiegen könnte.
#   - Jäger: Greift immer den schwächsten Gegner an.
#   - Magier: Greift den Gegner mit höchster Verteidigungkraft an.
#   - Heiler: Heilt immer den Helden mit den niedrigsten LP.

# TODO BONUS: Baue deine eigene Rolle eines Helden in das Spiel ein!

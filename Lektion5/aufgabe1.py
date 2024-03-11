""" Aufgabe 1: Klassen und Objekte

    Die meisten Programmierer verbringen ihren beruflichen Alltag damit
    komplexe Softwaresysteme zu entwickeln. Ob es sich dabei um ein
    Computerspiel, die Verwaltungssoftware eines Krankenhauses oder
    das Navigationsmodul einer Rakete handelt, spielt keine Rolle.
    Alle diese Programme basieren auf dem Prinzip der
    Objektorientierten Programmierung.

    In dieser Art zu Programmieren verhalten wir uns wie Architekten.
    Diese entwickeln üblichweise Entwürfe zum Bau eines Gebäudes.
    In dem Entwurf wird beschrieben wie ein Gebäude auszusehen hat und
    wie es gebaut werden soll. Das Bauunternehmen kann dann mit dem Entwurf
    nicht nur ein Gebäude bauen, sondern so viele es möchte. Vorausgesetzt der
    Bau ist an dem gewählten Ort möglich.

    Ein Software-Architekt entwickelt ebenfalls Entwürfe jedoch von Daten-
    modellen. Dieser Entwurf enthält Informationen über Variablen oder
    Funktionen, die im Datenmodell enthalten sein müssen. Man bezeichnet den
    Entwurf auch als Klasse und schreibt ihn so:

        class Haus:
            pass

    Eine Klasse ist wie der Entwurf des Gebäudes nur die Vorlage. Genau wie
    durch den Bau das Gebäude erst entsteht, erstellen wir aus der Klasse ein
    Objekt (oder auch Instanz genannt) mit dem Konstruktor:

        Haus()

    Die Klasse ist also der Entwurf, das Objekt das gebaute Gebäude und der
    Konstruktor das Bauunternehmen. Nur liegt unser Haus jetzt im Arbeits-
    speicher und steht nicht an einer Straße.

    Du bist Softwareentwickler und dein Kunde hat dich mit der Entwicklung
    des Rollenspiels "Die Schlacht der vier Helden" beauftragt. In dieser
    Aufgabe wirst du das Programm nach seinen Vorstellungen entwerfen:

        1. Der Spieler soll mit einer Gruppe aus zwei Helden gegen ein
           gegnerisches Team antreten.
        2. Jeder Held besitzt Lebenspunkte (LP), Angriffskraft (ATK),
           Verteidigungskraft (VRT) und Schaden (DMG).
        3. In jedem Zug darf jeder Held einmal entweder angreifen (attack)
           oder sich verteidigen (defend).
"""

# TODO Erstelle die Klasse Held und gib ihr die genannten Variablen mit
# den Standardwerten 10 LP, 3 ATK, 2 VRT, 0 DMG.

# TODO Verwende jetzt den Konstruktor um 2 Helden zu erstellen.
# Lass dir die LP beider Helden im Terminal ausgeben!

# TODO Es gibt zwei Arten von Variablen in Objektorientierter Programmierung:
#      -> Klassenvariablen: Verändere die LP mit Held.lp = 15.
#                           Untersuche die LP beider Helden.
#      -> Instanzvariablen: Setze die LP von Held 2 auf 20.
#                           Was stellst du fest?

# TODO Der Konstruktor ruft die magische Funktion __init__ auf um
# das Objekt zu erstellen und Variablen einen Wert zuzuweisen.
# Gib der Klasse Held die Option mit anderen Startwerten für LP, ATK und VRT
# initialisiert zu werden.

# TODO Mit der magische Funktion __str__ können wir das Objekt in einen
# String umwandeln. Gib so die aktuellen LP des Helden aus.

# TODO Die Funktionen eines Objekts nennt man Methoden und der Held bekommt:
#      -> attack: Greift den gewählten Helden an und reduziert
#                 DMG des Angegriffenen um ATK.
#      -> defend: Verteidigt sich gegen Angriffe anderer Helden
#                 und addiert VRT auf DMG.

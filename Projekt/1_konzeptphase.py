""" Tag 1: Konzeptphase und Prototyping

    Ein Projekt beginnt immer mit einer Konzeptphase.
    Hier fasst der Entwickler alle seine Ideen zusammen und
    schreibt sie auf. Moderne Programmierer entwerfen dabei
    die Anforderungen an ihr Programm immer aus Sicht des Nutzers.

    Moderne Softwareentwicklung erkennt man also immer daran, dass
    Merkmale (Features) eines Programms wie eine Geschichte ausformuliert
    werden. Agile Softwareentwickler nennen eine Anforderung deswegen
    auch Story. Hier das Beispiel aus der letzten Lektion:

    1. Der Spieler soll mit einer Gruppe aus zwei Helden gegen ein
       gegnerisches Team antreten.
    2. Jeder Held besitzt Lebenspunkte (LP), Angriffskraft (ATK),
       Verteidigungskraft (VRT) und Schaden (DMG).
    3. In jedem Zug darf jeder Held einmal entweder angreifen (attack)
       oder sich verteidigen (defend).
    4. Das Spiel soll vier Rollen von Helden besitzen: Ritter, Jäger,
       Magier und Heiler.
    5. Der Ritter hat 5 VRT, der Jäger 4 ATK, der Magier 2 ATK und
       der Heiler 1 ATK.
    6. Der Magier ignoriert beim Angriff die VRT des Gegners.
    7. Der Heiler verursacht keinen Schaden sondern heilt beim Angriff
       den anderen Helden.
    8. Der Spieler wählt zwei Helden für sein Team und der Computer wählt
       zwei Helden zufällig aus.
    9. In jeder Runde wird die Reihenfolge der Helden zufällig bestimmt
       und die Runde endet sobald alle Helden einmal am Zug waren.
    10. Ein Held kann in seinem Zug entweder angreifen oder
        sich verteidigen. Sobald er 0 LP hat, kommt er nicht mehr zum Zug.
    11. Bei Rundenende nehmen alle Helden Schaden mit negativen DMG.
        Ihre LP reduzieren sich um den DMG Wert.
    12. Das Spiel endet sobald alle Helden eines Teams besiegt wurden.

    Sobald du einen groben Überblick über dein Projekt hast, fängst du an
    deine Ideen auszuprobieren. Du versuchst also Teile des Projekts
    zu programmieren und findest dabei heraus ob und wie du ein Feature
    im Programm umsetzen kannst. Diese Phase nennt man Prototyping.
"""

# TODO Importiere pygame und erstelle ein leeres Spielfenster.

# TODO Implementiere den Prototyp deiner Game Loop.
# Beende das Spiel durch das Schließen des Fensters.

# TODO Zeichne ein prototypisches Level deines Spiels.
# Färbe dafür die Pixel des Bildschirms mithilfe von RGB-Werten
# (Rot-Grün-Blau) ein.

# TODO Bring nun 2D-Grafik in dein Level! Lade eine Bilddatei
# aus dem Ordner assets und zeichne das Bild auf den Bildschirm.

# TODO Versuche die Zeichnung deines Levels pro Frame zu ändern und damit
# eine Animation zu erzeugen!

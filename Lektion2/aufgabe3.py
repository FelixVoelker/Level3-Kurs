""" Aufgabe 3: PIP

    Nicht alle Module in Python sind sofort verfügbar.
    Manche müssen erst installiert werden!

    Diese Aufgabe erfüllt der Paketmanager PIP für uns. Die Begriffe
    Pakete und Module werden häufig in Python ähnlich verwendet.
    Ein Paket enthält jedoch meist noch weitere Dateien. Im Terminal
    können wir ein Modul so installieren:

        pip install pygame

    Mit pygame kannst du deine eigenen Spiele in Python entwickeln.
    Lass uns jedoch zuerst in dieser Aufgabe schauen, welche Beispiele
    in dem Modul bereits vorprogrammiert sind. Dafür werden wir
    auf Teilmodule von pygame zugreifen:

        from modul import teilmodul

"""

# Importiert das Teilmodul aliens vom Modul pygame.examples.
from pygame.examples import aliens

# Startet das Spiel Aliens.
aliens.main()

# TODO Ersetze den Funktionsaufruf aliens.main() durch aliens().

# TODO In pygame.examples gibt es noch ein Spiel.
# Importiere chimp und rufe es mit chimp.main() auf!

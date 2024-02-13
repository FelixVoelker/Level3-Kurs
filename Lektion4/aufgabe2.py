""" Aufgabe 2: Crashes

    Semantikfehler können nicht nur unerwünschtes Verhalten auslösen,
    sondern auch große Schäden verursachen. Darunter Schäden am Computer,
    finanzielle Verluste eines Unternehmens oder Verletzungen von Menschen.

    Um diese Probleme zu verhindern, kann die Ausführung eines Programms
    geplant oder ungeplant beendet werden. Man spricht auch von einem Absturz
    oder Crash des Programms. Ob der Entwickler eine Nutzung des Programms
    absichern oder beim Schreiben nicht alle Bugs gefunden hat, macht hier
    keinen Unterschied. Ein Crash tritt immer zur Laufzeit des Programms auf
    und beendet ein ungewolltes Verhalten. Damit ist er ein wichtiges
    Hilfsmittel um die Sicherheit zu erhöhen.

    Wir können einen Teil unseres Programms auf Fehler testen, die einen
    Crash auslösen könnten. Dafür wird in den **try** Block das zu testende
    Segment geschrieben. Wenn der Code fehlerfrei durchläuft, verlässt der
    Interpreter den Block. Tritt jedoch ein Fehler auf, springt er in
    den **except** Block. Dort können wir den Fehler beheben
    oder das Programm sicher beenden:

        try:
            print("Hier steht der zu testende Code!")
        except:
            print("Ein Fehler ist aufgetreten! Hier kannst du Fehler beheben.")

    4. Juni 1996, Französisch Guyana. Die Europäische Weltraumorganisation
    (ESA) startet heute ihre neu entwickelte Trägerrakete mit vier Satelliten
    an Bord. Der Bordcomputer der Ariane 5 stammt noch von ihrer Vorgängerin
    und sorgt nach 36,7 Sekunden dafür, dass die Rakete explodiert.
    Was ist passiert?
"""

import time
from cast_to_int import int16

print("Ariane 5 - LIFT OFF")

horizontale_geschwindkeit = 0.0

# Simuliere den Flug über 40 Sekunden.
for sekunde in range(40):

    # Prüfe ob die Geschwindigkeit negativ ist, dann breche den Start ab.
    if int16(horizontale_geschwindkeit) < 0:
        print("Countdown abgebrochen! Neustarten...")
        exit()

    print("Sekunde", sekunde, "aktuelle Geschwindigkeit:",
          horizontale_geschwindkeit)

    # Die Ariane 5 beschleunigt um 910.22 Meter pro Sekunde.
    horizontale_geschwindkeit += 910.22

    time.sleep(1)

# TODO Nach 36 Sekunden stürzt das Programm ab. Finde die problematische Zeile!
# Warum kam es zum Crash?

# TODO Die Entwickler der Ariane 5 gingen nicht davon aus, dass die Rakete so
# schnell fliegen würde. Sichere die problematische Typumwandlung mithilfe von
# **try** und **except** ab.

# TODO Korrigiere nun die problematische Zeile und füge ein **else** hinter
# den **except** Block ein, um zu testen ob dein Code fehlerfrei durchläuft.

# TODO Ersetze das **else** durch ein **finally**. Was ändert sich dadurch?

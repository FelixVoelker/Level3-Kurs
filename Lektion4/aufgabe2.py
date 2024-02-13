""" Aufgabe 2: Crashes

    Semantikfehler können nicht nur unerwünschtes Verhalten auslösen,
    sondern auch große Schäden verursachen. Darunter Schäden am Computer,
    finanzielle Verluste eines Unternehmens oder das Verletzen von Menschen.

    Um diese Probleme zu verhindern, kann die Ausführung eines Programms
    geplant oder ungeplant beendet werden. Man spricht auch von einem Absturz
    oder Crash des Programms. Ob der Entwickler eine Nutzung des Programms
    absichern oder beim Schreiben nicht alle Bugs gefunden hat, macht hier
    keinen Unterschied. Ein Crash tritt immer zur Laufzeit des Programms auf
    und beendet ein ungewolltes Verhalten. Damit ist er ein wichtiges Mittel
    um die Sicherheit zu erhöhen.

    Wir können einen Teil des Programms mithilfe von try und except antesten:

        try:
            print("Zu testender Code")
        except:
            print("Ein Fehler ist aufgetreten")

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
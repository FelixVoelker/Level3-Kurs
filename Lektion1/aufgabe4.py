""" Aufgabe 4: Fallunterscheidungen und Bedingungsschleifen

        Mit dem Datentyp **bool** unterscheidet der Computer die Wahrheitswerte
        **True** (Wahr) und **False** (Falsch). Dadurch können wir Bedingungen
        formulieren und den Programmfluss in verschiedene Fälle lenken:

            if bedingung1:
                print("bedingung1 ist wahr!")
            elif bedingung2:
                print("bedingung1 ist falsch aber bedingung2 ist wahr!")
            else:
                print("bedingung1 und bedingung2 sind falsch!")

        Außerdem können wir eine Schleife mit Bedingungen verbinden.
        Diese Bedingungsschleife wiederholt ihren Schleifenkörper dann solange
        bis ihre Bedingung falsch wird:

            while 3 < 5:
                print(""Dies ist eine Endlosschleife!)

        Jetzt wollen wir dein Alter mit dem deiner Mitschüler vergleichen!
"""

# TODO Kopiere die Namen und das Alter deiner Mitschüler aus Aufgabe 3
# in die entsprechende Liste.
teilnehmer_namen = []
teilnehmer_alter = []

alter = input("Gib dein Alter ein: ")

# Wir können alter noch nicht vergleichen weil alter ein **str** ist!
# Aber wir können alter in einen **int** umwandeln.
alter = int(alter)

for index in range(len(teilnehmer_namen)):
    name = teilnehmer_namen[index]
    if alter < teilnehmer_alter[index]:
        print(name, "ist älter als du.")
    elif alter == teilnehmer_alter[index]:
        # TODO Gib im Terminal aus ob dieser Mitschüler jünger, älter oder
        # genauso alt ist wie du!
        pass
    else:
        # TODO Gib im Terminal aus ob dieser Mitschüler jünger, älter oder
        # genauso alt ist wie du!
        pass

# TODO Ersetze die obere Zählschleife durch eine Bedingungsschleife!

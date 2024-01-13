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
students = []
ages = []

age = input("Gib dein Alter ein: ")

# Wir können age noch nicht vergleichen weil age ein **str** ist!
# Aber wir können age in einen **int** umwandeln.
age = int(age)

for index in range(len(students)):
    name = students[index]
    if age < ages[index]:
        print(name, "ist älter als du.")
    elif age == ages[index]:
        # TODO Gib im Terminal aus ob dieser Mitschüler jünger, älter oder
        # genauso alt ist wie du!
        pass
    else:
        # TODO Gib im Terminal aus ob dieser Mitschüler jünger, älter oder
        # genauso alt ist wie du!
        pass

# TODO Ersetze die obere Zählschleife durch eine Bedingungsschleife!

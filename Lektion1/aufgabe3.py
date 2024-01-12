""" Aufgabe 3: Listen und Zählschleifen

    Eine Liste sammelt mehrere Daten in einer Datenstruktur und
    wird mit eckigen Klammern [] erstellt:

        [0, 1, 2, 3, 4]

    Wir trennen die Daten in der Liste durch Kommas und
    nennen die einzelnen Einträge auch Elemente der Liste.

    Die obere Liste kennen wir schon recht gut! Sie wird auch
    durch den Befehl

        range(5) = [0, 1, 2, 3, 4]

    erzeugt und häufig bei der Zählschleife in Python verwendet.
    Als Erinnerung eine Zählschleife sieht so aus:

        for index in range(5):
            print("Dies ist eine Zählschleife!")

    In Python erwartet der in Operator eine Liste.
    Die Anzahl der Elemente dieser Liste entscheidet
    wie viele Iterationen die Schleife macht!
"""

# Jetzt erstellen wir eine Liste mit den Namen deiner Mitschüler.
students = []  # TODO Die Liste ist noch leer also fülle sie!

# Nutzen wir eine Zählschleife um deine Mitschüler im Terminal anzuzeigen.
print("In deinem Kurs sind folgende Mitschüler:")
for name in students:
    print(name)

# So greifst du nur auf den ersten Namen deiner Liste zu.
name = students[0]
# TODO Schreib den Namen ins Terminal!

# Die Länge der Liste (Anzahl der Elemente) bekommst du so:
count = len(students)
# TODO Schreib die Länge der Liste ins Terminal!

# Wie alt waren deine Mitschüler nochmal?
# TODO Erstelle eine Variable ages und speichere dort eine Liste.
# Die Liste soll das Alter deiner Mitschüler enthalten. Reihenfolge beachten!

# TODO Verändere nun die Zählschleife so, dass du den Namen und
# das Alter deines Mitschülers pro Zeile ausgibst.

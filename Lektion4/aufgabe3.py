""" Aufgabe 3: Exceptions

    Wenn ein Programm crasht, erzeugt es einen Fehler auch Exception genannt.
    Exceptions gibt es in den verschiedensten Arten und du bist beim
    Programmieren schon häufig darauf gestoßen. Hier ein paar Beispiele,
    die du bereits kennen solltest:

        NameError -> Variable wird verwendet aber ihr noch kein Wert zugewiesen
        TypeError -> Variable hat den falschen Datentyp (z.b. int + str)
        IndentationError -> Code ist falsch eingerückt

    Wenn eine Exception auftritt, muss das nicht zwangläufig zur Beendigung
    des Programms führen. Wir haben try/except kennengelernt um dies
    zu verhindern. Dennoch kann es Sinn ergeben, selbst eine Exception
    auszulösen um das Programm zu terminieren.
    Einen Fehler erzeugen wir so:

        raise NameError

    In dieser Aufgabe befinden sich kleinere Bugs, die großen Schaden
    angerichtet haben. Fange sie mithilfe von Exceptions ab!
"""

from bugs import double, umwandeln

# Intel Pentium Divisions-Fehler 1994 #
x = double(4195835.0)
y = double(3145727.0)
z = x - (x/y) * y
print(z)

# TODO Der Prozessor gab regelmässig falsche Ergebnisse bei der
# Gleitpunkt-Division. Finde heraus in welchen Abständen Fehler auftreten.

# TODO Fange nun das fehlerhafte Ergebnis ab, indem du eine Exception wirfst
# bevor falsch gerechnet wird. Gib eine Warnung in diesem Fall aus!

# NASA Venus-Erkundung 1962 #
variablen = {
    "-kraftstoff": 150000.667,
    "-geschwindigkeit": 266.98,
    "-verbrauch": -33.33
}

# reserve = variablen["kraftstoff"]
# reserve += variablen["-geschwindigkeit"] * variablen["-verbrauch"]
# print(reserve)

# TODO Die Venus Mariner 1 Sonde ging auf ihrer Mission verloren.
# Was war die Ursache dafür?

# TODO Der Code verursacht einen KeyError. Fange genau diesen Fehler ab
# und korrigiere das Program im **except** Block.

# Umrechnung Euro-Belgische Franken (Kurs 1 EUR = 39.5225 BEF) #
euro = 1.0
bef = umwandeln(euro)
# print("Für", euro, "Euro erhälst du:", bef, "Belgische Franken")

# TODO Teste das Programm für 1 Euro und für 0.01 Euro. Was stellst du fest?

# TODO Verhindere nun, dass der Nutzer Centbeiträge umwandelt. Schirme dafür
# die Funktion umwandeln mit **raise** und der richtigen Exception ab!
# Zuletzt gib dem Nutzer eine Warnung aus.

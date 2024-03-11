""" Aufgabe 3: Exceptions und Iteratoren

    Python besitzt Built-In Klassen die wir bereits genutzt haben.
    Wenn ein Crash ein Programm beendet, dann erstellt Python ein Objekt
    der Klasse Exception. Spezielle Exceptions wie NameError und TypeError
    sind lediglich Kindklassen davon. Wir können also durch Vererbung unsere
    eigenen Fehlercodes erstellen und diese durch raise auslösen.

    Erinnere dich an die Regel, dass die for-loop in Python eine Liste
    Element für Element durchläuft. Nun dies ist zwar richtig aber nicht
    die ganze Wahrheit. Denn die Python for-loop erwartet ein iterierbares
    Objekt, z.b. Listen und Dictionaries. Diese können nur deswegen durchlaufen
    werden, weil sie die Methode __iter__ besitzen und damit ein Objekt
    der Klasse Iterator der Schleife übergeben. Jedes Objekt mit dieser Methode
    kann also mit der for-loop abgelaufen werden.

    Iteratoren besitzen die Methode __next__ und sagen damit der Schleife,
    welches Element als nächstes an der Reihe ist. Gäbe es immer ein nächstes
    Element so wäre die for-loop auch eine Endlosschleife. Durch das Auslösen
    der StopIteration Exception kann der Iterator jedoch beendet werden.
"""

from aufgabe2 import Ritter, Jaeger, Magier, Heiler
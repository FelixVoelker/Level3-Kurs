""" Aufgabe 2: Type Casting

    Das Internet ist eine Autobahn für Daten und es werden dort
    täglich Milliarden von Texten, Bildern, Videos usw zwischen
    Computern verschickt. Um den Speicherplatzbedarf dabei
    so niedrig wie möglich zu halten, werden Daten verdichtet.

    Ein Server in Frankfurt hat uns eine Textdatei gesendet
    und in dieser ist beim Transport durch das World Wide Web (www)
    etwas Rauschen entstanden. Wir sollen die Datei einlesen und
    mit Typumwandlungen reparieren. Variablen beziehungsweise Literale
    werden so umgewandelt:

        datentyp(variable) oder datentyp(literal)

    Einen konstanten Wert nennt man beim Programmieren auch Literal.
    Beispiele für solche Typumwandlungen sind int(2.3) = 2,
    float(7) = 7.0, int(True) = 1. Den Datentyp einer Variable kannst
    du so überprüfen:

        type(variable)

"""

from code_knacken import zeige

# Öffne und lese die Textdatei mit dem Befehl read ein.
with open("Lektion3/verrauscht.txt", "r") as textdatei:
    kodierter_text = textdatei.read()

    # TODO Eine Gleitkommazahl hat sich in den String geschlichen.
    # Nutze den Befehl find um sie zu finden, dann verwandele sie in
    # eine ganze Zahl. Nutze replace um die Zahlen auszutauschen!

    # TODO Das 45.Zeichen des String ist wohl unterwegs verloren gegangen.
    # Finde das Zeichen indem du den leeren String in ein bool und dann
    # in eine ganze Zahl castest. Nutze replace um die Zeichen auszutauschen!

    # TODO Kurz dahinter wurde eine Zahl in binär übertragen.
    # Finde die Binärzahl und wandele sie in eine ganze Zahl um!
    # Nutze replace um die Zeichen auszutauschen!

    zeige(kodierter_text)

# TODO Schreibe das dekodierte Bild in eine JPEG Datei (.jpg).
# Verwende dafür den Schreibmodus "wb" und den Befehl write!

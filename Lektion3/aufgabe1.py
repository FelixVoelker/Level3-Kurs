""" Aufgabe 1: String Manipulation

    Kryptographie ist ein wichtiges Werkzeug um sensible Daten
    vor dem Zugriff von Fremden zu schützen. Dazu gehört unter anderem
    das Verschlüsseln und Entschlüsseln von Nachrichten
    oder auch Passwörtern.

    Unsere Spione haben heute eine Nachricht abgefangen, die wohl
    äußerst wichtige Informationen enthält! Man hat uns mitgeteilt,
    dass wir den String nur etwas manipulieren müssten um an den Inhalt
    zu gelangen.

    Zudem hat uns die Einsatzleitung ein Nachschlagewerk zum Übersetzen
    einzelner Symbole gestellt. Dieses haben sie uns in Form einer speziellen
    Datenstruktur übergeben. Ein Dictionary speichert Paare aus Schlüsseln
    und Werten:

        {"a": "0", "b": "1"}

    Hier sind "a" und "0" ein Paar, sowie "b" und "1". "a" und "b" sind
    Schlüssel und damit immer Strings. Werte können jedoch beliebige
    Datentypen besitzen.
"""

from code_knacken import nachschlagewerk

nachricht = "  qq61.q9.$P._qh@+9#x3.xq319pq.$Q_1yhpq9.1q+yq6z_@k6$!qqq "

# Zuerst entfernen wir die Leerzeichen am Anfang und Ende des Strings.
nachricht = nachricht.strip()

# TODO Unsere Code Knacker vermuten, dass drei Vokale
# im Nachschlagewerk fehlen. Analysiere den String und füge
# die fehlenden Vokale zum Nachschlagewerk hinzu!

# Mit upper werden alle Buchstaben groß!
nachricht_groß = nachricht.upper()

# Mit lower werden alle Buchstaben klein!
nachricht_klein = nachricht.lower()

# TODO Untersuche die Nachrichten mithilfe von upper und lower.
# Ersetze die unpassenden Symbole durch deine neuen Erkenntnisse!

# Ersetze mit replace jedes Zeichen durch seine Übersetzung.
for zeichen in nachschlagewerk.keys():
    nachricht = nachricht.replace(zeichen, nachschlagewerk[zeichen])

print(nachricht)

# TODO Hübsche die Nachricht noch etwas auf:
#      - Verwende split() um die Wörter bei allen Leerzeichen zu trennen
#      - Verwende capitalize auf jedem Substantiv

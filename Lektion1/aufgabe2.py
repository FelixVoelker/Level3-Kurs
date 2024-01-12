""" Aufgabe 2: Der Terminal - Eingabe

    Der Terminal kann mehr als der Chat in Minecraft Education.
    Wir können Text ausgeben aber auch Daten einlesen! Der Befehl dafür heißt:

        input()

    In dieser Aufgabe soll der Terminal uns der Gruppe vorstellen.
    Wir nehmen nur unsere Daten auf und speichern sie in Variablen ab.

    Variablen speichern Daten im Arbeitsspeicher des Computers ab.
    Sie funktionieren wie die Schubladen an deinem Schreibtisch. Dort legst du
    deine Schulbücher ab um später damit zu arbeiten.
    Eine Variable wird so erstellt:

        text = "Ich bin ein String!"

    Dies ist eine Variablenzuweisung. Die Variable heißt text und
    sie enthält einen String.
"""

print("Willkommen im Kurs!")

# Zuerst wollen wir deinen Namen in die Variable name speichern.
print("Wie heißt du?")
name = input()

print("Wie alt bist du?")
# TODO Lese jetzt dein Alter in die Variable age ein!

# Wir können uns das print sparen!
# input kannst du den String auch als Parameter übergeben.
hobby = input("Was ist dein Hobby?")

# TODO Erstelle eine Variable note und verwende input(String) um noch etwas
# über dich der Gruppe mitzuteilen!

# Jetzt stellen wir dich dem Kurs vor!
# Diese Version von print setzt bei den Kommas ein Leerzeichen.
print("Ich bin", name, "und", age, "Jahre alt!", "Mein Hobby ist", hobby, ".")
print(note)

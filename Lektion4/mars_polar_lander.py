# Die aktuelle Entfernung der Sonde zur Umlaufbahn in Meilen.
entfernung = 62.1371

# Umwandlungsfaktor 1 Meile zu Kilometer.
umwandlungsfaktor = 1.609344


# Pingt einmal die aktuelle Geschwindigkeit zur Sonde.
def ping(geschwindigkeit):
    global entfernung
    entfernung -= geschwindigkeit / umwandlungsfaktor

""" Aufgabe 2: Vererbung und Polymorphismen

    Das Konzept der Objektorientierung wurde erfunden um Programme zu
    modularisieren. Dabei nutzen wir Objekte um einzelne Bestandteile des
    Programms voneinander zu trennen. Projekte werden dadurch lesbarer,
    leichter zu korrigieren und zu verändern. Denn wir entwickeln damit
    unsere Programme nicht mehr nach der Idee welche Funktion es umsetzen soll.
    Sondern welche Beziehung die Objekte im Programm miteinander haben.

    Eine dieser Beziehung ist die Vererbung. Klassen können untereinander in
    eine Eltern-Kind Beziehung treten. Die Elternklasse vererbt dabei dem Kind
    alle ihre Variablen und Methoden. Die Kindklasse kann diese dann aufrufen.
    Hier ist ein Beispiel für eine Vererbung der Elternklasse Gebäude und
    der Kindklasse Restaurant:

        class Gebäude:
            räume = 3

            def putzen():
                print("Gebäude geputzt")

        class Restaurant(Gebäude):
            sitzplätze = 15

    Ein Objekt vom Typ Restaurant ist durch die Vererbung auch ein Gebäude.
    Es besitzt nicht nur die Variable sitzplätze sondern auch räume. Außerdem
    besitzt es die Methode putzen und kann diese aufrufen. Erhält unser
    Restaurant jedoch eine eigene Methode putzen, dann nutzt es nicht mehr die
    Methode der Elternklasse sondern seine eigene. Der Programmierer spricht
    dann von einem Polymorphismus (Vielgestaltigkeit) und meint damit, dass
    Methoden den gleichen Namen aber unterschiedliche Funktion besitzen dürfen.

    Fahren wir mit der Entwicklung des Spiels "Die Schlacht der vier Helden"
    fort:

        1. Das Spiel soll vier Rollen von Helden besitzen: Ritter, Jäger,
           Magier und Heiler.
        2. Der Ritter hat 5 VRT, der Jäger 4 ATK, der Magier 2 ATK und
           der Heiler 1 ATK.
        3. Der Magier ignoriert beim Angriff die VRT des Gegners.
        4. Der Heiler verursacht keinen Schaden sondern heilt beim Angriff
           den anderen Helden.
"""

from aufgabe1 import Held

# TODO Erstelle die Klassen Ritter, Jaeger, Magier und Heiler.
# Lasse sie von der Klasse Held erben.

# TODO Überschreibe den Konstruktur der Kinderklassen und nutze
# die magische Funktion __super__ um deren Werte anzupassen.

# TODO Nutze Polymorphie um die Methode attack vom Magier und Heiler
# zu überschreiben. Der Magier greift die LP des Gegners direkt an und
# der Heiler stellt LP wieder her sofern der Held weniger als 10 hat.

# TODO Operatorüberladung ist eine Form von Polymorphie. Dabei wird der
# Operator überschrieben und dessen Funktion für das Objekt geändert.
# Verändere mit der magischen Funktion __lt__ den <-Operator:
#   - Ritter: LP des Ritter kleiner als ATK eines Helden
#   - Jäger: LP eines Helden kleiner als ATK des Jäger
#   - Magier: ATK des Magiers kleiner als VRT eines Helden
#   - Heiler: LP eines Helden plus ATK des Heiler kleiner als 10

# TODO BONUS: Denke dir jetzt eine eigene Rolle Held aus!
# Wähle deine eignen Werte und nutze Polymorphie um attack und
# defend sowohl den <-Operator zu überschreiben.

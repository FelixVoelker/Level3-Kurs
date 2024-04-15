""" Tag 2: Implementierungsphase

    Wenn du eine grobe Vorstellung deines Spiels besitzt und erste Ideen
    ausprobiert hast, dann ist es Zeit das Spiel zu implementieren.
    In dieser Phase hast du viel Arbeit vor dir. Eine gute Strategie ist
    deinen Anforderungskatalog Punkt für Punkt abzuarbeiten. Dadurch kannst
    du gut beobachten wie dein Programm sich entwickelt und behälst leichter
    den Überblick sobald das Programm größer wird. Zögere nicht Teile deines
    Programms in Module auszulagern!

    In diesem Leitfaden geben wir unserer Terminalversion von "Die Schlacht der
    vier Helden" eine graphische Benutzeroberfläche (auch User Interface
    genannt).
"""

from helden import Ritter, Jaeger, Magier, Heiler
import random as r


class DieSchlachtDerVierHelden:

    class DSDVHError(Exception):

        def __init__(self):
            super().__init__("Fehlerhafter Spiel Setup")

    def __init__(self):
        self.helden_stapel = []
        self.helden_spieler = []
        self.helden_gegner = []

        self.runde = 1

        print("Das ist die Schlacht der vier Helden!")
        print("-------------------------------------")
        auswahl = input("Wähle deinen ersten Helden: ")
        self.held_auswaehlen(auswahl)
        auswahl = input("Wähle deinen zweiten Helden: ")
        self.held_auswaehlen(auswahl)

        self.gegner_auswaehlen(r.randint(1, 4))
        self.gegner_auswaehlen(r.randint(1, 4))

        print("Lasst die Schlacht beginnen!")

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.helden_stapel) == 0:
            print("Beginn der", self.runde, ".Runde!")
            self.runde += 1

            self.helden_stapel.extend(self.helden_spieler)
            self.helden_stapel.extend(self.helden_gegner)
            r.shuffle(self.helden_stapel)

            for held in self.helden_stapel:
                if held.dmg < 0:
                    held.lp += held.dmg
                    held.dmg = 0
                if held.lp <= 0:
                    self.helden_stapel.remove(held)

        if self.helden_spieler[0].lp <= 0 and self.helden_spieler[1].lp <= 0:
            print("Team des Spielers besiegt!")
            raise StopIteration
        if self.helden_gegner[0].lp <= 0 and self.helden_gegner[1].lp <= 0:
            print("Team des Gegner besiegt!")
            raise StopIteration
        return self.helden_stapel.pop(0)

    def held_auswaehlen(self, auswahl):
        if auswahl == "Ritter":
            self.helden_spieler.append(Ritter())
        elif auswahl == "Jäger":
            self.helden_spieler.append(Jaeger())
        elif auswahl == "Magier":
            self.helden_spieler.append(Magier())
        elif auswahl == "Heiler":
            self.helden_spieler.append(Heiler())
        else:
            raise DieSchlachtDerVierHelden.DSDVHError()

    def gegner_auswaehlen(self, auswahl):
        if auswahl == 1:
            self.helden_gegner.append(Ritter())
        elif auswahl == 2:
            self.helden_gegner.append(Jaeger())
        elif auswahl == 3:
            self.helden_gegner.append(Magier())
        elif auswahl == 4:
            self.helden_gegner.append(Heiler())

    def zug_spieler(self, held):
        print("Spieler:", type(held), "ist am Zug!")
        print(held)
        print("(1) Gegner", type(self.helden_gegner[0]), "angreifen?")
        print("(2) Gegner", type(self.helden_gegner[1]), "angreifen?")
        print("(3) Sich verteidigen?")

        auswahl = input("Wähle aus: ")
        if auswahl == "1":
            held.attack(self.helden_gegner[0])
        elif auswahl == "2":
            held.attack(self.helden_gegner[1])
        elif auswahl == "3":
            held.defend()
        else:
            raise DieSchlachtDerVierHelden.DSDVHError()

    def zug_gegner(self, held):
        print("Gegner:", type(held), "ist am Zug!")
        print(held)
        auswahl = r.randint(1, 2)
        if auswahl == 1:
            held.attack(self.helden_spieler[r.randint(0, 1)])
        else:
            held.defend()


spiel = DieSchlachtDerVierHelden()
for held in spiel:
    if held in spiel.helden_spieler:
        spiel.zug_spieler(held)
    else:
        spiel.zug_gegner(held)
print("Spiel beendet!")

class Held:

    dmg = 0

    def __init__(self, lp=10, atk=3, vrt=2):
        self.lp = lp
        self.atk = atk
        self.vrt = vrt

    def __str__(self):
        return "Der Held hat " + str(self.lp) + " Lebenspunkte."

    def attack(self, held):
        held.dmg -= self.atk

    def defend(self):
        self.dmg += self.vrt


class Ritter(Held):

    def __init__(self):
        super().__init__(vrt=5)

    def __lt__(self, held):
        return self.lp < held.atk


class Jaeger(Held):

    def __init__(self):
        super().__init__(atk=4)

    def __lt__(self, held):
        return held.lp < self.atk


class Magier(Held):

    def __init__(self):
        super().__init__(atk=2)

    def attack(self, held):
        held.lp -= self.atk

    def __lt__(self, held):
        return self.atk < held.vrt


class Heiler(Held):

    def __init__(self):
        super().__init__(atk=1)

    def attack(self, held):
        if held.lp < 10:
            held.lp += self.atk

    def __lt__(self, held):
        return held.lp + self.atk < 10
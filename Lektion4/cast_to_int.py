class OverflowError(Exception):

    def __init__(self):
        message = """Die Zahl kann nicht in eine 16-bit ganze Zahl umgewandelt werden.
                     Absturz des Bordcomputers...
                     Zusammenbruch des Lenksystems...
                     Flug instabil...
                     Selbstzerstörung eingeleitet...
                  """
        super().__init__(message)


# Wandelt eine Zahl auf ihre 16-bit Representation um [-32768, 32767].
def int16(zahl):
    zahl = int(zahl)
    binaerzahl = bin(zahl)
    if len(binaerzahl) >= 18:
        raise OverflowError()
    return int(binaerzahl, 2)

class OverflowError(Exception):
    pass


# Wandelt eine Zahl auf ihre 16-bit Representation um [-32768, 32767].
def int16(zahl):
    zahl = int(zahl)
    binaerzahl = bin(zahl)
    if len(binaerzahl) >= 18:
        raise OverflowError("Die Zahl kann nicht in eine 16-bit ganze Zahl umgewandelt werden.")
    return int(binaerzahl, 2)

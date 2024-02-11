import base64
import io
from PIL import Image

# Dies ist ein Nachschlagewerk zum Code knacken!
nachschlagewerk = {
    "6": "d",
    "_": "n",
    "9": "b",
    "$": "s",
    "p": "v",
    "P": "t",
    "k": "l",
    "+": "m",
    "#": "u",
    "x": "r",
    "3": "g",
    "1": "i",
    "y": "w",
    "Y": "c",
    "q": " "
}


# Wandelt einen base64-kodierten String in ein Bild um und zeigt es.
def zeige(text):
    bild = Image.open(io.BytesIO(dekodiere(text)))
    bild.show()


# Dekodiert den base-64 String.
def dekodiere(text):
    return base64.b64decode(text, validate=True)

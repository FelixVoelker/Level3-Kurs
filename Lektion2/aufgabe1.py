""" Aufgabe 1: Module

    Hast du dich schon einmal gefragt, woher die ganzen Befehle kommen
    mit denen wir hier programmieren? Die Antwort darauf lautet Module!

    Ein Modul ist eine Software-Bibliothek in Form einer Python-Datei.
    So wie in einer Bibliothek viele Bücher zum Verleih stehen,
    enthält ein Modul Funktionen und Variablen zur Verwendung
    in deinem Python-Programm!

    Ein Modul importierst du so:

        import modul

    Der Modulname ist identisch mit dem Dateinamen nur
    ohne die Dateiendung .py. Wir können diesen Namen dann
    in unserem Programm nutzen um auf die Variablen und
    Funktionen des Moduls zuzugreifen:

        modul.variable
        modul.funktion()

    Im Ordner dieser Lektion befindet sich die Datei minecraft.py.
    Wir wollen das Modul minecraft importieren und damit arbeiten!
"""

# Zuerst importieren wir das Modul.
import minecraft

# Nun können wir auf Variablen im Modul zugreifen!
print("Das Spiel heißt", minecraft.name)
print("Das Genre des Spiels ist", minecraft.genre)

# TODO Öffne nun minecraft.py und schau dir die Variablen an.
# Welche Variable haben wir noch nicht ins Terminal geschrieben?
# Benutze print um diese Variable auch auszugeben!

# TODO Das Modul minecraft enthält auch eine Funktion. Rufe sie auf!

# TODO Erstelle nun ein anderes Spiel als Modul und importiere es!
# Nimm dir dabei ein Beispiel an dem Modul minecraft.

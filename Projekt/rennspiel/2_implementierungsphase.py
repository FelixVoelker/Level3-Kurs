import pygame
import pygame.locals as key

pygame.init()

# Spielfenster
breite = 500
hoehe = 500
screen_groeße = (breite, hoehe)
screen = pygame.display.set_mode(screen_groeße)
pygame.display.set_caption("Rennspiel")

# Farben
grau = (100, 100, 100)
gruen = (76, 208, 56)
rot = (200, 0, 0)
weiss = (255, 255, 255)
gelb = (255, 232, 0)

# Maße und Koordinaten
strasse_breite = 300
strasse = (100, 0, strasse_breite, hoehe)

markierung_breite = 10
markierung_hoehe = 50
linke_fahrbahnmarkierung = (95, 0, markierung_breite, hoehe)
rechte_fahrbahnmarkierung = (395, 0, markierung_breite, hoehe)

linke_spur = 150
mittlere_spur = 250
rechte_spur = 350

# Game Loop
laeuft = True
while laeuft:
    for event in pygame.event.get():
        if event.type == key.QUIT:
            laeuft = False

    # Gras zeichnen
    screen.fill(gruen)

    # Straße zeichnen
    pygame.draw.rect(screen, grau, strasse)

    # Fahrbahnmarkierungen zeichnen
    pygame.draw.rect(screen, gelb, linke_fahrbahnmarkierung)
    pygame.draw.rect(screen, gelb, rechte_fahrbahnmarkierung)

    # Spurmarkierung zeichnen
    for y in range(0, hoehe, markierung_hoehe * 2):
        pygame.draw.rect(screen, weiss, (linke_spur + 45, y, markierung_breite, markierung_hoehe))
        pygame.draw.rect(screen, weiss, (mittlere_spur + 45, y, markierung_breite, markierung_hoehe))

    pygame.display.update()
pygame.quit()

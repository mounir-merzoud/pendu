import pygame
import sys
import random
import time
import os

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
FPS = 30

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# Chargement des images du pendu
IMAGES_PENDU = [pygame.image.load(f"images_pendu/{i}.png") for i in range(1, 8)]

# Fond blanc
background_color = WHITE

# Police de caractères pour le texte
font = pygame.font.SysFont(None, 48)

def choisir_mot():
    mots = ["python", "jouer", "danser", "manger", "rigoler", "pendu", "musique", "soleil", "ordinateur", "programmation", "pizza", "guitare", "chocolat", "vacances", "pygame"]
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    return "".join([lettre if lettre in lettres_trouvees else " _ " for lettre in mot])

def afficher_message(message, y):
    text = font.render(message, True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Attendre 2 secondes

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    erreurs = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and event.unicode.islower():
                    lettre = event.unicode.lower()
                    if lettre not in lettres_trouvees:
                        lettres_trouvees.add(lettre)
                        if lettre not in mot_a_deviner:
                            erreurs += 1

        screen.fill(background_color)  # Utiliser un fond blanc

        # Affichage du mot masqué
        mot_affiche = afficher_mot(mot_a_deviner, lettres_trouvees)
        text = font.render(mot_affiche, True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))

        # Affichage des images du pendu
        screen.blit(IMAGES_PENDU[erreurs], (WIDTH // 2 - IMAGES_PENDU[erreurs].get_width() // 2, 150))

        # Vérification de la victoire ou défaite
        if erreurs == len(IMAGES_PENDU) - 1:
            afficher_message("Perdu! Le mot était: " + mot_a_deviner, HEIGHT - 50)
            return
        elif "_" not in afficher_mot(mot_a_deviner, lettres_trouvees):
            afficher_message("Gagné! Le mot était: " + mot_a_deviner, HEIGHT - 50)
            return

        pygame.display.flip()

        clock.tick(FPS)

# Lancement du jeu
jouer_pendu()

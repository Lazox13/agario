import random

from pygame.math import Vector2

import core


class Carte:
    def __init__(self, largeur=1000, hauteur=1000):
        self.rayon = 10
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.taille = Vector2(largeur, hauteur)

        def dead(self):
            pass
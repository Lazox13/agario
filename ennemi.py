import random

from pygame.math import Vector2

import core


class Ennemi:
    def __init__(self, largeur=1000, hauteur=800):
        self.position = Vector2(random.randint(0, largeur), (random.randint(0, hauteur)))
        # self.vitesse =
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 10
        self.nom = "Hugo"

        # self.masse

        def dead(self):
            pass
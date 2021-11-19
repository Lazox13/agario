import random

from pygame.math import Vector2

class Creep:
    def __init__(self,largeur=1000, hauteur=800):
        self.rayon = 3
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0, largeur), (random.randint(0, hauteur)))

        def dead(self):
            pass
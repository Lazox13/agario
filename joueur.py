import random
from pygame.math import Vector2

class Joueur:
    def __init__(self, largeur=1000, hauteur=1000):
        self.position = Vector2(random.randint(0, largeur), (random.randint(0, hauteur)))
        self.direction = Vector2(0, 0)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 10
        self.nom = "Hugo"


        def dead(self):
            pass
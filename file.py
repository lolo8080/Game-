import pygame
from projectile import Projectile
from Alien import Alien
class Game:
    def __init__(self):
        self.plane=Plane()
        self.alien=Alien()
        self.pressed={}

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        image=pygame.image.load("plane.png")
        image=pygame.transform.scale(image,(75,85))
        super().__init__()
        self.vie=3
        self.maxvie=5
        self.attaque=1
        self.vitesse= 3
        self.all_projectiles=pygame.sprite.Group()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=250
        self.rect.y=500
    def move_right(self):
        self.rect.x+=self.vitesse
    def move_left(self):
        self.rect.x-=self.vitesse
    def move_up(self):
        self.rect.y-=self.vitesse
    def move_down(self):
        self.rect.y+=self.vitesse
    def shoot(self):
        self.all_projectiles.add(Projectile(self))

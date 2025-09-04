import pygame
import random as rd 
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Alien.png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.all_projectiles=pygame.sprite.Group()
        self.vitesse_x=rd.randint(1,4)/3
        self.vitesse_y=rd.randint(1,4)/3
        self.rect=self.image.get_rect()
        self.rect.x=rd.randint(0,1500)
        self.rect.y=-100
    def move(self):
        self.rect.y+=self.vitesse_x
        self.rect.x+=self.vitesse_y
    def create(self):
        self.all_projectiles.add(Alien())
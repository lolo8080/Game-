import pygame
class Projectile(pygame.sprite.Sprite):
    def __init__(self,plane):
        super().__init__()
        self.image=pygame.image.load("projectile.png")
        self.image=pygame.transform.scale(self.image,(6,30))
        self.vitesse=4
        self.rect=self.image.get_rect()
        self.rect.x=plane.rect.x+37.5
        self.rect.y=plane.rect.y
    def move(self):
        self.rect.y-=self.vitesse
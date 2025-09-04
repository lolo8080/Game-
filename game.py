import pygame

from file import Plane,Game
pygame.init()


score=0
pygame.display.set_caption("plane infinite loop") #créer un titre pour notre jeu 
screen=pygame.display.set_mode((1500,700)) #créer un écran de taille 900:600
font = pygame.font.Font(None, 50)
text = font.render("Score: "+str(score), True, (255,0,0))     
game=Game()
running=True
current_time = pygame.time.get_ticks()
background=pygame.image.load("OIP.jpeg")
background=pygame.transform.scale(background,(1500,900))
explo=pygame.image.load("projectile.png")
explo=pygame.transform.scale(explo,(50,50))
 
while running:
    
    screen.blit(background,(0,0))    #appliquer l'image sur l'écran
    screen.blit(game.plane.image,game.plane.rect) #appliquer l'image du joeur
    text = font.render("Score: "+str(score), True, (255,0,0))     
    screen.blit(text,(25,650))
    game.plane.all_projectiles.draw(screen)
    game.alien.all_projectiles.draw(screen)
    for projectile in game.plane.all_projectiles:
        projectile.move()
    
    if pygame.time.get_ticks()-current_time>=600:
      
        current_time=pygame.time.get_ticks()
        game.alien.create()
    
    for projectile in game.alien.all_projectiles:
        projectile.move()
        if(projectile.rect.x>1425 or projectile.rect.y>800 or projectile.rect.x<-100):
            game.alien.all_projectiles.remove(projectile)
        for shot in game.plane.all_projectiles:
            if projectile.rect.x>shot.rect.x-100 and projectile.rect.x<shot.rect.x and projectile.rect.y>shot.rect.y-50 and projectile.rect.y<shot.rect.y+50:
                game.alien.all_projectiles.remove(projectile)
                score+=1
                for i in range(5):
                    
                    
                     
                    explo=pygame.transform.scale(pygame.image.load("explo.png"),(100+i*20,100+i*20))
                    screen.blit(explo,projectile.rect)
                    pygame.display.flip()  
                    
                
    if game.pressed.get(pygame.K_RIGHT) and game.plane.rect.x<1425:
        game.plane.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.plane.rect.x>0:
        game.plane.move_left()
    elif game.pressed.get(pygame.K_UP)and game.plane.rect.y>0:
        game.plane.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.plane.rect.y<615:
        game.plane.move_down()
    pygame.display.flip()   #mettre à jour l'écran
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #si le joueur ferme la fenêtre
            running=False
            pygame.quit()
        elif event.type==pygame.KEYDOWN: #détecter les commandes du joueur
            game.pressed[event.key]=True
            
            if event.key==pygame.K_SPACE:
                game.plane.shoot()
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False 

    
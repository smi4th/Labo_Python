import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Les bases")

fpsClock = pygame.time.Clock() #Pour les FPS

x_add = 0
y_add = 0

# Boucle principale
while True:

    screen.fill((255, 255, 255)) #On remplit l'écran de blanc
    
    mx, my = pygame.mouse.get_pos() #On récupère la position de la souris

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP: # Toutes les touches sont dans pygame.locals : https://www.pygame.org/docs/ref/key.html
                y_add -= 5
            if event.key == K_DOWN:
                y_add += 5
            if event.key == K_LEFT:
                x_add -= 5
            if event.key == K_RIGHT:
                x_add += 5


    screen.blit(pygame.image.load("image.png"), (mx + x_add, my + y_add)) #On affiche l'image

    pygame.display.update()
    fpsClock.tick(60) #Pour les FPS
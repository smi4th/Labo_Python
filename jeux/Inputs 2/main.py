import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Les bases")

fpsClock = pygame.time.Clock() #Pour les FPS

keys = {
    K_UP: False,
    K_DOWN: False,
    K_LEFT: False,
    K_RIGHT: False
    }

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
                keys[K_UP] = True
            if event.key == K_DOWN:
                keys[K_DOWN] = True
            if event.key == K_LEFT:
                keys[K_LEFT] = True
            if event.key == K_RIGHT:
                keys[K_RIGHT] = True

        if event.type == KEYUP and event.key in keys:
            # On remet les touches qui sont True à False, c'est pareil que en haut mais pour les touches relachées
            keys[[key for key in keys if event.key == key][0]] = [False for key in keys if event.key == key][0]

    for key in keys:
        if key == K_UP and keys[key]:
            y_add -= 5
        if key == K_DOWN and keys[key]:
            y_add += 5
        if key == K_LEFT and keys[key]:
            x_add -= 5
        if key == K_RIGHT and keys[key]:
            x_add += 5

    #x_add, y_add = [x_add + 5 if keys[K_RIGHT] else x_add - 5 if keys[K_LEFT] else x_add, y_add + 5 if keys[K_DOWN] else y_add - 5 if keys[K_UP] else y_add]


    screen.blit(pygame.image.load("image.png"), (mx + x_add, my + y_add)) #On affiche l'image

    pygame.display.update()
    fpsClock.tick(60) #Pour les FPS
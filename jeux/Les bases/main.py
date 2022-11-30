import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Les bases")

fpsClock = pygame.time.Clock() #Pour les FPS

# Boucle principale
while True:

    screen.fill((255, 255, 255)) #On remplit l'écran de blanc

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.image.load("Les bases/image.png"), (0, 0)) #On affiche l'image

    pygame.display.update()
    fpsClock.tick(60) #Pour les FPS
import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Les bases")

fpsClock = pygame.time.Clock() #Pour les FPS

img = pygame.image.load("image.png")

img_rect = pygame.Rect(0, 0, img.get_width(), img.get_height()) #On crée un rectangle

blue_rect = pygame.Rect(0, 0, 100, 100) #On crée un rectangle

# Boucle principale
while True:
    
    screen.fill((255, 255, 255)) #On remplit l'écran de blanc
    
    mx, my = pygame.mouse.get_pos() #On récupère la position de la souris

    img_rect.x, img_rect.y = mx, my #On change la position du rectangle

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    color = (0, 0, 255)
    if img_rect.colliderect(blue_rect):
        color = (255, 0, 0) #On change la couleur du rectangle en fonction de la collision

    pygame.draw.rect(screen, color, blue_rect) #On dessine le rectangle

    screen.blit(pygame.image.load("image.png"), (img_rect.x, img_rect.y)) #On affiche l'image

    pygame.display.update()
    fpsClock.tick(60) #Pour les FPS
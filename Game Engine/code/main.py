import pygame
from pygame.locals import *
from constants import *
import fake_screens

pygame.init()
flags = pygame.RESIZABLE
screen = pygame.display.set_mode(WINDOW_SIZE, flags)
pygame.display.set_caption("PYENGINE")
clock = pygame.time.Clock()

NEW_PROJECT_INITIALISED = 0

fakesScreensList = []

while RUNNING:
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.VIDEORESIZE:
            WINDOW_SIZE = event.size
            screen = pygame.display.set_mode(WINDOW_SIZE, flags)
        if event.type == pygame.KEYDOWN:
            for fake_screen in fakesScreensList:
                for child in fake_screen.childrens:
                    if isinstance(child, fake_screens.InputText):
                        child.keyPressed = True


    #####################################
    #        Fake screens code          #
    #####################################
    #####################################
    #        NEW_PROJECT_POP            #
    #####################################
    if keys[K_LCTRL] and keys[K_LSHIFT] and keys[K_n]:
        NEW_PROJECT_POP_UP = fake_screens.new_project_pop_up()
        fakesScreensList.append(NEW_PROJECT_POP_UP)
        NEW_PROJECT_INITIALISED = 1

    if NEW_PROJECT_INITIALISED > 0:
        NEW_PROJECT_POP_UP.titleBarHover(pygame.mouse.get_pos())
        action = NEW_PROJECT_POP_UP.titleBarActions(pygame.mouse.get_pos(), pygame.mouse.get_pressed(), screen)

        NEW_PROJECT_POP_UP.childrens_Modifyer(pygame.mouse.get_pos(), pygame.mouse.get_pressed(), screen)

        fake_screens.blit_project_pop_up(screen, NEW_PROJECT_POP_UP)
        if action == "Closing":
            NEW_PROJECT_INITIALISED = 0
            NEW_PROJECT_POP_UP = None
        
        #NEW_PROJECT_INITIALISED += 1

    for fake_screen in fakesScreensList:
        for child in fake_screen.childrens:
            if isinstance(child, fake_screens.InputText):
                child.keyPressed = False

    #####################################
    #####################################
            
    pygame.display.flip()

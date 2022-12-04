import pygame
from pygame.locals import *
from constants import *

class FakeScreen:
    def __init__(self, size, color, title, pos):
        self.size = size
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.pos = pos
        self.rect = pygame.Rect(pos, size)
        self.title = title
        self.screen = None

        # --- TITLE BAR --- #
        self.titleBarRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 20)
        self.titleBarSurface = pygame.Surface((self.titleBarRect.width, self.titleBarRect.height))
        self.titleBarSurface.fill(LIGHT_GREY)
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render(self.title, True, BLACK), (0,5))
        
        self.titleBarXSurface = pygame.Surface((15,20))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("X", True, BLACK), (self.titleBarRect.width - 15, 5))
        self.titleBarXRect = pygame.Rect(self.titleBarRect.x + self.titleBarRect.width - 15, self.titleBarRect.y, 15, 20)
        
        self.titleBarSquareSurface = pygame.Surface((15,20))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("[]", True, BLACK), (self.titleBarRect.width - 30, 5))
        self.titleBarSquareRect = pygame.Rect(self.titleBarRect.x + self.titleBarRect.width - 30, self.titleBarRect.y, 15, 20)
        
        self.titleBarDashSurface = pygame.Surface((15,20))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("_", True, BLACK), (self.titleBarRect.width - 45, 5))
        self.titleBarDashRect = pygame.Rect(self.titleBarRect.x + self.titleBarRect.width - 45, self.titleBarRect.y, 15, 20)

        # --- CHILDRENS --- #
        self.childrens = []
        
    def titleBarHover(self, mousePos):
        self.titleBarSurface.fill(LIGHT_GREY)
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render(self.title, True, BLACK), (0,5))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("X", True, BLACK), (self.titleBarRect.width - 15, 5))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("[]", True, BLACK), (self.titleBarRect.width - 30, 5))
        self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("_", True, BLACK), (self.titleBarRect.width - 45, 5))
        if self.titleBarRect.collidepoint(mousePos):
            if self.titleBarXRect.collidepoint(mousePos):
                self.titleBarXSurface.fill(RED)
                self.titleBarSurface.blit(self.titleBarXSurface, (self.titleBarRect.width - 15, 0))
                self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("X", True, BLACK), (self.titleBarRect.width - 15, 5))

            elif self.titleBarSquareRect.collidepoint(mousePos):
                self.titleBarSquareSurface.fill(GREEN)
                self.titleBarSurface.blit(self.titleBarSquareSurface, (self.titleBarRect.width - 30, 0))
                self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("[]", True, BLACK), (self.titleBarRect.width - 30, 5))

            elif self.titleBarDashRect.collidepoint(mousePos):
                self.titleBarDashSurface.fill(BLUE)
                self.titleBarSurface.blit(self.titleBarDashSurface, (self.titleBarRect.width - 45, 0))
                self.titleBarSurface.blit(pygame.font.SysFont(FONT, 12).render("_", True, BLACK), (self.titleBarRect.width - 45, 5))
                
    def titleBarActions(self, mousePos, mousePressed,screen):
        if mousePressed[0]:
            if self.titleBarXRect.collidepoint(mousePos): # Close
                return "Closing"

            elif self.titleBarDashRect.collidepoint(mousePos): # Minimise
                self.rect = pygame.Rect((0,screen.get_height() - self.titleBarRect.height), self.size)
                self.surface = pygame.transform.scale(self.surface, (self.rect.width, self.rect.height))

                self.titleBarRect = pygame.Rect((0, screen.get_height() - self.titleBarRect.height), (self.size[0], 20))
                self.titleBarSurface = pygame.transform.scale(self.titleBarSurface, (self.titleBarRect.width, self.titleBarRect.height))

                self.titleBarXRect = pygame.Rect((self.titleBarRect.width - 15,screen.get_height() - self.titleBarRect.height), (self.titleBarXRect.width,self.titleBarXRect.height))

                self.titleBarSquareRect = pygame.Rect((self.titleBarRect.width - 30,screen.get_height() - self.titleBarRect.height), (self.titleBarSquareRect.width,self.titleBarSquareRect.height))

                self.titleBarDashRect = pygame.Rect((self.titleBarRect.width - 45,screen.get_height() - self.titleBarRect.height), (self.titleBarDashRect.width,self.titleBarDashRect.height))

                for child in self.childrens:
                    child.moveRect(self.rect)

                return "Minimising"

            elif self.titleBarSquareRect.collidepoint(mousePos): # Maximise
                self.rect = pygame.Rect((0,0), (screen.get_width(), screen.get_height()))
                self.surface = pygame.transform.scale(self.surface, (self.rect.width, self.rect.height))

                self.titleBarRect = pygame.Rect((0,0), (screen.get_width(), self.titleBarRect.height))
                self.titleBarSurface = pygame.transform.scale(self.titleBarSurface, (self.titleBarRect.width, self.titleBarRect.height))

                self.titleBarXRect = pygame.Rect((self.titleBarRect.width - 15,0), (self.titleBarXRect.width,self.titleBarXRect.height))

                self.titleBarSquareRect = pygame.Rect((self.titleBarRect.width - 30,0), (self.titleBarSquareRect.width,self.titleBarSquareRect.height))
                
                self.titleBarDashRect = pygame.Rect((self.titleBarRect.width - 45,0), (self.titleBarDashRect.width,self.titleBarDashRect.height))

                for child in self.childrens:
                    child.moveRect(self.rect)

                return "Maximising"

            elif self.titleBarRect.collidepoint(mousePos): # If the mouse is pressed on the title bar
                self.rect = pygame.Rect((0,0), self.size)
                self.surface = pygame.transform.scale(self.surface, self.size)

                self.titleBarRect = pygame.Rect((0,0), (self.size[0], 20))
                self.titleBarSurface = pygame.transform.scale(self.titleBarSurface, (self.size[0], 20))

                self.titleBarRect.height = self.rect.height
                
                pos = pygame.Vector2(pygame.mouse.get_pos())
                self.titleBarRect.center = pos
                self.rect.x, self.rect.y = self.titleBarRect.x, self.titleBarRect.y
                
                self.titleBarXRect = pygame.Rect((self.titleBarRect.x + self.titleBarRect.width - 15,self.titleBarRect.y), (self.titleBarXRect.width,self.titleBarXRect.height))
                self.titleBarSquareRect = pygame.Rect((self.titleBarRect.x + self.titleBarRect.width - 30,self.titleBarRect.y), (self.titleBarSquareRect.width,self.titleBarSquareRect.height))
                self.titleBarDashRect = pygame.Rect((self.titleBarRect.x + self.titleBarRect.width - 45,self.titleBarRect.y), (self.titleBarDashRect.width,self.titleBarDashRect.height))

                for child in self.childrens:
                    child.moveRect(self.rect)

                screen.blit(self.surface, self.rect)
                screen.blit(self.titleBarSurface, self.titleBarRect)
                return "Dragging"
        else:
            self.titleBarRect.height = 20

    def childrens_Modifyer(self, mousePos, mousePressed, screen):
        for child in self.childrens:
            if child.rect.collidepoint(mousePos): # If the mouse is on the child rect
                if mousePressed[0]: # If the mouse is pressed on the child rect
                    child.selectedChild()
            else:
                if mousePressed[0]:
                    child.selected = False

            if child.selected:
                child.modifyer(mousePos, mousePressed, screen, self.rect)

class Button:
    pass # I will add this later, after I've finished the InputText class

class InputText:
    def __init__(self, rect, surface, text, font, colour, backgroundColour, borderColour, borderThickness, borderRadius, relativePos):
        self.rect = rect # The rect of the input text
        self.surface = surface # The surface of the input text
        self.text = text # The text of the input text
        self.font = font # The font of the input text
        self.colour = colour # The colour of the input text
        self.backgroundColour = backgroundColour # The background colour of the input text
        self.borderColour = borderColour # The border colour of the input text
        self.borderThickness = borderThickness # The border thickness of the input text
        self.borderRadius = borderRadius # The border radius of the input text
        self.relativePos = relativePos

        self.textSurface = pygame.font.SysFont(self.font, 12).render(self.text, True, self.colour) # The text surface of the input text
        self.textRect = self.textSurface.get_rect() # The text rect of the input text
        self.charSize = pygame.font.SysFont(self.font, 12).size("a")[0] # The size of a character in the input text
        self.keyPressed = False # If a key is pressed

        self.cursorSurface = pygame.font.SysFont(self.font, 12).render("|", True, BLACK) # The cursor surface of the input text
        self.cursorRect = self.cursorSurface.get_rect() # The cursor rect of the input text
        self.cursorBlink = 0 # The cursor blink of the input text
        self.cursorPos = 0 # The cursor position of the input text

        self.selected = False # If the input text is selected

    def selectedChild(self): # To setup the input text when it is selected
        self.selected = True
        self.cursorBlink = 1
        self.cursorPos = 0

    def modifyer(self, mousePos, mousePressed, screen, parentRect): # To modify the input text
        # All of the code for the input text, kinda

        self.cursorBlink += 1
        if self.cursorBlink > 30:
            self.cursorBlink = 0

        if self.cursorBlink < 15:
            self.cursorSurface = pygame.font.SysFont(self.font, 12).render("|", True, BLACK)
        else:
            self.cursorSurface = pygame.font.SysFont(self.font, 12).render("|", True, WHITE)


        if self.cursorPos < 0:
            self.cursorPos = 0
        elif self.cursorPos > len(self.text):
            self.cursorPos = len(self.text)

        if self.keyPressed:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]: # If the backspace key is pressed
                if self.cursorPos > 0:
                    self.text = self.text[:self.cursorPos - 1] + self.text[self.cursorPos:]
                    self.cursorPos -= 1
                self.cursorBlink = 1 # The cursor blink is set to 1

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.cursorPos -= 1 # The cursor position is subtracted by 1
                self.cursorBlink = 1 # The cursor blink is set to 1
            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.cursorPos += 1
                self.cursorBlink = 1

            if pygame.key.get_pressed()[pygame.K_DELETE]: # If the delete key is pressed
                self.text = self.text[:self.cursorPos] + self.text[self.cursorPos + 1:] # The text is set to the text before the cursor position, and the text after the cursor position

            if pygame.key.get_pressed()[pygame.K_RETURN]: # If the enter key is pressed
                self.selected = False # The input text is not selected

            for key in KEYS_INPUT_TEXT:
                if pygame.key.get_pressed()[key]:
                    self.text = self.text[:self.cursorPos] + KEYS_INPUT_TEXT[key] + self.text[self.cursorPos:]
                    self.cursorPos += 1
                    self.cursorBlink = 1

        self.textSurface = pygame.font.SysFont(self.font, 12).render(self.text, True, self.colour) # The text surface of the input text
        self.textRect = self.textSurface.get_rect() # The text rect of the input text

        self.cursorRect = pygame.Rect((self.textRect.x + (self.cursorPos * self.charSize) - 4, self.textRect.y), (self.cursorSurface.get_width(), self.cursorSurface.get_height())) # The cursor rect of the input text

        self.surface.fill(self.backgroundColour) # The surface is filled with the background colour
        pygame.draw.rect(
            self.surface, # The surface
            self.borderColour, # The border colour
            (0, 0, self.rect.width, self.rect.height), # The border rect
            self.borderThickness, # The border thickness
            self.borderRadius # The border radius
            ) # The border is drawn
        self.surface.blit(self.textSurface, self.textRect) # The text surface is blitted to the surface

        self.surface.blit(self.cursorSurface, self.cursorRect) # The cursor surface is blitted to the surface

        screen.blit(self.surface, self.rect) # The surface is blitted to the screen        

    def moveRect(self, parentRect): # To move the rect of the input text
        pos = pygame.Vector2((parentRect.x + self.relativePos[0] ,parentRect.y + self.relativePos[1])) # The position of the input text
        self.rect.x, self.rect.y = pos

    def draw(self, screen, windowRect):
        
        self.surface.fill(self.backgroundColour) # The surface is filled with the background colour
        pygame.draw.rect(
            self.surface, # The surface
            self.borderColour, # The border colour
            (0, 0, self.rect.width, self.rect.height), # The border rect
            self.borderThickness, # The border thickness
            self.borderRadius # The border radius
            ) # The border is drawn

        self.surface.blit(self.textSurface, self.textRect) # The text surface is blitted to the surface

        self.surface.blit(self.cursorSurface, self.cursorRect) # The cursor surface is blitted to the surface

        screen.blit(self.surface, self.rect)

def create_fake_screen(title, size, pos):
    fake_screen = FakeScreen(size, WHITE, title, pos)
    return fake_screen

def new_project_pop_up():

    project_pop_up = create_fake_screen("New Project", (500, 500), (100, 100))
    project_pop_up.childrens.append(InputText(
        pygame.Rect((120, 120),
        (200, 20)),
        pygame.Surface((200, 20)),
        "Hello",
        FONT,
        BLACK, WHITE, BLACK, 1, 0,
        (20,20) # The position of the input text relative to the fake screen
        ))

    return project_pop_up

def blit_project_pop_up(screen, NEW_PROJECT_POP_UP):
    screen.blit(NEW_PROJECT_POP_UP.surface, NEW_PROJECT_POP_UP.rect)
    screen.blit(NEW_PROJECT_POP_UP.titleBarSurface, NEW_PROJECT_POP_UP.titleBarRect)

    for child in NEW_PROJECT_POP_UP.childrens:
        if isinstance(child, InputText):
            child.draw(screen, NEW_PROJECT_POP_UP.rect)

    pygame.display.flip()
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Window Example")
screen.fill((28, 130, 173))
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 20, 10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()  # Update the display
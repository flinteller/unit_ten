import pygame
import sys
from pygame.locals import*

pygame.init()
main_surface = pygame.display.set_mode((700, 500), 0, 32)
pygame.display.set_caption("SSFS Logo")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

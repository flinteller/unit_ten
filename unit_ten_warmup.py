import pygame
import sys
import logo
from pygame.locals import*

pygame.init()
main_surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("SSFS Logo")
my_logo = logo.Logo(main_surface)
my_logo.draw_logo()
my_logo.draw_words()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

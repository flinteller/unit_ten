# Flint Eller
# 12/4/18
# This program draws a target and lets the user click five times and
# adds up the total of the points from clicking on different colors
import pygame
import sys
from pygame.locals import*
import Bullseye

pygame.init()
main_surface = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption("Bullseye Game")

my_target = Bullseye.Target(main_surface)
my_target.draw_target()

times = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            my_target.add_points(pygame.mouse.get_pos())
            times += 1
        elif times == 5:
            MOUSEBUTTONDOWN = 0

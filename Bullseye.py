import pygame
import math
class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.main_surface.fill((255, 255, 255))
        pygame.init()

    def draw_target(self):
        black = (0, 0, 0)
        blue = (0, 0, 255)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        pygame.draw.circle(self.main_surface, black, (500, 500), 500, 1)
        pygame.draw.circle(self.main_surface, black, (500, 500), 400, 0)
        pygame.draw.circle(self.main_surface, blue, (500, 500), 300, 0)
        pygame.draw.circle(self.main_surface, red, (500, 500), 200, 0)
        pygame.draw.circle(self.main_surface, yellow, (500, 500), 100, 0)

        pygame.display.update()

    def add_points(self, position):
        self.main_surface.fill((255, 255, 255))
        self.draw_target()
        mouse_font = pygame.font.SysFont("Verdana", 32)
        x_value = position[0]
        y_value = position[1]
        distance = math.sqrt(((x_value - 500) ** 2) + ((y_value - 500) ** 2))
        points = 0
        times = 0
        if distance < 100:
            points = 9
            times += 1
        elif distance > 100 and distance < 200:
            points = 7
            times += 1
        elif distance > 200 and distance < 300:
            points = 5
            times += 1
        elif distance > 300 and distance < 400 :
            points = 3
            times += 1
        elif distance > 400 and distance < 500:
            points = 1
            times += 1
        mouse_label = mouse_font.render(str(points), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))

        pygame.display.update()

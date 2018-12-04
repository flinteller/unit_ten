import pygame
import math
class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.main_surface.fill((255, 255, 255))
        pygame.init()

    def draw_target(self):
        """
        Draws each circle of the target
        :return: none
        """
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
        """
        Finds distance from center and displays points for a click in that ring
        :param position:
        :return: none
        """
        self.main_surface.fill((255, 255, 255))
        self.draw_target()
        mouse_font = pygame.font.SysFont("Verdana", 32)
        x_value = position[0]
        y_value = position[1]
        distance = math.sqrt(((x_value - 500) ** 2) + ((y_value - 500) ** 2))
        if distance < 100:
            return 9
        elif distance > 100 and distance < 200:
            return 7
        elif distance > 200 and distance < 300:
            return 5
        elif distance > 300 and distance < 400 :
            return 3
        elif distance > 400 and distance < 500:
            return 1

        pygame.display.update()

    def points_system(self):
        mouse_label = mouse_font.render(str(points), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))

        pygame.display.update()

import pygame


class Logo:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.green = (0, 102, 71)
        self.gold = (255, 209, 63)
        self.white = (255, 255, 255)
        self.main_surface.fill((255, 255, 255))
        pygame.init()

    def draw_logo(self):
        pygame.draw.rect(self.main_surface, self.green, (5, 5, 400, 200), 3)
        pygame.draw.rect(self.main_surface, self.green, (10, 10, 390, 190), 0)
        pygame.draw.polygon(self.main_surface, self.gold, ((145, 100), (265, 100), (205, 20)), 3)
        pygame.draw.line(self.main_surface, self.gold, (205, 100), (205, 20), 3)
        pygame.draw.line(self.main_surface, self.gold, (205, 100), (235, 60), 3)
        pygame.draw.line(self.main_surface, self.gold, (205, 100), (175, 60), 3)

        pygame.display.update()

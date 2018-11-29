import pygame
class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.main_surface.fill((255, 255, 255))
        pygame.init()

    def draw_target(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        pygame.draw.circle(self.main_surface, WHITE, (500, 500), 500, 5)
        pygame.draw.circle(self.main_surface, BLACK, (500, 500), 400, 0)
        pygame.draw.circle(self.main_surface, BLUE, (500, 500), 300, 0)
        pygame.draw.circle(self.main_surface, RED, (500, 500), 200, 0)
        pygame.draw.circle(self.main_surface, YELLOW, (500, 500), 100, 0)

        pygame.display.update()

    def add_points(self, position):
        self.main_surface.fill((255, 255, 255))
        self.draw_target()
        mouse_font = pygame.font.SysFont("Verdana", 32)
        mouse_label = mouse_font.render(str(position), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))

        pygame.display.update()

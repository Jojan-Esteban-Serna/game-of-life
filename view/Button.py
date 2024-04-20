import pygame


class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.text_font = pygame.font.Font(None, 50)
        self.x = x
        self.y = y
        self.rect = None

    def set_text(self, text):
        self.text = text

    def draw(self, screen):
        text_rendered = self.text_font.render(self.text, True, (0, 0, 0))
        rect = text_rendered.get_rect(center=(self.x, self.y))
        self.rect = rect
        background_color = (255, 255, 255)
        self.draw_background(rect, background_color, screen)
        screen.blit(text_rendered, rect)

    def draw_background(self, rect, color, screen):
        background_rect = pygame.Rect(rect.left - 5, rect.top - 5, rect.width + 10,
                                      rect.height + 10)
        pygame.draw.rect(screen, color, background_rect)
        pygame.draw.rect(screen, (0, 0, 0), background_rect, 1)

    def is_hover(self, x, y):
        return self.rect.collidepoint(x, y)

import pygame

from model.WorldBoard import WorldBoard


class WorldView:
    def __init__(self, world_board, cell_size=18):
        self.world_board: WorldBoard = world_board
        self.cell_size = cell_size
        self.width = cell_size * self.world_board.num_cols
        self.height = cell_size * self.world_board.num_rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.paused = True
        self.speed = 5
        self.pattern_name = 'vacio'

        self.pausefont = pygame.font.Font(None, 50)
        self.speedfont = pygame.font.Font(None, 30)
        self.fade_counter = 0
        self.fade_direction = 1
        self.fade_speed = 5

    def draw(self):
        self.screen.fill((255, 255, 255))

        for row in range(self.world_board.num_rows):
            for col in range(self.world_board.num_cols):
                color = (0, 0, 0) if self.world_board.is_cell_alive(row, col) else (255, 255, 255)
                rect = (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color,rect)
                pygame.draw.rect(self.screen, (150, 150, 150), rect, 1)

        if self.paused:
            self.draw_paused_message()

        self.draw_speed()
        self.draw_info()
        pygame.display.flip()

    def draw_paused_message(self):
        text = self.pausefont.render("Pausado", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        alpha = min(max(0, self.fade_counter), 255)
        text.set_alpha(alpha)
        self.screen.blit(text, text_rect)

        self.fade_counter += self.fade_speed * self.fade_direction
        if self.fade_counter >= 255:
            self.fade_direction = -1
        elif self.fade_counter <= 0:
            self.fade_direction = 1

    def draw_speed(self):
        background_color = (255, 255, 255)
        speed_text = self.speedfont.render(f"Velocidad: {self.speed} ticks/seg", True, (0, 0, 0))
        speed_rect = speed_text.get_rect(topright=(self.width - 10, 10))

        self.draw_background(speed_rect, background_color)

        self.screen.blit(speed_text, speed_rect)

    def draw_info(self):
        background_color = (255, 255, 255)
        info_text = self.speedfont.render(f"Nombre del patron: {self.pattern_name}", True, (0, 0, 0))
        info_rect = info_text.get_rect(topleft=(10, 10))

        self.draw_background(info_rect,background_color)

        self.screen.blit(info_text, info_rect)

    def draw_background(self, rect, color):
        background_rect = pygame.Rect(rect.left - 5, rect.top - 5, rect.width + 10,
                                      rect.height + 10)
        pygame.draw.rect(self.screen, color, background_rect)


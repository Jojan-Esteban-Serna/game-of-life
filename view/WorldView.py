from typing import List

import pygame

from model.WorldBoard import WorldBoard
from observer.Observer import Observer
from view.Button import Button


class WorldView(Observer):
    def __init__(self, world_board, buttoms: List[Button], cell_size=18):
        self.world_board: WorldBoard = world_board
        self.cell_size = cell_size
        self.width = cell_size * self.world_board.num_cols
        self.height = cell_size * self.world_board.num_rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.paused = True
        self._speed = 5
        self.pattern_name = 'vacio'
        self.buttons = buttoms
        self.pausefont = pygame.font.Font(None, 50)
        self.speedfont = pygame.font.Font(None, 30)

    def increase_speed(self):
        self._speed += 5
        self.update()

    def decrease_speed(self):
        self._speed = max(1, self._speed - 5)
        self.update()

    def get_speed(self):
        return self._speed

    def toggle_paused(self):
        self.paused = not self.paused
    def is_paused(self):
        return self.paused
    def update(self):
        self.screen.fill((255, 255, 255))
        padding = 20

        for row in range(self.world_board.num_rows):
            for col in range(self.world_board.num_cols):
                color = (0, 0, 0) if self.world_board.is_cell_alive(row, col) else (255, 255, 255)
                rect = (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (150, 150, 150), rect, 1)

        if self.paused:
            self.draw_paused_message()

        self.draw_speed()
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.flip()

    def draw_paused_message(self):
        text = self.pausefont.render("Pausado (Presiona espacio para iniciar)", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

    def draw_speed(self):
        background_color = (255, 255, 255)
        speed_text = self.speedfont.render(f"Velocidad: {self._speed} fps/seg", True, (0, 0, 0))
        speed_rect = speed_text.get_rect(topright=(self.width - 10, 1 * self.cell_size))

        self.draw_background(speed_rect, background_color)

        self.screen.blit(speed_text, speed_rect)

    def draw_background(self, rect, color):
        background_rect = pygame.Rect(rect.left - 5, rect.top - 5, rect.width + 10,
                                      rect.height + 10)
        pygame.draw.rect(self.screen, color, background_rect)

import sys
from tkinter import filedialog
from typing import List

import pygame

from model.WorldBoard import WorldBoard
from observer.IO import read_file
from utils.WorldLoader import WorldLoader
from utils.WorldSaver import WorldSaver
from view.Button import Button
from view.WorldView import WorldView


class WorldController:
    def __init__(self, view: WorldView, world_board: WorldBoard):
        self.view = view
        self.world_board = world_board
        self.world_saver = WorldSaver()
        self.world_loader = WorldLoader()
        # Parte del problema incluye el analisis (diagrama de clases) y relaciones
        # Botones (accesibilidad)
        # Boton step, reset
        # Debe tener persistencia (cargar de un archivo)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 1:
                    for buttom in self.view.buttons:
                        if buttom.is_hover(x, y):
                            if buttom.text == "Step":
                                self.world_board.step()
                            elif buttom.text == "Reset":
                                self.world_board.reset()
                            elif buttom.text == "Play":
                                self.view.paused = not self.view.paused
                                buttom.text = "Pause"
                            elif buttom.text == "Pause":
                                self.view.paused = not self.view.paused
                                buttom.text = "Play"
                            elif buttom.text == "Load":
                                content = read_file()
                                if content:
                                    self.world_loader.load(self.world_board, content, 0, 0)
                            elif buttom.text == "Save":
                                self.world_saver.save(self.world_board,"save.rle")
                            return

                    row = y // self.view.cell_size
                    col = x // self.view.cell_size
                    self.world_board.toggle_cell(row, col)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.view.paused = not self.view.paused
                    self.view.buttons[0].text = "Pause" if not self.view.paused else "Play"

                elif event.key == pygame.K_UP:
                    self.view.speed += 5
                elif event.key == pygame.K_DOWN:
                    self.view.speed = max(1, self.view.speed - 5)

                elif event.key == pygame.K_r:
                    self.world_board.reset()

    def run_simulation(self):

        while True:
            self.handle_events()
            if not self.view.paused:
                self.world_board.step()
                self.view.clock.tick(self.view.speed)
            self.view.update()




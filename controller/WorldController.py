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
        self.patterns = {
            "Worker bee":"2o12b2o$bo12bo$bobo8bobo$2b2o8b2o2$5b6o2$2b2o8b2o$bobo8bobo$bo12bo$2o12b2o!!",
            "Dinner table":"bo$b3o7b2o$4bo6bo$3b2o4bobo$9b2o2$5b3o$5b3o$2b2o$bobo4b2o$bo6bo$2o7b3o$11bo!",
            "Buckingham":"4bo15bo$3bobo13bobo$3bobo13bobo$b3ob2o11b2ob3o$o23bo$b3ob2o11b2ob3o$3bob2o11b2obo$10bo3bo$11bobo$10b2ob2o$8bo2bobo2bo$7bobobobobobo$7b2o2bobo2b2o$11bobo$12bo!",
            "Cribbage":"4b2o$4bo$b2obo10bo$bo2b2o9b3o$3bo2bo11bo$bob4o10b2o$obo$o2b4o12b3o$b2o3bo11bo3bo6b2o$3b2o5b3o4bo5bo4bobo$3bo5bo3bo4bo3bo5bo$bobo4bo5bo4b3o5b2o$b2o6bo3bo11bo3b2o$10b3o12b4o2bo$29bobo$13b2o10b4obo$13bo11bo2bo$14b3o9b2o2bo$16bo10bob2o$27bo$26b2o!"
        }


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

                elif event.key == pygame.K_a:
                    parser = WorldLoader()
                    self.view.pattern_name = "Worker bee"
                    parser.load(self.world_board,self.patterns["Worker bee"], 15, 30)

                elif event.key == pygame.K_s:
                    parser = WorldLoader()
                    self.view.pattern_name = "Dinner Table"
                    parser.load(self.world_board,
                                self.patterns["Dinner table"], 15, 20)

                elif event.key == pygame.K_d:
                    parser = WorldLoader()
                    self.view.pattern_name = "Buckingham"
                    parser.load(self.world_board,
                                self.patterns["Buckingham"], 15, 20)

                elif event.key == pygame.K_f:
                    parser = WorldLoader()
                    self.view.pattern_name = "Cribbage"
                    parser.load(self.world_board,
                                self.patterns["Cribbage"], 10, 20)

                elif event.key == pygame.K_r:
                    self.world_board.reset()

    def run_simulation(self):

        while True:
            self.handle_events()
            if not self.view.paused:
                self.world_board.step()
                self.view.clock.tick(self.view.speed)
            self.view.update()




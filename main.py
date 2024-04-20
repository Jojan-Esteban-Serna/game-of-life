import pygame

from controller.WorldController import WorldController
from model.WorldBoard import WorldBoard
from view.WorldView import WorldView
from view.Button import Button

if __name__ == '__main__':
    pygame.init()

    world_board: WorldBoard = WorldBoard(36, 70)
    cell_size = 18
    offset = 14*cell_size
    view: WorldView = WorldView(world_board, [Button(text="Play", x=6 * cell_size+offset, y=34 * cell_size),
                                                      Button(text="Step", x=12 * cell_size+offset, y=34 * cell_size),
                                                      Button(text="Reset", x=18 * cell_size+offset, y=34 * cell_size),
                                                      Button(text="Save", x=24 * cell_size+offset, y=34 * cell_size),
                                                      Button(text="Load", x=30 * cell_size+offset, y=34 * cell_size),
                                                      Button(text="Input", x=36 * cell_size+offset, y=34 * cell_size)], cell_size)
    world_board.add_observer(view)
    world_controller: WorldController = WorldController(view, world_board)
    world_controller.run_simulation()

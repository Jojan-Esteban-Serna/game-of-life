import pygame

from controller.WorldController import WorldController
from model.WorldBoard import WorldBoard
from view.WorldView import WorldView

if __name__ == '__main__':
    pygame.init()

    world_board: WorldBoard = WorldBoard(36,70)
    view: WorldView = WorldView(world_board)
    world_controller: WorldController = WorldController(view, world_board)
    world_controller.run_simulation()
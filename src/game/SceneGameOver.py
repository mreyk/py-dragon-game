import sys
import random

import pygame

class SceneGameOver:
    def __init__(self, screen, Debug):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.Debug = Debug
        self.initialize()

    def initialize(self):
        """ """

    def run(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        return self

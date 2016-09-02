import sys
import random

import pygame

import SceneGame

class SceneGameOver:
    def __init__(self, screen, Debug, score=0):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.Debug = Debug
        self.lastGameScore = score
        # Why have it separated?
        self.initialize()

    def initialize(self):
        self.font = pygame.font.SysFont('Arial', 56)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def run(self):
        self.screen.fill((0, 0, 0))
        text1 = self.font.render('Game Over', True, (255, 255, 255))
        text2 = self.sfont.render('Score: ' + str(self.lastGameScore) , True, (255, 255, 255))
        text3 = self.sfont.render('> press space to start again <', True, (255, 255, 255))
        self.screen.blit(text1, (self.width/2 - text1.get_width()/2, 50))
        self.screen.blit(text2, (self.width/2 - text2.get_width()/2, 150))
        self.screen.blit(text3, (self.width/2 - text3.get_width()/2, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
                return SceneGame.SceneGame(self.screen, self.Debug)
        return self

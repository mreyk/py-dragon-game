import sys
import random
import os

import pygame

import SceneGame

class SceneGameStart:
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
        musicPath = os.path.join('data','music','gameover_royal_vagabond.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load(musicPath)
        pygame.mixer.music.play(-1)

    def run(self):
        self.screen.fill((0, 0, 0))
        text1 = self.font.render('PyDRAGON!!', True, (50, 0, 0))
        text3 = self.sfont.render('> press space to start the game <', True, (255, 255, 255))
        self.screen.blit(text1, (self.width/2 - text1.get_width()/2, 50))
        self.screen.blit(text3, (self.width/2 - text3.get_width()/2, 350))

        pygame.display.flip()

        if pygame.mixer.music.get_busy() == False:
                        pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
                return SceneGame.SceneGame(self.screen, self.Debug)
        return self

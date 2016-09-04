import math
import random

import pygame

import EnemyState

class Enemy:

    class StateIdle(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)

        def getName(self):
            return 'Idle'

    def __init__(self, game, drawable, col_rect):
        self.state = Enemy.StateIdle(self, game)
        self.dead = False
        self.drawable = drawable
        self.col_rect = col_rect # collision rect
        self.x = self.col_rect.x
        self.xSpeed = 0
        self.y = self.col_rect.y
        self.ySpeed = 0

    def draw(self, screen, debug=False):
        self.drawable.update(screen)
        if debug:
            pygame.draw.rect(screen, (0,255,0), self.drawable.rect, 2)
            pygame.draw.circle(screen, (255,0,255), (int(self.x) ,int(self.y)), 2)

    def update(self, screen, debug=False):
        self.updateState()
        self.act()
        self.move()
        self.isDead(screen)

    def isDead(self, screen):
        if (self.drawable.rect.right < 0 or
            self.drawable.rect.left > screen.get_width() or
            self.drawable.rect.top > screen.get_height() or
            self.drawable.rect.bottom < 0):
            self.dead = True


    def onDragonCollission(self):
        self.state.onDragonCollission()

    def updateState(self):
        self.state.updateState()

    def act(self):
        self.state.act()

    def move(self):
        self.y += self.ySpeed
        self.x += self.xSpeed

        self.col_rect.x = self.x - self.col_rect.width/2
        self.col_rect.y = self.y - self.col_rect.height/2

        self.drawable.rect.x = self.x - self.drawable.rect.width/2
        self.drawable.rect.y = self.y - self.drawable.rect.height/2

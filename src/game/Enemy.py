import math
import random

import pygame


class Enemy:
    
    def __init__(self, drawable, col_rect):
        self.drawable = drawable
        self.col_rect = col_rect # collision rect
        self.state = 'ENEMY';
        self.STATES = ('ENEMY', 'DEAD', 'AIMING', 'ATTACK')
        self.x = self.col_rect.x
        self.xSpeed = -1
        self.y = self.col_rect.y
        #Find other implementation for these variables
        self.ySpeed = 0
        #Temporary while I think of something better
        self.counter = 0
        self.xpTime = random.random()*30 + 10

    def draw(self, screen, debug=False):
        self.drawable.update(screen)
        if debug:
            pygame.draw.rect(screen, (0,255,0), self.drawable.rect, 2)
            pygame.draw.circle(screen, (255,0,255), (int(self.x) ,int(self.y)), 2)

    def update(self, screen, debug=False):
        # Change this with cooler functions
        self.counter+= 0.1
        if self.counter < self.xpTime:
            self.ySpeed = 4*math.sin(self.counter)
        elif self.state == 'ENEMY':
            self.state = 'AIMING'

        self.y += self.ySpeed
        self.x += self.xSpeed

        self.col_rect.x = self.x - self.col_rect.width/2
        self.col_rect.y = self.y - self.col_rect.height/2

        self.drawable.rect.x = self.x - self.drawable.rect.width/2
        self.drawable.rect.y = self.y - self.drawable.rect.height/2

        if self.drawable.rect.right < 0:
            self.state = 'DEAD'


    def handleEvents(self, event):            
        #Do nothing
        print ''

    def shoot(self, x, y):
        self.state = 'ATTACK'
        xSpeed = self.x - x
        ySpeed = self.y - y
        mod = math.sqrt(xSpeed * xSpeed + ySpeed * ySpeed)
        speedMod = 6
        self.xSpeed = -6*xSpeed/mod
        self.ySpeed = -6*ySpeed/mod

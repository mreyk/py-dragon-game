
import pygame

import Enemy

class EnemySkipper(Enemy.Enemy):

    def __init__(self, drawable, col_rect):
        Enemy.Enemy.__init__(self, drawable, col_rect)
        self.state = 'ENEMY'
        self.STATES = ('ENEMY', 'DEAD', 'HANGING', 'ATTACK')
        self.xSpeed = -2
    
    def update(self, screen, Debug=False):
        self.counter += 0.1
        
        if self.counter > self.xpTime and self.state == 'ENEMY':
            self.state = 'HANGING'
            self.xSpeed = 0
            self.ySpeed = 2
            
        if self.y > 50 and self.state == 'HANGING':
            self.ySpeed = -5
            self.xSpeed = 0.05
            self.state = 'ATTACK'

        if self.state == 'ATTACK':
            self.ySpeed += 0.1

        self.y += self.ySpeed
        self.x += self.xSpeed

        self.col_rect.x = self.x - self.col_rect.width/2
        self.col_rect.y = self.y - self.col_rect.height/2

        self.drawable.rect.x = self.x - self.drawable.rect.width/2
        self.drawable.rect.y = self.y - self.drawable.rect.height/2

        if (self.drawable.rect.right < 0 or self.drawable.rect.bottom > screen.get_height()):
            self.state = 'DEAD'

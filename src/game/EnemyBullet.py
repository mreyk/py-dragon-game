import math

import pygame

import Enemy
import EnemyState

class EnemyBullet(Enemy.Enemy):
    #Here the state does not do anything. Should we use it instead of having the logic in the 'aim' function?
    class StateTravelling(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)

        def getName(self):
            return 'Travelling'

    def __init__(self, game, drawable, col_rect):
        Enemy.Enemy.__init__(self, game, drawable, col_rect)
        self.state = EnemyBullet.StateTravelling(self, game)

    def aim(self, dragon):
        x = dragon.x
        y = dragon.y
        xSpeed = self.x - x
        ySpeed = self.y - y
        mod = math.sqrt(xSpeed * xSpeed + ySpeed * ySpeed)
        speedMod = 6
        self.xSpeed = -6*xSpeed/mod
        self.ySpeed = -6*ySpeed/mod

import math
import random

import pygame

import Enemy
import EnemyState

class EnemyWobbler(Enemy.Enemy):

    class StateIdle(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.counter = 0
            self.nextStateTimer = random.random()*30 + 10

        def getName(self):
            return 'Idle'

        def act(self):
            self.counter+= 0.1
            self.owner.ySpeed = 4*math.sin(self.counter)

        def updateState(self):
            if self.counter >= self.nextStateTimer:
                self.owner.state = EnemyWobbler.StateAttack(self.owner, self.game)

    class StateAttack(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            dragon = game.getDragon()
            x = dragon.x
            y = dragon.y
            xSpeed = self.owner.x - x
            ySpeed = self.owner.y - y
            mod = math.sqrt(xSpeed * xSpeed + ySpeed * ySpeed)
            speedMod = 6
            self.owner.xSpeed = -6*xSpeed/mod
            self.owner.ySpeed = -6*ySpeed/mod

        def getName(self):
            return 'Attack'


    def __init__(self, game, drawable, col_rect):
        Enemy.Enemy.__init__(self, game, drawable, col_rect)
        self.state = EnemyWobbler.StateIdle(self, game)
        self.xSpeed = -1

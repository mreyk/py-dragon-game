
import pygame

import Enemy
import EnemyState

class EnemyShooter(Enemy.Enemy):

    class StateMove(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.timer = 0
            self.owner.xSpeed = -2

        def getName(self):
            return 'Move'

        def updateState(self):
            self.timer += 1
            if self.timer > 200:
                self.owner.state = EnemyShooter.StateShoot(self.owner, self.game)

    class StateShoot(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.owner.xSpeed = 0
            self.shots = 3
            self.shotDelay = 25
            self.timer = 0

        def getName(self):
            return 'Shoot'

        def updateState(self):
            if self.timer % self.shotDelay == 0:
                self.owner.shoot(self.game)
                self.shots -= 1
            self.timer += 1
            if self.shots == 0:
                self.owner.state = EnemyShooter.StateMove(self.owner, self.game)


    def __init__(self, game, drawable, col_rect):
        Enemy.Enemy.__init__(self, game, drawable, col_rect)
        self.state = EnemyShooter.StateMove(self, game)
        self.dead = False

    def shoot(self, game):
        dragon = game.getDragon()
        """
        bullet = EnemyBullet.EnemyBullet(game, ..., ...)
        bullet.aim(dragon)
        game.addEnemy(bullet)
        """

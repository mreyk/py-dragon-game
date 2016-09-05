import pygame

import Enemy
import EnemyState
import EnemyBullet
import AnimDrawable

class EnemyShooter(Enemy.Enemy):

    class StateMove(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.timer = 0
            self.owner.xSpeed = -3

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
        enemy_001 = pygame.image.load('images/enemy_shooter/bullet.png').convert_alpha()
        enemy_frame_rect = enemy_001.get_rect()
        enemy_frames = {
            'enemy': ({'frame': enemy_001, 'time':100},
                      {'frame': enemy_001, 'time':100})
        }

        enemyHeight = 20
        enemy_rect = pygame.Rect(self.x, self.y, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())

        bullet = EnemyBullet.EnemyBullet(game, enemyAnimDrawable , enemy_rect)
        bullet.aim(dragon)
        game.addEnemy(bullet)

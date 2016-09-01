
import pygame

import Enemy
import EnemyState

class EnemySkipper(Enemy.Enemy):

    class StateHang(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.owner.xSpeed = 0
            self.owner.ySpeed = 2
            dragon = game.getDragon()
            self.owner.x = dragon.x

        def getName(self):
            return 'Attack'

        def updateState(self):
            if self.owner.y > 50:
                self.owner.state = EnemySkipper.StateAttack(self.owner, self.game)

    class StateAttack(EnemyState.EnemyState):
        def __init__(self, owner, game):
            EnemyState.EnemyState.__init__(self, owner, game)
            self.owner.xSpeed = 0
            self.owner.ySpeed = -4

        def getName(self):
            return 'Attack'

        def act(self):
            self.owner.ySpeed += 0.2

    def __init__(self, game, drawable, col_rect):
        Enemy.Enemy.__init__(self, game, drawable, col_rect)
        self.state = EnemySkipper.StateHang(self, game)
        self.dead = False
    
    def update(self, screen, Debug=False):
        self.state.updateState()
        self.state.act()

        self.move()

        if (self.drawable.rect.right < 0 or self.drawable.rect.bottom > screen.get_height()):
            self.dead = True

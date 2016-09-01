import sys
import random

import pygame

import AnimDrawable
import Dragon
import Enemy
import EnemySkipper
import Background
import LifeDisplay

class SceneGame:
    def __init__(self, screen, Debug):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.Debug = Debug
        self.initialize()

    def getDragon(self):
        return self.dragon

    def initialize(self):
        #Move 'background logic' to a class of its own
        backImage = pygame.image.load('images/background.jpg').convert()
        backXSpeed = -1
        gameBackground = Background.Background(self.screen, backImage, backXSpeed)
        backImage = pygame.image.load('images/background2.png').convert_alpha()
        backXSpeed = -5
        closerBackground = Background.Background(self.screen, backImage, backXSpeed)
        self.backgrounds = (gameBackground, closerBackground)
        lifeImage = pygame.image.load('images/life.png').convert_alpha()
        self.guiLives = LifeDisplay.LifeDisplay(lifeImage)

        # Come up with a more automated system for loading images and animations
        flyup_001 = pygame.image.load('images/dragon/flyup_001.png').convert_alpha()
        flyup_002 = pygame.image.load('images/dragon/flyup_002.png').convert_alpha()
        flydown_001 = pygame.image.load('images/dragon/flydown_001.png').convert_alpha()
        fire_001 = pygame.image.load('images/dragon/fire_001.png').convert_alpha()
        dragonAnimDrawable = AnimDrawable.AnimDrawable(
            'glide', flyup_001.get_rect(),
            {'glide': ({'frame': flyup_001, 'time':10},
                       {'frame': flyup_001, 'time':10}),
             'fly_up':({'frame': flyup_002, 'time': 20},
                       {'frame': flyup_001, 'time': 20}),
             'fly_down':({'frame': flydown_001, 'time': 20},
                         {'frame': flydown_001, 'time': 20}),
             'fire':({'frame': fire_001, 'time': 200},
                     {'frame':fire_001, 'time': 200})})

        self.dragon = Dragon.Dragon(dragonAnimDrawable)

        enemy_001 = pygame.image.load('images/enemy/enemy_001.png').convert_alpha()
        self.enemy_frame_rect = enemy_001.get_rect()
        self.enemy_frames = {
            'enemy': ({'frame': enemy_001, 'time':100},
                      {'frame': enemy_001, 'time':100})
        }


        fps = 2
        pygame.time.set_timer(pygame.USEREVENT + 1, fps) # Event to fps count (which does not work. Apply classic fixed dt for physics and separate render time)
        pygame.time.set_timer(pygame.USEREVENT + 2, 2000) # Event to create enemies every 2 seconds or so
        update = True
        draw = True
        self.enemyList = []
        self.update = True
        self.draw = True

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            self.dragon.handleEvents(event)
            if event.type == pygame.USEREVENT + 1:
                self.draw = True
                self.update = True
            if event.type == pygame.USEREVENT + 2:
                self.enemyList.append(create_enemy(self, self.enemy_frame_rect, self.enemy_frames, (self.width, self.height)))

        if self.update:
            self.update = False
            for back in self.backgrounds:
                back.update(self.screen, self.Debug)

            self.dragon.update(self.screen, self.Debug)
            if self.dragon.lives <= 0:
                newScene = SceneGame(self.screen, self.Debug)
                return newScene
            for enemy in self.enemyList:
                if enemy.dead:
                    self.enemyList.remove(enemy)
                enemy.update(self.screen, self.Debug)
                self.dragon.checkColl(enemy)
            self.guiLives.update(self.dragon)

        if self.draw:
            self.draw = False
            for back in self.backgrounds:
                back.draw(self.screen, self.Debug)
            self.dragon.draw(self.screen, self.Debug)
            for enemy in self.enemyList:
                enemy.draw(self.screen, self.Debug)
            self.guiLives.draw(self.screen)
            pygame.display.flip()

        return self

def create_enemy(game, enemy_frame_rect, enemy_frames, dims):
    width = dims[0]
    height = dims[1]
    if random.choice(('a','b')) == 'a':
        enemyHeight = 100
        ranges = range(enemyHeight, height + 1 - enemyHeight, height/5)
        yPos = random.choice(ranges)
        enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
        enemyPrototype = Enemy.Enemy(game, enemyAnimDrawable, enemy_rect)
    else:
        enemyHeight = 100
        yPos = -100
        enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
        enemyPrototype = EnemySkipper.EnemySkipper(game, enemyAnimDrawable, enemy_rect)

    pygame.time.set_timer(pygame.USEREVENT + 2, int(2000*random.random() + 1000)) # Event to create enemies every 2 seconds or so

    return enemyPrototype

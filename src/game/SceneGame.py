import sys
import random
import os

import pygame

import AnimDrawable
import Dragon
import EnemyWobbler
import EnemySkipper
import EnemyShooter
import Background
import LifeDisplay
import ScoreDisplay
import SceneGameOver

class SceneGame:
    def __init__(self, screen, Debug):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.Debug = Debug
        self.enemyList = []
        self.update = True
        self.draw = True
        self.gamePaused = False

        self.initialize()

    def getDragon(self):
        return self.dragon

    def addEnemy(self, enemy):
        self.enemyList.append(enemy)

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
        self.guiScore = ScoreDisplay.ScoreDisplay(False, self.width-300, 10)

        # This is more automated endeed, but there is an issue with setting a correct 'time' for each frame. Either the time is constant and the animator keeps extra frames, or we save the time somewhere, like in the image name or in a config file. Anyways, this solution is not really better than the other :(
        # On the other hand, the time is usually constant in animation (?maybe?)
        dragonAnims = {}
        top = 'images/dragon'
        for root, dirs, files in os.walk(top, topdown=False):
            for name in sorted(files):
                splitName = name.split('_')
                anim = splitName[0]
                num = splitName[1]
                frame = pygame.image.load(os.path.join(root, (name))).convert_alpha()
                if anim not in dragonAnims:
                    dragonAnims[anim] = []
                frame = {'frame': frame , 'time': 20}
                dragonAnims[anim].append(frame)

        dragonAnimDrawable = AnimDrawable.AnimDrawable(
            'glide', dragonAnims['flyup'][0]['frame'].get_rect(), dragonAnims)

        self.dragon = Dragon.Dragon(dragonAnimDrawable, (dragonAnimDrawable.rect.width, self.height/2-dragonAnimDrawable.rect.height/2))

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

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.gamePaused = not self.gamePaused
                    if(self.gamePaused):
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                    return self
            self.dragon.handleEvents(event)
            if event.type == pygame.USEREVENT + 1:
                self.draw = True
                self.update = True
            if event.type == pygame.USEREVENT + 2:
                self.enemyList.append(create_random_enemy(self, self.enemy_frame_rect, self.enemy_frames, (self.width, self.height)))

        if self.gamePaused:
            sfont = pygame.font.SysFont('Arial', 32)
            pausetext = sfont.render('>PAUSED: Press \'p\' to continue<', True, (255, 255, 255))
            self.screen.blit(pausetext, (self.width/2 - pausetext.get_width()/2, self.height/2))
            pygame.display.flip()
            return self

        if self.update:
            self.update = False
            for back in self.backgrounds:
                back.update(self.screen, self.Debug)

            self.dragon.update(self.screen, self.Debug)
            if self.dragon.lives <= 0:
                newScene = SceneGameOver.SceneGameOver(self.screen, self.Debug, self.guiScore.getScore())
                return newScene
            for enemy in self.enemyList:
                if enemy.dead:
                    self.guiScore.addScore(100)
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
            self.guiScore.draw(self.screen)
            pygame.display.flip()

        return self

def create_random_enemy(game, enemy_frame_rect, enemy_frames, dims):
    width = dims[0]
    height = dims[1]
    enemyChoice = random.choice(('a','b','c'))
    if enemyChoice == 'a':
        enemyHeight = 100
        ranges = range(enemyHeight, height + 1 - enemyHeight, height/5)
        yPos = random.choice(ranges)
        enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
        enemyPrototype = EnemyWobbler.EnemyWobbler(game, enemyAnimDrawable, enemy_rect)
    elif enemyChoice == 'b':
        enemyHeight = 100
        yPos = -100
        enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
        enemyPrototype = EnemySkipper.EnemySkipper(game, enemyAnimDrawable, enemy_rect)
    elif enemyChoice == 'c':
        enemyHeight = 100
        yPos = height - 200
        enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
        enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
        enemyPrototype = EnemyShooter.EnemyShooter(game, enemyAnimDrawable, enemy_rect)

    pygame.time.set_timer(pygame.USEREVENT + 2, int(2000*random.random() + 1000)) # Event to create enemies every 2 seconds or so

    return enemyPrototype

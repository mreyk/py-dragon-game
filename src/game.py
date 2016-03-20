import sys
import pygame
import json
import AnimDrawable, Dragon, Enemy
from pprint import *

print "Starting game..."

#Loads the configuration

with open('config/config.json') as config_file:
    config = json.load(config_file)

screen_size = width, height = config['screen']['width'], config['screen']['height']
fps = config['fps']

pygame.init()

# Come up with a more automated system for loading images and animations (images/dragon/fly_up001.png ... )
flyup_001 = pygame.image.load('images/dragon/flyup_001.png')
flyup_002 = pygame.image.load('images/dragon/flyup_002.png')
flydown_001 = pygame.image.load('images/dragon/flydown_001.png')
fire_001 = pygame.image.load('images/dragon/fire_001.png')
guy_rect = flyup_001.get_rect()
objectAnimDrawable = AnimDrawable.AnimDrawable('glide', flyup_001.get_rect(), {'glide': ({'frame': flyup_001, 'time':10},
                                                                                        {'frame': flyup_001, 'time':10}),
                                                                              'fly_up':({'frame': flyup_002, 'time': 20},
                                                                                        {'frame': flyup_001, 'time': 20}),
                                                                              'fly_down':({'frame': flydown_001, 'time': 20},
                                                                                          {'frame': flydown_001, 'time': 20}),
                                                                              'fire':({'frame': fire_001, 'time': 200},
                                                                                      {'frame':fire_001, 'time': 200})})
guy_rect = pygame.Rect(0,0,100,60)
dragon = Dragon.Dragon(objectAnimDrawable, guy_rect)

enemy_001 = pygame.image.load('images/enemy/enemy_001.png')
enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_001.get_rect(), {'enemy': ({'frame': enemy_001, 'time':100},
                                                                                        {'frame': enemy_001, 'time':100})})
enemy_rect = pygame.Rect(width, height/2 ,100,100)
enemy = Enemy.Enemy(enemyAnimDrawable, enemy_rect)

screen = pygame.display.set_mode(screen_size)

fps = 10
pygame.time.set_timer(pygame.USEREVENT + 1, fps)
update = True
draw = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        dragon.handleEvents(event)
        if event.type == pygame.USEREVENT + 1:
            draw = True
            update = True

    if update:
        update = False
        dragon.checkColls([enemy])
        dragon.update(screen, True)
        enemy.update(screen, True)
    if draw:
        draw = False
        screen.fill((0,0,0))
        dragon.draw(screen, True)
        enemy.draw(screen, True)
        pygame.display.flip()

print "Finished game."

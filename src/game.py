import sys, copy, json, random
import pygame
import AnimDrawable, Dragon, Enemy
from pprint import *

def main():
    print "Starting game..."

    #Loads the configuration
    with open('config/config.json') as config_file:
        config = json.load(config_file)

    #temporary:
    global width, height
    screen_size =  width, height = config['screen']['width'], config['screen']['height']
    fps = config['fps']

    pygame.init()

    # Come up with a more automated system for loading images and animations (images/dragon/fly_up001.png ... )
    flyup_001 = pygame.image.load('images/dragon/flyup_001.png')
    flyup_002 = pygame.image.load('images/dragon/flyup_002.png')
    flydown_001 = pygame.image.load('images/dragon/flydown_001.png')
    fire_001 = pygame.image.load('images/dragon/fire_001.png')
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
    enemy_frame_rect = enemy_001.get_rect()
    enemy_frames = {'enemy': ({'frame': enemy_001, 'time':100},
                              {'frame': enemy_001, 'time':100})}

    screen = pygame.display.set_mode(screen_size)

    fps = 10
    pygame.time.set_timer(pygame.USEREVENT + 1, fps) # Event to fps count (which does not work. Apply classic fixed dt for physics and separate render time)
    pygame.time.set_timer(pygame.USEREVENT + 2, 2000) # Event to create enemies every 2 seconds or so
    update = True
    draw = True
    enemyList = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            dragon.handleEvents(event)
            if event.type == pygame.USEREVENT + 1:
                draw = True
                update = True
            if event.type == pygame.USEREVENT + 2:
                enemyList.append(__create_enemy(enemy_frame_rect, enemy_frames))

        if update:
            update = False
            dragon.update(screen, True)
            for enemy in enemyList:
                if enemy.state == 'DEAD':
                    enemyList.remove(enemy)
                enemy.update(screen, True)
                dragon.checkColl(enemy)
        if draw:
            draw = False
            screen.fill((0,0,0))
            dragon.draw(screen, True)
            for enemy in enemyList:
                enemy.draw(screen, True)
            pygame.display.flip()

    print "Finished game."

def __create_enemy(enemy_frame_rect, enemy_frames):
    
    enemyAnimDrawable = AnimDrawable.AnimDrawable('enemy', enemy_frame_rect.copy(), enemy_frames.copy())
    enemyHeight = 100
    ranges = range(enemyHeight, height + 1 - enemyHeight, height/5)
    yPos = random.choice(ranges)
    enemy_rect = pygame.Rect(width, yPos, enemyHeight, enemyHeight)
    enemyPrototype = Enemy.Enemy(enemyAnimDrawable, enemy_rect)

    return enemyPrototype

if __name__ == "__main__":
    main()

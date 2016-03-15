import pygame
import sys, random

print "Playing game..."

size = width, height = 800, 600

speed = [0, 0]
enemy_speed = [-10, 0]
back_speed = [-5, 0]
acc = [0, 0.3]
MAX_SPEED = 8


black = 200, 100 , 255

pygame.init()
screen = pygame.display.set_mode(size)

guy_down = pygame.image.load('dragon1.png')
guy_up = pygame.image.load('dragon2.png')
guyrect = guy_down.get_rect()
enemyframe = pygame.image.load('test.png')
enemyrect = enemyframe.get_rect()
enemyrect.left = width
enemyrect.y = random.randint(0+100,height-100)
backgroundframe = pygame.image.load('background.png')
backrect = backgroundframe.get_rect()


counter = 0;
cur_frame = guy_down
next_frame = guy_up

all_enemies = [enemyrect]
while True:

    counter+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            speed[1] = -10
            counter = 0
            cur_frame = guy_up


    guyrect = guyrect.move(speed)

    for enemy in all_enemies:
        all_enemies[0] = enemy.move(enemy_speed)
        if enemy.colliderect(guyrect):
            all_enemies[0].left = width
            all_enemies[0].y = random.randint(0+100,height-100)

        if enemy.left < 0:
            sys.exit()
            all_enemies[0].left = width
            all_enemies[0].y = random.randint(0+100,height-100)


    

    if guyrect.top > height or guyrect.bottom < 0:
        #TODO:GAME OVER
        sys.exit()


    if counter > 20 and cur_frame == guy_up:
        counter = 0
        cur_frame = guy_down


    if speed[1] > MAX_SPEED:
        speed[1] = MAX_SPEED
    else:
        speed[1]+= acc[1]


    backrect = backrect.move(back_speed)
    if(backrect.right < width):
        backrect.left = 0

    screen.blit(backgroundframe, backrect)
    screen.blit(cur_frame, guyrect)
    for enemy in all_enemies:
        screen.blit(enemyframe, enemy)

    
    pygame.display.flip()
    pygame.time.delay(1)



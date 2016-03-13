import pygame
import math

class Dragon:
    def __init__(self, drawable, col_rect):
        self.drawable = drawable
        self.col_rect = col_rect # collision rect
        self.state = 'GLIDING';
        self.STATES = ('FLYING_UP','GLIDING','FLYING_DOWN')
        self.x = self.drawable.rect.x
        self.xSpeed = 0
        self.y = self.drawable.rect.y
        #Find other implementation for these variables
        self.glidingY = 0.5
        self.flyupY = -2
        self.flydownY = 2
        self.xMAXSPEED = 2

    def draw(self, screen):
        screen.blit(self.frame, self.rect)

    def update(self, screen, debug=False):
        # Change this with smoother functions
        if self.state == 'GLIDING':
            self.y += self.glidingY
        elif self.state == 'FLYING_UP':
            self.y += self.flyupY
        elif self.state == 'FLYING_DOWN':
            self.y += self.flydownY

        self.x += self.xSpeed


        self.col_rect.x = self.x - self.col_rect.width/2
        self.col_rect.y = self.y - self.col_rect.height/2

        #Screen boundaries logic (silly: there is a mini-bug, but let's leave it there for now)
        if self.col_rect.left < 0:
            self.x = 0 + self.col_rect.width/2
        elif self.col_rect.right > screen.get_width():
            self.x = screen.get_width() - self.col_rect.width/2
        if self.col_rect.top < 0:
            self.y = self.col_rect.height/2
        elif self.col_rect.bottom > screen.get_height():
            self.y = screen.get_height() - self.col_rect.height/2
        #End screen boundaries logic

        self.drawable.rect.x = self.x - self.drawable.rect.width/2
        self.drawable.rect.y = self.y - self.drawable.rect.height/2

        self.drawable.update(screen)
        if debug:
            pygame.draw.rect(screen, (0,255,0), self.col_rect, 2)
            pygame.draw.circle(screen, (255,0,255), (int(self.x) ,int(self.y)), 2)



    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.state = 'FLYING_UP'
                self.drawable.nextAnim('fly_up')
                self.drawable.restartAnim()
            elif event.key == pygame.K_s:
                self.state = 'FLYING_DOWN'
                self.drawable.nextAnim('fly_down')
                self.drawable.restartAnim()
            elif event.key == pygame.K_d:
                self.xSpeed = self.xMAXSPEED
            elif event.key == pygame.K_a:
                self.xSpeed = -self.xMAXSPEED
        if event.type == pygame.KEYUP:
            if((event.key == pygame.K_w and self.state == 'FLYING_UP') or
               (event.key == pygame.K_s and self.state == 'FLYING_DOWN')):
                self.state = 'GLIDING'
                self.drawable.nextAnim('glide')
                self.drawable.restartAnim()
            elif((event.key == pygame.K_d and self.xSpeed > 0) or
                 (event.key == pygame.K_a and self.xSpeed < 0)):
                self.xSpeed = 0
            

        

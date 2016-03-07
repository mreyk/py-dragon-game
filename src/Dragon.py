import pygame
import math

class Dragon:
    def __init__(self, drawable, collision_rect):
        self.drawable = drawable
        self.collision_rect = collision_rect
        self.state = 'GLIDING';
        self.STATES = ('FLYING_UP','GLIDING','FLYING_DOWN')
        self.x = self.drawable.rect.x
        self.y = self.drawable.rect.y
        #Find other implementation for these variables
        self.glidingY = 0.5
        self.flyupY = -2
        self.flydownY = 2

    def draw(self, screen):
        screen.blit(self.frame, self.rect)

    def update(self, screen):
        # Change this with smoother functions
        if self.state == 'GLIDING':
            self.y += self.glidingY
        elif self.state == 'FLYING_UP':
            self.y += self.flyupY
        elif self.state == 'FLYING_DOWN':
            self.y += self.flydownY

        self.drawable.rect.y = self.y
        self.drawable.update(screen)

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
        if event.type == pygame.KEYUP:
            self.state = 'GLIDING'
            self.drawable.nextAnim('glide')
            self.drawable.restartAnim()

        

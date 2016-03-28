import pygame

class Background:
    def __init__(self, screen, image, xSpeed):
        self.cur_frame = image
        self.x = 0
        self.xSpeed = xSpeed
        self.cur_rect = self.cur_frame.get_rect()

    def draw(self, screen, debug = False):
        width = self.cur_rect.width
        height = self.cur_rect.height
        screen.blit(self.cur_frame, self.cur_rect)
        screen.blit(self.cur_frame, self.cur_rect.move(width, 0))

    def update(self, screen, debug = False):
        self.x += self.xSpeed
        self.cur_rect.x = int(self.x)
        if self.x < -self.cur_rect.width:
            self.x = self.x + self.cur_rect.width

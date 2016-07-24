import pygame

class LifeDisplay:
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()
        self.lives = []

    def update(self, dragon):
        self.lives = dragon.lives

    def draw(self, screen):
        for life in range(self.lives):
            screen.blit(self.image, self.rect.move(self.rect.width*life, 0))

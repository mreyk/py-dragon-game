import pygame

class ScoreDisplay:
    def __init__(self, font=False, x=100, y=100):
        self.x = x
        self.y = y
        if(not font):
            font = pygame.font.Font(None, 60)
        self.font = font
        self.score = 0

    def addScore(self, score):
        self.score += score

    def getScore(self):
        return self.score

    def draw(self, screen):
        scoreText = self.font.render(str(self.score), False, (0,0,0))
        screen.blit(scoreText, (self.x, self.y))

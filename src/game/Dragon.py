import pygame

class Dragon:
    def __init__(self, drawable, xyPos=(0,0)):
        self.drawable = drawable
        self.state = 'GLIDING'
        self.state2 = 'HAPPY'
        self.STATES = ('FLYING_UP','GLIDING','FLYING_DOWN')
        self.x = xyPos[0]
        self.xSpeed = 0
        self.y = xyPos[1]
        #Find other implementation for these variables
        self.glidingY = 0.5
        self.flyupY = -4
        self.flydownY = 4
        self.xMAXSPEED = 4
        self.lives = 3
        self.blinking = True
        self.hitted_counter = 0

    def draw(self, screen, debug=False):
        if self.state2 != 'HITTED' or self.blinking:
            self.drawable.update(screen)
            if debug:
                pygame.draw.rect(screen, (0,255,0), self.drawable.rect, 2)
                pygame.draw.circle(screen, (255,0,255), (int(self.x) ,int(self.y)), 2)

    def update(self, screen, debug=False):
        # Change this with smoother functions
        if self.state == 'GLIDING':
            self.y += self.glidingY
        elif self.state == 'FLYING_UP':
            self.y += self.flyupY
        elif self.state == 'FLYING_DOWN':
            self.y += self.flydownY

        if self.state2 == 'HITTED':
            self.hitted_counter-= 1
            if self.hitted_counter <= 0:
                self.state2 = 'HAPPY'
                self.hitted_counter = 0

        self.x += self.xSpeed

        #Screen boundaries logic (silly: there is a mini-bug, but let's leave it there for now)
        if self.drawable.rect.left < 0:
            self.x = 0 + self.drawable.rect.width/2
        elif self.drawable.rect.right > screen.get_width():
            self.x = screen.get_width() - self.drawable.rect.width/2
        if self.drawable.rect.top < 0:
            self.y = self.drawable.rect.height/2
        elif self.drawable.rect.bottom > screen.get_height():
            self.y = screen.get_height()/2 - self.drawable.rect.height/2
            self.x = self.drawable.rect.width
            self.hitDragon(1)
        #End screen boundaries logic

        self.drawable.rect.x = self.x - self.drawable.rect.width/2
        self.drawable.rect.y = self.y - self.drawable.rect.height/2

        if self.hitted_counter % 10 == 0:
            self.blinking = not self.blinking

    def hitDragon(self, lives=1):
        if self.state2 != 'HITTED':
            self.state2 = 'HITTED'
            self.hitted_counter = 100
            self.lives -= lives

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

    def checkColl(self, enemy):
        if (self.drawable.checkMaskColl(enemy.drawable)):
            self.hitDragon(1)

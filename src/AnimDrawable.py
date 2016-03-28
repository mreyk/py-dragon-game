import pygame

class AnimDrawable():
    
    def __init__(self, start_anim, rect, frames):
        print "Init anim..."
        self.frames = frames
        self.rect = rect
        self.cur_frame = 0
        self.cur_anim = start_anim
        self.next_anim = start_anim
        self.counter = 0

    def nextAnim(self, next_anim):
        self.next_anim = next_anim

    def restartAnim(self):
        self.cur_frame = 0
        self.cur_anim = self.next_anim

    def update(self, screen):
        self.counter+=1
        #NOTE: It does not work for anims of 1 frame. TODO FIX
        if self.counter > self.frames[self.cur_anim][self.cur_frame]['time']:#Use references or something shorter, please
            self.counter = 0
            self.cur_frame+=1
        
        try:
            frame = self.frames[self.cur_anim][self.cur_frame]['frame']
        except:
            self.cur_anim = self.next_anim
            self.cur_frame = 0
            frame = self.frames[self.cur_anim][self.cur_frame]['frame']

        screen.blit(frame, self.rect)

    def checkMaskColl(self, other):
        if not self.rect.colliderect(other.rect):
            return False

        frame = self.frames[self.cur_anim][self.cur_frame]['frame']
        other_frame = other.frames[other.cur_anim][other.cur_frame]['frame']
        mask = pygame.mask.from_surface(frame, 170)
        other_mask = pygame.mask.from_surface(other_frame, 170)
        offset = (other.rect.x - self.rect.x, other.rect.y - self.rect.y)

        return True if mask.overlap(other_mask, offset) else False

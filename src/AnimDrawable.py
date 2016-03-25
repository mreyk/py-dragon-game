class Drawable:
    def __init__(self, rect, frame):
        self.rect = rect
        self.frame = frame

    def draw(self, screen):
        screen.blit(self.frame, self.rect)

class AnimDrawable(Drawable):
    
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
        return True

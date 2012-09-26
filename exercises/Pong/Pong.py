
import pygame

from FeedbackBase.PygameFeedback import PygameFeedback


class Pong(PygameFeedback):

    def init(self):
        PygameFeedback.init(self)
        # color, pos, width and height of the paddle
        self.color = [255, 0, 128]
        self.pos = 100
        self.width = 20
        self.height = 100

    def play_tick(self):
        # clear the background
        self.screen.fill(self.backgroundColor)
        # check for keyboard input
        if self.keypressed:
            if self.lastkey_unicode.lower() == 'w':
                self.pos -= 5
            elif self.lastkey_unicode.lower() == 's':
                self.pos += 5
            self.keypressed = False
        # check if paddle out of screen
        if self.pos < 0: self.pos = 0
        if self.pos > self.screenSize[1]: self.pos = self.screenSize[1]
        # draw the paddle
        pygame.draw.rect(self.screen, self.color,
                         [50, self.pos - self.height/2, self.width, self.height])
        pygame.display.flip()

    def on_control_event(self, data):
        d = data['cl_output']
        if d > 0: self.pos += 5
        elif d < 0: self.pos -= 5


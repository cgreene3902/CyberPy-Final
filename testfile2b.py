"""This is a seperate file that will be used
to test other things without changing the other testfiles
    This is the second variant of testfile2
"""

####
import pygame
import os
####

class PyView(object):
    
    def __init__(self, width=640, height=480, fps=30):
        """Initialize pygame, window, background, font, and 
        other things relating to those
        """
        pygame.init()
        pygame.display.set_caption('Press ESC to quit')
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        self.rect1_width = width
        self.rect1_height = 380
        #self.rectangle1 = pygame.Surface((50,50))
        # pygame.rect(Surface, color, Rect, width=0)
        # Rect: (x1, y1, width, height)
        #rectangle1_surface = self.rectangle1.convert()
        pygame.draw.rect(self.background,
        (200,200,255),
        (0,380,self.rect1_width,self.rect1_height))
        







    def run(self):
        """This is the mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_text('FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS'.format(
                           self.clock.get_fps(), ' '*5, self.playtime))
            
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()
    
    def draw_text(self, text):
        """displays text in window
        """
        
        
        #fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        
        self.screen.blit(surface, (15 // 2, 15 // 2))

####
if __name__ == '__main__':
    # call with width and height of window 
    PyView(640, 480).run()
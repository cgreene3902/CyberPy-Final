"""This file will be used to test a different
way for me to structure the code
"""
import pygame
import os
import random
####
class App(object):
    def __init__(self):
        self._running = True
        self._displ_surf = None
        self.size = self.width, self.height = 640, 480

    def on_init(self): # initializes pygame modules and creates main display
        pygame.init()
        self._displ_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._bg = pygame.Surface(self._displ_surf.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.seconds = 0.0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        self.x1 = 1
        #pygame.draw.rect(self._bg, (200,200,255), (0,380,self.width,380))
        
        
    
    def on_event(self, event): # events to called by the event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
    
    def on_loop(self): # controls changes in the game world
        ####
        ms = self.clock.tick(self.fps)
        self.seconds += ms / 1000.0
        text = 'FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS'
        self.text1 = text.format(self.clock.get_fps(), ' '*5, self.seconds)
        ####
        pygame.display.set_caption('FPS: %.2f' % (self.clock.get_fps()))
        
        # testing out object movement
        self.x1 += 1.5 * 0.75
        pygame.draw.rect(self._bg, (255,255,255), (0,380,self.x1,480))
        
    def on_render(self): # prints out screen graphics

        surface = self.font.render(self.text1, True, (0, 160, 185))
        self._displ_surf.blit(surface, (15 // 2, 15 // 2))
        
        pygame.display.flip()
        self._displ_surf.blit(self._bg, (0, 0))
        
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self): # initializes main loop
        if self.on_init() == False:
            self._running = False

        while(self._running): # main loop init
            for event in pygame.event.get(): # event handler 
                self.on_event(event) # calls event in on_event
            self.on_loop() # 
            self.on_render() # calls objects in on_render to be rendered
        self.on_cleanup()
####
class shapes(object):
    """This is where shape based objects will be defined
    """
    def __init__(self, x, y, speed_x=1, speed_y=1):

        self.x = x
        self.y = y
        self.speed_x = speed_x
        #self.speed_y = speed_y
    
    @property
    def max_x(self):

        return self.x

    def rel_move(self, dx, dy):
        self.x += dx
        self.y += dy

####
if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
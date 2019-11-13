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
        self._screen = None
        self.size = self.width, self.height = 640, 480
    
    def on_init(self): # initializes pygame modules and creates main display
        pygame.init()
        global _screen
        _screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._screen = _screen
        self._running = True
        global _bg
        _bg = pygame.Surface(self._screen.get_size()).convert()
        self._bg = _bg
        
        self._screen.fill((50,50,50))
        self.clock = pygame.time.Clock()
        self.fps = 65
        self.seconds = 0.0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        self.y = 100
        self.x = 615
        self.x1 = 1
        self.x2, self.y2 = 0, 0
        
        
        #pygame.draw.rect(self._bg, (200,200,255), (0,380,self.width,380))
        
        
        self._screen.blit(self._bg, (0, 0))
    
    def on_event(self, event): # events to called by the event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_1:
                self.fps = 150
            elif event.key == pygame.K_2:
                self.fps = 10
            elif event.key == pygame.K_r:
                self.fps = 65
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_a]:
            self.draw_rect(-2,0)
        if pressedkeys[pygame.K_d]:
            self.draw_rect(2,0)
        if pressedkeys[pygame.K_w]:
            self.draw_rect(0,-2)
        if pressedkeys[pygame.K_s]:
            self.draw_rect(0,2) 
        
        

    
    def on_loop(self): # controls changes in the game world
        
        #self._bg2 = self._screen.subsurface(pygame.get_size())
        self.moving_rect1 = pygame.draw.rect(self._screen, (255,255,255), (615,100,20,280))
        ####
        ms = self.clock.tick(self.fps)
        self.seconds += ms / 1000.0
        text = 'FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS'
        self.text1 = text.format(self.clock.get_fps(), ' '*5, self.seconds)
        ####
        pygame.display.set_caption('FPS: %.2f' % (self.clock.get_fps()))
        
    def draw_rect(self,x,y):
        
        self.moving_rect1 = self.moving_rect1.move(x, y); pygame.draw.rect(self._screen, (150,25,50), self.moving_rect1)
        pygame.display.update()
    
    
    def on_render(self): # prints out screen graphics
        pygame.draw.rect(self._screen, (255,255,255), ((self.width/2),0,1,480))
        pygame.draw.rect(self._screen, (255,255,255), (0,(self.height/2),640,1))
        
        
        
        
        surface = self.font.render(self.text1, True, (0, 160, 185))
        self._screen.blit(surface, (15 // 2, 15 // 2))
        pygame.display.update(pygame.Rect(0,0,640,480))
        self._screen.blit(self._bg, (self.x, self.y))
        
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self): # initializes main loop
        if self.on_init() == False:
            self._running = False

        while(self._running): # main loop init
            for event in pygame.event.get(): # event handler 
                self.on_event(event) # calls event in on_event
            #player = App.player_movement()
            
            self.on_loop() #
            #player.draw(self._screen)
            self.on_render() # calls objects in on_render to be rendered
            pygame.display.update()
        self.on_cleanup()
####
    """
    class player_movement():
        
        def __init__(self):
            self.moving_rect1 = pygame.draw.rect(_screen, (255,255,255), (615,100,20,280))

            # handle_keys
        def handle_keys(self):
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[pygame.K_a]:
                self.draw_rect(-1,0)
            if pressedkeys[pygame.K_d]:
                self.draw_rect(1,0)
            if pressedkeys[pygame.K_w]:
                self.draw_rect(0,1)
            if pressedkeys[pygame.K_s]:
                self.draw_rect(0,-1) 
        

        def draw_rect(self,x,y):
            _screen.fill((255,255,255))
            self.moving_rect1 = self.moving_rect1.move(x, y); pygame.draw.rect(self._screen, (255,255,255), self.moving_rect1)
            pygame.display.update()
            
        def draw(self,surface):
            pygame.draw.rect(_bg, (255,255,255), (615,100,20,280))
"""











if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
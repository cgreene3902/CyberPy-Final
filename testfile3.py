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
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._bg = pygame.Surface(self._screen.get_size()).convert()
        self._surface1 = pygame.Surface(self._bg.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.seconds = 0.0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        self.x, self.y = 615, 120 #player rect_start_pos
        self.player_rect_size_w, self.player_rect_size_h = 20, 250
        self.x1, self.y1 = 1, 1
        self.x2, self.y2 = 0, 0
        self.pressed_keys = {"left": False, "right": False, "up": False, "down": False}
        
        self._surface1.fill((50,50,50))
        self._bg.blit(self._surface1, (0, 0))
    
    def on_event(self, event): # events to called by the event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_1:
                self.fps = 30
            if event.key == pygame.K_2:
                self.fps = 60
            if event.key == pygame.K_3:
                self.fps = 120
            if event.key == pygame.K_a:
                self.pressed_keys["left"] = True
            if event.key == pygame.K_d:
                self.pressed_keys["right"] = True
            if event.key == pygame.K_w:
                self.pressed_keys["up"] = True
            if event.key == pygame.K_s:
                self.pressed_keys["down"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.pressed_keys["left"] = False
            if event.key == pygame.K_d:
                self.pressed_keys["right"] = False
            if event.key == pygame.K_w:
                self.pressed_keys["up"] = False
            if event.key == pygame.K_s:
                self.pressed_keys["down"] = False
        
        
    def key_press_events(self):
        
        
        if self.fps == 120:
            self.speed_reduction = 0.1
        if self.fps == 60:
            self.speed_reduction = 0.1
        if self.fps == 30:
            self.speed_reduction = 0.1

        
        
        #if self.pressed_keys["left"] == True:
            #self.x -= 10 * self.speed_reduction
        #if self.pressed_keys["right"] == True:
            #self.x += 10 * self.speed_reduction
        if self.pressed_keys["up"] == True:
            self.y -= 10 * self.speed_reduction
        if self.pressed_keys["down"] == True:
            self.y += 10 * self.speed_reduction
        
        
        
        

    
    def on_loop(self): # controls changes in the game world
        self._surface1.fill((50,50,50))
        pygame.draw.rect(self._bg, (255,255,255), ((self.width/2),0,1,480))
        pygame.draw.rect(self._bg, (255,255,255), (0,(self.height/2),640,1))
        pygame.draw.rect(self._surface1, (255,255,255), (self.x,self.y,self.player_rect_size_w,self.player_rect_size_h))
        ####
        ms = self.clock.tick(self.fps)
        self.seconds += ms / 1000.0
        text = 'FPS: {:6.4}{}PLAYTIME: {:6.4} SECONDS {}'
        self.text1 = text.format(self.clock.get_fps(), ' '*5, self.seconds, ' '*5)
        pygame.display.set_caption('FPS: %.2f' % (self.clock.get_fps()))
        ####

    
    
    def on_render(self): # prints out screen graphics
        
        
        
        surface = self.font.render(self.text1, True, (0, 160, 185))
        self._screen.blit(surface, (15 // 2, 15 // 2))
        pygame.display.update()
        self._screen.blit(self._bg, (0,0))
        self._bg.blit(self._surface1, (0,0))
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self): # initializes main loop
        if self.on_init() == False:
            self._running = False

        while(self._running): # main loop init
            for event in pygame.event.get(): # event handler 
                self.on_event(event) # calls event in on_event
            self.key_press_events()
            self.on_loop() #
            self.on_render() # calls objects in on_render to be rendered
        self.on_cleanup()
####




if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
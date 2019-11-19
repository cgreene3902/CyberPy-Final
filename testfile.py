import pygame
import os
import random
import time
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
        self.fps = 150
        self.seconds, self.minutes = 0, 0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        self.player_rect_size_w, self.player_rect_size_h = 20, 100
        self.x, self.y = 600, (self.height/2 - self.player_rect_size_h/2) #player rect_start_pos
        self.x_speed, self.y_speed = 10, 10
        self.x1, self.y1 = 20, (self.height/2 - self.player_rect_size_h/2)
        self.ball_w, self.ball_h = 20, 20
        self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
        self.pressed_keys = {"a": False, "d": False, "w": False,
        "s": False, "left": False, "right": False, "up": False, "down": False}
        self.clock = pygame.time.Clock()

    def on_event(self, event): # events to called by the event handler
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            
            if event.key == pygame.K_1:
                self.size = self.width, self.height = 640, 480
                self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                self._bg = pygame.Surface(self._screen.get_size()).convert()
                self._surface1 = pygame.Surface(self._bg.get_size()).convert()
                self.player_rect_size_w, self.player_rect_size_h = 20, 100
                self.x_speed, self.y_speed = 10, 10
                self.x1, self.y1 = 20, (self.height/2 - self.player_rect_size_h/2)
                self.x, self.y = self.width - 40, (self.height/2 - self.player_rect_size_h/2)
                self.ball_w, self.ball_h = 20, 20
                self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
                

            if event.key == pygame.K_2:
                self.size =  self.width, self.height = 1280, 720
                self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                self._bg = pygame.Surface(self._screen.get_size()).convert()
                self._surface1 = pygame.Surface(self._bg.get_size()).convert()
                self.player_rect_size_w, self.player_rect_size_h = int(20*1.75), int(100*2)
                self.x_speed, self.y_speed = 15, 15
                self.x1, self.y1 = 40, (self.height/2 - self.player_rect_size_h/2)
                self.x, self.y = self.width - 80, (self.height/2 - self.player_rect_size_h/2)
                self.ball_w, self.ball_h = 20*2, 20*2
                self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
                

            if event.key == pygame.K_3:
                self.fps = 60
            
            if event.key == pygame.K_4:
                self.fps = 120

            if event.key == pygame.K_5:
                self.fps = 150
            
            if event.key == pygame.K_a:
                self.pressed_keys["a"] = True
            
            if event.key == pygame.K_d:
                self.pressed_keys["d"] = True
            
            if event.key == pygame.K_w:
                self.pressed_keys["w"] = True
            
            if event.key == pygame.K_s:
                self.pressed_keys["s"] = True
        
            if event.key == pygame.K_LEFT:
                self.pressed_keys["left"] = True
            
            if event.key == pygame.K_RIGHT:
                self.pressed_keys["right"] = True
            
            if event.key == pygame.K_UP:
                self.pressed_keys["up"] = True
            
            if event.key == pygame.K_DOWN:
                self.pressed_keys["down"] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.pressed_keys["a"] = False
            
            if event.key == pygame.K_d:
                self.pressed_keys["d"] = False
            
            if event.key == pygame.K_w:
                self.pressed_keys["w"] = False
            
            if event.key == pygame.K_s:
                self.pressed_keys["s"] = False
            
            if event.key == pygame.K_LEFT:
                self.pressed_keys["left"] = False
            
            if event.key == pygame.K_RIGHT:
                self.pressed_keys["right"] = False
    
            if event.key == pygame.K_UP:
                self.pressed_keys["up"] = False
            
            if event.key == pygame.K_DOWN:
                self.pressed_keys["down"] = False
        
    def key_press_events(self):
        if self.fps == 150:
            self.speed_reduction = 0.1
        
        if self.fps == 120:
            self.speed_reduction = 0.1
        
        if self.fps == 60:
            self.speed_reduction = 0.1

        #if self.pressed_keys["left"] == True:
            #self.x -= self.x_speed * self.speed_reduction
        
        #if self.pressed_keys["right"] == True:
            #self.x += self.x_speed * self.speed_reduction
        
        if self.pressed_keys["up"] == True:
            if self.y - self.y_speed >= -5:
                self.y -= self.y_speed * self.speed_reduction
        
        if self.pressed_keys["down"] == True:
            if self.y + self.y_speed <= (self.height/2 + self.player_rect_size_h/5 + 125): 
                self.y += self.y_speed * self.speed_reduction
        
        if self.pressed_keys["w"] == True:
            if self.y1 - self.y_speed >= -5:
                self.y1 -= self.y_speed * self.speed_reduction
        
        if self.pressed_keys["s"] == True:
            if self.y1 + self.y_speed <= (self.height/2 + self.player_rect_size_h/5 + 125):
                self.y1 += self.y_speed * self.speed_reduction
        
        ###
        if (self.ball_y+self.ball_h/2) - (self.y1+self.player_rect_size_h/2) < 0:
            if self.y1 - self.y_speed >= -5:
                self.y1 -= self.y_speed // 5
    
        if (self.ball_y+self.ball_h/2) - (self.y1+self.player_rect_size_h/2) > 0:
            if self.y1 + self.y_speed <= (self.height/2 + self.player_rect_size_h/5 + 125):
                self.y1 += self.y_speed // 5
        ###

    def on_loop(self): # controls changes in the game world
        #self.rand_num = random.randint(1,4)
        self._surface1.fill((15,15,15))
        
        self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,self.ball_w,self.ball_h)
        pygame.draw.rect(self._surface1, (230,230,230), self.ball_rect)
        pygame.draw.rect(self._surface1, (150,150,150), ((self.width/2),0,1,self.height))
        pygame.draw.rect(self._surface1, (150,150,150), (0,self.height-1,self.width,1.5))
        pygame.draw.rect(self._surface1, (150,150,150), (0,(self.height-self.height),self.width,1.5))
        self.player_rect1 = pygame.draw.rect(self._surface1, (200,200,200), (self.x,self.y,self.player_rect_size_w,self.player_rect_size_h)) #player 1
        self.player_rect2 = pygame.draw.rect(self._surface1, (200,200,200), (self.x1,self.y1,self.player_rect_size_w,self.player_rect_size_h)) #player 2
        

        #
        self.ms = self.clock.tick(self.fps)
        self.seconds += self.ms / 1000
        text = 'FPS: {:6.4}{}PLAYTIME: {}:{:3.3} {}'
        
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
            self.seconds += self.ms / 1000
            
        pygame.display.set_caption('P2_pos_y: %.0f | Ball_pos: %.0f,%.0f | FPS: %.2f | Time: %.0f:%.2f' % (self.y1,
        self.ball_x, self.ball_y, self.clock.get_fps(), self.minutes, self.seconds))
        self.text1 = text.format(self.clock.get_fps(), ' '*5, self.minutes, self.seconds, ' '*5)
        #
        
        '''
        if self.rand_num == 1:
            if self.ball_x + self.x_speed <= self.width - self.ball_w:
                self.ball_x += self.x_speed / 2
        
        if self.rand_num == 2:
            if self.ball_x - self.x_speed >= 0:
                self.ball_x -= self.x_speed / 2
        
        if self.rand_num == 3:
            if self.ball_y - self.y_speed >= 0:
                self.ball_y -= self.y_speed / 2
        
        if self.rand_num == 4:
            if self.ball_y + self.y_speed <= self.height - self.ball_h:
                self.ball_y += self.y_speed / 2
        '''

    def on_render(self): # prints out screen graphics
        #
        surface = self.font.render(self.text1, True, (0, 255, 255))
        self._screen.blit(surface, (15 // 2, 15 // 2))
        #
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
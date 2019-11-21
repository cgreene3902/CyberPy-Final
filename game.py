"""This is the mostly finished version of the game
"""
import pygame
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
        self.fps = 80
        self.seconds, self.minutes = 0, 0
        self.font = pygame.font.SysFont('mono', 15, bold=True)
        self.player_rect_size_w, self.player_rect_size_h = 20, 100
        self.x, self.y = 600, (self.height/2 - self.player_rect_size_h/2) #player rect_start_pos
        self.rect_speed, self.ball_speed, self.ball_speed2 = 10, 10, 10
        self.x1, self.y1 = 20, (self.height/2 - self.player_rect_size_h/2)
        self.ball_w, self.ball_h = 20, 20
        self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
        self.pressed_keys = {"w": False, "s": False, "up": False, "down": False}
        self.clock = pygame.time.Clock()
        self.score1, self.score2 = 0, 0
        self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,self.ball_w,self.ball_h)
        self.direction = random.randint(1,4)
        self.ai_player = False

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
                self.rect_speed, self.ball_speed, self.ball_speed2 = 10, 10, 10
                self.x1, self.y1 = 20, (self.height/2 - self.player_rect_size_h/2)
                self.x, self.y = self.width - 40, (self.height/2 - self.player_rect_size_h/2)
                self.ball_w, self.ball_h = 20, 20
                self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
                self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,self.ball_w,self.ball_h)
                self.direction = random.randint(1,4)
                self.score1, self.score2 = 0, 0

            '''removed for now 
            if event.key == pygame.K_2:
                self.size =  self.width, self.height = 1280, 720
                self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                self._bg = pygame.Surface(self._screen.get_size()).convert()
                self._surface1 = pygame.Surface(self._bg.get_size()).convert()
                self.player_rect_size_w, self.player_rect_size_h = int(20*1.75), int(100*2)
                self.rect_speed, self.ball_speed, self.ball_speed2 = 15, 15, 15
                self.x1, self.y1 = 40, (self.height/2 - self.player_rect_size_h/2)
                self.x, self.y = self.width - 80, (self.height/2 - self.player_rect_size_h/2)
                self.ball_w, self.ball_h = 20*2, 20*2
                self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
            '''

            if event.key == pygame.K_3:
                self.fps = 80
            
            if event.key == pygame.K_4:
                self.fps = 120

            if event.key == pygame.K_5:
                self.fps = 150
            
            if event.key == pygame.K_LEFTBRACKET:
                self.ai_player = True

            if event.key == pygame.K_RIGHTBRACKET:
                self.ai_player = False                

            if event.key == pygame.K_w:
                self.pressed_keys["w"] = True
            
            if event.key == pygame.K_s:
                self.pressed_keys["s"] = True
            
            if event.key == pygame.K_UP:
                self.pressed_keys["up"] = True
            
            if event.key == pygame.K_DOWN:
                self.pressed_keys["down"] = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.pressed_keys["w"] = False
            
            if event.key == pygame.K_s:
                self.pressed_keys["s"] = False
    
            if event.key == pygame.K_UP:
                self.pressed_keys["up"] = False
            
            if event.key == pygame.K_DOWN:
                self.pressed_keys["down"] = False
        
    def key_press_events(self):
        
        if self.fps == 150:
            self.speed_reduction = 5
        
        if self.fps == 120:
            self.speed_reduction = 4
        
        if self.fps == 80:
            self.speed_reduction = 3
        
        if self.pressed_keys["up"] == True:
            if self.y - self.rect_speed >= -5:
                self.y -= self.rect_speed / self.speed_reduction
        
        if self.pressed_keys["down"] == True:
            if self.y + self.rect_speed <= (self.height/2 + self.player_rect_size_h/5 + 125): 
                self.y += self.rect_speed / self.speed_reduction
    
        if self.ai_player == False:
            if self.pressed_keys["w"] == True:
                if self.y1 - self.rect_speed >= -5:
                    self.y1 -= self.rect_speed / self.speed_reduction
        
            if self.pressed_keys["s"] == True:
                if self.y1 + self.rect_speed <= (self.height/2 + self.player_rect_size_h/5 + 125):
                    self.y1 += self.rect_speed / self.speed_reduction
        #"""ai_player is work in progress
        if self.ai_player == True:
            if (self.ball_y+self.ball_h/2) - (self.y1+self.player_rect_size_h/2) < 25:
                if self.y1 - self.rect_speed >= -5:
                    self.y1 -= self.rect_speed // 3
    
            if (self.ball_y+self.ball_h/2) - (self.y1+self.player_rect_size_h/2) > 25:
                if self.y1 + self.rect_speed <= (self.height/2 + self.player_rect_size_h/5 + 125):
                    self.y1 += self.rect_speed // 3
        
        if self.ai_player == True:
            if (self.ball_y+self.ball_h/2) - (self.y+self.player_rect_size_h/2) < 25:
                if self.y - self.rect_speed >= -5:
                    self.y -= self.rect_speed // 5
    
            if (self.ball_y+self.ball_h/2) - (self.y+self.player_rect_size_h/2) > 25:
                if self.y + self.rect_speed <= (self.height/2 + self.player_rect_size_h/5 + 125):
                    self.y += self.rect_speed // 5
        #"""

    def on_loop(self): # controls changes in the game world
        self._surface1.fill((15,15,15))
        
        self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,self.ball_w,self.ball_h)
        pygame.draw.rect(self._surface1, (230,230,230), self.ball_rect)
        pygame.draw.rect(self._surface1, (150,150,150), ((self.width/2),0,1,self.height))
        pygame.draw.rect(self._surface1, (150,150,150), (0,0,self.width,self.height), 5)
        self.player_rect1 = pygame.draw.rect(self._surface1, (200,200,200), (self.x,self.y,self.player_rect_size_w,self.player_rect_size_h)) #player 1
        self.player_rect2 = pygame.draw.rect(self._surface1, (200,200,200), (self.x1,self.y1,self.player_rect_size_w,self.player_rect_size_h)) #player 2
        
        self.ms = self.clock.tick(self.fps)
        self.seconds += self.ms / 1000
        text = 'player 1 score: {}{} player 2 score: {}'
        
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
            self.seconds += self.ms / 1000
            
        pygame.display.set_caption('| FPS: %.2f | Time: %.0f:%.2f | score p1, p2: %.0f, %.0f |' % (
        self.clock.get_fps(), self.minutes, self.seconds, self.score1, self.score2))
        self.text1 = text.format(self.score1,' ', self.score2)
        
        if self.direction == 1:
            self.ball_x += self.ball_speed/5
            self.ball_y += self.ball_speed2/5
        if self.direction == 2:
            self.ball_x -= self.ball_speed/5
            self.ball_y += self.ball_speed2/5
        if self.direction == 3:
            self.ball_x += self.ball_speed/5
            self.ball_y -= self.ball_speed2/5
        if self.direction == 4:
            self.ball_x -= self.ball_speed/5
            self.ball_y -= self.ball_speed2/5
        
        if self.ball_x <= self.x1 + 20:
            if self.ball_y >= self.y1 - 1 and self.ball_y <= self.y1 + 101:
                self.ball_x = 40
                self.ball_speed = -self.ball_speed
        
        if self.ball_x >= self.x - 20:
            if self.ball_y >= self.y - 1 and self.ball_y <= self.y + 101:
                self.ball_x = 580
                self.ball_speed = -self.ball_speed

        if self.ball_y <= 0:
            self.ball_speed2 = -self.ball_speed2
            self.ball_y = 0
        elif self.ball_y >= self.height-20:
            self.ball_speed2 = -self.ball_speed2
            self.ball_y = self.height-20

        if self.ball_x < 0:
            self.score2+=1
            self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
            self.direction = random.randint(1,4)

        elif self.ball_x > self.width - 20:
            self.score1+=1
            self.ball_x, self.ball_y = (self.width/2 - self.ball_w/2), (self.height/2 - self.ball_h/2)
            self.direction = random.randint(1,4)

        if self.score1 >= 11 and self.score1 > self.score2 + 2:
            print('player 1 wins')
            self._running=False
            
        
        if self.score2 >= 11 and self.score2 > self.score1 + 2:
            print('player 2 wins')
            self._running=False

    def on_render(self): # prints out screen graphics
        
        surface = self.font.render(self.text1, True, (0, 255, 255))
        self._screen.blit(surface, (self.width // 4, 15 // 2))
        
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
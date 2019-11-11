"""This file will be used to test a different
way for me to structure the code
"""
import pygame
import os

####
class App(object):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 480

    def on_init(self, fps=60):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._surf_bg = pygame.Surface(self._display_surf.get_size()).convert()
        pygame.display.set_caption('Press ESC to quit')
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 12, bold=True)
        pygame.draw.rect(self._surf_bg, (200,200,255), (0,380,self.width,380))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
    
    def on_loop(self):
        ms = self.clock.tick(self.fps)
        self.playtime += ms / 1000.0
        text = 'FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS'
        self.text1 = text.format(self.clock.get_fps(), ' '*5, self.playtime)
        

    def on_render(self):
        surface = self.font.render(self.text1, True, (0, 160, 185))
        self._display_surf.blit(surface, (15 // 2, 15 // 2))
        
        pygame.display.flip()
        self._display_surf.blit(self._surf_bg, (0, 0))
        
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
    
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
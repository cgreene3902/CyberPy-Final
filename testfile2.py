"""This is a seperate file that will be used
to test other things without changing the other testfile
"""

###
import pygame
import os
###

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
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE, pygame.DOUBLEBUF)
        pygame.Surface(self.screen.get_size()).convert()

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font.SysFont('', 20, bold=true)

    def run(self):
        """This is the mainloop
        """

"""
This is just a file that will be 
used to test different things from 
the pygame module
"""
import pygame
import os
# main function
def main():

    # initialize pygame module
    pygame.init()
    # loads and sets the logo
    logo = pygame.image.load(os.path.join('Images', 'logo.png'))
    
    image1 = pygame.image.load(os.path.join('Images', '3.png'))
    

    pygame.display.set_icon(logo)
    pygame.display.set_caption('test')

    # creates a surface on screen that is 640 x 480 in resolution
    screen = pygame.display.set_mode((640,480))
    # creates a background on the screen from variable 'bg_color'
    bg_color = 100, 100, 100 # red, green, blue
    screen.fill((bg_color))
    # makes the red parts of 'image1' transparent
    image1.set_alpha(None)
    image1.set_colorkey((255,0,0))
    
    # copies image 'image1' to the screen
    
    screen.blit(image1, (320,240))

    # displays the image 'image1' onto the screen
    pygame.display.flip()

    # variable to control main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                # change the value to False, to exit main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # if user pressed ESC, close window
                    running = False 
        clock = pygame.time.Clock()
        ms = clock.tick(20)
        pltime += ms / 1000.0

if __name__=="__main__":
    # call main function
    main()

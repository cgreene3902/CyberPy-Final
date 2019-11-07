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
    
    image1 = pygame.image.load(os.path.join('Images', '1.png'))
    

    pygame.display.set_icon(logo)
    pygame.display.set_caption('test')

    # creates a surface on screen that is 240 x 180 in resolution
    screen = pygame.display.set_mode((240,180))
    r, g, b = 100, 100, 100
    screen.fill((r,g,b))
    # copies image '1.png' to the screen
    screen.blit(image1, (50,50))
    # displays the image '1.png' onto the screen
    pygame.display.flip()

    # variable to control main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit main loop
                running = False

if __name__=="__main__":
    # call main function
    main()

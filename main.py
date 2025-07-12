import pygame
from constants import *
from player import * 

def main():
    print("Before pygame.init()")
    pygame.init()
    print("After pygame.init()")
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Screen set up.")
    
    # Just to keep the window open for a moment
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    print("Pygame quit.")

if __name__ == "__main__":
    main()


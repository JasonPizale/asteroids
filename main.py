import pygame
from constants import *
from player import *

def main():
    print("Initializing Pygame...")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Pygame initialized. Screen set up.")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    print("Player object created.") 

    clock = pygame.time.Clock()
    dt = 0
    print("Entering game loop...") 
    while True:
        print("Inside game loop iteration.")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event detected. Exiting game.")
                return
        screen.fill("black")
        
        # This print should appear before the call to player.draw
        print(f"Attempting to draw player. Player type: {type(player)}") 
        
        player.draw(screen) 
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
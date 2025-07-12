print("--- Player Module Loaded: Final Check Version ---")

from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # This print should ABSOLUTELY appear if this method is called
        print("--- Inside Player.draw method! CONFIRMED EXECUTION! ---") 
        try:
            # Your original drawing code
            pygame.draw.polygon(screen, "white", self.triangle(), 2)
            print("--- Polygon drawn successfully! ---") # New print
        except Exception as e:
            # Catch any error that might occur during drawing
            print(f"!!! ERROR IN PLAYER.DRAW: {e} !!!")
            import traceback # New import for detailed error
            traceback.print_exc() # Print full traceback
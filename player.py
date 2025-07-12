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
    print("Player draw method called!") # This one should definitely print!
    print(f"Player position: {self.position}")
    print(f"Player radius: {self.radius}")

    try:
        triangle_points = self.triangle()
        print(f"Triangle points: {triangle_points}")
        pygame.draw.polygon(screen, "white", triangle_points, 2)
    except Exception as e:
        print(f"Error drawing triangle: {e}")
from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
        self.rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            2 * self.radius,
            2 * self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
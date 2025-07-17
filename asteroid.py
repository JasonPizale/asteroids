from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            2 * self.radius,
            2 * self.radius
        )
    def draw(self, screen): 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        self.rect.center = (self.position.x, self.position.y)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        vel1 = vel1 * 1.2
        vel2 = vel2 * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position, vel1, new_radius)
        Asteroid(self.position, vel2, new_radius)

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
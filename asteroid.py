from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
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
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        offset_distance = new_radius / 2
        new_pos1 = self.position + vel1.normalize() * offset_distance
        new_pos2 = self.position + vel2.normalize() * offset_distance

        Asteroid(new_pos1.x, new_pos1.y, new_radius, vel1)
        Asteroid(new_pos2.x, new_pos2.y, new_radius, vel2)


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
import pygame
from circleshape import CircleShape  # Import the base CircleShape class
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        position = pygame.Vector2(x, y)  # Construct position from x and y
        super().__init__(position, radius)

        # Add the asteroid into all containers
        if hasattr(self.__class__, 'containers'):
            for container in self.__class__.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", (int(self.position.x), int(self.position.y)), self.radius, 2)
        #print(f"Asteroid created at {self.position.x}, {self.position.y} with radius {self.radius}")

    def update(self, dt):
        self.position += self.velocity * dt
        print(f"Position: {self.position}, Velocity: {self.velocity}, dt: {dt}")

import pygame
from circleshape import CircleShape  # Import the base CircleShape class
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
import random

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
        #print(f"Position: {self.position}, Velocity: {self.velocity}, dt: {dt}")

    def split(self):
        # Kill the asteroid first
        self.kill()
        
        # If it's too small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Create an explosion at the asteroid's position (if you have this feature)
        # Use self.position instead of self.rect.center
        # Explosion(self.position, self.radius)
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the current position
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = velocity1 * 1.2  # Make it move faster
        
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = velocity2 * 1.2  # Make it move faster

    def draw_with_offset(self, screen, offset):
        # Calculate position with offset
        offset_position = (int(self.position.x + offset[0]), int(self.position.y + offset[1]))
        
        # Draw the circle with the offset position
        pygame.draw.circle(screen, "brown", offset_position, self.radius, 2)

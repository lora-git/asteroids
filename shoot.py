import pygame
from circleshape import CircleShape  # Import the base CircleShape class
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        position = pygame.Vector2(x, y)
        super().__init__(position, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity
    
    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        #print(f"Position: {self.position}, Velocity: {self.velocity}, dt: {dt}")
        
        # Optional: Remove the shot if it goes off-screen
        if (self.position.x < -100 or self.position.x > SCREEN_WIDTH + 100 or
            self.position.y < -100 or self.position.y > SCREEN_HEIGHT + 100):
            self.kill()
            
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius, 5)
        #print(f"Shot created at {self.position.x}, {self.position.y} with radius {self.radius}")

    def set_shots_group(self, shots_group):
        self.shots_group = shots_group
    
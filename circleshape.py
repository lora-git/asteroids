import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        # Check if containers are defined, as before.
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Use the provided position directly
        self.position = position  # pygame.Vector2
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
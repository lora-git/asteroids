import pygame
import random

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, radius, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.position = pygame.Vector2(position)
        self.particles = []
        self.lifetime = 0.5  # How long the explosion lasts in seconds
        self.timer = 0
        self.color = color
        self.radius = radius  # Store radius for screen shake calculation
        
        # Create particles based on asteroid size
        particle_count = int(radius * 2)  # More particles for bigger asteroids
        for _ in range(particle_count):
            # Random direction and speed for each particle
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            velocity = pygame.Vector2(speed, 0).rotate(angle)
            size = random.uniform(1, 3)
            lifetime = random.uniform(0.2, self.lifetime)
            
            # Small color variation for particles
            particle_color = (
                min(255, self.color[0] + random.randint(-20, 20)),
                min(255, self.color[1] + random.randint(-20, 20)),
                min(255, self.color[2] + random.randint(-20, 20))
            )
            
            self.particles.append({
                "pos": pygame.Vector2(position),
                "vel": velocity,
                "size": size,
                "lifetime": lifetime,
                "max_lifetime": lifetime,
                "color": particle_color
            })
    
    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifetime:
            self.kill()
            return
            
        # Update each particle
        for particle in self.particles:
            particle["pos"] += particle["vel"] * dt
            particle["lifetime"] -= dt
    
    def draw(self, surface):
        for particle in self.particles:
            # Skip dead particles
            if particle["lifetime"] <= 0:
                continue
            
            # Fade out as lifetime decreases
            alpha = int(255 * (particle["lifetime"] / particle["max_lifetime"]))
            
            # Draw the particle
            color = (255, 255, 255, alpha)  # White particles with alpha
            pos = particle["pos"].int_tuple() if hasattr(particle["pos"], "int_tuple") else (int(particle["pos"].x), int(particle["pos"].y))
            pygame.draw.circle(surface, color, pos, int(particle["size"]))

    def draw_with_offset(self, surface, offset):
        for particle in self.particles:
            # Skip dead particles
            if particle["lifetime"] <= 0:
                continue
            
            # Fade out as lifetime decreases
            alpha = int(255 * (particle["lifetime"] / particle["max_lifetime"]))
            
            # Draw the particle with offset
            color = (255, 255, 255, alpha)  # White particles with alpha
            
            # Calculate offset position
            offset_pos = (
                int(particle["pos"].x) + offset[0], 
                int(particle["pos"].y) + offset[1]
            )
            
            # Draw the particle at the offset position
            pygame.draw.circle(surface, color, offset_pos, int(particle["size"]))
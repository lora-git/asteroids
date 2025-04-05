import pygame
import random
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from explosion import Explosion
import sys  # for sys.exit()


def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock() # Create clock obj
   dt = 0 # Initialize detla time var
   
   # Add screen shake variables
   screen_shake = 0.0
   shake_intensity = 0.0

   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   # Create our groups
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()
   explosions = pygame.sprite.Group()

   # Set both groups as containers for the Player class
   Player.containers = (updatable, drawable)

   # Set static containers before creating instances
   #Asteroid containers
   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = (updatable,)
   Explosion.containers = (explosions, drawable)

   Shot.containers = (shots, updatable, drawable)

   # Create an instance of AsteroidField
   asteroid_field = AsteroidField()

   # Create a player at the center of the screen
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   player.set_shots_group(shots)  # Pass the shots group to the player
   
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      dt = clock.tick(60) / 1000  # Update dt

      # Update screen shake (reduce it over time)
      if screen_shake > 0:
          screen_shake -= dt
          if screen_shake <= 0:
              screen_shake = 0
              shake_intensity = 0

      updatable.update(dt) # Call update on all objects in the updatable group

      #print(f"Drawable entities: {drawable.sprites()}") #Debug: Print all drawable entities

      # Collision Detection: Check if player collides with any asteroid
      for asteroid in asteroids:
         for bullet in shots:
            # Compare positions and radii of asteroid and bullet
            distance = asteroid.position.distance_to(bullet.position)
            if distance <= asteroid.radius + bullet.radius:  # Simple circle collision check
                  # Determine color based on asteroid size
                  if asteroid.radius > ASTEROID_MIN_RADIUS * 2:  # Large asteroid
                     color = (100, 150, 255)  # Blue
                     # Add screen shake for large asteroids
                     screen_shake = 0.3  # Duration in seconds
                     shake_intensity = 8  # Pixels
                  elif asteroid.radius > ASTEROID_MIN_RADIUS:  # Medium asteroid
                     color = (255, 255, 100)  # Yellow
                     # Medium asteroids cause less screen shake
                     screen_shake = 0.2
                     shake_intensity = 4
                  else:  # Small asteroid
                     color = (160, 120, 80)  # Brown
                     # No screen shake for small asteroids
                  
                  # Create explosion with the appropriate color
                  Explosion(asteroid.position, asteroid.radius, color)
                  
                  asteroid.split()  # Split or destroy asteroid
                  bullet.kill()  # Destroy the bullet

         if player.collision_check(asteroid):  # Assuming Player has collision_check method
            print("Game over!")
            pygame.quit()
            sys.exit()

      # Fill the screen with black
      screen.fill("black")

      # Calculate shake offset
      shake_offset = (0, 0)
      if screen_shake > 0:
         shake_offset = (
            random.uniform(-shake_intensity, shake_intensity),
            random.uniform(-shake_intensity, shake_intensity)
         )

      # Draw all objects in the drawable group with shake offset
      for entity in drawable:
         entity.draw_with_offset(screen, shake_offset)

      # Refresh the screen
      pygame.display.flip()
   
   pygame.quit()

if __name__ == "__main__":
    main()
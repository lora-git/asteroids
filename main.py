import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock() # Create clock obj
   dt = 0 # Initialize detla time var
   
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   # Create our groups
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()  # The asteroids-specific group


   # Set both groups as containers for the Player class
   Player.containers = (updatable, drawable)

   #Asteroid containers
   Asteroid.containers = (asteroids, updatable, drawable)
   import random
   random_position = pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
   asteroid = Asteroid(random_position.x, random_position.y, 30)
   asteroid.velocity = pygame.Vector2(50, 50)  # Move diagonally

   # Set static containers before creating instances
   AsteroidField.containers = (updatable,)

   # Create an instance of AsteroidField
   asteroid_field = AsteroidField()

   # Create a player at the center of the screen
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      dt = clock.tick(60) / 1000  # Update dt
      updatable.update(dt) # Call update on all objects in the updatable group

      # Debug: Print all drawable entities
      #print(f"Drawable entities: {drawable.sprites()}")

      # Fill the screen with black
      screen.fill("black")

      # Draw all objects in the drawable group
      for entity in drawable:
         entity.draw(screen)

      # Refresh the screen
      pygame.display.flip()
   
   pygame.quit()

if __name__ == "__main__":
    main()
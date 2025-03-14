import pygame
from constants import *

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock() # Create clock obj
   dt = 0 # Initialize detla time var
   
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
            
      screen.fill((0, 0, 0)) # Fill the screen with black

      # Refresh the screen
      pygame.display.flip()
   
      dt = clock.tick(60) / 1000  # Update dt

   pygame.quit()

if __name__ == "__main__":
    main()
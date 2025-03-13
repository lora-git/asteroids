import pygame
from constants import *

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
         
      # Fill the screen with black
      screen.fill((0, 0, 0))

      # Refresh the screen
      pygame.display.flip()

   pygame.quit()

if __name__ == "__main__":
    main()
import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock() # Create clock obj
   dt = 0 # Initialize detla time var
   
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   # Create a player at the center of the screen
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      dt = clock.tick(60) / 1000  # Update dt
      player.update(dt)

      # Fill the screen with black
      screen.fill("black")

      # Draw the player
      player.draw(screen)

      # Refresh the screen
      pygame.display.flip()
   

   pygame.quit()

if __name__ == "__main__":
    main()
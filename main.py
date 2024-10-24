import pygame
import input
from player import Player
from sprite import sprites
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Practice Clicker Game")
clock = pygame.time.Clock()
running = True
FPS = 30

#Set Colors
CLEAR = (0,0,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIBLUE=(0,128,255)

player = Player("Assets/Lloyd.PNG", 0, 0)

# Game loop

while running:
    # Event handling
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #should be the only IF, so the game will always close first. i think
            running = False
        # Check if keys are currently down or up and handle that
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
    #Update
    player.update()

    # Clear the screen
    screen.fill(BLACK) # Passively fills all blank space with white. Shouldn't do much
    for s in sprites:
        s.draw(screen)

    # Update the display
    pygame.display.flip()
    pygame.time.delay(17) #waits 17ms each loop

# Quit Pygame
pygame.quit()
sys.exit()

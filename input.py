import pygame
import pygame.display as display
import time
from screen import CHIP8Display


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    CHIP8Display()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("LEFT DOWN")
        if keys[pygame.K_RIGHT]:
            print("RIGHT DOWN")

        # Lock framerate at 60
        clock.tick(60)



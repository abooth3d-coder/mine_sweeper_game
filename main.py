import pygame

import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("\nWelcome to Minesweeper")
    print(f"Screen size: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")
    pygame.init()
    print(f"pygame version: {pygame.__version__}")
    pygame.display.set_caption("Minesweeper")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    while True:
        screen.fill(constants.BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == '__main__':
    main()
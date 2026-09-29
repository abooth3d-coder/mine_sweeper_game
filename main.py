import pygame
import grid
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
    game_grid = grid.Grid(SCREEN_WIDTH, SCREEN_HEIGHT, constants.GRID_SIZE)
    game_grid.create_grid()
    while True:
        screen.fill(constants.BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        game_clock.tick(60)
        game_grid.draw_grid(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
import pygame
import mine_grid
import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    # Initializing each logic of the game and the game loop
    print("\nWelcome to Minesweeper")
    print(f"Screen size: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")
    pygame.init()
    print(f"pygame version: {pygame.__version__}")
    pygame.display.set_caption("Minesweeper")    # Set the window title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the window size
    game_clock = pygame.time.Clock()    # Create a clock to manage the frame rate
    game_grid = mine_grid.MineGrid(SCREEN_WIDTH, SCREEN_HEIGHT, constants.GRID_SIZE)    # Create the mine grid instance
    game_grid.create_grid()     # Create the grid of cells
    game_grid.populating_mines()    # Populate the grid with mines
    game_grid.calculate_proximity_numbers()  # Calculate the numbers for each cell based on adjacent mines
    grid_width = constants.GRID_TILES * constants.GRID_SIZE     # Calculate the width of the grid in pixels
    grid_height = constants.GRID_TILES * constants.GRID_SIZE     # Calculate the height of the grid in pixels
    grid_surface = screen.subsurface(pygame.Rect(10, 10, grid_width, grid_height))  # Create a subsurface for the grid to draw on
    while True: # Main game loop
        screen.fill(constants.BACKGROUND_COLOR)     # Fill the screen with the background color
        for event in pygame.event.get(): #Event handling loop
            if event.type == pygame.QUIT: return     # Quit the game if the user closes the window
            elif event.type == pygame.MOUSEBUTTONDOWN:   # Handle mouse button down events
                raw_x, raw_y = event.pos    # Get the raw mouse position
                adjusted_pos = (raw_x - 10, raw_y - 10)  # Adjust the mouse position to account for the grid's offset
                game_grid.handle_click(adjusted_pos, event.button)  # Handle the click event on the grid
        game_clock.tick(60)     # Limit the frame rate to 60 frames per second
        game_grid.draw_grid(grid_surface)   # Draw the grid on the grid surface
        pygame.display.flip()   # Update the display to show the drawn grid

if __name__ == '__main__':      # Run the main function if this script is executed directly
    main()
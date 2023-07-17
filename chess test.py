import pygame

# Initialize Pygame
# If it doesnt work use "pip3 install pygame" on the terminal
pygame.init()

# Set the size of the chessboard and the size of each square
# Use this link for color preference https://www.w3schools.com/colors/colors_picker.asp
board_size = 8
square_size = 80
board_width = board_size * square_size
board_height = board_size * square_size

# Define colors

pink = (255, 230, 255)
purple = (206, 153, 255)

# Create the chessboard surface
board_surface = pygame.Surface((board_width, board_height))
board_surface.fill(purple)

# Draw the squares on the chessboard
for row in range(board_size):
    for col in range(board_size):
        square_color = purple if (row + col) % 2 == 0 else pink
        pygame.draw.rect(board_surface, square_color, (col * square_size, row * square_size, square_size, square_size))

# Create the Pygame window
window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Pink and Purple Chess Board")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chessboard on the window
    window.blit(board_surface, (0, 0))

    # Update the window
    pygame.display.flip()

# Quit Pygame
pygame.quit()

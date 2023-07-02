import pygame
import time

# RGB color constants
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)  # barely visible color for grid

# window size
WIDTH = 750
HEIGHT = 480

# Clock attributes
HOURS = 24
MINUTES = 60
SECONDS = 60

# Size of binary blocks
BLOCK_SIZE = 50
GAP_SIZE = 10
# Size of binary blocks for reference
REF_BLOCK_SIZE = BLOCK_SIZE // 4
REF_GAP_SIZE = GAP_SIZE // 4


# Grid size
GRID_SIZE = 6  # enough to accommodate 24 hours, 60 minutes, and 60 seconds

# Initialize pygame
pygame.init()

# Set the window size
win = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_binary(num, x_start, y_start, max_length):
    binary = bin(num)[2:].zfill(max_length)
    for i, bit in enumerate(binary):
        color = WHITE if bit == '1' else GRAY
        pygame.draw.rect(win, color, pygame.Rect(x_start + i * (BLOCK_SIZE + GAP_SIZE), y_start, BLOCK_SIZE, BLOCK_SIZE))


def draw_small_binary(num, x_start, y_start, max_length):
    binary = bin(num)[2:].zfill(max_length)
    for i, bit in enumerate(binary):
        color = WHITE if bit == '1' else GRAY
        pygame.draw.rect(win, color, pygame.Rect(x_start + i * (REF_BLOCK_SIZE + REF_GAP_SIZE), y_start, REF_BLOCK_SIZE, REF_BLOCK_SIZE))

def draw_reference():
    # Calculate the middle value
    middle_value = 30
    for num in range(60):
        # Calculate the position to draw on screen
        if num < middle_value:
            y_start = num * (REF_BLOCK_SIZE + REF_GAP_SIZE) + 30  # offset from top
            x_start_text = 450  # x-coordinate to start drawing from for text
            x_start_binary = 480  # x-coordinate to start binary representation from
        else:
            y_start = (num - middle_value) * (REF_BLOCK_SIZE + REF_GAP_SIZE) + 30
            x_start_text = 600  # x-coordinate to start drawing from for second column text
            x_start_binary = 630  # x-coordinate to start binary representation from for second column

        # Draw the text and binary representation
        text = pygame.font.Font(None, REF_BLOCK_SIZE).render(str(num), 1, WHITE)
        win.blit(text, (x_start_text, y_start))
        draw_small_binary(num, x_start_binary, y_start, 6)  


def main():
    clock = pygame.time.Clock()
    running = True

    last_update = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = time.time()
        if current_time - last_update >= 1:  # Check if a second has passed
            # Fill the window with black color
            win.fill(BLACK)

            # Get the current time
            time_struct = time.localtime(current_time)
            hours = time_struct.tm_hour
            minutes = time_struct.tm_min

            # Draw hours, minutes, and seconds in binary
            draw_binary(hours, 30, 30, 6)  # 24 hours need 5 bits
            draw_binary(minutes, 30, 130, 6)  # 60 minutes need 6 bits

            # Draw reference
            draw_reference()

            pygame.display.flip()

            last_update = current_time  # Update the time of the last update

        # Delay to maintain an appropriate frame rate (60 FPS is common for games)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

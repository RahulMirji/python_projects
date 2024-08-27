import pygame
import sys
import itertools

# Initialize Pygame
pygame.init()

# Set up displa
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Krishna Janmashtami Animation')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 192, 203)]  # Red, Green, Blue, Yellow, Orange, Pink
color_cycle = itertools.cycle(COLORS)  # Cycle through colors

# Load and resize Krishna image
krishna_image = pygame.image.load('images/krishna 2.jpeg')
krishna_image = pygame.transform.scale(krishna_image, (500, 500))  # Resize the image to 500x500 pixels
krishna_rect = krishna_image.get_rect()

# Center the image vertically, start from the left
krishna_rect.midleft = (0, height // 2)

# Set up movement variables
speed = 5

# Set up font for greeting text
font = pygame.font.SysFont(None, 72)  # Choose a font and size
greeting_text = "Wishing You a Joyous Krishna Janmashtami!"

# Text animation variables
text_x = width  # Start text off-screen
text_y = 100
text_speed = 3 # Speed at which the text moves horizontally
color_change_interval = 15  # Frames before changing color
frame_count = 0  # To track the number of frames#

# Initialize text_surface with the first color
current_color = next(color_cycle)
text_surface = font.render(greeting_text, True, current_color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Krishna horizontally
    krishna_rect.x += speed
    if krishna_rect.left > width:
        krishna_rect.right = 0  # Wrap around to the left

    # Animate text position
    text_x += text_speed
    if text_x > width:
        text_x = -text_surface.get_width()  # Reset text position to start from left again

    # Change text color periodically
    frame_count += 1
    if frame_count % color_change_interval == 0:
        current_color = next(color_cycle)
        text_surface = font.render(greeting_text, True, current_color)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the animated greeting text
    text_rect = text_surface.get_rect(topleft=(text_x, text_y))
    screen.blit(text_surface, text_rect)

    # Draw Krishna
    screen.blit(krishna_image, krishna_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

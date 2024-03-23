import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set the path to your image
image_path = "C:\\Users\\elpid\\OneDrive\\Desktop\\gamespace\\buttonsframe1\\frame1-entire\\Frame 1.png"
lever_image_path = "C:\\Users\\elpid\\OneDrive\\Desktop\\gamespace\\buttonsframe1\\astroglide-lever.png"
spaceship_path = r"C:\Users\elpid\OneDrive\Desktop\gamespace\buttonsframe1\spaceship.png"
pressure_lever_path = r"C:\Users\elpid\OneDrive\Desktop\gamespace\buttonsframe1\pressure-lever.png"

# Get the width and height of the image
image = pygame.image.load(image_path)
image_width, image_height = image.get_rect().size

# Set up display
screen_width = 600  # Set your desired small width
screen_height = int(image_height * (screen_width / image_width))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display Image")

# Load frame image
frame_image = pygame.image.load(image_path)
frame_image = pygame.transform.scale(frame_image, (screen_width, screen_height))  # Scale image to fit the smaller window

# Load spaceship
spaceship = pygame.image.load(spaceship_path)
spaceship_width = 60
spaceship_height = 55
spaceship = pygame.transform.scale(spaceship, (spaceship_width, spaceship_height))
spaceship_y = 50
spaceship_x = 50

# Load pressure lever
pressure_lever = pygame.image.load(pressure_lever_path)
pressure_lever_width = 40
pressure_lever_height = 25
pressure_lever = pygame.transform.scale(pressure_lever, (pressure_lever_width, pressure_lever_height))
pressure_lever_y = 450  # Initial y-coordinate
pressure_lever_x = 529

# Load lever image
astroglide_lever = pygame.image.load(lever_image_path)
lever_width = 40  # New width
lever_height = 25  # New height

# Scale lever image to the new dimensions
astroglide_lever = pygame.transform.scale(astroglide_lever, (lever_width, lever_height))

# Initial position of the lever
lever_y = 265
lever_x = 180  # Set the initial x-coordinate of the lever (40 to 180)

# Define button dimensions and colors
red_button_width = 60
red_button_height = 30

blue_button_width = 60
blue_button_height = 30

green_button_width = 100
green_button_height = 50

black_button_width = 100
black_button_height = 50

# Define button coordinates
red_button_x = 323
red_button_y = 260

blue_button_x = 387
blue_button_y = 260

green_button_x = 67
green_button_y = 430

black_button_x = 70
black_button_y = 367

# Initialize dragging flag
lever_dragging = False
pressure_lever_dragging = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (red_button_x <= mouse_pos[0] <= red_button_x + red_button_width and
                    red_button_y <= mouse_pos[1] <= red_button_y + red_button_height):
                print("You have clicked Ventilation On!")
            elif (blue_button_x <= mouse_pos[0] <= blue_button_x + blue_button_width and
                    blue_button_y <= mouse_pos[1] <= blue_button_y + blue_button_height):
                print("You have clicked Ventilation Off!")
            elif (green_button_x <= mouse_pos[0] <= green_button_x + green_button_width and
                    green_button_y <= mouse_pos[1] <= green_button_y + green_button_height):
                print("You have clicked TechTouch Lock!")
            elif (black_button_x <= mouse_pos[0] <= black_button_x + black_button_width and
                    black_button_y <= mouse_pos[1] <= black_button_y + black_button_height):
                print("You have clicked TechTouch Unlock!")
            elif (lever_x <= mouse_pos[0] <= lever_x + lever_width and
                    lever_y <= mouse_pos[1] <= lever_y + lever_height):
                lever_dragging = True
                # Calculate the offset between mouse click and lever position
                offset_x = mouse_pos[0] - lever_x
            elif (pressure_lever_x <= mouse_pos[0] <= pressure_lever_x + pressure_lever_width and
                    pressure_lever_y <= mouse_pos[1] <= pressure_lever_y + pressure_lever_height):
                pressure_lever_dragging = True
                # Calculate the offset between mouse click and pressure lever position
                pressure_offset_y = mouse_pos[1] - pressure_lever_y
        elif event.type == pygame.MOUSEBUTTONUP:
            lever_dragging = False
            pressure_lever_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if lever_dragging:
                mouse_x, _ = pygame.mouse.get_pos()
                # Update lever position based on mouse movement in x-axis only
                lever_x = mouse_x - offset_x
                # Limit lever position within specified range
                lever_x = max(50, min(lever_x, 215 - lever_width))
            if pressure_lever_dragging:
                _, mouse_y = pygame.mouse.get_pos()
                # Update pressure lever position based on mouse movement in y-axis only
                pressure_lever_y = mouse_y - pressure_offset_y
                # Limit pressure lever position within specified range
                pressure_lever_y = max(305, min(pressure_lever_y, 450))

    # Draw the frame image onto the screen
    screen.blit(frame_image, (0, 0))

    # Draw the lever image
    screen.blit(astroglide_lever, (lever_x, lever_y))

    # Draw the spaceship
    screen.blit(spaceship, (spaceship_x, spaceship_y))

    # Draw the pressure lever
    screen.blit(pressure_lever, (pressure_lever_x, pressure_lever_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

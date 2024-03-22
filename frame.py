import pygame
import os

# Initialize Pygame
pygame.init()

# Set display size
display_width = 800  # Adjust as needed
display_height = 600  # Adjust as needed
scrn = pygame.display.set_mode((display_width, display_height))

# Load button images
try:
   button1_image = pygame.image.load(r"C:\Users\elpid\OneDrive\Desktop\gamespace\frame1\Child Support.png").convert_alpha()
   button2_image = pygame.image.load(r"C:\Users\elpid\OneDrive\Desktop\gamespace\frame1\Rectangle 21.png").convert_alpha()
   button3_image = pygame.image.load(r"C:\Users\elpid\OneDrive\Desktop\gamespace\frame1\Rectangle 24.png").convert_alpha()
except pygame.error as e:
   print("Error loading button images:", e)
   pygame.quit()
   os._exit(1)

# Define initial button positions
button1_pos = [101, 387]
button2_pos = [68, 466]
button3_pos = [101, 443]

# Main loop
status = True
while status:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         status = False

      # Handle mouse events
      elif event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse clicked on a button and update its position
            if button1_image.get_rect(topleft=button1_pos).collidepoint(mouse_pos):
               button1_pos = list(mouse_pos)
            elif button2_image.get_rect(topleft=button2_pos).collidepoint(mouse_pos):
               button2_pos = list(mouse_pos)
            elif button3_image.get_rect(topleft=button3_pos).collidepoint(mouse_pos):
               button3_pos = list(mouse_pos)

   # Clear the screen
   scrn.fill((0, 0, 0))

   # Blit buttons onto the screen at their respective positions
   scrn.blit(button1_image, button1_pos)
   scrn.blit(button2_image, button2_pos)
   scrn.blit(button3_image, button3_pos)

   # Update the display
   pygame.display.flip()

# Quit Pygame
pygame.quit()

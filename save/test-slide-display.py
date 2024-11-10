import pygame
import os
import signal
import sys

# Function to load images from a text file
def load_image_list(filename):
    image_list = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("file"):
                # Extract the filename from the line
                image_name = line.split("'")[1]
                image_list.append(image_name)
    return image_list

# Function to display an image with the correct aspect ratio and black bars
def display_image(screen, image):
    screen_width, screen_height = screen.get_size()
    image_width, image_height = image.get_size()
    
    image_aspect = image_width / image_height
    screen_aspect = screen_width / screen_height

    if image_aspect > screen_aspect:
        new_width = screen_width
        new_height = int(screen_width / image_aspect)
    else:
        new_height = screen_height
        new_width = int(screen_height * image_aspect)

    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    x = (screen_width - new_width) // 2
    y = (screen_height - new_height) // 2

    screen.fill((0, 0, 0))
    screen.blit(scaled_image, (x, y))
    pygame.display.flip()

# Function to handle the signal for moving to the next slide
def handle_signal(signum, frame):
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)
    print(f"Received signal {signum}: moving to slide {current_image_index + 1}")

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Image Slideshow")

# Load the list of images
images = load_image_list('image_list.txt')

# Main loop variables
current_image_index = 0
running = True

# Set up signal handling
signal.signal(signal.SIGUSR1, handle_signal)

# Main loop
while running:
    image_path = images[current_image_index]
    
    if not os.path.isfile(image_path):
        print(f"Image not found: {image_path}")
        current_image_index = (current_image_index + 1) % len(images)
        continue

    image = pygame.image.load(image_path)
    display_image(screen, image)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_DOWN, pygame.K_RETURN]:
                current_image_index = (current_image_index + 1) % len(images)
            elif event.key == pygame.K_UP:
                current_image_index = (current_image_index - 1) % len(images)
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_HOME:
                current_image_index = 0
            elif event.key == pygame.K_END:
                current_image_index = len(images) - 1

# Clean up
pygame.quit()

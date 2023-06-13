import pygame
import os
import cv2
from datetime import datetime
from pygame.locals import *

# Set the dimensions of the window
window_width = 1000
window_height = 500

# Initialize pygame and create the window
pygame.init()
window = pygame.display.set_mode((window_width, window_height), NOFRAME)
pygame.display.set_caption("Hello Yajnesh")
pygame.mouse.set_visible(False)

# Set the font properties
font_size = 120
font_color = (255, 255, 255)
font_path = "font.otf"  # Replace with the path to your custom font file
font_style = pygame.font.Font(font_path, font_size)
text = "Hello Yajnesh"
text_render = font_style.render(text, True, font_color)

# Calculate the position of the text to center it
text_x = (window_width - text_render.get_width()) // 2
text_y = (window_height - text_render.get_height()) // 2

# Load the video file
video_path = "vid.mp4"  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Get the original video dimensions
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Rotate the video 90 degrees counterclockwise
video_rotated = cv2.rotate(cap.read()[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
video_height_rotated, video_width_rotated, _ = video_rotated.shape

# Calculate the position to center the video
video_x = (window_width - video_width_rotated) // 2
video_y = (window_height - video_height_rotated) // 2

# Load the sound file
sound_path = "hello_yajnesh.mp3"  # Replace with the path to your sound file
pygame.mixer.init()
sound = pygame.mixer.Sound(sound_path)

# Set the volume to 25% (0.25)
sound.set_volume(0.1)

clock = pygame.time.Clock()  # Initialize the clock

running = True
start_time = pygame.time.get_ticks()

# Play the sound after a delay of 1 second
pygame.time.wait(1000)
sound.play()

# Create a transparent surface for drawing the curved border
border_surface = pygame.Surface((window_width, window_height), SRCALPHA)
border_radius = 30  # Adjust the radius as desired

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read a frame from the video
    ret, frame = cap.read()

    if ret:
        # Rotate the frame 90 degrees counterclockwise
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convert the frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a Pygame surface
        frame = pygame.surfarray.make_surface(frame)

        # Blit the frame onto the window
        window.blit(frame, (video_x, video_y))

    # Blit the text onto the window
    window.blit(text_render, (text_x, text_y))

    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")  # 12-hour format
    current_date = now.strftime("%d-%m-%Y")

    # Set the font properties for the time and date
    font_size_dt = 32
    font_color_dt = (255, 255, 255)
    font_path_dt = "font1.otf"  # Replace with the path to your custom font file
    font_style_dt = pygame.font.Font(font_path_dt, font_size_dt)

    # Render the time and date text surfaces
    time_render = font_style_dt.render(current_time, True, font_color_dt)
    date_render = font_style_dt.render(current_date, True, font_color_dt)

    # Calculate the position of the time and date texts
    time_x = window_width - time_render.get_width() - 20
    time_y = window_height - time_render.get_height() - 20
    date_x = window_width - date_render.get_width() - 20
    date_y = time_y - date_render.get_height() - 10

    # Blit the time and date onto the window
    window.blit(time_render, (time_x, time_y))
    window.blit(date_render, (date_x, date_y))

    # Clear the border surface
    border_surface.fill((0, 0, 0, 0))

    # Draw the curved border on the border surface
    pygame.draw.rect(border_surface, (255, 255, 255, 100),
                     (0, 0, window_width, window_height), border_radius)

    # Blit the border surface onto the window
    window.blit(border_surface, (0, 0))

    # Update the window display
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS

    # Check if 3 seconds have passed and exit the program
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time >= 3000:
        running = False

# Release the video capture and exit pygame
cap.release()
pygame.quit()

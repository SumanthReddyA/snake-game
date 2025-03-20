import pygame
pygame.font.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
button_color = (100, 100, 100)
button_hover_color = (150, 150, 150)

# Screen dimensions
screen_width = 600
screen_height = 480

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Difficulty settings
difficulty_presets = {
    "easy": 10,
    "medium": 15,
    "hard": 25
}
current_difficulty = "medium"  # Default difficulty

# Fonts
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)
menu_font = pygame.font.SysFont(None, 40)
title_font = pygame.font.SysFont(None, 60)

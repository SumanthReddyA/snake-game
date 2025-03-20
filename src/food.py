import pygame
import random
from src.constants import *

class Food:
    def __init__(self, screen, snake_block):
        self.screen = screen
        self.snake_block = snake_block
        self.x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    def respawn(self):
        self.x = round(random.randrange(0, screen_width - self.snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - self.snake_block) / 10.0) * 10.0

    def draw(self):
        pygame.draw.rect(self.screen, red, [self.x, self.y, self.snake_block, self.snake_block])

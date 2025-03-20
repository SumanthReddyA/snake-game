import pygame
from src.constants import *

class Snake:
    def __init__(self, screen, snake_block):
        self.screen = screen
        self.snake_block = snake_block
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length = 1

    def update_direction(self, direction):
        if direction == "LEFT" and self.x_change == 0:
            self.x_change = -snake_block
            self.y_change = 0
        elif direction == "RIGHT" and self.x_change == 0:
            self.x_change = snake_block
            self.y_change = 0
        elif direction == "UP" and self.y_change == 0:
            self.y_change = -snake_block
            self.x_change = 0
        elif direction == "DOWN" and self.y_change == 0:
            self.y_change = snake_block
            self.x_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def grow(self):
        self.length += 1

    def draw(self):
        for segment in self.snake_list:
            pygame.draw.rect(self.screen, green, [segment[0], segment[1], self.snake_block, self.snake_block])

    def reset(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length = 1

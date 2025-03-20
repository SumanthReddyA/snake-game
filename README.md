# Snake Game

A simple Snake game built with Python and Pygame.

## Features

- Snake that grows when it eats food.
- Food that appears randomly on the screen.
- Game over on collision with self or walls.
- Score counter.
- Basic UI with start and restart options.
- Difficulty Levels: Easy, Medium, and Hard.
  - Easy: Slower snake speed for beginners.
  - Medium: Moderate snake speed, balanced gameplay.
  - Hard: Faster snake speed for experienced players.

## Setup Instructions

1. **Install Pygame:**
   ```bash
   pip install pygame
   ```

2. **Ensure Assets Directory:**
   Make sure the `assets` directory is located in the project root (`snake-game/assets`). This directory contains the `eat.wav` and `game_over.wav` sound files, which are required for the game to run properly.

## VS Code Configuration

If you encounter issues with the "import pygame could not be resolved" error in VS Code, ensure that VS Code is using the correct Python interpreter for the project.

1.  **Check Python Interpreter:** In VS Code, look at the bottom-right corner of the window. You should see the name of the selected Python interpreter.
2.  **Select Correct Interpreter:** If the selected interpreter is not the one where Pygame is installed, click on it. A list of available Python interpreters will appear. Choose the interpreter where Pygame is installed (e.g., the one associated with your Miniconda environment).

## Dependencies

- Pygame

## Directory Structure

```
snake-game/
├── assets/              # For images, sounds, etc.
├── src/                  # Source code
│   ├── __init__.py
│   ├── play_game.py           # Main game logic
│   ├── snake.py          # Snake class
│   ├── food.py          # Food class
│   └── constants.py     # Constants like screen size, colors, etc.
├── tests/                # Unit tests
│   └── test_snake.py
├── requirements.txt       # Dependencies
└── README.md             # Project documentation

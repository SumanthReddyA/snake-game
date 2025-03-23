# Snake Game

A simple Snake game built with Python and Pygame, leveraging modern tools like auto-code agents and LLMs to enhance productivity and learning.

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

## Development Process

This Snake game was developed using modern tools and techniques to enhance productivity and learning:
- **Auto-Code Agents**: Used to generate boilerplate code and assist with repetitive tasks.
- **LLM Models (Gemini 2.0 Flash)**: Leveraged for brainstorming, problem-solving, and generating initial prompts.
- **Manual Development**: The final implementation, debugging, and customization were done manually to ensure the game meets all requirements.

### Example Prompts
Here are some of the prompts used during development:
- **Initial Prompt**:  
  ```plaintext
  Help me define the scope of a Snake game project. The game should include:
  - A snake that grows when it eats food.
  - Food that appears randomly on the screen.
  - Game over when the snake collides with itself or the wall.
  - A score counter.
  - Basic UI with a start and restart option.
  - The game should be built using Python and a simple GUI library like Pygame.

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

# Snake Game

A classic Snake game built with Python and Pygame.

## Source Code
[Snake.py](./Snake.py)

## Requirements

- Python 3.x
- Pygame

Install Pygame with:

```bash
pip install pygame
```

## How to Run

```bash
python snake.py
```

## How to Play

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |

- Guide the snake to eat the **red food** to grow longer and increase your score.
- The game ends if the snake hits a **wall** or runs into **itself**.
- After a game over, click **"Play Again?"** to restart.

## Features

- Score display
- Animated snake with eyes and a mouth
- Random food placement
- Collision detection (walls and self)
- Game over screen with restart button

## Game Variables

| Variable | Value | Description |
|----------|-------|-------------|
| Screen size | 600 × 600 px | Game window dimensions |
| Cell size | 10 px | Size of each snake segment and food |
| Starting length | 4 segments | Initial snake length |


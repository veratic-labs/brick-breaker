# Brick Breaker

A simple Brick Breaker game developed with Python and Pygame.

## Features

* Player-controlled paddle
* Ball and brick collision detection
* Different collision responses depending on the impact direction
* Victory and game over screens
* Restart functionality
* Well-suited for AI and reinforcement learning experiments

### Collision Mechanics

* The ball bounces off walls and the paddle.
* When the ball hits a brick from the top or bottom, its vertical velocity is reversed.
* When the ball hits the side of a brick, its horizontal velocity is reversed.
* The paddle affects the ball's horizontal velocity:

  * Hits near the center produce the smallest horizontal speed.
  * Hits near the edges produce larger horizontal speeds, allowing the player to control the ball's direction.

## AI Potential

The game is designed with simple and deterministic mechanics, making it a good environment for experimenting with AI agents and reinforcement learning algorithms.

Possible future applications include:

* Rule-based agents
* Genetic algorithms
* Q-Learning
* Deep Q Networks (DQN)
* Other reinforcement learning approaches

## Requirements

* Python 3
* Pygame

Install Pygame:

```bash
pip install pygame
```

## Running the Game

Clone the repository and run:

```bash
python game.py
```

## Controls

* Left Arrow: Move paddle left
* Right Arrow: Move paddle right

## License

Copyright (c) 2026 Veratic Labs

Licensed under the Apache License 2.0.

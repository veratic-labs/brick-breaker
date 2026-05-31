"""
Brick Breaker
A classic Brick Breaker game built with Pygame.

Copyright (c) 2026 Ignaxus
Licensed under the Apache License, Version 2.0
"""

#import modules
import pygame
import sys

#import other classes
from ball import Ball
from paddle import Paddle
from brick import Brick
from interface import Interface

#class for the game
class Game:
    def __init__(self):
        pygame.init()

        #set icon
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        self.width = 800
        self.height = 640

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (200, 0, 0)
        self.GREEN = (0, 180, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Brick Breaker")

        self.clock = pygame.time.Clock()

        #add all other classes
        self.ball = Ball(self)
        self.paddle = Paddle(self)
        self.interface = Interface(self)

        #add bricks
        self.arrange_bricks()

        #scores and gameover status
        self.score = 0
        self.game_over = False
        self.victory = False

    #arrange bricks on the screen
    def arrange_bricks(self):
        self.bricks = []

        for row in range(10):
            for col in range(26):
                x = 38 + col * 28
                y = 90 + row * 28
                brick = Brick(self, x, y)
                self.bricks.append(brick)
    
    #enable user to quit   
    def check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.interface.restart_button.collidepoint(event.pos):
                        self.restart()
    
    def check_game_over(self):
        if self.ball.y - self.ball.radius > self.height:
            self.game_over = True

    def check_victory(self):
        if len(self.bricks) == 0:
            self.victory = True
   
    def restart(self):
        self.score = 0
        self.game_over = False

        self.ball = Ball(self)
        self.paddle = Paddle(self)

        self.arrange_bricks()

    #update the position of all elements
    def update_position(self):
        self.paddle.move()
        self.ball.move(self, self.paddle, self.bricks)
        
    #update all element in the screen
    def update_screen(self):
        self.screen.fill(self.WHITE)
        self.ball.draw()
        self.paddle.draw()

        for brick in self.bricks:
            brick.draw()

        self.interface.draw_interface(self)
        
        pygame.display.update()
        self.clock.tick(60)
    
    #main loop of the game
    def run(self):
        while True:
            self.check_event()

            if not self.game_over and not self.victory:
                self.check_game_over()
                self.check_victory()
                self.update_position()

            self.update_screen()

#start running the game
if __name__ == "__main__":
     game = Game()
     game.run()
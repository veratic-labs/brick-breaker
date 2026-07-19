"""
Copyright (c) 2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

class Paddle:
    def __init__(self, game):
        self.screen = game.screen

        #set the size and color of the paddle
        self.width = 80
        self.height = 8
        self.color = game.BLACK

        #original position
        self.x = 360
        self.y = 610

        #set speed
        self.speed = 10

    #control the movement of paddle when keys are pressed
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        #prevent paddle moving out of the window
        if self.x < 0:
            self.x = 0

        if self.x + self.width > 800:
            self.x = 800 - self.width

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))


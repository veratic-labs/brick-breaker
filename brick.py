"""
Copyright (c) 2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

#class for brick
class Brick:
    def __init__(self, game, x, y):
        self.screen = game.screen

        #position
        self.x = x
        self.y = y

        #size
        self.width = 25
        self.height = 25

        #color
        self.color = game.BLACK

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
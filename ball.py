"""
Copyright (c) 2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame
import random

#class for the ball
class Ball:
    def __init__(self, game):
        self.screen = game.screen

        #initial position, random position under bricks
        self.x = random.randint(100, 700)
        self.y = random.randint(390, 490)   
        
        #set radius and color
        self.radius = 15
        self.color = game.BLACK

        #set speed
        self.speed_x = 4*random.choice([-1,1])
        self.speed_y = -4

    #movement of the ball, including collisions
    def move(self, game, paddle, bricks):
        self.x += self.speed_x
        self.y += self.speed_y

        self.wall_collision()
        self.paddle_collision(game, paddle)
        self.brick_collision(bricks)

    def wall_collision(self):
        # left wall
        if self.x - self.radius <= 0:
            self.speed_x *= -1

        # right wall
        if self.x + self.radius >= 800:
            self.speed_x *= -1

        # top wall
        if self.y - self.radius <= 40:
            self.speed_y *= -1

    def paddle_collision(self, game, paddle):
        #check collision
        if (
            self.y + self.radius >= paddle.y
            and self.y - self.radius <= paddle.y + paddle.height
            and self.x + self.radius >= paddle.x
            and self.x - self.radius <= paddle.x + paddle.width
            and self.speed_y > 0
        ):
            #x speed would vary when the ball hit different places on paddle
            #x speed becomes minimum when hit the middle and maximum when hit the edges,
            #the speed varies linearly

            #distance of ball from the centre of the paddle as a percentage of its half length
            hit_pos = abs(self.x - (paddle.x + paddle.width / 2)) / (paddle.width / 2)

            #only change speed, not change direction
            if self.speed_x >= 0:
                self.speed_x = 2 + hit_pos * 4

            else:
                self.speed_x = -2 - hit_pos * 4

            #change y direction
            self.speed_y = -abs(self.speed_y)

            #prevent ball going into the paddle
            self.y = paddle.y - self.radius

            #when collide, add one score
            game.score += 1

    def brick_collision(self, bricks):
        for brick in bricks[:]:
            #check collision
            if (
                self.x + self.radius >= brick.x
                and self.x - self.radius <= brick.x + brick.width
                and self.y + self.radius >= brick.y
                and self.y - self.radius <= brick.y + brick.height
            ):

                brick_center_x = brick.x + brick.width / 2
                brick_center_y = brick.y + brick.height / 2

                #distance from brick's centre to ball's centre
                dx = self.x - brick_center_x
                dy = self.y - brick_center_y

                #decide which direction is changed
                #prevent ball going into the bricks
                if abs(dx) > abs(dy):
                    self.speed_x *= -1

                    if dx > 0:
                        self.x = brick.x + brick.width + self.radius
                    else:
                        self.x = brick.x - self.radius
                
                else:
                    self.speed_y *= -1

                    if dy > 0:
                        self.y = brick.y + brick.height + self.radius
                    else:
                        self.y = brick.y - self.radius

                bricks.remove(brick)
                break
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
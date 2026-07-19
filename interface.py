"""
Copyright (c) 2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

#class for score, gameover and restart interface
class Interface:
    def __init__(self, game):
        self.screen = game.screen

        #font sizes
        self.font = pygame.font.SysFont(None, 30)
        self.large_font = pygame.font.SysFont(None, 60)

        #position of restart button
        self.restart_button = pygame.Rect(game.width - 90, 5, 80, 30)
 
    #show scores
    def draw_score(self, game):
        text = self.font.render(f"Score: {game.score}", True, game.BLACK)
        self.screen.blit(text, (10, 8))

    #draw separation lines
    def draw_separation(self, game):
        pygame.draw.line(self.screen, game.BLACK, (0, 40), (800, 40), 2)

    #draw gameover
    def draw_game_over(self, game):
        text = self.large_font.render("GAME OVER", True, game.WHITE)

        text_rect = text.get_rect(center=(game.width / 2, game.height / 2))

        padding = 20

        background_rect = pygame.Rect(
            text_rect.left - padding,
            text_rect.top - padding,
            text_rect.width + padding * 2,
            text_rect.height + padding * 2
        )

        pygame.draw.rect(self.screen, game.RED, background_rect)
        
        self.screen.blit(text, text_rect)

    #draw victory
    def draw_victory(self, game):
        text = self.large_font.render("VICTORY", True, game.WHITE)

        text_rect = text.get_rect(center=(game.width / 2, game.height / 2))

        padding = 20

        background_rect = pygame.Rect(
            text_rect.left - padding,
            text_rect.top - padding,
            text_rect.width + padding * 2,
            text_rect.height + padding * 2
        )

        pygame.draw.rect(self.screen, game.GREEN, background_rect)

        self.screen.blit(text, text_rect)

    #show restart button
    def draw_restart_button(self, game):
        #white bg color, if mouse is on, bg color turn black
        mouse_pos = pygame.mouse.get_pos()

        if self.restart_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, game.BLACK, self.restart_button)

            text_color = game.WHITE

        else:
            pygame.draw.rect(self.screen, game.BLACK, self.restart_button, 2)

            text_color = game.BLACK

        text = self.font.render("Restart", True, text_color)

        text_rect = text.get_rect(center=self.restart_button.center)
        self.screen.blit(text, text_rect)

    def draw_interface(self, game):
        self.draw_score(game)
        self.draw_separation(game)
        self.draw_restart_button(game)

        if game.victory:
            self.draw_victory(game)
        
        elif game.game_over:
            self.draw_game_over(game)
#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the button class

import pygame


class ButtonClass:
    def __init__(self, color, position_x, position_y, width, height, text=''):
        self._color = color
        self._position_x = position_x
        self._position_y = position_y
        self._width = width
        self._height = height
        self._text = text

    def draw_button(self, screen, text_size, outline=None):
        # draw button
        if outline:
            pygame.draw.rect(screen, outline, (self._position_x - 2, self._position_y - 2, self._width + 4, self._height + 4), 0)

        pygame.draw.rect(screen, self._color, (self._position_x, self._position_y, self._width, self._height), 0)

        if self._text != '':
            # draw text
            font = pygame.font.SysFont("comicsansms", text_size)
            text = font.render(self._text, True, (0, 0, 0))
            screen.blit(text, (
            self._position_x + (self._width / 2 - text.get_width() / 2), self._position_y + (self._height / 2 - text.get_height() / 2)))

    def is_over(self, mouse_pos):
        # check if the mouse is over the button
        if self._position_x < mouse_pos[0] < self._position_x + self._width:
            if self._position_y < mouse_pos[1] < self._position_y + self._height:
                return True

        return False

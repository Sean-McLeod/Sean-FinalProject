#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the maps class

import pygame


class Maps:
    def __init__(self, sprite, tile_x_distance, tile_y_distance, screen, level):
        self._screen = screen
        self._sprite = sprite
        self._width = self._sprite.get_width()
        self._height = self._sprite.get_height()
        self.maps = []
        self.level = level
        self.tile_x_distance = tile_x_distance
        self.tile_y_distance = tile_y_distance
        self.angle = 90
        self.rotated_sprite = pygame.transform.rotate(self._sprite, self.angle)
        self.rotated_width = self.rotated_sprite.get_width()
        self.rotated_height = self.rotated_sprite.get_height()
        self.new_rect = self._sprite.get_rect()
        self.reduce_distance = self.tile_y_distance / 2
        self._game_scene_one_map = """





wwwwwwwwww  ww""".splitlines()

        self._game_scene_two_map = """ ff
 rr
 fwww w
 r     r
wwwwwww
     r 
 r   r 
 wwww ww

wwwww wwww
""".splitlines()
        self.maps.append(self._game_scene_one_map)
        self.maps.append(self._game_scene_two_map)

    def build_map(self, sprite2):
        for nth_line, line in enumerate(self.maps[self.level - 1]):
            for nth_character, character in enumerate(line):
                if character == "w":
                    self._screen.blit(self._sprite,
                                      (nth_character * self.tile_x_distance, nth_line * self.tile_y_distance))
                    self.new_rect = pygame.Rect(nth_character * self.tile_x_distance, nth_line * self.tile_y_distance,
                                                self._width, self._height)
                    # pygame.draw.rect(self._screen, (0, 0, 255), self.new_rect)
                    # check collision
                    if self.new_rect.colliderect(sprite2):
                        print("collided with map")
                elif character == "r":
                    self.rotated_rect = pygame.Rect(nth_character * self.tile_x_distance,
                                                    nth_line * self.tile_y_distance - self.reduce_distance,
                                                    self.rotated_width, self.rotated_height)
                    self._screen.blit(self.rotated_sprite, (
                    nth_character * self.tile_x_distance, nth_line * self.tile_y_distance - self.reduce_distance))
                    # check collision
                    if self.rotated_rect.colliderect(sprite2):
                        print("collided with map")

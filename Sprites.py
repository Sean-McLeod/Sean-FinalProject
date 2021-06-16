import pygame

class Sprites:
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        self._sprite = sprite
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._screen = screen
        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()
        self.moving_rect = pygame.Rect(self._sprite_x, self._sprite_y, self.width, self.height)
        self.current_sprite = 0

    def sprite_upload(self):
        self._screen.blit(self._sprite, (self.moving_rect.x, self.moving_rect.y))

    def flip_sprite(self):
        self._sprite = pygame.transform.flip(self._sprite, True, False)

    def sprite_move(self, x_change, y_change):
        self.moving_rect.x += x_change
        self.moving_rect.y += y_change

    def sprite_animation(self, sprite_list):
        self.current_sprite += 1
        # if self.current_sprite >= len(sprite_list):
        #     self.current_sprite = 0

    def get_x_speed(self):
        return self._x_speed

    def set_x_speed(self, new_x_speed):
        self._x_speed = new_x_speed

    def get_y_speed(self):
        return self._y_speed

    def set_y_speed(self, new_y_speed):
        self._y_speed = new_y_speed

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, new_sprite):
        self._sprite = new_sprite

    def print_anything(self):
        print("hey!")

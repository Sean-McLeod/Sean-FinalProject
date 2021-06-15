#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prison escape game

import sys

import pygame

from Bullets import Bullets
from Maps import Maps
from Monsters import Monsters
from PrisonerClass import PrisonerClass
from Sprites import Sprites


# def sprite_collision2(sprite1, sprite2):
#     # build rect
#     my_dragon.build_rect()
#     my_prisoner.build_rect()
#     # get rect
#     dragon_rect = my_dragon.get_rect()
#     prisoner_rect = my_prisoner.get_rect()
#     # check collision
#     my_prisoner.check_collision(prisoner_rect, dragon_rect)
#


# def create_map(screen, my_prisoner):
#     # tile = pygame.image.load("cell.png")
#     # create object
#     # my_cell_map = Monsters(tile, 24, 53, screen)
#
#     # this is the map
#     map1 = """
#
#
#
#
#
# wwwwwwwwwwwww""".splitlines()
#
#     for y, line in enumerate(map1):
#         for x, c in enumerate(line):
#             if c == "w":
#                 screen.blit(tile, (x * 60, y * 50))



    # cell_rect = my_cell_map.get_rect()
    # prisoner_rect = my_prisoner.get_rect()
    # # check collision
    # my_cell_map.check_collision(cell_rect, prisoner_rect)


def third_game_scene(screen):
    prisoner_x = 400
    prisoner_y = 500
    ship_x = 400
    ship_y = 100
    clock = pygame.time.Clock()
    now = pygame.time.get_ticks()


    print("THIRD!!")
    # create background
    background = pygame.image.load("Backgrounds/Game Scene 3.jpg")

    # create sprites
    prisoner = pygame.image.load("Sprites/prisoners/prisoner.png")
    ship = pygame.image.load("Sprites/ship.png")
    laser = pygame.transform.rotate(pygame.image.load("Sprites/laser.png"), 270)

    # create object
    my_prisoner = PrisonerClass(prisoner, prisoner_x, prisoner_y, screen)
    my_ship = Monsters(ship, ship_x, ship_y, screen)
    my_bullet = Monsters(laser, ship_x, ship_y, screen)

    # sprite group
    bullet_group = pygame.sprite.Group()


    running = True
    while running:
        KEYDOWN = False
        K_LEFT = False
        K_RIGHT = False
        K_UP = False
        K_DOWN = False
        KEYUP = False
        now+=3

        # upload image
        screen.blit(background, (0, 0))

        # get rect
        prisoner_rect = my_prisoner.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                KEYDOWN = True
                if event.key == pygame.K_LEFT:
                    K_LEFT = True
                if event.key == pygame.K_RIGHT:
                    K_RIGHT = True
                    # bullet_group.add(my_ship.create_bullet())
                if event.key == pygame.K_UP:
                    K_UP = True
                if event.key == pygame.K_DOWN:
                    K_DOWN = True
            if event.type == pygame.KEYUP:
                KEYUP = True

            if event.type == pygame.QUIT:
                # running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)

        my_prisoner.prisoner_move(20, 15, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYUP)

        my_prisoner.more()

        # flip prisoner
        my_prisoner.prisoner_flip()
        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.sprite_animation()
        my_prisoner.is_out_of_screen()
        # increase prisoner size
        my_prisoner.modify_sprite_size(2)

        # now = pygame.time.get_ticks()
        print(now)
        if now >= 10:
            now = 0
            bullet_group.add(my_ship.create_bullet())




        # move ship
        my_ship.ship_move()
        # shoot lasers
        bullet_group.draw(screen)
        bullet_group.update()

        # check collision

        # bullet_group







        # check collisions
        my_ship.attack(prisoner_rect)



        # upload sprites
        my_prisoner.sprite_upload()
        my_ship.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(10)



def second_game_scene(screen):
    prisoner_x = 700
    prisoner_y = 540
    clock = pygame.time.Clock()


    print("welcome!")
    # create background
    background = pygame.image.load("Backgrounds/Game Scene 2.png")

    # create sprites
    prisoner = pygame.image.load("Sprites/prisoners/prisoner.png")
    tile = pygame.image.load("Sprites/barbed-wire (3).png")
    door = pygame.image.load("Doors/castledoors.png")

    # create object
    my_prisoner = PrisonerClass(prisoner, prisoner_x, prisoner_y, screen)
    my_door = Sprites(door, 130, 0, screen)
    my_cell_map = Maps(tile, 100, 57, screen, 2)

    running = True
    while running:
        KEYDOWN = False
        K_LEFT = False
        K_RIGHT = False
        K_UP = False
        K_DOWN = False
        KEYUP = False

        # upload image
        screen.blit(background, (0, 0))

        # get rect
        prisoner_rect = my_prisoner.get_rect()
        door_rect = my_door.get_rect()

        # build map
        my_cell_map.build_map(prisoner_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                KEYDOWN = True
                if event.key == pygame.K_LEFT:
                    K_LEFT = True
                if event.key == pygame.K_RIGHT:
                    K_RIGHT = True
                if event.key == pygame.K_UP:
                    K_UP = True
                if event.key == pygame.K_DOWN:
                    K_DOWN = True
            if event.type == pygame.KEYUP:
                KEYUP = True

            if event.type == pygame.QUIT:
                # running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)

        my_prisoner.prisoner_move(20, 15, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYUP)

        my_prisoner.more()

        # flip prisoner
        my_prisoner.prisoner_flip()
        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.sprite_animation()
        my_prisoner.is_out_of_screen()
        # upload prisoner image
        my_prisoner.sprite_upload()

        # collision detection
        if my_door.check_collision(door_rect, prisoner_rect):
            running = False

        my_door.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(10)







def first_game_scene(screen):
    prisoner_x = 700
    prisoner_y = 450
    prisoner_x_change = 0
    prisoner_y_change = 0
    golem_x_change = 30
    golem_y_change = 0
    looking_right = False
    clock = pygame.time.Clock()
    is_animating = False

    # create background
    background = pygame.image.load("Backgrounds/Game Scene 1.png")

    # create sprites
    prisoner = pygame.image.load("Sprites/prisoners/prisoner.png")
    golem = pygame.image.load("Sprites/golems/golem-walk.png")
    dragon = pygame.image.load("Sprites/Dragon.png")
    tile = pygame.image.load("Sprites/cell.png")
    door = pygame.image.load("Doors/Door.png")

    # objects
    my_prisoner = PrisonerClass(prisoner, prisoner_x, prisoner_y, screen)
    my_golem = Monsters(golem, 100, 100, screen)
    my_golem_two = Monsters(golem, 800, 200, screen)
    my_dragon = Monsters(dragon, 50, 300, screen)
    my_cell_map = Maps(tile, 60, 50, screen, 1)
    my_door = Sprites(door, 213, 0, screen)

    my_dragon.modify_sprite_size(2)

    running = True
    while running:
        KEYDOWN = False
        K_LEFT = False
        K_RIGHT = False
        K_UP = False
        K_DOWN = False
        KEYUP = False

        # upload image
        screen.blit(background, (0, 0))

        # get rect
        # dragon_rect = my_dragon.get_rect()
        prisoner_rect = my_prisoner.get_rect()
        # golem_rect = my_golem.get_rect()
        # golem_rect_two = my_golem_two.get_rect()
        door_rect = my_door.get_rect()

        # check collision with prisoner
        my_cell_map.build_map(prisoner_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                KEYDOWN = True
                if event.key == pygame.K_LEFT:
                    K_LEFT = True
                if event.key == pygame.K_RIGHT:
                    K_RIGHT = True
                if event.key == pygame.K_UP:
                    K_UP = True
                if event.key == pygame.K_DOWN:
                    K_DOWN = True
            if event.type == pygame.KEYUP:
                KEYUP = True

            if event.type == pygame.QUIT:
                # running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)


        my_prisoner.prisoner_move(20, 20, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYUP)
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             is_animating = True
        #             looking_right = False
        #             prisoner_x_change = -20
        #         if event.key == pygame.K_RIGHT:
        #             is_animating = True
        #             looking_right = True
        #             prisoner_x_change = 20
        #         if event.key == pygame.K_UP:
        #             is_animating = True
        #             prisoner_y_change = -20
        #         if event.key == pygame.K_DOWN:
        #             is_animating = True
        #             prisoner_y_change = 20
        #     if event.type == pygame.KEYUP:
        #         is_animating = False
        #         prisoner_x_change = 0
        #         prisoner_y_change = 0
        #     if event.type == pygame.QUIT:
        #         running = False
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         mouse_position = pygame.mouse.get_pos()
        #         print(mouse_position)

        # golem stuff
        # my_golem.sprite_move(20, 0)
        # golem_x_change = my_golem.golem_move(golem_x_change, golem_y_change)
        # my_golem.sprite_upload()

        # if it is animating, use animated images. if not, use standard image
        my_prisoner.more()
        # move the sprite using the x and y change
        # my_prisoner.sprite_move(prisoner_x_change, prisoner_y_change)

        # change sprite size of prisoner
        my_prisoner.modify_sprite_size(2)
        # flip prisoner
        my_prisoner.prisoner_flip()
        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.sprite_animation()
        my_prisoner.is_out_of_screen()
        # upload prisoner image
        my_prisoner.sprite_upload()

        # move golem
        my_golem.golem_move()
        # upload golem
        my_golem.sprite_upload()
        # move golem
        my_golem_two.golem_move()
        # upload golem
        my_golem_two.sprite_upload()



        # check collision
        my_dragon.attack(prisoner_rect)
        my_golem.attack(prisoner_rect)
        my_golem_two.attack(prisoner_rect)
        if my_door.check_collision(door_rect, prisoner_rect):
            running = False


        # upload dragon
        my_dragon.sprite_upload()

        my_door.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(10)


def splash_screen(screen):
    # create background
    background = pygame.image.load("Backgrounds/Splash.jpg")

    # upload image
    screen.blit(background, (0, 0))

    # update splash screen once
    pygame.display.update()

    # wait 1000ms
    pygame.time.wait(1000)


def start_screen(screen):
    # constants
    rect_x_position = 100
    rect_y_position = 150
    text_size = 100

    # create background
    background = pygame.image.load("Backgrounds/StartScreen.jpg")

    # initialize color
    black = (0, 0, 0)
    white = (255, 255, 255)
    # initialize font
    font = pygame.font.Font(None, text_size)
    # this is the text
    text = font.render("START", False, black)

    # Game loop
    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))
        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        # create button(surface, color, position & dimensions)
        button = pygame.draw.rect(
            screen,
            white,
            [rect_x_position, rect_y_position, text_size * 2.5, text_size],
        )

        # upload text
        screen.blit(text, (rect_x_position + 20, rect_y_position + 20))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse presses button, move to game scene 1
                if button.collidepoint(mouse_position):
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        # refresh the screen every frame
        pygame.display.update()


def main():
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # splash_screen(screen)
    # start_screen(screen)
    # first_game_scene(screen)
    # second_game_scene(screen)
    third_game_scene(screen)


if __name__ == "__main__":
    main()


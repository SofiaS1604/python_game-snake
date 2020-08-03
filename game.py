import pygame
import random

from pygame import *

pygame.init()  # start pygame
screen = pygame.display.set_mode((800, 600))  # (width window, height window)
pygame.display.set_caption('Game Snake')  # title window

# color
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10  # size snake
snake_speed = 15  # speed

score_font = pygame.font.SysFont("Monaco", 35)
clock = pygame.time.Clock()


def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [10, 10])  # output window


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])  # draw snake


def gameLoop():
    game_over = False

    x1 = 400
    y1 = 300

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, 800 - snake_block) / 10) * 10
    food_y = round(random.randrange(0, 600 - snake_block) / 10) * 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(blue)
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        our_snake(snake_block, snake_list)  # draw snake
        your_score(snake_length - 1)  # draw score

        pygame.display.update()

        if x1 == food_x and y1 == food_y:  # collision
            food_x = round(random.randrange(0, 800 - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, 600 - snake_block) / 10.0) * 10
            snake_length += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()

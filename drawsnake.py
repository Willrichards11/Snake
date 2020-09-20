import pygame


def drawsnake(window, snake):
    for i, j in zip(snake.x, snake.y):
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (i, j, snake.width, snake.height)
        )

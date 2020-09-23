import pygame


def drawsnake(window, snake):
    for i, j in zip(snake.x, snake.y):
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (i, j, snake.width, snake.height)
        )


def drawFood(food, window):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (food.x, food.y, food.width, food.height)
    )


def overscreen(window):
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = window.get_width() / 2 - text_rect.width / 2
    text_y = window.get_height() / 2 - text_rect.height / 2
    window.blit(text, [text_x, text_y])
    pygame.display.flip()
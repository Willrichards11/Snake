import pygame
from components.snake import Snake
from components.food import Food
from collide import collision
from drawsnake import drawsnake
import time


def main():

    pygame.init()

    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Snake")

    snake = Snake()
    food = Food()
    game = True

    while game is True:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        strokes = pygame.key.get_pressed()

        snake.setdir(strokes)
        window.fill((0, 0, 0))
        snake.move()

        drawsnake(window, snake)

        if snake.checkEdges():
            game = False

        if (collision(snake, food)):
            food = Food()
            snake.grow()


        pygame.draw.rect(
            window,
            (0, 0, 255),
            (food.x, food.y, food.width, food.height)
        )

        pygame.display.update()

    window.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = window.get_width() / 2 - text_rect.width / 2
    text_y = window.get_height() / 2 - text_rect.height / 2
    window.blit(text, [text_x, text_y])
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()


if __name__ == "__main__":
    main()
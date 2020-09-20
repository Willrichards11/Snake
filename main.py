import pygame
from components.snake import Snake
from components.food import Food
from collide import collision
from drawsnake import drawsnake


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

        snake.move(strokes)
        window.fill((0, 0, 0))

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


    pygame.quit()

if __name__ == "__main__":
    main()
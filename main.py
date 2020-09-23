import pygame
from components.snake import Snake
from components.food import Food
from collide import collision
from draw import drawsnake, drawFood, overscreen
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

        if collision(snake, food):
            food.newloc(snake)
            snake.grow()

        drawFood(food, window)
        pygame.display.update()

    window.fill((0, 0, 0))

    overscreen(window)
    time.sleep(5)
    pygame.quit()


if __name__ == "__main__":
    main()
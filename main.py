import pygame
from components.snake import Snake
from components.food import Food
from collide import collision
from draw import drawsnake, drawFood, overscreen
import time


def main():
    pygame.init()
    score = 0

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
        # if collides with self or edge end game
        if snake.checkEdges() or snake.checkSelf():
            game = False

        if collision(snake, food):
            food.newloc(snake)
            snake.grow()
            score += 1

        drawFood(food, window)
        pygame.display.update()

    window.fill((0, 0, 0))

    overscreen(window, score)
    time.sleep(5)
    pygame.quit()


if __name__ == "__main__":
    main()
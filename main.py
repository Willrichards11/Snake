import pygame
from components.snake import Snake
from components.food import Food
from collide import collision
from draw import drawsnake, drawFood, overScreen, startScreen
import time


def main():
    while True:
        pygame.init()
        score = 0

        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Snake")

        snake = Snake()
        food = Food()
        game = True
        start = False

        while start is False:
            startScreen(window)
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = True
                        window.fill((0, 0, 0))

        while game is True:

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
            pygame.time.delay(100)

        window.fill((0, 0, 0))

        overScreen(window, score)
        time.sleep(5)
        
    pygame.quit()


if __name__ == "__main__":
    main()
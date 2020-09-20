import pygame
from components.snake import Snake


def main():

    pygame.init()

    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Snake")

    snake = Snake()
    game = True

    while game is True:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        window.fill((0, 0, 0))
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (snake.x, snake.y, snake.width, snake.height)
        )
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
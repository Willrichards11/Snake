def collision(snake, food):
    return (snake.x[0] - food.x)**2 +  (snake.y[0] - food.y)**2 <=15**2


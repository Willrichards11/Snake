def collision(snake, food):
    # record collision if within 5 units
    return (abs(snake.x[0] - food.x < 5)) and (abs(snake.y[0] - food.y) < 5)

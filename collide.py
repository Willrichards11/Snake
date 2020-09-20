def collision(snake, food):
    return (abs(snake.x - food.x < 5)) and (abs(snake.y - food.y) < 5)

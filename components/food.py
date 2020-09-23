import pygame
import numpy


class Food:
    def __init__(self):
        self.x = numpy.random.randint(10, 490)
        self.y = numpy.random.randint(10, 490)
        self.width = 15
        self.height = 15

    def newloc(self, snake):
        cont = True
        while cont is True:

            self.x = numpy.random.randint(10, 490)
            self.y = numpy.random.randint(10, 490)

            min_dist_x = min([self.x - val for val in snake.x])
            min_dist_y = min([self.y - val for val in snake.y])

            if min_dist_x**2 + min_dist_y**2 > 15**2:
                cont = False

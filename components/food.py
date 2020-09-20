import pygame
import numpy


class Food:
    def __init__(self):
        self.x = numpy.random.randint(10, 490)
        self.y = numpy.random.randint(10, 490)
        self.width = 5
        self.height = 5

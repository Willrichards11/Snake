import pygame


class Snake:
    def __init__(self, x=250, y=250):
        self.width = 5
        self.height = 5
        self.x = x
        self.y = y
        self.vel = 5

    def move(self, strokes):
        if strokes[pygame.K_LEFT]:
            self.x -= self.vel

        if strokes[pygame.K_RIGHT]:
            self.x += self.vel

        if strokes[pygame.K_UP]:
            self.y -= self.vel

        if strokes[pygame.K_DOWN]:
            self.y += self.vel


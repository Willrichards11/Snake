import pygame


class Snake:
    def __init__(self, x=[250], y=[250]):
        self.width = 5
        self.height = 5
        self.x = x
        self.y = y
        self.vel = 5
        self.lastmove = "u"

    def setdir(self, strokes):
        if strokes[pygame.K_LEFT]:
            self.lastmove = "l"

        if strokes[pygame.K_RIGHT]:
            self.lastmove = "r"

        if strokes[pygame.K_UP]:
            self.lastmove = "u"

        if strokes[pygame.K_DOWN]:
            self.lastmove = "d"

    def move(self):
        if self.lastmove == "l":
            self.x = [pos - self.vel for pos in self.x]

        if self.lastmove == "r":
            self.x = [pos + self.vel for pos in self.x]

        if self.lastmove == "u":
            self.y = [pos - self.vel for pos in self.y]

        if self.lastmove == "d":
            self.y = [pos + self.vel for pos in self.y]


    def checkEdges(self):
        hrztls = (self.x[0] > 500) or (self.x[0] < 0)
        verts = (self.y[0] > 500) or (self.y[0] < 0)
        return hrztls or verts


    def grow(self):
        self.x.append(self.x[-1] - 5)
        self.y.append(self.y[-1] - 5)

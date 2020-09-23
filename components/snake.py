import pygame


class Snake:
    def __init__(self, x=[250, 250, 250], y=[250, 265, 280], lastmove="u"):
        self.width = 15
        self.height = 15
        self.x = x
        self.y = y
        self.vel = 1
        self.lastmove = lastmove

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
            head_x = [self.x[0] - self.vel*15]
            body_x = self.x[:-1]
            head_y = [self.y[0]]
            body_y = self.y[:-1]

        if self.lastmove == "r":
            head_x = [self.x[0] + self.vel*15]
            body_x = self.x[:-1]
            head_y = [self.y[0]]
            body_y = self.y[:-1]

        if self.lastmove == "u":
            head_x = [self.x[0]]
            body_x = self.x[:-1]
            head_y = [self.y[0] - self.vel*15]
            body_y = self.y[:-1]

        if self.lastmove == "d":
            head_x = [self.x[0]]
            body_x = self.x[:-1]
            head_y = [self.y[0] + self.vel*15]
            body_y = self.y[:-1]

        self.x = head_x + body_x
        self.y = head_y + body_y

    def checkEdges(self):
        hrztls = (self.x[0] > 492.5) or (self.x[0] < 7.5)
        verts = (self.y[0] > 492.5) or (self.y[0] < 7.5)
        return hrztls or verts

    def checkSelf(self):
        return (self.x[0], self.y[0]) in zip(self.x[1:], self.y[1:])

    def grow(self):
        self.x.append(self.x[-1] - 15)
        self.y.append(self.y[-1] - 15)

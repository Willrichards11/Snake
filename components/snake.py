import pygame


class Snake:
    def __init__(self, x=[250, 250, 250], y=[250, 265, 280], lastmove="u"):
        self.width = 15
        self.height = 15
        self.x = x
        self.y = y
        self.vel = 15
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
            head_x = [self.x[0] - self.vel]
            body_x = self.x[:-1]
            head_y = [self.y[0]]
            body_y = self.y[:-1]

        if self.lastmove == "r":
            head_x = [self.x[0] + self.vel]
            body_x = self.x[:-1]
            head_y = [self.y[0]]
            body_y = self.y[:-1]

        if self.lastmove == "u":
            head_x = [self.x[0]]
            body_x = self.x[:-1]
            head_y = [self.y[0] - self.vel]
            body_y = self.y[:-1]

        if self.lastmove == "d":
            head_x = [self.x[0]]
            body_x = self.x[:-1]
            head_y = [self.y[0] + self.vel]
            body_y = self.y[:-1]

        self.x = head_x + body_x
        self.y = head_y + body_y

    def checkEdges(self):
        hrztls = (self.x[0] > 500) or (self.x[0] < 0)
        verts = (self.y[0] > 500) or (self.y[0] < 0)
        return hrztls or verts

    def checkSelf(self):
        min_dist_x = min([self.x[0] - val for val in self.x[1:]])
        min_dist_y = min([self.y[0] - val for val in self.y[1:]])
        return min_dist_x ** 2 + min_dist_y ** 2 < 15**2

    def grow(self):
        self.x.append(self.x[-1] - 5)
        self.y.append(self.y[-1] - 5)

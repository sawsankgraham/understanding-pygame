import pygame as pg
import random
import vars

class Obstacle:
    def __init__(self):
        self.score = 0
        self.rects = [pg.rect.Rect((i * 200) + 400, random.randint(vars.HEIGHT - 15, vars.HEIGHT - 5), vars.OBSTACLE_WIDTH, vars.OBSTACLE_HEIGHT) for i in range(4)]

    def draw(self, screen):
        for rect in self.rects:
            pg.draw.rect(screen, (255, 0, 0), rect )
        self.move()
        self.loop_around()

    def move(self):
        for rect in self.rects:
            rect.move_ip(-5, 0)

    def loop_around(self):
        for rect in self.rects:
            if rect.centerx < -10:
                self.score += 1
                rect.centerx =  vars.WIDTH + random.randint(100, 200)
                rect.centery = random.randint(vars.HEIGHT - 15, vars.HEIGHT - 5)
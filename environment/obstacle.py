from shutil import move
import pygame as pg
import random
import vars

class Obstacle:
    def __init__(self):
        self.rects = [pg.rect.Rect(i * random.randint(20, 100), random.randint(vars.HEIGHT - 100, vars.HEIGHT - 10), vars.OBSTACLE_WIDTH, vars.OBSTACLE_HEIGHT) for i in range(10)]

    def draw(self, screen):
        for rect in self.rects:
            pg.draw.rect(screen, (255, 0, 0), rect )
        self.move()

    def move(self):
        for rect in self.rects:
            rect.move_ip(-1, 0)
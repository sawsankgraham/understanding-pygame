import sys
import vars
import pygame as pg

pg.init()
screen = pg.display.set_mode(vars.SIZE)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        screen.fill((0, 0, 0))
        pg.display.flip()

if __name__:
    main()
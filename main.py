import sys
import vars
import pygame as pg
from environment import player, obstacle

pg.init()
pg.display.set_caption("Understanding PyGame")
screen = pg.display.set_mode(vars.SIZE)
clock = pg.time.Clock()

player = player.Player()
obstacle = obstacle.Obstacle()

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        screen.fill(vars.BACKGROUND)
        obstacle.draw(screen)
        player.draw(screen)
        player.handle_movement() 
        # if ( player.is_crash(obstacle.rects)):
        #     sys.exit()
        clock.tick(vars.FPS)
        pg.display.flip()

if __name__:
    main()
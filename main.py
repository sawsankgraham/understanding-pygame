import sys
import vars
import pygame as pg
from environment import player, obstacle

pg.init()
pg.display.set_caption("Understanding PyGame")
screen = pg.display.set_mode(vars.SIZE)
clock = pg.time.Clock()
pg.font.init()

player = player.Player()
obstacle = obstacle.Obstacle()
font = pg.font.SysFont('Comic Sans MS', 30)


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        screen.fill(vars.BACKGROUND)
        obstacle.draw(screen)
        player.draw(screen)
        player.handle_movement() 
        scoresurface = font.render(str(obstacle.score), False, (0, 255, 0))
        screen.blit(scoresurface, (0,0))
        if ( player.is_crash(obstacle.rects)):
            print("Final Score: " + obstacle.score)
            sys.exit()
        clock.tick(vars.FPS)
        pg.display.flip()

if __name__:
    main()
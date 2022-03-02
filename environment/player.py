import pygame as pg
import vars

class Player:
    def __init__(self):
        self.jumping = False
        self.jump_frame = 10
        self.y = 40
        self.rect = pg.rect.Rect(200, self.y, vars.PLAYER_WIDTH, vars.PLAYER_HEIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, vars.PLAYER_COLOR, self.rect )
        print(self.rect.y)
        if  self.rect.y < (vars.HEIGHT - vars.PLAYER_HEIGHT):
            self.rect.move_ip(0, 9.8)
        if self.jumping:
            self.jump()

    def is_crash(self, rect):
        result = self.rect.collidelistall(rect)
        return result

    def handle_movement(self):
        key = pg.key.get_pressed()
        if (key[pg.K_SPACE]):
            if not(self.jumping): self.jumping = True  
    
    def jump(self):
        if self.jumping:
            if self.jump_frame > 0:
                self.jump_frame -= 1
                self.rect.move_ip(0, -14)
 
            else:
                self.jumping = False
                self.jump_frame = 10
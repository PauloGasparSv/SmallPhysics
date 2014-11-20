import pygame as pg;import sys;import time
from pygame.locals import *;from const import *;from manager import *

pg.mixer.pre_init(44100,-16,2,2048)
pg.init()

display = pg.display.set_mode(SIZE_0)
pg.display.set_caption('Game')

mainClock = pg.time.Clock()

def main():
    RUNNING = True
    gameManager = GameManager()

    while(RUNNING):
        for ev in pg.event.get():
            if(ev.type == QUIT):
                RUNNING = False
        key = pg.key.get_pressed()
        if(key[pg.K_ESCAPE]):
            RUNNING=False
        #UPDATE
        gameManager.Update(key)

        #DRAW
        gameManager.Draw(display)

        pg.display.update()
        mainClock.tick(FPS)





    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()
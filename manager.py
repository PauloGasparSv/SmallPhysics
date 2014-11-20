import pygame as pg
from pygame.locals import *
from const import *
from box import *
from lineCol import *
#from Cannon2 import *
from Cannon2 import *

class GameManager:
    def __init__(self):
        self.image_original = pg.image.load('Assets/Objects/box.png').convert_alpha()
        self.surface = pg.Surface((1024,768)).convert_alpha()
        self.box = Box([30,30],self.image_original)
        self.box2 = Box([240,300],self.image_original)
        self.velx=5
        self.vely = 0
        self.canhao =Cannon(1)

    def Update(self,key):
        #self.box.pos[0]+=self.velx
        #self.box.pos[1]+=self.vely
        #self.velx-=0.06
        self.vely+=0.1
        self.box.Rotate(0.5)
        if(self.velx<0):
           self.velx=0

        if(self.box.hitTest(self.box2)):
            self.box.color = (255,0,0)
            self.box2.color = (255,0,0)
            #self.velx-=0.1
           # self.vely-=4
           # self.box.pos[1]-=5
        else:
            self.box.color = (255,255,255)
            self.box2.color = (255,255,255)


        ####################################

        self.canhao.update()
        if(self.canhao.projectiles.__len__()==1):
            if(self.box.hitTest(self.canhao.projectiles[0])):
                self.canhao.projectiles[0].vx=-self.canhao.projectiles[0].vx
                self.canhao.projectiles[0].vy=-self.canhao.projectiles[0].vy
                self.canhao.projectiles[0].pos+=[self.canhao.projectiles[0].vx+3,self.canhao.projectiles[0].vy-3]
                self.canhao.projectiles[0].Rotate(1)
                self.box.Rotate(-1)

        self.box2.Update(-1)
        self.box.Update(key)

    def Draw(self,display):
        self.surface.fill((255,255,255))
        self.box2.Draw(self.surface,self.image_original)
        self.box.Draw(self.surface,self.image_original)
        self.canhao.draw(self.surface)

        display.blit(self.surface,(0,0))

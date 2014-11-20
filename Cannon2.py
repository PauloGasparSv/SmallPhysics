import pygame as pg
from pygame.locals import *
from const import *
from box import Box
import math

#This is an actual cannon that shoots rigid stuff
#Is more of a slingshot

class Cannon:
    def __init__(self,max):
        self.position = [0,0]
        self.initPos = [0,0]

        self.max = max

        self.image_original = pg.image.load('Assets/Objects/box.png').convert_alpha()

        self.shoot = False
        self.projectiles =[]

        self.line = []

        self.angle = 0
        self.deltax=0
        self.deltay=0
    def update(self):
        self.position = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]]

        if(pg.mouse.get_pressed()[0] and self.shoot==False and self.projectiles.__len__()<self.max):
            self.shoot = True
            self.initPos = self.position

        if(self.shoot):
            #SLING SHOT
            self.line = [self.initPos,self.position]


            self.deltaY = self.initPos[1]-self.position[1]
            self.deltaX = self.initPos[0]-self.position[0]

            print('Y: '+str(self.deltaY)+' X: '+str(self.deltaX))
            self.angle = math.atan2(self.deltaY,self.deltaX)
            #END SLING
            if(pg.mouse.get_pressed()[0]==False):
                self.shoot=False

                magnitude = math.sqrt((self.position[0]-self.initPos[0])*(self.position[0]-self.initPos[0]) +
                                      (self.position[1]-self.initPos[1])*(self.position[1]-self.initPos[1]))

                self.projectiles.append(Box(self.position,self.image_original,self.angle,magnitude/25))


        for projectile in self.projectiles:
            projectile.Update(-1)
            if(projectile.destroy):
                self.projectiles.remove(projectile)


    def draw(self,display):
        for projectile in self.projectiles:
            projectile.Draw(display,self.image_original)
        if(self.shoot):
            pg.draw.lines(display, RED, False,self.line,2)



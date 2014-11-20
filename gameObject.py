import pygame as pg
from const import *
import math
#This file would be home of the GameObject class
#So i made a cannon that shoot not rigid bodies

class Cannon:
    def __init__(self,max):
        self.position = [0,0]
        self.initPos = [0,0]

        self.max = max

        self.fonte = pg.font.Font('Assets/fonte.ttf',30)
        self.cannonBall_image = pg.image.load('Assets/Objects/box.png')
        self.shoot = False
        self.projectiles =[]

        self.pontuacao = 0

        self.line = []

        self.counter= 0

        self.angle = 0
        self.deltax=0
        self.deltay=0
    def update(self):

        #print(math.degrees(math.asin(0.5)))

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

                self.projectiles.append(Projectile(self.position,self.angle,magnitude/25,self.cannonBall_image.get_rect().width,self.cannonBall_image.get_rect().height))


        for projectile in self.projectiles:
            projectile.update()
            if(projectile.ponto):
                self.pontuacao+=1
            if(projectile.destroy):
                self.projectiles.remove(projectile)

        if(self.projectiles.__len__()==0):
            self.pontuacao = 0
            self.counter=0
        else:
            self.counter+=1
            if(self.counter>300):
                self.pontuacao+=self.projectiles.__len__()
                self.counter=0


    def draw(self,display):
        display.blit(Text('Points: '+str(self.pontuacao),self.fonte,RED),(500,30))
        for projectile in self.projectiles:
            projectile.draw(display,self.cannonBall_image)
        if(self.shoot):
            pg.draw.lines(display, RED, False,self.line,2)
            display.blit(Text('angle: '+str(self.angle),self.fonte,RED),(30,30))
            display.blit(Text('DeltaX: '+str(self.deltaX),self.fonte,RED),(30,60))
            display.blit(Text('DeltaY: '+str(self.deltaY),self.fonte,RED),(30,90))


class Projectile:
    def __init__(self,position,angle,strenght,w,h):
        self.position = position
        self.w=w
        self.h=h
        self.vy = math.sin(angle)*strenght*1.8
        self.vx=math.cos(angle)*strenght*1.5
        self.destroy = False
        self.gravity = 0.3
        self.ponto = False
        #should be around 0.15 if realistic
    def update(self):
        self.ponto = False
        self.vy+=self.gravity
        self.position[0]+=self.vx
        self.position[1]+=self.vy
        if(self.position[1]>700):
            self.destroy = True
        if(self.position[0]>=740 or self.position[0]<=0):
            self.vx=-self.vx/2
        if(self.hitTest(pg.Rect(self.position[0],self.position[1],60,60),
                   pg.Rect(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],2,2))and self.vy>0):
            self.vy-=15
            self.vx+=(self.position[0]+30-pg.mouse.get_pos()[0])/10
            self.position[1]-=10
            self.ponto=True


    def draw(self,display,image):
        display.blit(image,self.position)

    def hitTest(self,rect1,rect2):
        return rect1.colliderect(rect2)
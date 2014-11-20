import pygame as pg
from pygame.locals import *
from const import *
import math
UL = 0
UR = 1
DL = 2
DR = 3
class Box:
    def __init__(self,pos,imagem,angle=None,magnitude=None):
        self.destroy=False
        self.angle = angle
        self.magnitude=magnitude
        if(angle!=None and magnitude!= None):
            self.vy = math.sin(angle)*magnitude*1.8
            self.vx=math.cos(angle)*magnitude*1.5
        else:
            self.vy=0
            self.vx=0
        self.magnitude =magnitude
        self.rotation = 0.0001
        self.image_rotation=-0.0001
        self.pos = pos
        self.w = imagem.get_rect().width
        self.h = imagem.get_rect().height
        self.diagonal = math.sqrt(self.w*self.w+self.h*self.h)/2
        self.bound = {}
        self.tempo = 0
        self.color = (255,255,255)
        self.CalculateBounds()


    def Update(self,key):
        if(self.angle!=None and self.magnitude!=None):
            self.vy+=0.3
            self.pos[0]+=self.vx
            self.pos[1]+=self.vy
            if(self.pos[1]>700):
                self.destroy = True
            if(self.pos[0]>=740 or self.pos[0]<=0):
                self.vx=-self.vx/2

        if(self.rotation==0):
            self.rotation+=0.0001
            self.image_rotation-=0.0001
        if(key!=-1):self.Input(key)
        self.CalculateBounds()
        self.hitTest(self)

    #Little Input class to separate stuff
    def Input(self,key):
        if(key[pg.K_LEFT]):
            self.image_rotation+=10
            self.rotation-=10
        if(key[pg.K_RIGHT]):
            self.image_rotation-=10
            self.rotation+=10
        if(key[pg.K_d]):
            self.pos[0]+=5
        elif(key[pg.K_a]):
            self.pos[0]-=5
        if(key[pg.K_w]):
            self.pos[1]-=5
        elif(key[pg.K_s]):
            self.pos[1]+=5

    #Calculating collision beetween two box classes
    #I was intending to make the Box class a child of a GameObject class
    #And make any other rigid body a child of GameObject, so that the hitTest function
    #would be global, but i did this in two nights and... yeah
    def hitTest(self,box):
        myL1 = [self.bound[UL],self.bound[UR]];myL2 = [self.bound[UR],self.bound[DR]]
        myL3 = [self.bound[DR],self.bound[DL]];myL4 = [self.bound[UL],self.bound[DL]]
        hisL1 = [box.bound[UL],box.bound[UR]];hisL2 = [box.bound[UR],box.bound[DR]]
        hisL3 = [box.bound[DR],box.bound[DL]];hisL4 = [box.bound[DR],box.bound[UL]]

        if(self.isIntersecting(myL1[0],myL1[1],hisL1[0],hisL1[1])or self.isIntersecting(myL1[0],myL1[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL1[0],myL1[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL1[0],myL1[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL2[0],myL2[1],hisL1[0],hisL1[1])or self.isIntersecting(myL2[0],myL2[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL2[0],myL2[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL2[0],myL2[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL3[0],myL3[1],hisL1[0],hisL1[1])or self.isIntersecting(myL3[0],myL3[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL3[0],myL3[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL3[0],myL3[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL4[0],myL4[1],hisL1[0],hisL1[1])or self.isIntersecting(myL4[0],myL4[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL4[0],myL4[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL4[0],myL4[1],hisL4[0],hisL4[1])):
            return True

    #So heres another hitTest class that can be used in any other body
    def hitTest2(self,UL,UR,DL,DR):
        myL1 = [self.bound[UL],self.bound[UR]];myL2 = [self.bound[UR],self.bound[DR]]
        myL3 = [self.bound[DR],self.bound[DL]];myL4 = [self.bound[UL],self.bound[DL]]
        hisL1 = [UL,UR];hisL2 = [UR,DR]
        hisL3 = [DR,DL];hisL4 = [DR,UL]

        if(self.isIntersecting(myL1[0],myL1[1],hisL1[0],hisL1[1])or self.isIntersecting(myL1[0],myL1[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL1[0],myL1[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL1[0],myL1[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL2[0],myL2[1],hisL1[0],hisL1[1])or self.isIntersecting(myL2[0],myL2[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL2[0],myL2[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL2[0],myL2[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL3[0],myL3[1],hisL1[0],hisL1[1])or self.isIntersecting(myL3[0],myL3[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL3[0],myL3[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL3[0],myL3[1],hisL4[0],hisL4[1])
        or self.isIntersecting(myL4[0],myL4[1],hisL1[0],hisL1[1])or self.isIntersecting(myL4[0],myL4[1],hisL2[0],hisL2[1])
        or self.isIntersecting(myL4[0],myL4[1],hisL3[0],hisL3[1]) or self.isIntersecting(myL4[0],myL4[1],hisL4[0],hisL4[1])):
            return True

    #Function that calculate the 4 points of the body
    def CalculateBounds(self):
        self.bound[UL] =[self.pos[0]+math.floor(math.cos(math.radians(self.rotation+225))*self.diagonal),self.pos[1]+math.floor(math.sin(math.radians(self.rotation+225))*self.diagonal)]
        self.bound[UR] =[self.pos[0]+math.floor(math.cos(math.radians(self.rotation+315))*self.diagonal),self.pos[1]+math.floor(math.sin(math.radians(self.rotation+315))*self.diagonal)]
        self.bound[DR] =[self.pos[0]+math.floor(math.cos(math.radians(self.rotation+45))*self.diagonal),self.pos[1]+math.floor(math.sin(math.radians(self.rotation+45))*self.diagonal)]
        self.bound[DL] =[self.pos[0]+math.floor(math.cos(math.radians(self.rotation+135))*self.diagonal),self.pos[1]+math.floor(math.sin(math.radians(self.rotation+135))*self.diagonal)]

    def Draw(self,display,imagem):
        temp_image = self.MathRotate(imagem,self.image_rotation)
        center_offset = [temp_image.get_rect().center[0]-imagem.get_rect().center[0],temp_image.get_rect().center[1]-imagem.get_rect().center[1]]
        temp_pos = (self.pos[0]-center_offset[0],self.pos[1]-center_offset[1])
        display.blit(temp_image,[temp_pos[0]-self.w/2,temp_pos[1]-self.h/2])

        pg.draw.rect(display,self.color,(self.pos[0]-5,self.pos[1]-5,10,10),0)
        pg.draw.rect(display,(255,0,0),(self.bound[UL][0],self.bound[UL][1],5,5),0)
        pg.draw.rect(display,(255,0,0),(self.bound[UR][0],self.bound[UR][1],5,5),0)
        pg.draw.rect(display,(255,0,0),(self.bound[DL][0],self.bound[DL][1],5,5),0)
        pg.draw.rect(display,(255,0,0),(self.bound[DR][0],self.bound[DR][1],5,5),0)

    #Line collision method
    def isIntersecting(self,a,b,c,d):
        denominator = ((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0]))
        numerator1 = ( (a[1] - c[1]) * (d[0] - c[0])) - ((a[0] - c[0]) * (d[1] - c[1]))
        numerator2 = ((a[1] - c[1]) * (b[0] - a[0])) - ((a[0] - c[0]) * (b[1] - a[1]))

        if (denominator == 0):
            return numerator1 == 0 and numerator2 == 0

        r = numerator1 / denominator
        s = numerator2 / denominator

        return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)

    #Image rotating method
    def MathRotate(self,image, angle):
        loc = image.get_rect().center
        rot_sprite = pg.transform.rotate(image, angle)
        rot_sprite.get_rect().center =loc
        return rot_sprite.convert_alpha()

    #Actual rotating
    def Rotate(self,value):
        self.rotation+=value
        self.image_rotation-=value
import pygame as pg
from pygame.locals import *
from const import *

#A class for checking collision beetween two lines
#Shown with graphics and stuff

class LineCol:
    def __init__(self):
        self.isL1 = False
        self.isL2 = False
        self.creatingL1 = False
        self.creatingL2 = False
        self.line1 = [[],[]]
        self.line2 = [[],[]]
        self.color = (0,0,0)
    def update(self):
        if(pg.mouse.get_pressed()[2]):
            self.isL1 = False
            self.isL2 = False
            self.creatingL1 = False
            self.creatingL2 = False
            self.line1 = [[],[]]
            self.line2 = [[],[]]
            self.color = (0,0,0)
        if(self.creatingL1==False and pg.mouse.get_pressed()[0]and self.isL1 == False):
            self.line1[0] = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]]
            self.creatingL1 = True

        if(self.creatingL1 and self.isL1==False):
            self.line1[1]=[pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]]
            if(pg.mouse.get_pressed()[0]==False):
                self.isL1 = True

        if(self.creatingL2==False and pg.mouse.get_pressed()[0]and self.isL2 == False and self.isL1):
            self.line2[0] = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]]
            self.creatingL2 = True

        if(self.creatingL2 and self.isL2==False):
            self.line2[1]=[pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]]
            if(self.IsIntersecting(self.line1[1],self.line1[0],self.line2[1],self.line2[0])
            and self.IsIntersecting(self.line1[0],self.line1[1],self.line2[1],self.line2[0])):
                print(self.line2[0])
                self.color = (255,0,0)
            else:
                self.color = (0,0,0)
            if(pg.mouse.get_pressed()[0]==False):
                self.isL2 = True

    def draw(self,display):
        if(self.creatingL1 or self.isL1):
            pg.draw.lines(display,self.color, False,self.line1,2)
        if(self.creatingL2 or self.isL2):
            pg.draw.lines(display,self.color, False,self.line2,2)


    def IsIntersecting(self,a,b,c,d):

        denominator = ((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0]))
        numerator1 = ( (a[1] - c[1]) * (d[0] - c[0])) - ((a[0] - c[0]) * (d[1] - c[1]))
        numerator2 = ((a[1] - c[1]) * (b[0] - a[0])) - ((a[0] - c[0]) * (b[1] - a[1]))

        if (denominator == 0):
            return numerator1 == 0 and numerator2 == 0

        r = numerator1 / denominator
        s = numerator2 / denominator

        return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)
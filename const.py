import pygame as pg

#VARIABLES
FPS = 60
SIZE_0 = (800,600)
RESOLUTION = (1024,768)
RED = [255,0,0]

#METHODS
def Text(text,font,color):
    return font.render(text,True,color)
def getSubImage(sheet,x,y,w,h):
    sheet.set_clip(pg.Rect(x,y,w,h))
    return sheet.subsurface(sheet.get_clip())
def getWidth(image):
    return image.get_size()[0]
def getHeight(image):
    return image.get_size()[1]
def Scale(image,w,h):
    return pg.transform.scale(image,(w,h))







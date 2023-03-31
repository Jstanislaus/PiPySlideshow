import pygame
from PIL import Image, ImageDraw
import os.path
import random
path = "/home/pi64/PiPySlideshow"
def show_image(image_path):	
    screen.fill(pygame.Color("white")) # clear the screen	
    img = pygame.image.load(image_path) # load the image
    img = img.convert()	
    infoObject = pygame.display.Info()
    set_demensions(img.get_width(), img.get_height()) # set pixel dimensions based on image	
    x = (infoObject.current_w / 2) - (img.get_width() / 2)
    y = (infoObject.current_h / 2) - (img.get_height() / 2)
    screen.blit(img,(x,y))
    pygame.display.flip()
piclist =[]
def updatepics(path,piclist):
    dir_list = os.listdir(path)
    for i in range(0,len(dir_list)):
        if dir_list[i] not in piclist:
            piclist.append(dir_list[i])
    return piclist
i=0
##SHow the 5 most recent pics first
piclist = updatepics(path,piclist)
random.shuffle(piclist)
while True:
    show_image(path+"/"+str(countarray[i]))
    if i %15 ==14:
        piclist = updatepics(path,piclist)
        random.shuffle(piclist)
    i+=1


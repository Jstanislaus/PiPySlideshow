import pygame
from PIL import Image, ImageDraw
import PIL.Image
import os.path
import random
import time
pygame.init()
path = "/home/pi64/PiPySlideshow"
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w,infoObject.current_h), pygame.FULLSCREEN)  # Full screen 
def set_demensions(img_w, img_h):
    # Note this only works when in booting in desktop mode. 
	# When running in terminal, the size is not correct (it displays small). Why?

    # connect to global vars
    global transform_y, transform_x, offset_y, offset_x

    # based on output screen resolution, calculate how to display
    ratio_h = (infoObject.current_w * img_h) / img_w 

    if (ratio_h < infoObject.current_h):
        #Use horizontal black bars
        #print "horizontal black bars"
        transform_y = ratio_h
        transform_x = infoObject.current_w
        offset_y = (infoObject.current_h - ratio_h) / 2
        offset_x = 0
    elif (ratio_h > infoObject.current_h):
        #Use vertical black bars
        #print "vertical black bars"
        transform_x = (infoObject.current_h * img_w) / img_h
        transform_y = infoObject.current_h
        offset_x = (infoObject.current_w - transform_x) / 2
        offset_y = 0
    else:
        #No need for black bars as photo ratio equals screen ratio
        #print "no black bars"
        transform_x = infoObject.current_w
        transform_y = infoObject.current_h
        offset_y = offset_x = 0
def show_image(image_path):	
    screen.fill(pygame.Color("black")) # clear the screen	
    img = pygame.image.load(image_path) # load the image
    img = img.convert()	
    set_demensions(img.get_width(), img.get_height()) # set pixel dimensions based on image	
    x = (infoObject.current_w / 2) - (img.get_width() / 2)
    y = (infoObject.current_h / 2) - (img.get_height() / 2)
    screen.blit(img,(x,y))
    pygame.display.flip()
piclist =[]
def updatepics(path,piclist):
    dir_list = os.listdir(path)
    for i in range(0,len(dir_list)):
        print(dir_list[i][-3:])
        if dir_list[i] not in piclist:
            if dir_list[i][-3:]=="jpg" or dir_list[i][-3:]=="JPG" or dir_list[i][-3:]=="PNG" or dir_list[i][-3:]=="png":
                print("Hi3")
                piclist.append(dir_list[i])
    return piclist
i=0
##SHow the 5 most recent pics first
piclist = updatepics(path,piclist)
random.shuffle(piclist)
count = len(piclist)
print(piclist)
while True:
    if i ==count:
        i=0
    print(path+"/"+str(piclist[i]))
    show_image(path+"/"+str(piclist[i]))
    time.sleep(2)
    if i %15 ==14:
        gpout = subprocess.Popen("rsync -avz -e ssh pi@192.168.1.155:Slideshow/ PiPySlideshow",shell =True) 
        gpout1=gpout.wait()
        piclist = updatepics(path,piclist)
        random.shuffle(piclist)
    for event in pygame.event.get():   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("escape Key Pressed Exiting..")
                pygame.quit()
    i+=1


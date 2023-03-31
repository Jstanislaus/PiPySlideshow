import pygame
from PIL import Image, ImageDraw

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
def updatepics(path,screen_width,screen_height,win,countarray):    
    for i in range(0,len(dir_list)):
        if dir_list[i] not in countarray:
            if dir_list[i][-3:]=="jpg" or dir_list[i][-3:]=="JPG" or dir_list[i][-3:]=="PNG" or dir_list[i][-3:]=="png":
                img = Image.open(str(dir_list[i]))
                w,h = img.size
                ratio = h/w
                if ratio > 1:
                    resized_image = img.resize((int(screen_width),int(ratio * screen_width)))
                else:
                    ratio = w/h
                    resized_image = img.resize((int(screen_height * ratio),int(screen_height)))
                img = ImageTk.PhotoImage(resized_image)
                imgarray.append(img)
                countarray.append(dir_list[i])
    return imgarray,countarray
imgarray, countarray = updatepics(path,screen_width,screen_height,win,countarray)

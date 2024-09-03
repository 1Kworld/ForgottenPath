import sys
import pygame
from pygame.locals import *
from pyparsing import White
import gradient_pygame as gp
import random
import os.path

pygame.init()
#asks user for width and height
print("Enter the dimensions of the piece (>150x150)")

# input1 = input("Enter Width: ")
# input1_int = int(input1)
# input2 = input("Enter Height: ")
# input2_int = int(input2)
input1_int = 500        
input2_int = 500
#continues to ask user for dimensions until > 150
# while input1_int < 150 or input2_int < 150:
#     input1 = input("Enter Width: ")
#     input1_int = int(input1)
#     input2 = input("Enter Height: ")
#     input2_int = int(input2)
        


(Screenwidth, Screenheight) = (input1_int, input2_int)
# red1 = random.randint(0, 255)
# green2 = random.randint(0, 255)
# blue3 = random.randint(0, 255)

#print(red1)
#print(green2)
#print(blue3)
# color = (0,0,0)
# bgC = (red1,green2,blue3)

pygame.display.set_mode()
screen = pygame.display.set_mode((Screenwidth, Screenheight))
# screen.fill(bgC)
#hand selected images
images = pygame.image.load("data/00.jpeg").convert()




#array for images to randomize selection

#images = manyImages[random.randint(0,138)]
#original = pygame.transform.scale(images, (150, 150))
#images = 
#images = pygame.image.load("data/145.jpeg").convert()

width = images.get_width()
print("original image width = ", width) 

height = images.get_height()
print("original image height = ", height)

x1 = 0 
y1 = 0
x2 = Screenwidth - 10
y2 = Screenheight - 10
#screen.blit(images, (x1,y1))
#pygame.display.flip()

#10x10 subsections for entire user created canvas
while (y1 < Screenheight / 2 ):
    x1 = 0
    x2 = Screenwidth - 10
    while (x1 < Screenwidth ):
        x = random.randint(0,width -10)
        y = random.randint(0,height -10)
        crop_region = (x,y, 10, 10)
        x3 = random.randint(0,width -10)
        y3 = random.randint(0,height -10)
        crop_region2 = (x3,y3, 10, 10)
       
        screen.blit(images, (x1,y1), crop_region)
        screen.blit(images, (x2,y2), crop_region2)
        pygame.display.flip()
        x1 = x1 + 10   
        x2 = x2 - 10  
    y1 = y1 + 10
    y2 = y2 - 10
#user inputs for width and height
#checks to make sure height or width > 150


a1 = random.randint(0,screen.get_width() - 150) 
b1 = random.randint(0,screen.get_height() - 150) 
for c in range (75):
    a = random.randint(0,width - 150)
    b = random.randint(0,height - 150)
    
    crop_region = (a,b, 150, 150)
    screen.blit(images, (a1,b1), crop_region)
    pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 150)
    b1 = random.randint(0,screen.get_height() - 150) 

#50x50 subsections 
a1 = random.randint(0,screen.get_width() - 50) 
b1 = random.randint(0,screen.get_height() - 50) 
for b in range (150):
    a = random.randint(0,width - 50)
    b = random.randint(0,height - 50)
    
    crop_region = (a,b, 50, 50)
    screen.blit(images, (a1,b1), crop_region)
    #pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 50)
    b1 = random.randint(0,screen.get_height() - 50) 
    
#25x25 subsections    
a1 = random.randint(0,screen.get_width() - 25)
b1 = random.randint(0,screen.get_height() - 25) 
for a in range (250):
    a = random.randint(0,width - 25)
    b = random.randint(0,height - 25)
    
    crop_region = (a,b, 25, 25)
    screen.blit(images, (a1,b1), crop_region)
    #pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 25)
    b1 = random.randint(0,screen.get_height() - 25)   
     
#15x15 subsections
a1 = random.randint(0,screen.get_width() - 15)
b1 = random.randint(0,screen.get_height() - 15) 
for a in range (100):
    a = random.randint(0,width - 15)
    b = random.randint(0,height - 15)
    
    crop_region = (a,b, 15, 15)
    screen.blit(images, (a1,b1), crop_region)
    #pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 15)
    b1 = random.randint(0,screen.get_height() - 15)  
    
# x = 0
# y = 0
# x1 = 500
# y1 = 0    
# for z in range(45):
#     screen.blit(image, (x,y))
#     x = x + 15
#     y = y + 15
#     abc = random.randint(1,2)
#     print(abc)
#     if abc == 1:
#         continue
#     else: 
#         screen.blit(image, (x1,y1))
#         x1 = x1 - 35
#         y1 = y1 + 35    

pygame.display.set_caption("Forgotten Path")
#s = 580

pygame.display.flip() 

# Define a function for exiting program
#saves an image but replaces the image after each run
pygame.image.save(screen, "image.png")
running = True
# Keep Displaying the window until close it manually
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          


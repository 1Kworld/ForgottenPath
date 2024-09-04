import sys
import pygame
from pygame.locals import *
from pyparsing import White
import gradient_pygame as gp
import random
import os.path

pygame.init()

pygame.display.set_caption("Forgotten Path")

(Screenwidth, Screenheight) = (750, 750)

pygame.display.set_mode()
screen = pygame.display.set_mode((Screenwidth, Screenheight))


image_paths = [f"data/{i:02d}.jpeg" for i in range(17)]  # Adjusted range to include 00.jpeg
manyImages = [pygame.image.load(path).convert() for path in image_paths]

# Select a random image
images = random.choice(manyImages)

width = images.get_width()
print("Image width =", width) 
height = images.get_height()
print("Image height =", height)

x1 = 0 
y1 = 0
x2 = Screenwidth - 10
y2 = Screenheight - 10

while (y1 < 750 / 2 ):
    x1 = 0
    x2 = 740
    while (x1 < 750 ):
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
    y2 = y2 -10
    
a1 = random.randint(0,screen.get_width() - 150) 
b1 = random.randint(0,screen.get_height() - 150)

for c in range (75):
     a = random.randint(0,width - 150)
     b = random.randint(0,height - 150)
     
     crop_region = (a,b, 150, 150)
     screen.blit(images, (a1,b1), crop_region)
     pygame.display.flip()
     pygame.time.delay(75)
     
     a1 = random.randint(0,screen.get_width() - 150)
     b1 = random.randint(0,screen.get_height() - 150) 

a1 = random.randint(0,screen.get_width() - 50) 
b1 = random.randint(0,screen.get_height() - 50) 
for b in range (150):
    a = random.randint(0,width - 50)
    b = random.randint(0,height - 50)
    
    crop_region = (a,b, 50, 50)
    screen.blit(images, (a1,b1), crop_region)
    pygame.display.flip()
    pygame.time.delay(50)
    
    a1 = random.randint(0,screen.get_width() - 50)
    b1 = random.randint(0,screen.get_height() - 50) 
    
a1 = random.randint(0,screen.get_width() - 25)
b1 = random.randint(0,screen.get_height() - 25) 
for a in range (250):
    a = random.randint(0,width - 25)
    b = random.randint(0,height - 25)
    
    crop_region = (a,b, 25, 25)
    screen.blit(images, (a1,b1), crop_region)
    pygame.display.flip()
    pygame.time.delay(25)
    
    a1 = random.randint(0,screen.get_width() - 25)
    b1 = random.randint(0,screen.get_height() - 25)   
     

a1 = random.randint(0,screen.get_width() - 15)
b1 = random.randint(0,screen.get_height() - 15) 
for a in range (100):
    a = random.randint(0,width - 15)
    b = random.randint(0,height - 15)
    
    crop_region = (a,b, 15, 15)
    screen.blit(images, (a1,b1), crop_region)
    pygame.display.flip()
    pygame.time.delay(15)
    
    a1 = random.randint(0,screen.get_width() - 15)
    b1 = random.randint(0,screen.get_height() - 15)  
  
pygame.display.flip() 



# Define a function for exiting program
pygame.image.save(screen, "image.png")
running = True
# Keep Displaying the window until close it manually
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          


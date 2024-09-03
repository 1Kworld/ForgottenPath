import sys
import pygame
from pygame.locals import *
from pyparsing import White
import gradient_pygame as gp
import random
import os.path

# Initialize Pygame
pygame.init()

# Input dimensions
input1_int = 500        
input2_int = 500

# Set up the screen
screen_width, screen_height = input1_int, input2_int
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Forgotten Path")

# Load and convert images
image_paths = [f"data/{i:02d}.jpeg" for i in range(17)]  # Adjusted range to include 00.jpeg
manyImages = [pygame.image.load(path).convert() for path in image_paths]

# Select a random image
selected_image = random.choice(manyImages)

# Get image dimensions
width, height = selected_image.get_width(), selected_image.get_height()
print("Original image width =", width)
print("Original image height =", height)

x1 = 0 
y1 = 0
x2 = screen_height - 10
y2 = screen_width - 10


#10x10 subsections for entire user created canvas
while (y1 < screen_height / 2 ):
    x1 = 0
    x2 = screen_width - 10
    while (x1 < screen_width ):
        x = random.randint(0,width -10)
        y = random.randint(0,height -10)
        crop_region = (x,y, 10, 10)
        x3 = random.randint(0,width -10)
        y3 = random.randint(0,height -10)
        crop_region2 = (x3,y3, 10, 10)
       
        screen.blit(selected_image, (x1,y1), crop_region)
        screen.blit(selected_image,(x2,y2), crop_region2)
        #pygame.display.flip()
        x1 = x1 + 10   
        x2 = x2 - 10  
    y1 = y1 + 10
    y2 = y2 - 10

#150x150 subsections
a1 = random.randint(0,screen.get_width() - 150) 
b1 = random.randint(0,screen.get_height() - 150) 
for c in range (75):
    a = random.randint(0,width - 150)
    b = random.randint(0,height - 150)
    
    crop_region = (a,b, 150, 150)
    screen.blit(selected_image, (a1,b1), crop_region)
    #pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 150)
    b1 = random.randint(0,screen.get_height() - 150) 

#50x50 subsections 
a1 = random.randint(0,screen.get_width() - 50) 
b1 = random.randint(0,screen.get_height() - 50) 
for b in range (150):
    a = random.randint(0,width - 50)
    b = random.randint(0,height - 50)
    
    crop_region = (a,b, 50, 50)
    screen.blit(selected_image, (a1,b1), crop_region)
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
    screen.blit(selected_image, (a1,b1), crop_region)

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
    screen.blit(selected_image, (a1,b1), crop_region)

    #pygame.display.flip()
    
    a1 = random.randint(0,screen.get_width() - 15)
    b1 = random.randint(0,screen.get_height() - 15)  
    
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
            
pygame.quit()

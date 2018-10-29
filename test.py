# This is an example that uses pygame.draw.rect:
import os, sys
import random
import pygame
from pygame.locals import *
pygame.init()
APPLICATION_x_size = 400
APPLICATION_y_size = 300
screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Fun Boring Example comes with Source Code too!!')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()
Weeee = True
while Weeee:
    # a color can be: (0 to 255, 0 to 255, 0 to 255)
   My_red_color = (255, 0, 0)
   My_blue_color = (0, 0, 255)
   My_green_color = (0, 255, 0)
   My_yellow_color = (255, 255, 0)
   WHITE_WHITE_HOORAY = (255, 255, 255)
   My_light_red_color = (255, 180, 180)
   My_light_blue_color = (190, 190, 255)
    # "screen.set_at((x, y), Color)" and "pygame.draw.rect(screen, Color, (x, y, x_size, y_size))" draw colors on to an "in computer memory image" called: "screen"
   screen.set_at(( 1,  1), My_yellow_color)
   screen.set_at(( 2,  2), My_yellow_color)
   screen.set_at(( 3,  3), My_yellow_color)
   screen.set_at(( 4,  4), My_yellow_color)
   screen.set_at(( 5,  5), My_yellow_color)
   screen.set_at(( 6,  6), My_yellow_color)
   screen.set_at(( 7,  7), My_yellow_color)
   screen.set_at(( 8,  8), My_yellow_color)
   screen.set_at(( 9,  9), My_yellow_color)
   screen.set_at((10, 10), My_yellow_color)
   screen.set_at((11, 11), My_yellow_color)
   screen.set_at((12, 12), My_yellow_color)
   screen.set_at((13, 13), My_yellow_color)
   screen.set_at((14, 14), My_yellow_color)
   screen.set_at((15, 15), My_yellow_color)
   screen.set_at((16, 16), My_yellow_color)
   screen.set_at((17, 17), My_yellow_color)
   screen.set_at((18, 18), My_yellow_color)
   screen.set_at((19, 19), My_yellow_color)
   screen.set_at((20, 20), My_yellow_color)
   pygame.draw.rect(screen, My_red_color,        (50,  50,   10,   10))
   pygame.draw.rect(screen, My_red_color,        (50,  120,  20,   20))
   pygame.draw.rect(screen, My_blue_color,       (50,  150,  30,   30))
   pygame.draw.rect(screen, My_blue_color,       (50,  1000, 1000, 10))
   pygame.draw.rect(screen, My_green_color,      (200, 10,   40,   40))
   pygame.draw.rect(screen, My_light_red_color,  (10,  200,  50,   50))
   pygame.draw.rect(screen, My_light_blue_color, (200, 200,  60,   60))
   pygame.draw.rect(screen, My_light_blue_color, (100, 200,  10,    2))
   pygame.draw.rect(screen, WHITE_WHITE_HOORAY,  (0, 100,  50,   52))
    # If you delete the below line you should no longer see the vibrant colors.
   pygame.display.flip()
    # if the 'X' button is pressed the window should close:
   Geesh = pygame.event.get()
   if len(Geesh) > 0:
    if Geesh[0].type == QUIT: Weeee = False
## Once this line is reached the window should close
import pygame
from pygame.locals import *
pygame.init()


pygame.display.set_caption("MENDELBROT")

x1 = -1.2
x2 = 1.2
y1 = -1.2
y2 = 1.2
zoom = 500
iteration_max = 100


image_x = (x2-x1)*zoom
image_y = (y2-y1)*zoom

window = pygame.display.set_mode((1000, 500))
window.fill((0, 0, 0))
x = 0
while x < image_x:
    pygame.display.flip()

    y = 0
    while y < image_y:
        c_r = x/zoom + x1
        c_i = y/zoom + y1
        z_r = 0
        z_i = 0
        i = 0

        tmp1 = 0

        while ((z_r*z_r + z_i*z_i)<4) and (i<iteration_max):
            tmp = z_r
            tmp1 += tmp
            z_r = z_r*z_r - z_i*z_i + c_r
            z_i = 2*z_i*tmp + c_i
            i+=1

        if i < iteration_max:
            window.fill((255*abs(tmp1)/100,i,0), ((x,y), (1,1)))

        y+=1
    x+=1

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False


pygame.quit()
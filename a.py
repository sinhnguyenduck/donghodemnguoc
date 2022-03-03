from tkinter.constants import TRUE
import pygame
from pygame import time

pygame.init()
screen = pygame.display.set_mode((500,600))
GREY = (22, 14, 240)
WHILE = (250, 250, 250)
BLACK = (0,0,0)
RED = (255,0,0)
clock= pygame.time.Clock()
font= pygame.font.SysFont('san',25)
font2= pygame.font.SysFont('san',80)

min1= font.render('MIN+', True, BLACK)
min2= font.render('MIN-', True, BLACK)
sec1= font.render('SEC+', True, BLACK)
sec2= font.render('SEC-', True, BLACK)
start= font.render('START', True, BLACK)
reset= font.render('RESET', True, BLACK)
min0= 0
haicham= ':'
sec0= 0
a=0
start=False




running = True

while running:
    mouse_x,mouse_y=pygame.mouse.get_pos()

    clock.tick(60)
    screen.fill(GREY)
#taohinh
    pygame.draw.rect(screen, WHILE, (100,50,50,50))
    pygame.draw.rect(screen, WHILE, (250,50,50,50))
    pygame.draw.rect(screen, WHILE, (250,150,50,50))
    pygame.draw.rect(screen, WHILE, (100,150,50,50))
    pygame.draw.rect(screen, WHILE, (350,50,100,50))
    pygame.draw.rect(screen, WHILE, (350,150,100,50))
    pygame.draw.circle(screen, WHILE, (250,350),100)
    pygame.draw.circle(screen,BLACK, (250,350),5)
    pygame.draw.rect(screen, WHILE, (50,500,400,50))

#taochu
    screen.blit(min1,(108,62))
    screen.blit(min2,(108,165))
    screen.blit(sec1,(252,65))
    screen.blit(sec2,(252,165))
    screen.blit(start,(365,65))
    screen.blit(reset,(365,165))

#time
    min0=a//60
    sec0= a-(min0*60)
    text_time1=font2.render(str(min0),TRUE,RED)
    screen.blit(text_time1,(160,100))
    text_time=font2.render(str(haicham),TRUE,RED)
    screen.blit(text_time,(190,100))
    text_time2=font2.render(str(sec0),TRUE,RED)
    screen.blit(text_time2,(210,100))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(100<mouse_x<150) and (50<mouse_y<100):
                  a+=1
                if(250<mouse_x<300) and (50<mouse_y<100):
                  a+=60
                if(100<mouse_x<150) and (150<mouse_y<200):
                  a-=1
                if(250<mouse_x<300) and (150<mouse_y<200):
                  a-=60
                if(350<mouse_x<450) and (50<mouse_y<100):
                  start=True
                if(350<mouse_x<450) and (150<mouse_y<200):
                  a=0    

#lenhstart
                if  start:
                 if sec0>0:
                  sec0-=1
                  time.sleep(1)
                else:
                  start=False                                  
        
pygame.display.flip()

pygame.quit()    
print("ahiiiiiiiiiiiiiiiii")

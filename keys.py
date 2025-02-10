import pygame
from time import *
from pygame.locals import *

pygame.init()
s=pygame.display.set_mode((600,600))
player_x=300
player_y=300

keys=[False ,False ,False ,False]

bg=pygame.image.load("back.jpg")
rocket=pygame.image.load("rocket.png")

image=pygame.transform.scale(bg,(600,600))

while player_y < 600:
    s.blit(image, (0,0))
    s.blit(rocket,(player_x, player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key ==K_UP:
                keys[0]=True
            if event.key == K_DOWN:
                keys[1]=True
            if event.key == K_LEFT:
                keys[2]=True
            if event.key == K_RIGHT:
                keys[3] =True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit (0)
        if event.type ==pygame.KEYUP:
            if event.key ==K_UP:
                keys[0]=False
            if event.key == K_DOWN:
                keys[1]=False
            if event.key == K_LEFT:
                keys[2]=False
            if event.key == K_RIGHT:
                keys[3]=False
    if keys [0]:
        if player_y > 0:
            player_y -=7

    if keys [1]:
        if player_y < 530:
            player_y +=5
    if keys [2]:
        if player_x > 0:
            player_x -= 5
    if keys[3]:
        if player_x < 530:
            player_x += 5

    player_y += 5
    sleep(0.05)

print("game over!")

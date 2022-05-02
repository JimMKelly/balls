import pygame
from ball import Ball
from settings import *
import random

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

for ball in range(0,NUM_BALLS):
    r = random.randint(10,40)
    x = random.randint(r,WIDTH-r)
    y = random.randint(r,HEIGHT-r)
    
    ball = Ball(x,y,r,0,BLUE)
    balls.append(ball)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('black')

    for ball in balls:
        ball.move()
        ball.check_collision()
        ball.draw(screen)
    
    #pygame.time.delay(10)
    pygame.display.update()
    
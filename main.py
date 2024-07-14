import pygame
from ball import Ball
from settings import *
import random

# Initialize Pygame
pygame.init()

def create_ball(x,y,r):
    ball = Ball(x,y,r,0,BLUE)
    balls.append(ball)

def main():
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    for ball in range(0,NUM_BALLS):
        r = random.randint(10,40)
        x = random.randint(r,SCREEN_WIDTH-r)
        y = random.randint(r,SCREEN_HEIGHT-r)
        create_ball(x,y,r)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Handle MOUSEBUTTONUP
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                create_ball(mouse_x,mouse_y, random.randint(10,40))

        screen.fill('black')

        for ball in balls:
            ball.update()
            ball.check_collision()
            ball.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
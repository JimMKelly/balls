import pygame
from pygame.math import Vector2
import math
import random
from settings import *

class Ball:
    def __init__(self, x, y, r, w, colour):
        self.direction = Vector2((random.randint(-5,5)),(random.randint(-5,5)))
        self.pos = Vector2(x,y)
        self.r = r
        self.w = w
        self.volume = 3.14 * r**2
        self.velocity = 2
        self.colour = colour
        self.gravity = GRAVITY
    
    def draw(self,screen):
        pygame.draw.circle(screen, (self.colour), (self.pos), self.r, self.w)

    def move(self):
        self.apply_gravity()
        self.pos.x += self.direction.x * self.velocity
        self.pos.y += self.direction.y * self.velocity
    
    def bounce(self,other):
        new_velocity = ((self.volume - other.volume)/(self.volume + other.volume))*self.velocity + ((2*other.volume) / (self.volume + other.volume)) * other.velocity
        new_velocity2 = ((2*self.volume)/(self.volume + other.volume))*self.velocity - ((self.volume - other.volume)/(self.volume + other.volume)) * other.velocity
        self.velocity = new_velocity
        other.velocity = new_velocity2

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.pos.y += self.direction.y

    def check_collision(self):
        if self.pos.x <= self.r: 
            self.pos.x = self.r
            self.direction.x = self.direction.x * -1
        if self.pos.x + self.r >=WIDTH: 
            self.direction.x = self.direction.x * -1
            self.pos.x = WIDTH - self.r
        if self.pos.y <= self.r: 
            self.direction.y = self.direction.y * -1
            self.pos.y = self.r
        if self.pos.y + self.r >=HEIGHT: 
            self.direction.y = self.direction.y * -1
            self.pos.y = HEIGHT - self.r

        for ball in balls:
            if ball != self:
                distance = math.hypot(ball.pos.x - self.pos.x, ball.pos.y - self.pos.y)

                if distance <= (self.r + ball.r):
                    self.colour = GREEN
                    ball.colour = RED
                    new_vector = ball.pos - self.pos
                    new_vector2 = self.pos - ball.pos
                    m1 = pygame.math.Vector2(self.direction.x, self.direction.y).reflect(new_vector)
                    m2 = pygame.math.Vector2(ball.direction.x, ball.direction.y).reflect(new_vector2)
                    self.direction.x, self.direction.y = m1.x, m1.y
                    ball.direction.x, ball.direction.y = m2.x, m2.y
                    
                    self.bounce(ball)

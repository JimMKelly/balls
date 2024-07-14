import pygame
from pygame.math import Vector2
import math
import random
from settings import *

class Ball:
    def __init__(self, x, y, r, w, colour):
        self.pos = Vector2(x,y)
        self.velocity = Vector2((random.randint(-5,5)),(random.randint(-5,5)))
        self.r = r
        self.w = w
        self.mass = 3.14 * r**2
        self.acceleraton = 1
        self.colour = colour
        self.gravity = GRAVITY
    
    def draw(self,screen):
        pygame.draw.circle(screen, (self.colour), (self.pos), self.r, self.w)

    def update(self):
        self.apply_gravity()
        self.pos += self.velocity * self.acceleraton

    def apply_gravity(self):
        self.velocity.y += self.gravity
        self.pos.y += self.velocity.y

    def check_collision(self):
        #Check collision with walls
        if self.pos.x - self.r < 0 or self.pos.x + self.r > SCREEN_WIDTH:
            self.velocity.x *= -1
        if self.pos.y - self.r < 0 or self.pos.y + self.r > SCREEN_HEIGHT:
            self.velocity.y *= -1

        #Check collision with other balls
        for ball in balls:
            if ball != self:
                if (self.pos.distance_to(ball.pos) < self.r + ball.r):
                    self.bounce(ball)
                    self.colour = GREEN
                    ball.colour = RED
    
    def bounce(self, other):
        assert ( isinstance(other, Ball) )

        distance = self.pos.distance_to(other.pos)
        if distance < self.r + other.r:
            # Separate the balls so they are no longer overlapping
            overlap = self.r + other.r - distance
            direction = (self.pos - other.pos).normalize()
            self.pos += direction * (overlap / 2)
            other.pos -= direction * (overlap / 2)

            # Reflect velocities based on the normal
            self_velocity_along_normal = self.velocity.dot(direction)
            other_velocity_along_normal = other.velocity.dot(direction)

            self.velocity -= direction * self_velocity_along_normal
            other.velocity -= direction * other_velocity_along_normal

            self.velocity += direction * other_velocity_along_normal
            other.velocity += direction * self_velocity_along_normal
"""
File: ball.py
Author: Ali Cope
A Ball class which imports Velocity class from velocity.py and 
Point class from point.py Ball has the variables center(point) and 
velocity(Velocity) as well as the methods ball() advance() 
bounce_horizontal, bounce_vertical() and restart()"""

from velocity import Velocity
from point import Point
import arcade
import random
from pong_constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS

class Ball():
    def __init__(self):
        #create a new ball with a point at the center and a velocity
        self.center = Point()
        self.velocity = Velocity()
        #set x to the balls radius so that it appears on the screen
        self.center.x = BALL_RADIUS
        #set y to a random number that is between the balls radius and the highest point subtract the radius
        self.center.y = random.uniform(BALL_RADIUS,SCREEN_HEIGHT - BALL_RADIUS)
        #assign the ball a random velocity
        self.velocity.dx = random.uniform(0.25,5)
        self.velocity.dy = random.uniform(0.25,5)

    def draw(self):
        #draw the ball as red ball 10px radius
        arcade.draw_circle_filled(self.center.x,self.center.y,BALL_RADIUS,arcade.color.RED)
        return

    def advance(self):
        #set new x location to current location plus velocity
        self.center.x = self.center.x + self.velocity.dx
        #set new y location to current location plus velocity
        self.center.y = self.center.y + self.velocity.dy
        #draw the ball at the new location
        self.draw()
        return

    def bounce_horizontal(self):
        #set the new velocity on x axis to opposite the current velocity because of bounce
        self.velocity.dx = self.velocity.dx * -1

    def bounce_vertical(self):
        #set the new velocity on y axis to opposite the current velocity because of bounce
        self.velocity.dy = self.velocity.dy * -1

    def restart(self):
        #draw a new ball on the left side of the screen and assign it a random velocity
        self.center.x = BALL_RADIUS
        self.center.y = random.uniform(BALL_RADIUS,SCREEN_HEIGHT - BALL_RADIUS)
        self.velocity.dx = random.uniform(0.25,5)
        self.velocity.dy = random.uniform(0.25,5)
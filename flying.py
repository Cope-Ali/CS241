"""
File: flying.py
Author: Ali Cope

Creates a flying base class that contains a point and velocity.
imports velocity and point
"""

import arcade
from velocity import Velocity
from point import Point

class Flying():
    """
    flying class containing a point and velocity for a flying object
    """
    def __init__(self):
        #create a point to be the center of our flying object
        self.center = Point()
        #create a velocity so the object can fly
        self.velocity = Velocity()
        self.alive = True
        self.radius = 0.0
        self.angle = 0

    def draw(self):
        """
        draw function is placeholder for drawing flying object. Each flying object will override this with their own draw function. 
        For now we will draw a dot representing the center of the flying object. 
        """
        #draw a dot at the flying object center point, dot is blue and 5px
        arcade.draw_point(self.center.x, self.center.y, arcade.color.BLUE_SAPPHIRE, 5)

    def advance(self):
        """
        advance function moves the center along the velocity
        """
        # set x equal to x plus dx
        self.center.x += self.velocity.dx
        # set y equal to y plus dy
        self.center.y += self.velocity.dy


    def wrap(self, screen_width, screen_height):
        """
        wrap item when it goes off of the screen
        """
         #check if it is off the left side
        if self.center.x < 0:
            self.center.x = screen_width
        #check if it is off the right side
        if self.center.x > screen_width:
            self.center.x = 0
        #check if it is off the top
        if self.center.y > screen_height:
            self.center.y = 0
        #check if it is off the bottom
        if self.center.y < 0:
            self.center.y = screen_height
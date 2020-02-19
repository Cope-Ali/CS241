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

    def draw(self):
        """
        draw function is placeholder for drawing flying object. Each flying object will override this with their own draw function. For now we will draw a dot representing the center of the flying object. 
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
        #draw the flying object at its new point.
        self.draw()

    def is_off_screen(self, screen_width, screen_height):
        """
        will return a bool value for if the flying object is off screen
        """
        #check if the x coord is off of the screen
        if self.center.x < 0 or self.center.x > screen_width:
            return True
        #check if the y coord is off of the screen
        elif self.center.y < 0 or self.center.y > screen_height:
            return True
        #if it is not off the x or y axis then it is not off the screen     
        else:
            return False
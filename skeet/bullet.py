"""
File: bullet.py
Author: Ali Cope
Creates a bullet class with the following:

radius : float

__init__()
+fire(angle:float) : None

it will inheriate from flying:
center : Point
velocity : Velocity
alive : Boolean
+advance() : None
+is_off_screen(screen_width, screen_height) : Boolean

and will override the following inherited from flying
+draw() : None
"""
import arcade
import math
from flying import Flying

# These are Global constants to use throughout the game
BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

class Bullet(Flying):
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = float(BULLET_RADIUS)
        self.velocity.dy = BULLET_SPEED
        self.velocity.dx = BULLET_SPEED

    def fire(self, angle):
        """
        method takes an angle parameter and uses it to set the bullets velocity
        """
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED


    def draw(self):
        """
        function overwrites the draw method from the flying class, draws bullet at center point.
        """
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)
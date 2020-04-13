"""
File: bullet.py
Author: Ali Cope
Creates a bullet class with the following:

__init__()
life : int
+fire(angle:float) : None

it will inheriate from flying:
center : Point
velocity : Velocity
alive : Boolean
radius : float
+is_off_screen(screen_width, screen_height) : Boolean

and will override the following inherited from flying
+draw() : None
+advance() : None
"""
import arcade
import math
from flying import Flying

# These are Global constants to use throughout the game
BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_COLOR = arcade.color.CANARY_YELLOW

class Bullet(Flying):
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = float(BULLET_RADIUS)
        self.velocity.dy = BULLET_SPEED
        self.velocity.dx = BULLET_SPEED
        self.life = BULLET_LIFE
        self.angle = 0.0

    def fire(self, angle, x, y, dx, dy):
        """
        method takes an angle parameter and uses it to set the bullets velocity
        """
        self.center.x = x
        self.center.y = y
        self.angle = angle
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dy = dy + (math.sin(math.radians(self.angle)) * BULLET_SPEED)
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dx = dx + (math.cos(math.radians(self.angle)) * BULLET_SPEED)


    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/laserBlue01.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

    def advance(self):
        """
        advance function moves the center along the velocity
        """
        # set x equal to x plus dx
        self.center.x += self.velocity.dx
        # set y equal to y plus dy
        self.center.y += self.velocity.dy
        #remove one life from the bullet
        self.life = self.life - 1
        #make sure bullet is still alive
        if self.life <= 0:
            self.alive = False
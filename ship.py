"""
File: ship.py
Author: Ali Cope

Contains Ship class for asteroid game
"""

import arcade
import math
import random
from flying import Flying

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

class Ship(Flying):
    """
    Creates a ship class with the following
    angle: float
    +__init__()
    + thrustUp() : None
    + thrustDown() : None //Bonus funtion

    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +draw() : None
    
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = float(SHIP_RADIUS)
        #start the target randomly on the top half of the screen
        self.center.y = SCREEN_HEIGHT/2
        #start the target randomly on the top half of the screen
        self.center.x = SCREEN_WIDTH/2
        #start ship pointing up
        self.angle = 90
        self.alive = True
        

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        if self.alive:
            alpha = 255 # For transparency, 1 means not transparent
        else:
            alpha = 0
        x = self.center.x
        y = self.center.y
        angle = self.angle - 90

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

    def thrustUp(self):
        """
        override the advance function in flying class
        """
        #The up arrow will increase the velocity in the direction the ship is pointed by 0.25 pixels/frame.
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dy += (math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT)
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dx += (math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT)

    def thrustDown(self):
        """
        override the advance function in flying class
        """
        #The up arrow will increase the velocity in the direction the ship is pointed by 0.25 pixels/frame.
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dy += math.sin(math.radians(self.angle)) * (SHIP_THRUST_AMOUNT * -1)
        #convert the angle to the slope multiply by bullet speed for velocity
        self.velocity.dx += math.cos(math.radians(self.angle)) * (SHIP_THRUST_AMOUNT * -1)   
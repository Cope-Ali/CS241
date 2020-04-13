"""
File: rock.py
Author: Ali Cope

Contains Rock class and three derived Rocks to be used as asteroids: LargeRock, MediumRock and SmallRock

"""

import arcade
import math
import random
from flying import Flying

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Rock(Flying):
    """
    Creates a rock class with the following
    spin : int
    +__init__()
    +hit() : none

    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    +is_off_screen(screen_width, screen_height) : Boolean
    +draw() : None

    and will override the following inherited from flying
    +advance() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = 0.0
        #start the asteroid randomly on the top half of the screen
        self.center.y = random.uniform(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        #start the asteroid randomly on the horizontal axis
        self.center.x = random.uniform(0, SCREEN_WIDTH)
        
        #create spin for asteroid rotation
        self.spin = 0
      
    #TODO Turn into abstract class
    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """


    def advance(self):
        """
        advance function moves the center along the velocity
        """
        # set x equal to x plus dx
        self.center.x += self.velocity.dx
        # set y equal to y plus dy
        self.center.y += self.velocity.dy
        #rotate the asteroid
        self.angle += self.spin


class LargeRock(Rock):
    """
    Creates a large asteroid class with the following
    +__init__()
    
    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    spin : int
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +hit() : none
    +draw() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = BIG_ROCK_RADIUS
        #create spin for asteroid rotation
        self.spin = BIG_ROCK_SPIN
        #set initial velocity for large asteroid
        #set a random direction for the rock
        direction = random.uniform(0,4)
        if direction <=1:
            self.velocity.dx = 1.5
            self.velocity.dy = 1.5
        elif direction <=2:
            self.velocity.dx = -1.5
            self.velocity.dy = 1.5
        elif direction <=3:
            self.velocity.dx = 1.5
            self.velocity.dy = -1.5
        else:
            self.velocity.dx = -1.5
            self.velocity.dy = -1.5
      
    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """
        med1 = MediumRock(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy+2)
        med2 = MediumRock(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy-2)
        small = SmallRock(self.center.x, self.center.y, self.velocity.dx+5, self.velocity.dy)
        rocks = [med1, med2, small]
        return rocks

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

class MediumRock(Rock):
    """
    Creates a medium asteroid class with the following
    +__init__()
    
    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    spin : int
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +hit() : none
    +draw() : None
    """
    def __init__(self, x, y, dx, dy):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = MEDIUM_ROCK_RADIUS
        #create spin for asteroid rotation
        self.spin = MEDIUM_ROCK_SPIN
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """
        small1 = SmallRock(self.center.x, self.center.y, self.velocity.dx+1.5, self.velocity.dy+1.5)
        small2 = SmallRock(self.center.x, self.center.y, self.velocity.dx-1.5, self.velocity.dy-1.5)
        rocks = [small1, small2]
        return rocks

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/meteorGrey_med1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

class SmallRock(Rock):
    """
    Creates a medium asteroid class with the following
    +__init__()
    
    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    spin : int
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +hit() : none
    +draw() : None
    """
    def __init__(self, x, y, dx, dy):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = MEDIUM_ROCK_RADIUS
        #create spin for asteroid rotation
        self.spin = MEDIUM_ROCK_SPIN
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

      
    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """
        #no new rocks are created
        rocks = []
        return rocks

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/meteorGrey_small1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

class Ufo(Rock):
    """
    Creates a Ufo class with the following
    +__init__()
    
    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    spin : int
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +hit() : none
    +draw() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = 10
        self.center.x = random.uniform(0, SCREEN_WIDTH)
        self.center.y = random.uniform(0, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-2, 2)
        self.velocity.dy = random.uniform(-2, 2)

      
    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """
        #eject two aliens
        alien1 = Alien(self.center.x, self.center.y, self.velocity.dx+1.5, self.velocity.dy+1.5)
        alien2 = Alien(self.center.x, self.center.y, self.velocity.dx-1.5, self.velocity.dy-1.5)
        aliens = [alien1, alien2]
        return aliens

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/ufo.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

class Alien(Rock):
    """
    Creates a medium asteroid class with the following
    +__init__()
    
    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    radius : float
    spin : int
    +is_off_screen(screen_width, screen_height) : Boolean
    +advance() : None

    and will override the following inherited from flying
    +hit() : none
    +draw() : None
    """
    def __init__(self, x, y, dx, dy):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = 7
        #create spin for asteroid rotation
        self.spin = -2
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

      
    def hit(self):
        """
        hit method abstract for what happens when the astroid is hit
        """
        #no new rocks are created
        rocks = []
        return rocks

    def draw(self):
        """
        override the draw function in flying class
        """
        img = "images/Alien.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha) 

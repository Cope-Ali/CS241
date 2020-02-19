"""
File: target.py
Author: Ali Cope

Contains Target class and three derived targets; Strong, Standard, and Safe
BONUS TARGET "UFO" - STRETCH CHALLENGE
Bonus UFO target is made of two drawn elements an elipse and a circle.
- The UFO will be generated 1 in 20 probability
- The UFO has 5 lives and give 20 bonus points when destroyed
- The UFO turns red when there is one life remaining
- The UFO reverses direction at twice the speed when it reaches the edge of the screen.
"""

import arcade
import math
import random
from flying import Flying

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE

TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

TARGET_UFO_HEIGHT = 10
TARGET_UFO_WIDTH = 40
TARGET_UFO_COLOR = arcade.color.SILVER

class Target(Flying):
    """
    Creates a target class with the following
    radius : float
    life : int
    score : int
    bonus : int
    +__init__()
    +hit() : int

    it will inheriate from flying:
    center : Point
    velocity : Velocity
    alive : Boolean
    +advance() : None
    +is_off_screen(screen_width, screen_height) : Boolean

    and will override the following inherited from flying
    +draw() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #add radius
        self.radius = float(TARGET_RADIUS)
        #start the target randomly on the top half of the screen
        self.center.y = random.uniform(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        #start velocity randomly for dx between 1 and 5
        self.velocity.dx = random.uniform(1,5)
        #start velocity randomly for dy between -2 and 5
        self.velocity.dy = random.uniform(-2, 5)
        #standard targets can survive 1 hit
        self.life = 1
        # you get one point per hit
        self.score = 1
        # standard targets gets no bonus points for being destroyed
        self.bonus = 0

    def hit(self):
        """
        hit class, returns point value for a hit and kills target
        """
        self.life -= 1
        total_score = 1
        if self.life == 0:
            self.alive = False
            total_score += self.bonus
        return total_score

    def draw(self):
        """
        override the draw function in flying class
        """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)

class Strong(Target):
    """
    Creates a Strong class with the following
    +__init__()

    it will inheriate from Target:
    center : Point
    velocity : Velocity
    radius : float
    alive : Boolean
    +advance() : None
    +is_off_screen(screen_width, screen_height) : Boolean
    +hit() : int

    and will override the following inherited from target
    life : int
    score : int
    bonus : int
    +draw() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #start velocity randomly for dx between 1 and 3 (slower than normal target)
        self.velocity.dx = random.uniform(1,3)
        #start velocity randomly for dy between -2 and 3 (slower than normal target)
        self.velocity.dy = random.uniform(-2, 3)
        #strong targets can survive 3 hit
        self.life = 3
        # strong targets gets 4 bonus points for being destroyed
        self.bonus = 4

    def draw(self):
        """
        override the draw function in flying class
        """
        #method provided https://content.byui.edu/file/856c5360-ff89-4409-a7ae-bca07f06f19c/1/week06/skeet.html
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.life), text_x, text_y, TARGET_COLOR, font_size=20)

class Safe(Target):
    """
    Creates a Strong class with the following
    +__init__()

    it will inheriate from Target:
    center : Point
    velocity : Velocity
    alive : Boolean
    life : int
    +advance() : None
    +is_off_screen(screen_width, screen_height) : Boolean
    +hit() : int

    and will override the following inherited from target
    radius : float
    score : int
    bonus : int
    +draw() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #set safe radius
        self.radius = TARGET_SAFE_RADIUS
        #no points for hitting safe target
        self.score = 0
        # safe targets have -10 penelty for being destroyed
        self.bonus = -10

    def draw(self):
        """
        override the draw function in flying class
        """
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius, TARGET_SAFE_COLOR)

class UFO(Target):
    """
    Creates a UFO class with the following
    +__init__()

    it will inheriate from Target:
    center : Point
    velocity : Velocity
    alive : Boolean
    life : int
    radius : float
    +advance() : None
    +is_off_screen(screen_width, screen_height) : Boolean
    +hit() : int

    and will override the following inherited from target
    life : int
    score : int
    bonus : int
    +draw() : None
    +advance() : None
    """
    def __init__(self):
        #call the base class to set up our point and velocity
        super().__init__()
        #two points for hitting ufo
        self.score = 2
        # UFO have 20 bonus points for being destroyed
        self.bonus = 20
        #UFOs have to be hit 5 times to be destroyed
        self.life = 5

    def draw(self):
        """
        override the draw function in flying class
        """
        #if the UFO has only 1 life left, turn it red
        if(self.life <= 1):
            TARGET_UFO_COLOR = arcade.color.RED
        #If UFO has more than 1 life left, keep it silver
        else:
            TARGET_UFO_COLOR = arcade.color.SILVER
        arcade.draw_circle_outline(self.center.x, self.center.y, TARGET_UFO_HEIGHT, TARGET_UFO_COLOR, 3)
        arcade.draw_ellipse_filled(self.center.x, self.center.y, TARGET_UFO_WIDTH, TARGET_UFO_HEIGHT, TARGET_UFO_COLOR, 15)
        

    def advance(self):
        """
        advance function moves the center along the velocity
        """
        #if see if the UFO is almost at the edge of the screen
        if (self.center.x >= SCREEN_WIDTH-20 or self.center.y >= SCREEN_HEIGHT-20):
            #if it is change the velocity to negative to reverse direction
            self.velocity.dx *= -2
            self.velocity.dy *= -2
            
        # set x equal to x plus dx
        self.center.x += self.velocity.dx
        # set y equal to y plus dy
        self.center.y += self.velocity.dy
        #draw the flying object at its new point.
        self.draw()
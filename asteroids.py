"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import math
import random
from point import Point
from bullet import Bullet
from rock import LargeRock, MediumRock, SmallRock, Ufo, Alien
from ship import Ship

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2




class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        #create our ship
        self.ship = Ship()
        #create an array to hold all of our bullets
        self.bullets = []
        #create an array to hold all of our asteroid rocks
        self.rocks = []
        #build 5 large asteroids for the start of game and add to rocks[]
        for i in range(0,5):
            rock = LargeRock()
            self.rocks.append(rock)
        #create a UFO
        if (random.uniform(0,25)) <= 1:
            ufo = Ufo()
            self.rocks.append(ufo)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        #draw our ship
        self.ship.draw()
        
        #draw all of the bullets
        for bullet in self.bullets:
            bullet.draw()

        #draw all of the asteroid rocks
        for rock in self.rocks:
            rock.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        #advance our ship
        self.ship.advance()
            
        #advance all of the bullets
        for bullet in self.bullets:
            bullet.advance()

        #advance all of the asteroid rocks
        for rock in self.rocks:
            rock.advance()

        #Check for collisions
        self.check_collisions()

        #check if anything has moved
        self.check_off_screen()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += 3

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= 3

        if arcade.key.UP in self.held_keys:
            self.ship.thrustUp()

        if arcade.key.DOWN in self.held_keys:
            self.ship.thrustDown()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet()
                bullet.fire(self.ship.angle, self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    #TODO check for collisions
    def check_collisions(self):
        """
        checks for any collisions between bullets, rocks and the ship
        """
        
        for rock in self.rocks:
            #check for collisions between rocks and bullets
            for bullet in self.bullets:
                if bullet.alive and rock.alive:
                    close_enough = bullet.radius + rock.radius

                    if(abs(bullet.center.x - rock.center.x) < close_enough and abs(bullet.center.y - rock.center.y) < close_enough):
                        bullet.alive = False
                        littles = rock.hit()
                        for r in littles:
                            self.rocks.append(r)
                        rock.alive = False
                        

            #check for collisions between rocks and ship
            if self.ship.alive and rock.alive:
                close_enough = rock.radius + self.ship.radius

                if(abs(rock.center.x - self.ship.center.x) < close_enough and abs(rock.center.y - self.ship.center.y) < close_enough):
                    self.ship.alive = False
                    littles = rock.hit()
                    for r in littles:
                        self.rocks.append(r)
                    rock.alive = False

        self.cleanup_zombies()

    #TODO check for anything dead and remove it from lists
    def cleanup_zombies(self):
        """
        removes any dead bullets or rocks from lists
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for rock in self.rocks:
            if not rock.alive:
                self.rocks.remove(rock)

    #TODO check for items going off screen and wrap around the side
    def check_off_screen(self):
        """
        Check if any of the items have moved off screen and wrap them around
        """
        #wrap ship
        self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
        #wrap bullets
        for bullet in self.bullets:
            bullet.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
        #wrap asteroids
        for rock in self.rocks:
            rock.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

    #gets the angle of degrees, copied from SKEET
    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
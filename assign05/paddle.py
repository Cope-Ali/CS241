"""
File: paddle.py
Author: Ali Cope
Created paddle class which imports Point class from point.py it contains center(Point)
and three methods draw(), move_up() and move_down()
"""

from point import Point
import arcade
from pong_constants import *

class Paddle():
    def __init__(self):
        self.center = Point()
        #set starting point for the paddle, screen is 400px wide, 300px high, paddle is 10px wide, 50 px high 
        self.center.x = SCREEN_WIDTH - PADDLE_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
    
    def draw(self):
        #draw the paddle as a black rectangle 10 px wide by 50 px high
        arcade.draw_rectangle_filled(self.center.x,self.center.y,PADDLE_WIDTH,PADDLE_HEIGHT,arcade.color.BLACK)

    def move_up(self):
        #the paddle cannot move off the screen, check if located at the top of screen
        if(self.center.y < SCREEN_HEIGHT - PADDLE_HEIGHT):
            #paddle is not at the top so move down 5 px
            self.center.y = self.center.y + MOVE_AMOUNT
        else:
            self.center.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def move_down(self):
        #the paddle cannot move off the screen, check if located at the bottom of screen
        if(self.center.y > PADDLE_HEIGHT/2):
            #paddle is not at the bottom so move down 5 px
            self.center.y = self.center.y - MOVE_AMOUNT
        else:
            self.center.y = PADDLE_HEIGHT/2

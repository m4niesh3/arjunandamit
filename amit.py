import pygame
from pygame.sprite import Sprite

class Amit(Sprite) :
    """ a class to represent a single amit in a fleet of amits """
    def __init__(self,ai_game) :
        """initialize the amit and set its starting position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings

        #load the amit image and set its rect attribute
        self.image=pygame.image.load('images/amit.bmp')
        self.rect=self.image.get_rect()

        #start each new amit near the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store the aliens exact horizontaL postion
        self.x=float(self.rect.x)
    def check_edges(self) :
        """return True if amit is at edge of the screen"""
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
            return True

    def update(self) :
        """move the amit to the right """
        self.x += self.settings.amit_speed*self.settings.fleet_direction
        self.rect.x=self.x

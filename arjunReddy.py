import pygame

class Ship :
    
    """a class to manage the ship"""
    
    def __init__(self,ai_game) :
         """initialize the ship ans set its starting positon"""
         
         self.screen=ai_game.screen
         self.screen_rect=ai_game.screen.get_rect()

         #load the ship image and get its rect.
         
         self.image=pygame.image.load('images/arjunReddy.bmp')
         self.rect=self.image.get_rect()
         self.setting=ai_game.settings #because already [self.settings]=Settings() is defined in alien_invasion.py,we are denoting or assigning the one in square brakets
         
         #start each new ship at the bottom center of the screen 
         
         self.rect.midbottom=self.screen_rect.midbottom
         self.moving_right= False
         self.moving_left=False
         
         #store a decimal value for arjun horizontal position
         
         self.x=float(self.rect.x)
    
    
    
    def update(self) :
        
        """"update arjun postion based on the movement flag """
        
        
        if self.moving_right and self.rect.right  < self.screen_rect.right :
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.setting.ship_speed
        
        #update rect object from self.x
        self.rect.x=self.x
    
    
    
    def blitme(self) :
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

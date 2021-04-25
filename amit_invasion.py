import sys
import pygame
from setting import Settings
from arjunReddy import Ship
from bullet import Bullet
from amit import Amit


class Alieninvasion :
     """overall class to manage game assets and behavior"""

     def __init__(self) : 
         """initialize the game,and create game resources."""
         pygame.init()
         self.settings=Settings()
         self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
         pygame.display.set_caption('alien invasion')
         self.ship=Ship(self)
         self.bullets=pygame.sprite.Group()
         self.amits=pygame.sprite.Group()
         self._create_fleet()

     def run_game(self) :
         """start the main loop for the game """
         while True :
             self._check_events()
             self.ship.update()
             self._update_bullets()
             self._update_amits()
             self._update_screen()
      
     def _create_fleet(self) :
         """create fleet of amits"""
         #create an amit and the find number of amits in a row
         #spacing between each amit  is equal to one amit width
         amit=Amit(self)
         amit_width,amit_height=amit.rect.size
         amit_width=amit.rect.width
         available_space_x=self.settings.screen_width-(2*amit_width)
         number_amits_x=available_space_x//(2*amit_width)

         #determine the number of rows of amits that fit on the screen
         ship_height=self.ship.rect.height
         available_space_y=(self.settings.screen_height - (3*amit_width)- ship_height)
         number_rows=available_space_y//(2*amit_height)

         #create the first fleet of amits
         for row_number in range(number_rows) :
             for amit_number in range(number_amits_x) :
                 self._create_amit(amit_number,row_number)
             
     def _create_amit(self,amit_number,row_number) :
         """ create an amit and place it in the row """       
         amit=Amit(self)
         amit_width,amit_height=amit.rect.size
         amit.x=amit_width+2*amit_width*amit_number
         amit.rect.x=amit.x
         amit.rect.y=amit.rect.height+2*amit.rect.height*row_number
         self.amits.add(amit)
         
     def _check_fleet_edges(self) :
         """respond appropriately if any amits have reached an edge """
         for amit in self.amits.sprites()  :
             if amit.check_edges() :
                 self._change_fleet_direction()
                 break

     def _change_fleet_direction(self) :
         """ drop the entire fleet and change the fleets direction """
         for amit in self.amits.sprites() :
             amit.rect.y += self.settings.fleet_drop_speed 
         self.settings.fleet_direction *= -1


     def _update_bullets(self) :
         """update positon of bullets and get rid of old bullets """
         #update bullet postion
         self.bullets.update()
         #get rid of bulletrs that have disappeared
         for bullet in self.bullets.copy() :
                 if bullet.rect.bottom <= 0 :
                     self.bullets.remove(bullet)
         #check for any bullets that have hit one of the amit
         # if so,get rid of the bullet and that amit
         collisions=pygame.sprite.groupcollide(self.bullets,self.amits,True,True)

     
     def _check_events(self) :
         """" responds to keypresses and mouse events"""
         for event in pygame.event.get() :
             if event.type==pygame.QUIT :
                 sys.exit()
             elif event.type==pygame.KEYDOWN :
                 self._check_keydown_events(event)
             elif event.type==pygame.KEYUP :
                 self._check_keyup_events(event)
     
     def _check_keydown_events(self,event) :
         if event.key==pygame.K_RIGHT :
                     self.ship.moving_right= True
         elif event.key==pygame.K_LEFT :
                     self.ship.moving_left=True     
         elif event.key==pygame.K_q :
                     sys.exit()
         elif event.key==pygame.K_SPACE :
                     self._fire_bullet()

     def _check_keyup_events(self,event)  :
         if event.key==pygame.K_RIGHT :
                     self.ship.moving_right= False
         elif event.key==pygame.K_LEFT :
                     self.ship.moving_left= False
    
     def _fire_bullet(self) :
         if len(self.bullets) < self.settings.bullets_allowed :
             new_bullet=Bullet(self)
             self.bullets.add(new_bullet)
        
     def _update_amits(self) :
         """check if the fleet is at the edge, then update the positions at all aliens in the fleet """
         self._check_fleet_edges()
         self.amits.update()
     
     def _update_screen(self) :
         """update images on screen and flip  ton the new screen """
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         for bullet in self.bullets.sprites() :
             bullet.draw_bullet()
         self.amits.draw(self.screen)
         #make the most recently drawn screen visible
         pygame.display.flip()




if __name__=='__main__' :
    #make a game instance and run the game
    ai=Alieninvasion()
    ai.run_game()


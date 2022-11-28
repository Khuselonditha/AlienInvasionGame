import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        # Create a bullect rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    
    def update(self):
        """ Move bullet up the screeen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        
        # Update the rect position.
        self.rect.y = self.y

    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect )





"""
# CREATING A BULLET CLASS

#-- The Bullet class inherits from Sprite, whicj=h we import from the pygame.sprite module.
#-- When you use Sprites, you can group related elements in the game and act on them at once.
#-- To create a bullet instance, __init__() needds the current instance of AlienInvasion, and we 
# call super() to inherit properly from class Sprite
#-- We also set attributes for the sceen and settings objects, and for the bullet colour.

#--  we then create the bullet's rect attribute.
# The bullet is not created from an image, therefore we need to create a rect from scratch using
# the pygame.Rect() class.
#-- This class requires the x and y coordinates of the top-left corner of the rect, and the width and
# height of the rect.
#-- We initialize the rect at (0, 0), well change it later, because the ships bullet depends on the
# position. Then we get the bullets width and height from the values stored in self.settings

#-- We set the bullet's midtop attribute to match the ship's midtop attribute.
#-- This will make the bullet appear as if it is being fired from the ship.

#-- We then store a decimal value for the bullet's y- cooordinates so we can make fine adjusments to 
# the bullet's speed.


# update() and draw() methods

#-- The update method manages the bullet's position.
#-- When the is fired, it moves up the screen, which corresponds to decreasing y-coordinate values
#-- To update the position, we subtract the amount stored in settings.bullet_speed from self.y
#-- We the use the value o f self.y to set the value of self.rect.y

#-- The bullet_speed setting allows us to increase the speed of the bullets as the game progresses
# or as needed to refine the game's behaviour.
#-- Once the bullet is fired we need to change the value of its x-coordinate, so it will travel 
# vertically in a stright line even if the ship moves

#-- When we want to draw the bullet, we call draw_bullet() method.
#-- The draw.rect() function inside this method, fills the part of the screen defined by the bullet's
# rect with the colour stored in self.colour
"""
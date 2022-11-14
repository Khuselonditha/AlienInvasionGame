import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


"""
#-- Pygame treats all elements like rectangles (rects) even if they are not shaped like rectangles.
#-- We first import the pygame module, and define a class called Ship.
#-- The __init__() method takes two arguments, self and the instance of the AlienInvasion class.
# giving Ship the access to all the game resources defined in the AlienInvasion class.
#-- We assign the scrren to the attribute of Ship, so we can access it easily in all the methods in
# this class (Ship)
#-- We the access the screens rect attribute using the get_rect() method and assign it to self.screen_rect()
#-- This allows us to place the ship in a correct position on the screen
#-- To load the image we call pygame.image.load() and give it the location of our ship image. This function
# returns the surface of the ship which we assign to self.image
#-- When the image is loaded, we call get_rect() to access the ships surfaces rect attribute so we can
# use it to place the ship.
#-- We then position the ship at the bottom center of the screen (midbottom)
#-- Pygame uses these rect attributes to position the ship image so its centered horizontally and aligned
# with the bottom of the screen.
#-- We the define the blitme() method, which draws the image to the screen at the position specified
# by self.rect
"""
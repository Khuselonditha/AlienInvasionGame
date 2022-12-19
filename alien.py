import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the game and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/icons8-alien-monster-emoji-48.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)


    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    
    def update(self):
        """Move the alien to the right or left."""
        self.x +=  (self.settings.alien_speed * 
                            self.settings.fleet_direction)
        self.rect.x = self.x 





"""
# CREATING AN ALIEN CLASS

#-- Most of this class is like the Ship class except for the aliens position on the screen.
#-- We initially place the alien in the top-left corner of the screeen.
#-- We add space to the left of it that is equal to the alien's width and space above it equal to 
# its height so its easy to see.
#-- We also add the code to check the precise horizontal position of the alien 
#-- This Alien class doesnt need a method for drawing it  to the screen, instead we use pygame's
# group method that automatically draws elements of a group to the screen.
"""

"""
# MOVING ALIENS TO THE RIGHT

#-- We create a setting parameter in __init__() so we can access it in the update() method
#-- Each time we update the alien's position, we move it to the right by the amount stored in
# alien_speed
#-- We the track the alien's position with the self.x attribute, which can hold decimal values.
#-- We then use the self.x attribute to update the position of the alien's rect
"""

"""
# CHECKING WHETHER AN ALIEN HAS HIT THE EDGE

#-- We create a new method called check_edges(), to see whether an alien is on the right or left edge.
#-- Its on the right if its right attibute is greater or equals the screen's right rect attribute
# And on the left edge if its left attribute is less or equals to zero.

#-- We then modify the update() method to allow motion to the left or right by multiplying the alien's 
# speed by the value of the fleet_direction
#-- If fleet_direction is 1, the value of alien_speed will be addded to the alien's current position,
# moving the alien to the right.
#-- If fleet_direction is -1, the value of alien_speed will be subtracted to the alien's current
# position moving it to the left
"""
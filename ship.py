import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's x and y values not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y



        
    
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

"""
# Allowing Continouos Movement
#-- We first add self.moving_right attibute for all arrows in the __init__() method and set it to False intially.
#-- THen we add update() which moves the ship to the right, left, up and down the flag is True
#-- The update() will be called through an instance of Ship.
"""

"""
# ADJUSTING THE SHIPS SPEED

#-- We create a setting attribute of class Ship, so we can use it in the update() method.
#-- We can use a decimal value to set an accurate rect value, but for us to be more accurate, we create
# a new self.x and self.y attributes that can hold decimal values.
#-- We then use the float() function to convert the value of self.rect.x and self.rect.y to a decimal
# and assign the values to self.x and self.y respectively.
#-- Now when we change the ship's speed in update() method, the value of self.x and self.y is adjusted
# by the value stored in settings.ships.speed
#-- After self.x and self.y have benn updated, we use the new value to update self.rect.x and self.rect.y
# which controls the position of the ship.
#-- Only thhe interger part of self.x will be stored in the self.rect.x, but its fine for displaying
# the ship

#NB Now we can change the value of ship_speed, and any value greater than 1 will make the ship move 
# faster. 
#-- This will inturn make the ship respond quickly enough to shoot down the aliens and will let us 
# chnge the tempo of the game as the player progresses in game play. 
"""

"""
# LIMITING THE SHIP'S RANGE

#-- We write code that checks the position of the ship before changing the value of self.x and self.y
#-- The code self.rect.right returns the x-coordinates of the right edge of the ship's rect. 
#-- If the self.rect.right is less than the value returned by self.screen_rect.right, the ship hasnt
# reached the right edge of the screen. 
#-- Also, if the value of the left side of the ship's rect is greater than 0, the ship hasnt reached
# the left edge of the screen.
#-- If the value of the top side of the ship is greater than 0, it means the ship hasnt reached the
# top edge of the screen and is still within bounds of changing the self.y values.
#-- Same for the self.rect.bottom of the ship, if its value is less than the screen_rect.bottom, it is
# in bound to change the self.y of the ship and hasnt reached the edge of the screen.
# This ensures that the ship is within bounds before adjusting the self.x and self.y values.
"""
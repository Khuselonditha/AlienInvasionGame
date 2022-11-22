class Settings:
    """A class to store all the seettings of the Alien Invasion game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width  = 1200
        self.screen_height = 700
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5






"""
#-- Each time we introduce a new functionality to the game, we'll need to create some new settings
# as well.
#-- So instead of adding settings throughout our code, we created a module called settings that
# contains a class called Settings to store all the values in one place.
#-- This makes it easier to modify the game's appearance and behaviour as our project grows.
#-- To modify the game we'll simply change the values in the settings.py module .
"""
"""
#EXPLANATION
#-- WE import the settings to the main program file (alien_invasion.py).
#-- Then we create an instance of the settings and assign it to self.settings after the pygame.init()
#-- When we create the screen, we use the screen_width and screen_height attributes of self.settings.
#-- And then we use the self.settings to access background colour when filling the screen after a loop.

"""

"""
# ADJUSTING THE SHIP'S SPEED

#-- We set the initial value of ship_speed to 1.5.
#-- When the ship moves now, its position is now adjusted by 1.5 pixels, instead of 1 on each pass 
# of the loop.
#-- We are using decimals values for the speed to give us finer coontrol of the ship for when we icrease
# the tempo of the game later on.
#-- The rect.x are in interger values not float. we need to change that.
"""
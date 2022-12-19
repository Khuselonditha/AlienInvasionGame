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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1






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

"""
# ADDING THE BULLET SETTINGS

#-- These settings create dark grey bullets with a width of 3 pixels and a height of 15 pixels.
#-- The bullets will travels much slower than the ship
"""

"""
# LIMITING NUMBER OF BULLETS

#-- We limit the number of bullets fire to 5. Then we'll use this setting in AlienInvasion to check
# how may bullets exist before creating a new bullet in _fire_bullet() 
"""

"""
# MOVING ALIENS TO THE RIGHT

#-- First, we add settings to control the speed of each alien.
# Then we'll use an update() method in alien.py to move the aliens.
"""

"""
# CREATING SETTINGS FOR FLEET DIRECTION

#-- The setting fleet_drop_speed controls how quickly the fleet drops down the screen each time an
# alien reaches either edge
#-- To implement the setting fleet_direction, we use values 1 and -1 and switch between them as the 
# fleet changes direction.
#-- Moving to the right adds to each alien's x-coordinate value, and moving to the left involves
# subtracting from each aliens x-coordinate value.
"""
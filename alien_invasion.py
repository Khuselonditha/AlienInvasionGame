import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manange the game assets and behaviour"""

    def __init__(self):
        """Initializee the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set background colour
        self.bg_colour = (230, 230, 230)


    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

           
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Redraw the screen during each pass through loop."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # MAke a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()


"""
# CREATING A PYGAME WINDOW AND USER RESPONSES

#-- First, we import the sys and pygame modules. The pygame module conatains the functionality we
# need to create the game, while the tools in the sys module we'll use when the player decides exit
# quiting the game.
#-- We the create a class called AlienInvasion. In the __init__() method, the pygame.init() funtion
# initializes the background setting that needs the pygame to work properly.
#-- We the call the pygame.display.setmode() to create a display window, on which well draw the games
# graphic elements.
#-- The argurment (1200, 800) is a tuple that sets our screen to 1200px wide and 800px high. They
# can be adjusted any how.
#-- We then assign the object to self.screen - the surface of our game, where the elements will be
# displayed.
#-- The surface returned by the display.set_mode() method, represents the entire game window.
#-- The surface will be redrawn every time the animation loop runs due to being updated with any
# any changes triggered by the user inputs.

#-- The game is controlled by the run_game() method. This method contains a while loop that runs continualy.
#-- The while loop contains an event loop and code that mananges the screen updates. An event is an
# action that the user performs while playing the game, such as pressing a key.
#-- To make our program to respond to an event, we write an event loop to listen to events and
# perform the appropriate tas depending on the said event.
# The for loop in the run_game() method is an event loop.

#-- We the use pygame.event.get() funtion to access the events pygame detects.
#-- Any event the keyboard or mouse makes will cause this loop to run.
#-- The inside the loop we'll write a series of if statements to detect and respond to certain events.
#-- In our program when a player clicks the game's close button, a pygame.QUIT event is detected and
# and we call the sys.exit() function to exit the game.
#-- The pygame.display.flip() tell pygame to make the recently drawn screen to be visible.
#-- When we move the pygame elements around, pygame.display.flip() continuosly updates the screen
# to show the new position of the elements while hiding the old ones, creating an illuion of 
# smooth movements.

#-- At the end of the file, we create  an instance of the game and call run_game().
#-- We place the ru_game() in an if block only running if the file is called directly.
"""

"""
# SETTING BACKGROUND COLOUR

#-- Colours in pygame are specified as RGB colours: a mix of Red, Green and Blue. The colours can range
# from 0 to 255. Red = (255, 0, 0), Green =  (0, 255, 0), Blue = (0, 0, 255). These combinations can 
# make up to 16 million colours. 
# In our program we created a gray colour by mixing RGB colours as (230, 230,230).

#-- We the also fill the screen  with the background colour using the fill() method, which takes the
# argument of the colour be created in the __init__() method.
"""

"""
# DRAWING THE SHIP TO THE SCREEN

#-- We first import Ship and then make a instance of Ship after the screen has been created.
#-- The call of Ship(), requires one argument, an instance of the AlienInvasion. The self here refers
# to the current instance of AlienInvasion. This is the parameter tha gives Ship class the access to
# the games resources such as screen object.
#-- We assign this Ship instance to self.ship
#-- After filling the background we draw the ship to the screen by calling ship.blitme() so the ship
# appears in the background. 
"""

"""
# Refactoring: The _check_events() and _update_screen() Methods
1. _check_events()
#-- We make a new _check_events() method, and move the lines that check whether the player has clicked
# the close window, into this method.
#-- To call a method within a class, we use a dot notation with the variable "self" and the name of
# the method
#-- We call this method from within a while loop in run_game()

2. _update_screen()
#-- We move the code that draws the background and the ship and flips the screen into _update_screen()
#-- Now the body of the main loop run_game() is much simpler.
#-- Its easier to see that we are looking for new events and updating the screen on each each pass though 
# the loop.
 
"""
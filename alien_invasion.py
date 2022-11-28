import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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

        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

           
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    

    def _check_keydown_events(self, event):
        """Respond t keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left  = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up  = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down  = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                

    def _check_keyup_events(self, event):
        """Respond to key realeases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappered
        for bullet in self.bullets.copy():
                if bullet.rect. bottom <= 0:
                    self.bullets.remove(bullet)


    def _update_screen(self):
        """Update images o the screen ad flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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

"""
# RESPONDING TO PRESSED KEY

#-- Inside the _check_events() method we add an elif block to the vent loop to respond when Pygame
# detects a KEYDOWN event.
#-- We then check if the wehether the key pressed is the right arrow, event.key
#-- The right key is represented by pygame.K_RIGHT. 
#-- If the right key is pressed move the ship to the right by increasing the value of 
# self.ship.rect.x by 1
"""

"""
# ALLOWING CONTINOUOS MOVEMENT
#-- We first modify how the game responds when the player presses the right arrow, insatead of directly
# changing the position of the ship, we merely just set self.moving_right to True.
#-- WE then add an elif block with responds to the KEYUP event. 
#-- When the player releases the right,left, up down arrow, we set self.Moving_right to False.

#-- THe ships position will then be updated after we've checked for keyboard events and before we
# update the screen
#-- This allows the ship's position to be updated in response to the player input and ensure the
# updated position will be used when ddrawing the ship on the screen.
"""

"""
# REFRACTORING _check_events()

#-- We first make two helper methods: _check_keydown_events() and _check_keyup_events()
#-- Each needs a parameter self, and an event parameter.
#-- The _check_events() method now checks for keypress and a keydown event and calls one of our new
# helper methods with moves the ship.
"""

"""
# PRESSING Q TO QUIT

#-- In the _check_keydown_events() method we add a new block that ends the game when the player presses
# Q.
"""

"""
# STORING BULLETS IN A GROUP

#-- We create the group to store all the live bullets so we can manage the bullets that have already
# been fired.
#-- This group is an instance of the pygame.sprite.Group class which behaves like a list with some 
# extra functionality that is helpful when building games
# we use this group to draw the bullets into the screen on each passthrough the main loop and update
# each bullet's position.

#-- When you call Update() on a group, the group automatically calls update on each sprite in the
# group.
#-- The line self.bullets.update() calls bullets.update() for each bullet we place in the group bullets
"""

"""
# FIRING BULLETS

#-- First we import Bullet class
#-- Then we call _fire_bullet() when spacebar is pressed.
#-- In the _fire_bullet(), we create a new instance of Bullet and call it new_bullet. We then add it
# to the group of bullets using the add() method.
#-- The add() method is similar to the append() method, but its method is written specifically for
# pygame groups
#-- The bullet.sprites() method returns a list of all sprites in the group of bullets
#-- To draw all the bullets fired to the screen, we loop through the sprites in bullets and call
# draw_bullet() on each one. 
"""

"""
# DELETING OLD BULLETS

#-- When you use a for loop with a list (or group in Pygame), Pyton expects that list to stay the 
# same length as long as the loop is running.
#-- Since we can't remove items from a list or a group within a for loop, we have to loop over a 
# copy of the group.
#-- We use a copy() to set up the for loop, which enaables us to modify the bullets inside the loop.
#-- We then check each bullet to see if it has dissapeared off the top of the screen.
#-- And if it has we remove it from bullets (the group) 
"""

"""
# LIMITING NUMBER OF BULLETS

#-- Now when the player presses the spacebar, we first check the lenght(number) of the bullets.
#-- If len(self.bullets) is less than 5, we create or can shoot a new bullet.
#-- But if 5 bullets already exist, nothing will happen when spacebar is pressed.
"""

"""
# CREATING THE _update_bullets() METHOD

#-- We create a new method called _update_bullets() and call the method in the _run_game() just after
# the _update screen()
#-- The code for _update_bullets() is cut and pasted from the run_game(), all we've done is clarify the
# comments.
#-- The while loop in run_game() looks simple again.

#-- Now the main loop in run_game() checks for player input, and then updates the position of the ship
# and any bullets fired. Then we use the updated positions to draw a new screen.
"""
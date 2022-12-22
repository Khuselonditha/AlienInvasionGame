import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        
        self._check_bullets_aliens_collisions()

    
    def _check_bullets_aliens_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
                
        if not self.aliens:
            # Destroy existing bullets and create new alien fleet.
            self.bullets.empty()
            self._create_fleet()


    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Make an alien and find the number of aliens in a row
        # Spacig between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                    (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)                                    

        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond appropristely if any aliens have reaches an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    
    def _update_aliens(self):
        """
        Check if the fleet is at the edge,
        then update the position of all the aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        
    def _update_screen(self):
        """Update images o the screen ad flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

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

"""
# CREATING AN INSTANCE OF ALIEN

# -- We first import Alien
#-- Then update the __init__() method, we create a group to hold the fleet of aliens, and make 
# a method that we'll call in this method call _create_fleet()

#-- In the _create_fleet() method, we create an instance of Alien, and then add it to the group that
# will hold the fleet
# The alien by default will be placed in the upper-left of the screen, perfet for the first alien.

#-- To make the alien appear, we call the groups's draw() method in the update_screen() method
#-- When we call the draw() on a group, pygame draws each element at the position defined by its rect
# position
#-- The draw() method takes one argument, the surface on which to draw the element of the group, 
# in our case the screen
"""

"""
# BUILDING AN ALIEN FLEET 

1. Determining how many aliens fit in a row (Calculation)
#-- To figure how many aliens fit in  row, wee look at how much horizontal space we have.
#-- The screen width is stored in settings.screen_width, but we need an empty margin on either side
# of the screen.
#-- We'll make this margin the width of one alien, because we have 2 margins the available space for
# aliens is the screen width minus 2 alien widths.

#-- We also need to set spacing between aliens, we'll make this space one alien width.
#-- The space needed to display the one alien is twice its width: One width for the alien, one width
# for the empty space to its right.
#-- To fid the number of aliens to fit the across the screen, we devide the available space by 2 times
# the width of the alien.
#-- We use floor(//) division which divides the two numbers and leaves any remainder, so we get an
# integer number of the aliens.

2. Creating a row of aliens
#-- We ned to know the width and height of the alien, so we create an instance of alien first before
# adding the calculations.
#-- We get the aliens width from its rect attribute and store the value in alien_width.
#-- We then calculate the horizontal space for the aliens and the number of aliens that will fit in
# that space

#-- Next we create a loop that counts form 0 to the number of aliens that need to fit into the space
# we calculated before.
#-- In the main body of the loop, we create an instance of alien, and set its x-coordinates value to
# place it in the row.
#-- Each alien is pushed to the right one alien width from the left margin.
#-- Then we multiply the alien width by 2 alien widths to account for the space one alien takes up
# including the space to its right and we multipl that amount by the alien's position in the row
#-- We the use the alien's x attribute to set its rect position, then we add the new alien to the 
# group aliens.

Running the game will show that the row is offset to the left, which is good since we want our fleet
to move to the right until it reaches the edge of the screen then drop down. instead of dump moving
down.
"""

"""
# REFACTORING _create_fleet()

#-- The method _create_alien() requires one parameter in addition to self: the position number of the
# lien being created.
#-- We still use the same body we used fo _create_fleet(), but we get the width of the alien inside
# the method instead of passingit as an argument
"""

"""
# ADDING ROWS

#-- First we'll want to determine the number of rows that fit onto the screen then repeat the loop
# for creating aliens in one row until we have the correct number of rows.
#-- To determine the number of rows, we find the available vertical space by subtracting the alien
# height from the top, the ships height from the bottom and alien heights from the bottom of the 
# screen.
#-- This will ccreate some empty space above the ship, so the player has time to start shooting at 
# the aliens at the beggining of each level.

#-- Each row needs some space below it, which will makae it equal to the height of an alien.
#-- To find the number of rows, we devide the available space by 2 times the height of an alien.
#-- We use floor division because we can only make an integer amount of rows. 


#-- We need the width and height of an alien, so we use the attribute size, which contains a tuple
# with the width and height of a rect object.
#-- To calculate the number of rows we can fit to the screen, we write our available_space_y calculation
# right after the calculation of available_space_x
#-- To create multiple rows, we use to nested loops: one outer and inner loop
#-- The inner loop creates the aliens in one row, the outer loop counts from 0 to the number of rows
# we want
#-- Now when we call _create_alien() we include the argument for the row number, s that more rows can 
# be placed further down the screen
#-- The definiton of _create_alien() needs a parameter to hold the row number
#-- Within the create_alien() method we change the aliens y-coordinates value when it is not in the
# first row by starting with one alien's height to create an empty space at the top of the screen
#-- Each row starts two alien height after the previous row, so we multiply the alien height by 2 and 
# then by the row number.
#-- The first row is number 0, so the vertical placement of the first row is unchanged, all other following
# rows are placed further down the screen
"""

"""
# MOVING THE ALIEN TO THE RIGHT

#-- In the main while loop, we already have calls to update the ship and bullet positions, Now we 
# Add the call to update the position of the alien's aswell

#-- We create a new method called _update_aliens to manage the movement of the fleet
#-- We use the _update_aliens() method to call the update() method in the alien.py
#-- We place the _update_aliens() method between the _update_bullets() and _update_screen methods 
"""

"""
# DROPPING THE FLEET AND CHANGING DIRECTION

#-- In the _check_fleet_edges(), we loop through the fleet and call check_edges() on each alien.
#-- If check_edge() returns True, we know an alien is at the edge and the whole fleet needs to change
# direction, so we call _change_fleet_direction() and break out of the loop.
#-- In _change _fleet_direction(), we loop through all the aliens and drop each one using the setting
# fleet_drop_speed()
#-- We then change the value of fleet_direction by multiplying its current value by -1
#-- The line that changes the direction isn't part of the for loop, we want to change each alien's
# vertical position, but we only want to change the direction of the fleet once.

#-- We then modify the the _update_aliens() method by calling _check_fleet_edges() before updating
# each alien's position.
"""

"""
 SHOOTING ALIENS

# DETECTING BULLET COLLISIONS

#-- The new code we added compares the position of all the bullets in self.bullets and all the aliens
# in self.aliens, and identifies any that overlap.
#-- Whenever the rect of a bullet and alien overlap, groupcollide() adds a key_value pair to the
# dictionary it returns.
#-- The two True arguments tell pygame to delete the bullets and aliens that have collided.

NB. To create a super bullet that can destroy all the aliens it collides with until it reaches the
#   top of the screen, set the first boolean to False and keep the second one as True.
"""

"""
# REPOPULATING THE FLEET

#-- We first check whether the aliens group is empty. An empty group evaluates to False, a simple way
# to check whether the group is empty.
#-- If it is we get rid of any existig bullets using the empty() method, whic removes all the remaining
# sprites of a group.
#-- we also call _create_fleet(), which fills the screen with aliens again.
"""

"""
# REFRACTORING _Update_bullets()

#-- The code that deals with bullets and alien collisions was moved to the _check_bullet_alien_collision()
# method.
#-- This keeps the _update_bullets() method from being too long and simplified.
"""
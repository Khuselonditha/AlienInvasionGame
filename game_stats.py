class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statisctics."""
        self.settings = ai_game.settings
        self.reset_stats()

    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit





"""
# RESPONDING TO ALIEN AND SHIP COLLISIONS

#-- Now we need to figure out what happens when an alien collides with a ship.
#-- Instead of destroying the ship's instance and creating a new one, we'll count how many times the
# ship has been hit by tracking the statistics for the game.

# we first create a games_stats.py file, we'll then make one GameStats instance for the etire time
# Alien Invasion is running.
#-- We'l also need to reset some statistics each time a player restarts the game.
#-- We will initialize the statistics in reset_game() method instead of the __ini__()
#-- We'll then call this method from the __init__() method anythime a player restarts the game.
#-- For now we hav only one statistic, ship_left which has a value that changes through out the game
#-- The number of ships the player starts with is stored in the settings.py file.
"""
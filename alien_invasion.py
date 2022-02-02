#!/usr/bin/python3
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage Game assets and behaviors."""
    def __init__(self):
        """Initialize the dame and create game resources."""
        
        pygame.init()
        self.settings=Settings()
        
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")
        # Creating the Ship or i should say     
            
        self.ship=Ship(self)
        
      
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            
            self._check_events()
            
            self._update_screen()
        
    def _check_events(self):
        # This is a helper method , they all start with _
        #Whatch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        """Update Images ON the screen, and flip to the new Screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) 
        
        self.ship.blitme()
        #Make the most recently Drawn screen visible    
        pygame.display.flip()

if __name__=="__main__":
    #Make a game instance and run the game
    ai=AlienInvasion()
    ai.run_game()
        
        
        
        
        
        
        
        
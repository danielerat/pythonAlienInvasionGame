#!/usr/bin/python3
import sys
import pygame
class AlienInvasion:
    """Overall Class to manage Game assets and behaviors."""
    def __init__(self):
        """Initialize the dame and create game resources."""
        pygame.init()
        
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Whatch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Make the most recently Drawn screen visible    
            pygame.display.flip()


if __name__=="__main__":
    #Make a game instance and run the game
    print("LEt's Rock")
    ai=AlienInvasion()
    ai.run_game()
        
        
        
        
        
        
        
        
import pygame
import sys

class AlienInvasion:
    """The over all class to manage game assests and behavior"""

    def __init__self(self):
        """Initialize the game , and creats game resources """
        
        self.bg_color = (230,230,230)


    def run_game(self):
        """Start the main loop for the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        while True:
            # watching for the keyboard event 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            self.screen.fill(self.bg_color)
            # make ethe most recently drawn screen visible 
            pygame.display.flip()





if __name__ == "__main__":
    #making a game instance , and running the game 
    ai = AlienInvasion()
    ai.run_game()

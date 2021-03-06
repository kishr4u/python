import pygame
import sys
from settings import Settings

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings= Settings()
        
        #dimensions of game window displayed
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        
        #set background color of screen that is opened
        self.bg_color=(230,230,230)

    def run_game(self):
        #main loop for the game
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            #make the recently drawn screen visible.        
            pygame.display.flip()            
if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()
        
        
    
        


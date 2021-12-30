import pygame

class Ship:
    
    def __init__(self, ai_game):
        #ai_game here is alien invasion class..
        self.screen= ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()
        #returns surface representing ship
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #here we are placing ship in midbotton of alien invasion rect, which is whole surface
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    
        
        
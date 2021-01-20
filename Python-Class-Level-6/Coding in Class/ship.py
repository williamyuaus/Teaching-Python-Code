import pygame
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/cannon2.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.rect.x += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)


import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Initializing Sprite attributes
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, (0, 0, width, height))

        self.rect = self.image.get_rect()
     
    # Moving the paddle to left, with 0 as limit
    def move_left(self, pixels):
        self.rect.x = max(0, self.rect.x - pixels)
    
    # Moving the paddle to right, with 700 as limit
    def move_right(self, pixels):
        self.rect.x = min(self.rect.x + pixels, 700)
import pygame

from random import randint

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Initializing Sprite attributes
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, (0, 0, width, height))
        
        # Initializing with random velocity
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()
    
    # Updating position
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    # Changing direction and new random velocity for Y-axis
    def collision(self):
        self.velocity[0] *= -1
        self.velocity[1] = randint(-8, 8)
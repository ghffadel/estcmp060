import pygame, sys


class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = [
            pygame.image.load("assets/mario_%d.png" % i) for i in range(4)
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.is_jumping = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def jump(self):
        self.is_jumping = True

    def update(self, speed):
        if self.is_jumping:
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.is_jumping = False

        self.image = self.sprites[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()

width = height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario jumping")

sprites = pygame.sprite.Group()
mario = Mario(175, 160)
sprites.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            mario.jump()

    screen.fill((0, 0, 0))
    sprites.draw(screen)
    sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)

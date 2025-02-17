import pygame

class Rubik(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Rubik.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def draw(self, screen):
        #screen.blit(self.image, self.rect)
        pass

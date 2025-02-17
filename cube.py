import pygame

class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 100
        self.pos = [100, 100]
        self.rect = pygame.Rect(self.pos, (self.size, self.size))

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)
    
    def move_right(self):
        if self.rect.right < 600:
            self.rect.centerx += 20
        
    def move_left(self):
        if self.rect.left > 0:
            self.rect.centerx -= 20
    
    def move_down(self):
        if self.rect.bottom < 400:
            self.rect.centery += 20
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.centery -= 20

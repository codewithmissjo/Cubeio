import pygame
import random

colors = ["red", "yellow", "blue", "green"]

class Cube(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.size = 10
        self.pos = pos
        self.c = random.randint(0, len(colors) - 1)
        self.rect = pygame.Rect(self.pos, (self.size, self.size))
        self.COOLDOWN = 30
        self.cooldown = self.COOLDOWN

    def draw(self, screen):
        pygame.draw.rect(screen, colors[self.c], self.rect)

    def boop(self):
        if self.cooldown < 0:
            self.c += 1
            if self.c == len(colors):
                self.c = 0
            self.cooldown = self.COOLDOWN
        else:
            self.cooldown -= 1
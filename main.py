import sys
import pygame
from pygame.locals import *
from cube import Cube
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

rubikvar = pygame.sprite.Group()

gamerunning = True

score = 0

def init():
    # create multiple rubiks
    for r in range(20):
        rubikvar.add(Cube((random.randint(15, 585), random.randint(15, 385))))

def main():
    global score, gamerunning

    # init things
    init()

    # pygame loop
    while gamerunning:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # update stuff
        screen.fill("black")
        for r in rubikvar.sprites():
            r.boop()
            r.draw(screen)

        # the last thing in your loop
        pygame.display.flip()

main()
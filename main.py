import sys
import pygame
from pygame.locals import *
from cube import Cube
from player import Rubik
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

cubegroup = pygame.sprite.GroupSingle()
rubikvar = pygame.sprite.Group()

gamerunning = True

score = 0

def init():
    # create multiple rubiks
    for r in range(10):
        rubikvar.add(Rubik(random.randint(15, 585), random.randint(15, 385)))

def main():
    global score, gamerunning

    # init things
    init()
    # local variables
    cubevar = Cube()
    cubegroup.add(cubevar)

    # pygame loop
    while gamerunning:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # key or mouse events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            cubevar.move_right()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            cubevar.move_left()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            cubevar.move_up()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            cubevar.move_down()

        # update stuff
        
        # collisions!
        hit_list = pygame.sprite.groupcollide(cubegroup, rubikvar, False, True)
        if len(hit_list) > 0:
            score += 1
        if len(rubikvar) < 1:
            init()
        if score > 200:
            gamerunning = False
        
        # draw stuff
        screen.fill("lime")
        pygame.draw.rect(screen, "navy", Rect(0, 0, 600, 200))
        cubevar.draw(screen)
        rubikvar.draw(screen)

        # the last thing in your loop
        pygame.display.flip()

main()

# 1. define the class
# 2. import the class
# 3. create the object
# 4. draw the object
# 5. change the object

'''
Todo!
Text
'''

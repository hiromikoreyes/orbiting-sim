import pygame
import simulation
import numpy as np
import time
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

#constants



#objects in simulation

thingy1 = simulation.Body(5000, (1920//2 + 200, 1080//2 + 200), (0,0), (0,0))
thingy2 = simulation.Body(5000, (1920//2,1080//2), (0,0), (0,0))
List = simulation.BodyList([thingy2])

for i in range(100):
    List.objects.append(simulation.Body(random.randint(1,10), (1920//2 + random.randint(-200,200),1080//2 + random.randint(-200,200)), (5,0), (0, 0)))
    # objects.append(simulation.Body(1, (1920//2 - 200 ,1080//2 + 200), (0.5, 0.5), (0, 0)))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            List.objects.append(simulation.Body(1, (pos[0],pos[1]), (1, 0),(0,0)))
            

    #logical stuff
    screen.fill("white")

    

    #rendering stuff
    for body in List.objects:

        List.removedFlagged()
        pygame.draw.circle(screen, (0,0,0), (body.pos[0], body.pos[1]), body.radius)
        body.updateVelocity(1)
        body.updatePosition(1)

        # For when we want wacky things to happen
        # if body.pos_x > 1920:
        #     body.pos_x = 0
        # elif body.pos_x < 0:
        #     body.pos_x = 1920
        # if body.pos_y > 1080:
        #     body.pos_y = 0
        # elif body.pos_y < 0:
        #     body.pos_y = 1080


        #orbiting physics calculation
        body.acc[0] = 0
        body.acc[1] = 0
        for body_alt in List.objects:
            if body_alt is not body:
                body.collide(body_alt)
                body.gravity(body_alt)

        


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
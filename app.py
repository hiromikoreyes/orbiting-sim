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
frame_count = 0


#objects in simulation

# thingy1 = simulation.Body(5000, (1920//2 + 200, 1080//2 + 200), (0,0), (0,0))
thingy2 = simulation.Body(500, (1920//2,1080//2), (0,0), (0,0))
List = simulation.BodyList([thingy2])

for i in range(20):
    List.objects.append(simulation.Body(random.randint(1,10), (1920//2 + random.randint(-200,200),1080//2 + random.randint(-200,200)), (random.randint(-5,5),random.randint(-5,5)), (0, 0)))
    # objects.append(simulation.Body(1, (1920//2 - 200 ,1080//2 + 200), (0.5, 0.5), (0, 0)))





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            List.objects.append(simulation.Body(10, (pos[0],pos[1]), (-5, 0),(0,0)))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            List.updateGlobal((-2, 0), (0,0), (0,0))
        if keys[pygame.K_w]:
            List.updateGlobal((0, -2), (0,0), (0,0))
        if keys[pygame.K_d]:
            List.updateGlobal((2, 0), (0,0), (0,0))
        if keys[pygame.K_s]:
            List.updateGlobal((0, 2), (0,0), (0,0))


                

            
    #Count Frames
    frame_count += 1
    if frame_count == 60:
        screen.fill("black")
        frame_count = 0
    screen.fill("black")

    #Body Render + Logic
    for body in List.objects:
        List.removedFlagged()
        body.renderTrail(screen)
        pygame.draw.circle(screen, (255,0,0), (round(body.pos[0]), round(body.pos[1])), body.radius)
        body.updateVelocity(1)
        body.updatePosition(1)
        body.acc[0] = 0
        body.acc[1] = 0
        for body_alt in List.objects:
            if body_alt is not body:
                body.collide(body_alt)
                body.gravity(body_alt)
    
    #Trail Render



        


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
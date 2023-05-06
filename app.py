import pygame
import simulation
import numpy as np
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

#constants
pi = 3.1415
G = 0.06 #making it up


#objects in simulation


thingy = simulation.Body(10, (100, 100), (0,0), (0,0))
thingy2 = simulation.Body(100, (1920//2,1080//2), (0,0), (0,0))
objects = [thingy, thingy2]
# for i in range(100):
#     objects.append(simulation.Body(3, (i,i), (random.randint(-2,2), random.randint(-2,2)), (0,0)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #logical stuff

    screen.fill("black")

    

    #rendering stuff
    for body in objects:
        radius = np.cbrt(4 * body.mass / 3 * pi) 
        pygame.draw.circle(screen, (255,255,255), (body.pos_x, body.pos_y), radius)
        
        #Update position each frame
        body.pos_x += body.vel_x
        body.pos_y += body.vel_y

        # For when we want wacky things to happen
        # if not 0 < body.pos_x < 1920:
        #     body.pos_x = 0
        # if not 0 < body.pos_y < 1920:
        #     body.pos_y = 0

        #orbiting physics calculation
        for body_alt in objects:
            if body_alt is not body:
                body.gravity(body_alt)


                    

        #collision calculation

        #Update velocity each frame
        body.vel_x += body.acc_x  
        body.vel_y += body.acc_y
        #we need a way to calculate acceleration :DDD
        
            

        



    pygame.display.flip()

    clock.tick(120)

pygame.quit()
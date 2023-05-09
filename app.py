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



#objects in simulation

# thingy1 = simulation.Body(3000, (1920//2 - 300, 1080//2), (0,0), (0,0))
thingy2 = simulation.Body(3000, (1920//2,1080//2), (0,0), (0,0))
List = simulation.BodyList([thingy2])

# for i in range(100):
    # List.objects.append(simulation.Body(random.randint(1,10), (1920//2 + random.randint(-200,200),1080//2 + random.randint(-200,200)), (1,-0.5), (0, 0)))
    # objects.append(simulation.Body(1, (1920//2 - 200 ,1080//2 + 200), (0.5, 0.5), (0, 0)))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            List.objects.append(simulation.Body(random.randint(1,10), (pos[0],pos[1]), (random.randint(-1,1),random.randint(-1,1)),(0,0)))
            

    #logical stuff
    screen.fill("black")

    

    #rendering stuff
    for body in List.objects:


        
        pygame.draw.circle(screen, (255 - 4 * (np.log2(body.mass)), 255 - 4 * np.log2(body.mass) ,255), (body.pos_x, body.pos_y), body.radius)
        
        #Update position each frame


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
        for body_alt in List.objects:
            if body_alt is not body:
                body.collide(List.objects, body_alt)
                if(body_alt != None): body.gravity(screen, body_alt)


                    
        body.pos_x += body.vel_x
        body.pos_y += body.vel_y
        body.vel_x += body.acc_x  
        body.vel_y += body.acc_y
        thingy2.pos_x = 1920//2
        thingy2.pos_y = 1080//2

        # print(body.acc_x)
    pygame.display.flip()

    clock.tick(120)

pygame.quit()
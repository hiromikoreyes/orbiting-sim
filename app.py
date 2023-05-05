import pygame
import simulation
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

#constants
pi = 3.1415
G = 0.06 #making it up


#objects in simulation



thingy = simulation.Body(5, (100,0), (0,0), (0,0))
thingy2 = simulation.Body(100, (500,500), (0,0), (0,0))
objects = [thingy, thingy2]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #logical stuff

    screen.fill("white")

    

    #rendering stuff
    for body in objects:
        radius = body.mass / 2 * pi
        pygame.draw.circle(screen, (25,0,25), (body.pos_x, body.pos_y), radius)
        body.pos_x += body.vel_x
        body.pos_y += body.vel_y  

        #orbiting physics calculation
        for body_alt in objects:
            if(body_alt is not body):
                dist_x = body_alt.pos_x - body.pos_x
                dist_y = body_alt.pos_y - body.pos_y
                dist = math.sqrt((dist_x)**2 + (dist_y)**2)
                accel = (G * body_alt.mass) / (dist ** 2)
                theta = math.atan(dist_x/dist_y)
                accel_x = math.sin(theta) * accel
                accel_y = math.cos(theta) * accel
                body.acc_x += accel_x
                body.acc_y += accel_y

        #collision calculation



        body.vel_x += body.acc_x  
        body.vel_y += body.acc_y


        #we need a way to calculate acceleration :DDD
        
            

        



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
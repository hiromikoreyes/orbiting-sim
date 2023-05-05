import pygame
import simulation

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


#Body
thingy = simulation.Body(10, (50,50), (1,0), (0,0))
objects = [thingy]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #logical stuff

    screen.fill("white")

    #rendering stuff
    for item in objects:
        pygame.draw.circle(screen, (0,0,0), (item.pos_x, item.pos_y), item.mass)
        item.pos_x += item.vel_x
        item.pos_y += item.vel_y

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
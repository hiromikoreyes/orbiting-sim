import numpy as np
import pygame as pg 
G = 0.0006 #making it up

class Body:
    def __init__(self, mass: float, pos: tuple[float], vel: tuple[float], acc: tuple[float]):
        self.mass = mass
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.acc_x = acc[0]
        self.acc_y = acc[1]

    def collision(self, body_alt):
        print("bodies collided!!!!")

    def __get_angle(self, body_alt, displ_x, displ_y):
        """ Returns the angle between two bodies, from the point of reference of self """

        if(displ_x == 0 and displ_y > 0):
            return np.pi / 2
        elif(displ_x == 0 and displ_y < 0):
            return -np.pi / 2

        theta = np.arctan(displ_y/displ_x)
        

        if(displ_x > 0 and displ_y > 0): #body_alt is north east to self
            return theta
        elif(displ_x < 0 and displ_y > 0): #body_alt is north west to self
            return np.pi - theta
        elif(displ_x < 0 and displ_y < 0):  #body_alt is south west to self
            return np.pi + theta
        elif(displ_x > 0 and displ_y < 0): #body_alt is south east to self
            return 2 * np.pi - theta
        

    def gravity(self, surface, body_alt):
        """ Calculates then modifies self.acc_x, self.acc_y based on physics calculation """
        displ_x = body_alt.pos_x - self.pos_x
        displ_y = body_alt.pos_y - self.pos_y
        displ = np.sqrt(displ_x ** 2 + displ_y ** 2)
        
        accel = (G * body_alt.mass) / (displ_x ** 2 + displ_y ** 2)
        theta = self.__get_angle(body_alt, displ_x, displ_y)

        if(self.mass == 10):
            x_prime = (self.pos_x * np.cos(theta) - self.pos_y * np.sin(theta))
            y_prime = (self.pos_x * np.sin(theta) + self.pos_y * np.cos(theta))
            # pg.draw.line(surface, (255,0,0), (self.pos_x, self.pos_y), (x_prime, y_prime))
            pg.draw.line(surface, (0,255,0), (self.pos_x, self.pos_y), (body_alt.pos_x, body_alt.pos_y))
            pg.draw.line(surface, (0,255,0), (self.pos_x, self.pos_y), (self.pos_x, body_alt.pos_y))
            pg.draw.line(surface, (0,255,0), (body_alt.pos_x, body_alt.pos_y), (self.pos_x, body_alt.pos_y))




            print((theta * 180)/ np.pi)

        self.acc_x += np.cos(theta) * accel
        self.acc_y += np.sin(theta) * accel
        


        
        
    


        

        






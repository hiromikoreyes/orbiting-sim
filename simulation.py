import numpy as np
import pygame as pg 
G = 0.6 #making it up



class BodyList:
    def __init__(self, objects):
        self.objects = objects


class Body:
    def __init__(self, mass: float, pos: tuple[float], vel: tuple[float], acc: tuple[float]):
        self.mass = mass
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.acc_x = acc[0]
        self.acc_y = acc[1]
        self.radius = np.cbrt(4 * self.mass / 3 * np.pi)


    def collide(self, List, body_alt):
        displ_x = body_alt.pos_x - self.pos_x
        displ_y = body_alt.pos_y - self.pos_y
        bounds = max(self.radius, body_alt.radius)
        
        if np.sqrt(displ_x ** 2 + displ_y ** 2) < bounds:
            if self.mass >= body_alt.mass:
                mass_coeff = body_alt.mass/self.mass
                self.acc_x += mass_coeff * body_alt.acc_x
                self.acc_y += mass_coeff * body_alt.acc_y
                self.vel_x += mass_coeff * body_alt.vel_x
                self.vel_y += mass_coeff * body_alt.vel_y
                self.mass += body_alt.mass
                List.remove(body_alt)
            else:
                mass_coeff = self.mass/body_alt.mass
                body_alt.acc_x += mass_coeff * self.acc_x
                body_alt.acc_y += mass_coeff * self.acc_y
                body_alt.vel_x += mass_coeff * self.vel_x
                body_alt.vel_y += mass_coeff * self.vel_y
                body_alt.mass += self.mass
                List.remove(self)


    def gravity(self, surface, body_alt):
        """ Calculates then modifies self.acc_x, self.acc_y based on physics calculation """
        displ_x = body_alt.pos_x - self.pos_x
        displ_y = body_alt.pos_y - self.pos_y
        displ = np.sqrt(displ_x ** 2 + displ_y ** 2)
        soft_cap = 2000
        accel = (G * body_alt.mass) / np.sqrt((displ_x ** 2 + displ_y ** 2) ** 2 + soft_cap) 

        if(displ_x > 0 and displ_y < 0): #body_alt is north east to self
            theta = np.arctan(-displ_y/displ_x)
            self.acc_x += np.cos(theta) * accel
            self.acc_y -= np.sin(theta) * accel
        elif(displ_x < 0 and displ_y < 0): #body_alt is north west to self
            theta = np.pi - np.arctan(displ_y/displ_x)
            self.acc_x += np.cos(theta) * accel
            self.acc_y -= np.sin(theta) * accel
        elif(displ_x < 0 and displ_y > 0):  #body_alt is south west to self
            theta = np.pi - np.arctan(displ_y/-displ_x)
            self.acc_x += np.cos(theta) * accel
            self.acc_y += np.sin(theta) * accel
        elif(displ_x > 0 and displ_y > 0): #body_alt is south east to self
            theta = 2 * np.pi - np.arctan(displ_y/displ_x)
            self.acc_x += np.cos(theta) * accel
            self.acc_y -= np.sin(theta) * accel

        if(displ_y == 0 and displ_x > 0):
            theta = 0
            self.acc_x += accel
        elif(displ_y == 0 and displ_x < 0):
            theta = np.pi
            self.acc_x -= accel
        elif(displ_x == 0 and displ_y > 0):
            theta = np.pi/2
            self.acc_y += accel
        elif(displ_x == 0 and displ_y < 0):
            theta = 3 * np.pi/2
            self.acc_y -= accel 

        self.vel_x += self.acc_x 
        self.vel_y += self.acc_y

        if(self.mass == 1 ):
            
            x_prime = 50 * np.cos(theta) + self.pos_x
            y_prime = -50 * np.sin(theta) + self.pos_y
            if(displ_x < 0 and displ_y > 0):
                y_prime = 50 * np.sin(theta) + self.pos_y

            # pg.draw.line(surface, (255,0,0), (1920//2, 1080//2), (10000 * self.acc_x, 10000 * self.acc_y))
            if(0 < self.mass < 200 and body_alt.mass > 2000): pg.draw.line(surface, (0,255,0), (self.pos_x, self.pos_y), (x_prime, y_prime))
            print("-------------------")
            print(self.acc_x, self.acc_y)
            print(self.vel_x, self.vel_y)
            print(self.pos_x, self.pos_y)

            # pg.draw.line(surface, (0,255,0), (body_alt.pos_x, body_alt.pos_y), (self.pos_x, self.pos_y))
            

    def updatePosition(self, time_step):
        self.pos_x += self.vel_x * time_step
        self.pos_y += self.vel_y * time_step
        

        






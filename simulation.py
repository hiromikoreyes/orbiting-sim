import numpy as np
import pygame as pg 
G = 6 #making it up



class BodyList:
    def __init__(self, objects):
        self.objects = objects

    def updateGlobal(self, delta_pos, delta_vel, delta_acc):
        delta_pos = np.array(delta_pos)
        delta_vel = np.array(delta_vel)
        delta_acc = np.array(delta_acc)

        for body in self.objects:
            for i in range(len(body.prev_pos)):
                body.prev_pos[i] += delta_pos
            body.pos += delta_pos
            body.vel += delta_vel
            body.acc += delta_acc

    def removedFlagged(self):
        for body in self.objects:
            if body.deletion_flag:
                self.objects.remove(body)


class Body:
    def __init__(self, mass: float, pos: tuple[float], vel: tuple[float], acc: tuple[float]):
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.acc = np.array(acc, dtype=float)
        self.radius = np.cbrt(4 * self.mass / 3 * np.pi)
        self.prev_pos = []
        self.deletion_flag = False

    def collide(self, body_alt):
        displ = body_alt.pos - self.pos
        max_radius = max(self.radius, body_alt.radius)
        if np.linalg.norm(displ) < max_radius:
            if self.mass >= body_alt.mass:
                mass_coeff = body_alt.mass/self.mass
                self.acc += mass_coeff * body_alt.acc
                self.vel += mass_coeff * body_alt.vel
                self.mass += body_alt.mass
                body_alt.deletion_flag = True
            else:
                mass_coeff = self.mass/body_alt.mass
                body_alt.acc += mass_coeff * self.acc
                body_alt.vel += mass_coeff * self.vel
                body_alt.mass += self.mass
                self.deletion_flag = True

    def gravity(self, body_alt):
        displ = body_alt.pos - self.pos
        accel = (G * body_alt.mass) / (np.linalg.norm(displ) ** 2 + 100)
        angle = np.arctan2(displ[1], displ[0])
        self.acc[0] += np.cos(angle) * accel
        self.acc[1] += np.sin(angle) * accel
    

    def updateVelocity(self, time_step):
        self.vel += self.acc * time_step


    def updatePosition(self, time_step):
        self.prev_pos.append((round(self.pos[0]), round(self.pos[1])))
        self.pos += self.vel * time_step
        if(len(self.prev_pos) > 10):
            self.prev_pos.pop(0)


    def renderTrail(self, display):
        if len(self.prev_pos) > 1: pg.draw.line(display, (255,0,255), self.pos, self.prev_pos[len(self.prev_pos)-1])
        for i in range(1, len(self.prev_pos)-1):
            pg.draw.line(display, (255,255,255), self.prev_pos[i], self.prev_pos[i+1])

            
    


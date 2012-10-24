"""
A Pygame toy where the eight home row keys map to musical notes and points 
on the screen. 
Copyright (C) 2012 James Heslin

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import pygame
import random
from pygame.locals import *

from particle import Particle

class Burst():

    def __init__(self, x, y, colour, count, sound):
        self.x = x
        self.y = y
        self.colour = colour
        self.count = count
        self.sound = sound
        self.particles = []
        self.particles.append(Particle(self.x, self.y, 5, self.colour))

    def update(self):
        self.particles.append(Particle(random.randint(1, 30) + self.x, 
            random.randint(1, 30) + self.y, 2, self.colour))    
        self.y += random.randint(-50, 50)
        self.x += random.randint(-50, 50)
        modR = random.randint(-40, 40)
        modG = random.randint(-40, 40)
        modB = random.randint(-40, 40)
        if self.colour.r + modR <= 255 and self.colour.r + modR >=0:
            self.colour.r += modR
        if self.colour.g + modG <= 255 and self.colour.g + modG >=0:
            self.colour.g += modG
        if self.colour.b + modB <= 255 and self.colour.b + modB >=0:
            self.colour.b += modB

    def draw(self, screen):
        for p in self.particles:
            pygame.draw.rect(screen, p.colour, p.rect) 



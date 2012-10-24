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

notes = {}
channels = {}
clock = pygame.time.Clock()
screen = None

class Particle():

    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


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

    def draw(self):
        global screen
        for p in self.particles:
            pygame.draw.rect(screen, p.colour, p.rect) 

class Canvas():
    
    def __init__(self):
        self.bursts = []

    def update(self):
        global screen, notes, channels
        #print "Updating canvas"
        for b in self.bursts:
            if b.count < 15:
                b.update()
                b.draw()
                b.count += 1
            else:
                self.bursts.remove(b)
            
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    raise SystemExit
                if e.key == K_a:
                    self.bursts.append(Burst(30, 80, pygame.Color(0, 0, 128), 0, 
                        notes['c']))
                    #if notes['c'].get_num_channels() > 0:
                        #notes['c'].stop()
                    channels['c_chan'].play(notes['c'])
                    #print "C"

                elif e.key == K_s:
                    self.bursts.append(Burst(110, 80, pygame.Color(0, 0, 255), 0, 
                        notes['d']))
                    channels['d_chan'].play(notes['d'])
                    #print "D"
                elif e.key == K_d:
                    self.bursts.append(Burst(190, 80, pygame.Color(0, 128, 0), 0, 
                        notes['e']))
                    channels['e_chan'].play(notes['e'])
                    #print "E"

                elif e.key == K_f:
                    self.bursts.append(Burst(270, 80, pygame.Color(0, 128, 128), 0, 
                        notes['f']))
                    channels['f_chan'].play(notes['f'])
                    #print "F"

                elif e.key == K_j:
                    self.bursts.append(Burst(350, 80, pygame.Color(0, 255, 0), 0,
                        notes['g']))
                    channels['g_chan'].play(notes['g'])
                    #print "G"

                elif e.key == K_k:
                    self.bursts.append(Burst(430, 80, pygame.Color(0, 255, 128), 0, 
                        notes['a']))
                    channels['a_chan'].play(notes['a'])
                    #print "A"

                elif e.key == K_l:
                    self.bursts.append(Burst(510, 80, pygame.Color(0, 255, 255), 0, 
                        notes['b']))
                    channels['b_chan'].play(notes['b'])
                    #print "B"

                elif e.key == K_SEMICOLON:
                    self.bursts.append(Burst(590, 80, pygame.Color(128, 0, 0), 0, 
                        notes['hc']))
                    channels['hc_chan'].play(notes['hc'])
                    #print "HC"
                elif e.key == K_SPACE:
                    print self.bursts
                    #for a in self.bursts:
                        #print a.colour
        

def main():
    global screen, notes, channels
    pygame.init()
    notes = {'c': pygame.mixer.Sound('note_c.ogg'), 
            'd': pygame.mixer.Sound('note_d.ogg'), 
            'e': pygame.mixer.Sound('note_e.ogg'), 
            'f': pygame.mixer.Sound('note_f.ogg'), 
            'g': pygame.mixer.Sound('note_g.ogg'), 
            'a': pygame.mixer.Sound('note_a.ogg'), 
            'b': pygame.mixer.Sound('note_b.ogg'),
            'hc': pygame.mixer.Sound('note_hc.ogg')}
    channels = {'c_chan': pygame.mixer.Channel(0), 
            'd_chan': pygame.mixer.Channel(1), 
            'e_chan': pygame.mixer.Channel(2), 
            'f_chan': pygame.mixer.Channel(3), 
            'g_chan': pygame.mixer.Channel(4), 
            'a_chan': pygame.mixer.Channel(5),
            'b_chan': pygame.mixer.Channel(6),
            'hc_chan':pygame.mixer.Channel(7)}
    for c in channels:
        channels[c].set_volume(0.2)
    screen = pygame.display.set_mode((640, 200))
    c = Canvas()
    while True:
        screen.fill((0, 0, 0))
        c.update()
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

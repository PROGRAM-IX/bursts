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

from burst import Burst
from particle import Particle

class Canvas():
    
    notes = {}
    channels = {}
    
    def __init__(self):
        self.bursts = []
        self.notes = {'c': pygame.mixer.Sound('note_c.ogg'), 
            'd': pygame.mixer.Sound('note_d.ogg'), 
            'e': pygame.mixer.Sound('note_e.ogg'), 
            'f': pygame.mixer.Sound('note_f.ogg'), 
            'g': pygame.mixer.Sound('note_g.ogg'), 
            'a': pygame.mixer.Sound('note_a.ogg'), 
            'b': pygame.mixer.Sound('note_b.ogg'),
            'hc': pygame.mixer.Sound('note_hc.ogg')}
        self.channels = {'c_chan': pygame.mixer.Channel(0), 
            'd_chan': pygame.mixer.Channel(1), 
            'e_chan': pygame.mixer.Channel(2), 
            'f_chan': pygame.mixer.Channel(3), 
            'g_chan': pygame.mixer.Channel(4), 
            'a_chan': pygame.mixer.Channel(5),
            'b_chan': pygame.mixer.Channel(6),
            'hc_chan':pygame.mixer.Channel(7)}

    def update(self, screen):
        #print "Updating canvas"
        for b in self.bursts:
            if b.count < 15:
                b.update()
                b.draw(screen)
                b.count += 1
            else:
                self.bursts.remove(b)
            
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    raise SystemExit
                if e.key == K_a:
                    self.bursts.append(Burst(30, 80, pygame.Color(0, 0, 128), 0, 
                        self.notes['c']))
                    #if notes['c'].get_num_channels() > 0:
                        #notes['c'].stop()
                    self.channels['c_chan'].play(self.notes['c'])
                    #print "C"

                elif e.key == K_s:
                    self.bursts.append(Burst(110, 80, pygame.Color(0, 0, 255), 0, 
                        self.notes['d']))
                    self.channels['d_chan'].play(self.notes['d'])
                    #print "D"
                elif e.key == K_d:
                    self.bursts.append(Burst(190, 80, pygame.Color(0, 128, 0), 0, 
                        self.notes['e']))
                    self.channels['e_chan'].play(self.notes['e'])
                    #print "E"

                elif e.key == K_f:
                    self.bursts.append(Burst(270, 80, pygame.Color(0, 128, 128), 0, 
                        self.notes['f']))
                    self.channels['f_chan'].play(self.notes['f'])
                    #print "F"

                elif e.key == K_j:
                    self.bursts.append(Burst(350, 80, pygame.Color(0, 255, 0), 0,
                        self.notes['g']))
                    self.channels['g_chan'].play(self.notes['g'])
                    #print "G"

                elif e.key == K_k:
                    self.bursts.append(Burst(430, 80, pygame.Color(0, 255, 128), 0, 
                        self.notes['a']))
                    self.channels['a_chan'].play(self.notes['a'])
                    #print "A"

                elif e.key == K_l:
                    self.bursts.append(Burst(510, 80, pygame.Color(0, 255, 255), 0, 
                        self.notes['b']))
                    self.channels['b_chan'].play(self.notes['b'])
                    #print "B"

                elif e.key == K_SEMICOLON:
                    self.bursts.append(Burst(590, 80, pygame.Color(128, 0, 0), 0, 
                        self.notes['hc']))
                    self.channels['hc_chan'].play(self.notes['hc'])
                    #print "HC"
                elif e.key == K_SPACE:
                    print self.bursts
                    #for a in self.bursts:
                        #print a.colour
        

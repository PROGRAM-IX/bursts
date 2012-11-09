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

from canvas import Canvas
from burst import Burst
from particle import Particle

notes = {}
channels = {}
clock = pygame.time.Clock()
screen = None

def main():
    global screen
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=128)
    can = Canvas()
    for c in can.channels:
        can.channels[c].set_volume(0.1)
    screen = pygame.display.set_mode((640, 200))
    
    while True:
        screen.fill((0, 0, 0))
        can.update(screen)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

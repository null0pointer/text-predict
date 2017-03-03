import os
import sys
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))

rows, columns = os.popen('stty size', 'r').read().split()

x = 0
y = 0

def render():
    for row in range(int(rows)):
            for column in range(int(columns)):
                if row == y and column == x:
                    sys.stdout.write('.')
                else:
                    sys.stdout.write(' ')
    sys.stdout.flush()
        
while True:
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key <= 256:
                y += 1
            elif event.type == pygame.KEYUP and event.key <= 256:
                y -= 1
            elif event.type == pygame.KEYLEFT and event.key <= 256:
                x -= 1
            elif event.type == pygame.KEYRIGHT and event.key <= 256:
                x += 1
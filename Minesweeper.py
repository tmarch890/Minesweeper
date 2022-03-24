import pygame
from sys import exit
import random
import time

# make a 30x30 board
# 160 mines

board = [[0 for y in range(32)] for x in range(32)]

mine = 0
while mine <140:
    x = random.randint(1,30)
    y = random.randint(1,30)
    if board[x][y] != 9:
        board[x][y] = 9
    mine += 1

for x in range(1, 31):
    for y in range(1, 31):
        if board[x][y] != 9:
            for s in range(3):
                s -= 1
                for t in range(3):
                    t -= 1
                    if board[x+s][y+t] == 9:
                        board[x][y] += 1

# add border mine checks

coverstate = [[0 for y in range(30)] for x in range(30)]

pygame.init()
screen = pygame.display.set_mode((512,612))
pygame.display.set_caption('Minesweeeper')
clock = pygame.time.Clock()

screen.fill((219,219,219,255))
square = pygame.image.load('graphics/square.png').convert()
emptysquare =pygame.image.load('graphics/emptysquare.png').convert()
flag = pygame.image.load('graphics/flag.png').convert()
mine = pygame.image.load('graphics/mine.png').convert()
one = pygame.image.load('graphics/1.png').convert()
two = pygame.image.load('graphics/2.png').convert()
three = pygame.image.load('graphics/3.png').convert()
four = pygame.image.load('graphics/4.png').convert()
five = pygame.image.load('graphics/5.png').convert()
six = pygame.image.load('graphics/6.png').convert()
seven = pygame.image.load('graphics/7.png').convert()
eight = pygame.image.load('graphics/8.png').convert()
cursor = pygame.image.load('graphics/cursor.png').convert_alpha()

x_offset = 16
y_offset = 116

cursorx = x_offset
cursory = y_offset

x = 0
y = 0

while not(coverstate[x][y] == 1 and board[x+1][y+1] == 9):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and cursory > 116:
                cursory -= 16
            if event.key == pygame.K_DOWN and cursory < 580:
                cursory += 16
            if event.key == pygame.K_LEFT and cursorx > 16:
                cursorx -= 16
            if event.key == pygame.K_RIGHT and cursorx < 480:
                cursorx += 16
            if event.key == pygame.K_a:
                coverstate[int((cursorx-x_offset)/16)][int((cursory-y_offset)/16)] = 1
            if event.key == pygame.K_z:
                coverstate[int((cursorx-x_offset)/16)][int((cursory-y_offset)/16)] = 2

    for x in range(30):
        for y in range(30):
            if coverstate[x][y] == 0:
                screen.blit(square, (x*16 + x_offset, y*16 + y_offset))
            if coverstate[x][y] == 1:
                if board[x+1][y+1] == 0:
                    for s in range(3):
                        s -= 1
                        for t in range(3):
                            t -= 1
                            if (x+s) >= 0 and (x+s) <= 29 and (y+t) >= 0 and (y+t) <= 29:
                                coverstate[x+s][y+t] = 1
                    screen.blit(emptysquare, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 1:
                    screen.blit(one, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 2:
                    screen.blit(two, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 3:
                    screen.blit(three, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 4:
                    screen.blit(four, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 5:
                    screen.blit(five, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 6:
                    screen.blit(six, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 7:
                    screen.blit(seven, (x*16 + x_offset, y*16 + y_offset))
                if board[x+1][y+1] == 8:
                    screen.blit(eight, (x*16 + x_offset, y*16 + y_offset))
            if coverstate[x][y] == 2:
                screen.blit(flag, (x*16 + x_offset, y*16 + y_offset))

    screen.blit(cursor, (cursorx, cursory))

    x = int((cursorx-x_offset)/16)
    y = int((cursory-y_offset)/16)

    pygame.display.update()
    clock.tick(60)

if coverstate[x][y] == 1 and board[x+1][y+1] == 9:
    for x in range(30):
        for y in range(30):
            if board[x+1][y+1] == 9:
                screen.blit(mine, (x*16 + x_offset, y*16 + y_offset))
                pygame.display.update()
                time.sleep(.01)

time.sleep(10)

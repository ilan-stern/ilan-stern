import sys

import pygame

background_colour = (255,255,255)
BLACK = (0,0,0)
WHITE = (200,200,200)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

def main():
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.Fill(background_colour)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)





# Create window (size it too)
# Create grid
# Make centre number 1
# Make left number two
# spiral numbers
# If number is prime colour square white
# If number has 2 prime factors colour square light gray 2-almost prime
# If number has 3 prime factors colour square gray 3-almost prime
# If number has 4 prime factors colour square dark gray 4-almost prime

import pygame
import sys

# initializing pygame
pygame.init()

# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
SQUARE_SIZE = 200

#color
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)



screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )


def draw_lines():
	# first horizontal line
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# second horizontal line
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

	# first vertical line
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# second vertical line
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )


draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
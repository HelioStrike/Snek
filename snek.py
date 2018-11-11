import pygame, sys
from pygame.locals import *
import random
from math import floor

WINDOWWIDTH = 800
WINDOWHEIGHT = 640
FPS = 15

SNEKSIZE = 20
FOODSIZE = 30
MOVESPEED = 20

BLACK 	=	(  0,   0,   0)
WHITE 	= 	(255, 255, 255)
RED		=	(255,   0,   0)
GREEN 	=	(  0, 255,   0)
BLUE 	=	(  0,   0, 255)
CYAN	=	(  0, 255, 255)

SNEKCOLOR = GREEN

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('snek')


def main():
	direction = 'right'


	snek = []
	snekx = WINDOWWIDTH/2
	sneky = WINDOWHEIGHT/2

	snek.append([snekx, sneky])

	sneklen = 1
	score = 0

	foodx, foody = getFoodPos()

	gameStart()

	while True:
		drawMap()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.locals.KEYDOWN:
				if event.key == K_UP:
					direction = 'up'
				if event.key == K_RIGHT:
					direction = 'right'
				if event.key == K_DOWN:
					direction = 'down'
				if event.key == K_LEFT:
					direction = 'left'

		if(direction == 'right'):
			snekx += MOVESPEED
		elif(direction == 'down'):
			sneky += MOVESPEED
		elif(direction == 'left'):
			snekx -= MOVESPEED
		elif(direction == 'up'):
			sneky -= MOVESPEED

		if (snekx >= WINDOWWIDTH) or (snekx <= 0) or (sneky >= WINDOWWIDTH) or (sneky <= 0):
			gameOver(score)

		if([snekx, sneky] in snek):
			gameOver(score)

		snek.append([snekx, sneky])

		if(abs(foodx - snekx) < (FOODSIZE + SNEKSIZE)/2 and abs(foody - sneky) < (FOODSIZE + SNEKSIZE)/2):
			foodx, foody = getFoodPos()
			sneklen += 1
			score += 5

		pygame.draw.rect(DISPLAYSURF, RED, (foodx, foody, FOODSIZE, FOODSIZE))
		snek = snek[len(snek)-sneklen:]

		for x in snek:
			pygame.draw.rect(DISPLAYSURF, SNEKCOLOR, (x[0], x[1], SNEKSIZE, SNEKSIZE))

		displayScore(score)

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def gameStart():
	drawMap()

	titleFont = pygame.font.Font('freesansbold.ttf', 40)

	title = titleFont.render("SNEK", True, GREEN)
	titleRect = title.get_rect()
	titleRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)

	DISPLAYSURF.blit(title, titleRect)

	startTextFont = pygame.font.Font('freesansbold.ttf', 20)

	startText = startTextFont.render("Enter 'p' to play or 'q' to quit.", True, BLUE)
	startTextRect = startText.get_rect()
	startTextRect.center = (WINDOWWIDTH/2, 3*WINDOWHEIGHT/4)

	DISPLAYSURF.blit(startText, startTextRect)

	pygame.display.update()

	play = False

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.locals.KEYDOWN:
				if event.key == K_q:
					pygame.quit()
					sys.exit()
				if event.key == K_p:
					play = True
					
		if play:
			break

def gameOver(score):
	drawMap()

	overFont = pygame.font.Font('freesansbold.ttf', 40)

	over = overFont.render("GAME OVER", True, RED)
	overRect = over.get_rect()
	overRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/4)

	DISPLAYSURF.blit(over, overRect)

	titleFont = pygame.font.Font('freesansbold.ttf', 40)

	title = titleFont.render("SNEK", True, GREEN)
	titleRect = title.get_rect()
	titleRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)

	DISPLAYSURF.blit(title, titleRect)

	startTextFont = pygame.font.Font('freesansbold.ttf', 20)

	startText = startTextFont.render("Enter 'p' to get to game start screen or 'q' to quit.", True, BLUE)
	startTextRect = startText.get_rect()
	startTextRect.center = (WINDOWWIDTH/2, 3*WINDOWHEIGHT/4)

	DISPLAYSURF.blit(startText, startTextRect)

	displayScore(score)

	pygame.display.update()

	play = False

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.locals.KEYDOWN:
				if event.key == K_q:
					pygame.quit()
					sys.exit()
				if event.key == K_p:
					play = True
					
		if play:
			main()


def intersect(snekx, sneky, snek):
	return ([snekx, sneky] in snek[1:])

def displayScore(score):
	scoreFont = pygame.font.Font('freesansbold.ttf', 20)

	score = scoreFont.render("Score: " + str(score) , True, RED)
	scoreRect = score.get_rect()
	scoreRect.center = (WINDOWWIDTH/12, WINDOWHEIGHT/12)

	DISPLAYSURF.blit(score, scoreRect)


def getFoodPos():
	foodx = floor(random.randint(FOODSIZE/2, WINDOWWIDTH-(FOODSIZE/2)))
	foody = floor(random.randint(FOODSIZE/2, WINDOWHEIGHT-(FOODSIZE/2)))
	return foodx, foody

def drawMap():
	DISPLAYSURF.fill(BLACK)
	for x in range(WINDOWHEIGHT/SNEKSIZE):
		pygame.draw.line(DISPLAYSURF, BLUE, (0, SNEKSIZE*x), (WINDOWWIDTH, SNEKSIZE*x), 1)
	for y in range(WINDOWWIDTH/SNEKSIZE):
		pygame.draw.line(DISPLAYSURF, BLUE, (SNEKSIZE*y, 0), (SNEKSIZE*y, WINDOWHEIGHT), 1)


if __name__ == '__main__':
	main()

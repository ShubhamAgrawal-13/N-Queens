import pygame
import random
import numpy as np
from time import sleep
import sys

pygame.init()
TIME=0.05
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 
colors=[(255,0,255),(255,255,0),(0,255,255),(128,255,255),(255,128,255),(255,255,128)]
QImg = pygame.image.load('queen.jpg')
QImg = pygame.transform.scale(QImg, (70, 70))

class cube(object):
	"""docstring for Cube"""
	def __init__(self, x, y, val):
		self.x=x
		self.y=y
		self.val=val

	def draw_cube(self, win, width, n):
		t=width//n
		xx=0
		yy=0
		for l in range(n):
			xx+=t
			yy+=t
			pygame.draw.line(win, white, (xx,0) , (xx,width))
			pygame.draw.line(win, white, (0,yy) , (width,yy))
		pygame.draw.rect(win, black, (self.x*t+1,self.y*t+1,t-2,t-2))

	def draw_cube_border(self, win, width, n):
		t=width//n
		# pygame.draw.rect(win, green, (self.x*t+1,self.y*t+1,t-2,t-2))
		win.blit(QImg, (self.x*t+1,self.y*t+1,t-2,t-2))

	def draw_cube_border_1(self, win, width, n):
		t=width//n
		pygame.draw.rect(win, green, (self.x*t+1,self.y*t+1,t-2,t-2))


def check_safe(row, col, board, n):
	board[row][col].draw_cube_border_1(win,width,n)
	pygame.display.update() 
	sleep(TIME)
	for i in range(n):
		if(board[row][i].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False

	for i in range(n):
		if(board[i][col].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False

	r=row
	c=col
	while(r>=0 and c>=0):
		if(board[r][c].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False
		r-=1
		c-=1

	r=row
	c=col
	while(r<n and c<n):
		if(board[r][c].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False
		r+=1
		c+=1
	r=row
	c=col
	while(r>=0 and c<n):
		if(board[r][c].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False
		r-=1
		c+=1
	r=row
	c=col
	while(r<n and c>=0):
		if(board[r][c].val=='Q'):
			board[row][col].draw_cube(win,width,n)
			pygame.display.update() 
			return False
		r+=1
		c-=1
	board[row][col].draw_cube(win,width,n)
	pygame.display.update() 
	return True


def solve(col,board,n):
	sleep(TIME)
	if(col==n):
		#cprint()
		sleep(10)
		pygame.quit()
		sys.exit(0)
		return
	for i in range(n):
		if(check_safe(i,col,board,n)):
			board[i][col].val='Q'
			board[i][col].draw_cube_border(win,width,n)
			pygame.display.update() 
			solve(col+1,board,n)
			board[i][col].val='.'
			board[i][col].draw_cube(win,width,n)
			pygame.display.update() 
		sleep(TIME)


def drawWindow(win,width,n,board,f):
	win.fill(black)
	#draw the grid
	t=width//n
	x=0
	y=0
	for l in range(n):
		x+=t
		y+=t
		pygame.draw.line(win, white, (x,0) , (x,width))
		pygame.draw.line(win, white, (0,y) , (width,y))
	for i in range(n):
		for j in range(n):
			board[i][j].draw_cube(win,width,n)
	level_label=f.render(f"Board: {n}*{n}",1,(255,255,0))
	p_label=f.render(f"N-Queens",1 ,(0,255,0))
	win.blit(level_label,(10,(n)*t+10))
	win.blit(p_label,((n//2)*t,(n)*t+10))
	pygame.display.update() 


n=int(input("Enter n : "))
run=True
width=n*70

win = pygame.display.set_mode((width,width+50))
win.fill((0,0,0))
pygame.display.set_caption("N - Queens")
f=pygame.font.SysFont("comicsans",30)
clock = pygame.time.Clock()

board=[]

for i in range(n):
	board.append([cube(i,j,'.') for j in range(n)])


drawWindow(win,width,n,board,f)
solve(0,board,n)

pygame.quit()


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from lighting import ObjectQuads,Material
import math
import time
verticies = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1))
surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6))
def Button(x,y,Img,gameDisplay):
    gameDisplay.blit(Img,(x,y))
def main():
	pygame.init()
	display=(800,600)
	gameDisplay=pygame.display.set_mode(display,DOUBLEBUF|OPENGLBLIT)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0,0.0, -5)
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)
	Img = pygame.image.load('button.png')
	speed=0.5
	moving=[0,0,0]
	lightposition=(5,2,0)
	while True:
		start=time.time()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_w:
					moving[2]+=-speed
				if event.key==pygame.K_s:
					moving[2]+=speed
				if event.key==pygame.K_d:
					moving[0]+=speed
				if event.key==pygame.K_a:
					moving[0]+=-speed
				if event.key==pygame.K_q:
					moving[1]+=-speed
				if event.key==pygame.K_e:
					moving[1]+=speed
		basic=Material(100,1,5,1,(1,0,0))
		light=Material(100,1,10,1,(1,1,1))
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		ObjectQuads(verticies,surfaces,lightposition,light,(5,2,0),scale=0.05)
		ObjectQuads(verticies,surfaces,tuple(moving),basic,(5,2,0),scale=1)
		pygame.display.flip()
		end=time.time()
		print('Fps:',1/(end-start))
main()
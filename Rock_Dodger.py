#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, time, random
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480

# --------------------------------------------------------------------- 
# Clases
# ---------------------------------------------------------------------
class elemento(pygame.sprite.Sprite):
	def __init__(self,imagen,transp,posx,posy,velx,vely):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image(imagen, transp)
		self.rect = self.image.get_rect()
		self.rect.centerx = posx
		self.rect.centery = posy
		self.speed = [velx, vely]

# ---------------------------------------------------------------------
# Funciones generales
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
        
def texto(texto, fuente, posx, posy, color):
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect

# ---------------------------------------------------------------------
# Funciones del juego
# ---------------------------------------------------------------------
def ProcesarMovimiento(tiempo,keys,jugador):
	if jugador.rect.left >= 0:
		if keys[K_LEFT]:
			jugador.rect.x -= jugador.speed[0] * tiempo
			jugador.image = load_image("images/spelunker2.png", True)
	if jugador.rect.right <= WIDTH:
		if keys[K_RIGHT]:
			jugador.rect.x += jugador.speed[0] * tiempo
			jugador.image = load_image("images/spelunker.png", True)
	if keys[K_SPACE] and jugador.rect.centery==HEIGHT-48:
		jugador.speed[1]=-1.1
	if jugador.speed[1]!=0:
		jugador.rect.y += jugador.speed[1] * tiempo
		jugador.speed[1] = jugador.speed[1] + 0.005 * tiempo
	if jugador.rect.y>=HEIGHT-48:
		jugador.speed[1]=0
		jugador.rect.centery = HEIGHT-48

# Cuadrado
def ActualizarPantalla(tiempo,cuadrado,cuadrado2,cuadrado3,cuadrado4,cuadrado5,jugador,puntos,cuads,diamond,piedra,moneda):
# Actualizamos el cuadrado
	cuadrado.rect.centery -= cuadrado.speed[1] * tiempo
# Control de la puntuación
	if cuadrado.rect.bottom >= HEIGHT:
		cuads[0] = random.choice([True,False])
		cuadrado.rect.centery = 0
		
# Miramos las colisiones y restamos vidas
	if pygame.sprite.collide_rect(cuadrado, jugador):
		if cuads[0] == True:
			piedra.play()
			cuadrado.rect.centery = 0
			cuads[0] = random.choice([True,False])
			puntos[1] -= 1
			
# Actualizamos el cuadrado 2
	cuadrado2.rect.centery -= cuadrado2.speed[1] * tiempo
# Control de la puntuación
	if cuadrado2.rect.bottom >= HEIGHT:
		cuads[1] = random.choice([True,False])
		cuadrado2.rect.centery = 0
		
# Miramos las colisiones y restamos vidas
	if pygame.sprite.collide_rect(cuadrado2, jugador):
		if cuads[1] == True:
			piedra.play()
			cuadrado2.rect.centery = 0
			cuads[1] = random.choice([True,False])
			puntos[1] -= 1
			
# Actualizamos el cuadrado 3
	cuadrado3.rect.centery -= cuadrado3.speed[1] * tiempo
# Control de la puntuación
	if cuadrado3.rect.bottom >= HEIGHT:
		cuads[2] = random.choice([True,False])
		cuadrado3.rect.centery = 0
		
# Miramos las colisiones y restamos vidas
	if pygame.sprite.collide_rect(cuadrado3, jugador):
		if cuads[2] == True:
			piedra.play()
			cuadrado3.rect.centery = 0
			cuads[2] = random.choice([True,False])
			puntos[1] -= 1
			
# Actualizamos el cuadrado 4
	cuadrado4.rect.centery -= cuadrado4.speed[1] * tiempo
# Control de la puntuación
	if cuadrado4.rect.bottom >= HEIGHT:
		cuads[3] = random.choice([True,False])
		cuadrado4.rect.centery = 0
		
# Miramos las colisiones y restamos vidas
	if pygame.sprite.collide_rect(cuadrado4, jugador):
		if cuads[3] == True:
			piedra.play()
			cuadrado4.rect.centery = 0
			cuads[3] = random.choice([True,False])
			puntos[1] -= 1
			
# Actualizamos el cuadrado 5
	cuadrado5.rect.centery -= cuadrado5.speed[1] * tiempo
# Control de la puntuación
	if cuadrado5.rect.bottom >= HEIGHT:
		cuads[4] = random.choice([True,False])
		cuadrado5.rect.centery = 0
	elif cuads[0] and cuads[1] and cuads[2] and cuads[3]:
		cuads[4] = False
		
# Miramos las colisiones y restamos vidas
	if pygame.sprite.collide_rect(cuadrado5, jugador):
		if cuads[4] == True:
			piedra.play()
			cuadrado5.rect.centery = 0
			cuads[4] = random.choice([True,False])
			puntos[1] -= 1
	
	if puntos[0]>=5:
		if pygame.sprite.collide_rect(diamond, jugador):
			moneda.play()
			puntos[2]+=1
			diamond.rect.centerx = random.choice([WIDTH/2,WIDTH-500, WIDTH-100])
			diamond.rect.centery = random.choice([HEIGHT-48,HEIGHT-200]) 
# ---------------------------------------------------------------------
# Programa Principal
# --------------------------------------------------------------------- 
def main():
# Inicializaciones pygame
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.mixer.music.load("sounds/fondo.mp3")
	pygame.mixer.music.set_volume(0.2)
	moneda=pygame.mixer.Sound("sounds/moneda.wav")
	piedra=pygame.mixer.Sound("sounds/golpe.wav")
	pygame.display.set_caption("Rock Dodger")
	background_image = load_image('images/cueva.png')
	intro_image = load_image('images/intro.png')
	carga_image = load_image('images/carga.png')
	start_image = pygame.image.load("images/start.png").convert_alpha()
	salir_image = pygame.image.load("images/quit.png").convert_alpha()
# Inicializaciones elementos de juego
	cuads=[True,True,True,True,False]
	cuadrado = elemento("images/boulder.png",True,52,HEIGHT,0,-0.4)
	cuadrado2 = elemento("images/boulder.png",True,WIDTH/2,HEIGHT,0,-0.4)
	cuadrado3 = elemento("images/boulder.png",True,WIDTH-52,HEIGHT,0,-0.4)
	cuadrado4 = elemento("images/boulder.png",True,WIDTH/4+30,HEIGHT,0,-0.4)
	cuadrado5 = elemento("images/boulder.png",True,WIDTH-200,HEIGHT,0,-0.4)
	diamond = elemento("images/diamond.png",True,WIDTH-200,HEIGHT-48,0,0)
	jugador = elemento("images/spelunker.png",True,WIDTH/2,HEIGHT-48,0.5,0)
	puntos = [0,3,0]
	punto = 0
	fuentetextocont = pygame.font.Font("images/reintentar.ttf", 25)
	fuentetextocont1 = pygame.font.Font("images/reintentar.ttf", 15)
	fuentetextointro = pygame.font.Font("images/reintentar.ttf", 60)
	fuentetextogover = pygame.font.Font("images/game.ttf", 60)
	colortextopuntos=(255, 255, 255)
	exitGame = False
	clock = pygame.time.Clock()
	intro = True
	carga = True
	gameOver = False
	while intro:
		screen.blit(intro_image, (0, 0))
		start=screen.blit(start_image, (HEIGHT/2,WIDTH/2-80))
		salir=screen.blit(salir_image, (HEIGHT/2,WIDTH/2))
		i_int, i_int_rect = texto("Rock Dodger", fuentetextointro, WIDTH/2, HEIGHT/2-60, colortextopuntos)
		screen.blit(i_int, i_int_rect)
		pygame.display.update()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
			if eventos.type == pygame.MOUSEBUTTONDOWN:
				pos=pygame.mouse.get_pos()
				if start.collidepoint(pos):
					intro = False
				if salir.collidepoint(pos):
					sys.exit(0)
	while carga:
		screen.blit(carga_image,(0,0))
		pygame.display.update()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
		time.sleep(5)
		carga = False
	pygame.mixer.music.play(2)
	while not exitGame:
		pygame.mouse.set_visible(False)
		tiempo = clock.tick(60)
		punto += 1
		if punto == 60:
			puntos[0] += 1
			punto = 0
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
# Procesamos jugador
		keys = pygame.key.get_pressed()
		fin = pygame.key.get_pressed()
		ProcesarMovimiento(tiempo,keys,jugador)
		
		
# Actualizamos estado de la partida
		ActualizarPantalla(tiempo,cuadrado,cuadrado2,cuadrado3,cuadrado4,cuadrado5,jugador,puntos,cuads,diamond,piedra,moneda)
		p_jug, p_jug_rect = texto(str(puntos[0]), fuentetextocont1, 110, 20,colortextopuntos)
		t_jug, t_jug_rect = texto(str("Tiempo:"), fuentetextocont1, 50, 20,colortextopuntos)
		diamond_img = pygame.image.load("images/diamond.png").convert_alpha()
		hearth_img = pygame.image.load("images/corazon.png").convert_alpha()
		hearthv_img = pygame.image.load("images/corazonv.png").convert_alpha()
		d_jug, d_jug_rect =	texto(str(puntos[2]), fuentetextocont1, WIDTH/2, 20,colortextopuntos)
		
# Renderizamos
		screen.blit(background_image, (0, 0))
		screen.blit(p_jug, p_jug_rect)
		screen.blit(t_jug, t_jug_rect)
		screen.blit(d_jug, d_jug_rect)
		screen.blit(diamond_img, (WIDTH/2-60,0))
# Vidas
		if puntos[1]==3:
			screen.blit(hearth_img, (WIDTH/2+200,0))
			screen.blit(hearth_img, (WIDTH/2+235,0))
			screen.blit(hearth_img, (WIDTH/2+270,0))
		if puntos[1]==2:
			screen.blit(hearth_img, (WIDTH/2+200,0))
			screen.blit(hearth_img, (WIDTH/2+235,0))
			screen.blit(hearthv_img, (WIDTH/2+270,0))
		if puntos[1]==1:
			screen.blit(hearth_img, (WIDTH/2+200,0))
			screen.blit(hearthv_img, (WIDTH/2+235,0))
			screen.blit(hearthv_img, (WIDTH/2+270,0))
		if puntos[1]==0:
			screen.blit(hearthv_img, (WIDTH/2+200,0))
			screen.blit(hearthv_img, (WIDTH/2+235,0))
			screen.blit(hearthv_img, (WIDTH/2+270,0))
# Diamantes
		if puntos[0]>=5:
			screen.blit(diamond.image,diamond.rect)
# Rocas
		if cuads[0]:
			screen.blit(cuadrado.image,cuadrado.rect)
		if cuads[1]:
			screen.blit(cuadrado2.image,cuadrado2.rect)
		if cuads[2]:
			screen.blit(cuadrado3.image,cuadrado3.rect)
		if cuads[3]:
			screen.blit(cuadrado4.image,cuadrado4.rect)
		if cuads[4]:
			screen.blit(cuadrado5.image,cuadrado5.rect)
		screen.blit(jugador.image,jugador.rect)
		pygame.display.flip()
# Game Over
		if puntos[1]<=0:
			g_over, g_over_rect = texto("GAME OVER", fuentetextogover, WIDTH/2, HEIGHT/2, colortextopuntos)
			c_cont, c_cont_rect = texto("Reintentar? (S/N)", fuentetextocont, WIDTH/2, HEIGHT/2+60, colortextopuntos)
			screen.blit(g_over, g_over_rect)
			screen.blit(c_cont, c_cont_rect)
			cuadrado.rect.centery = HEIGHT
			cuadrado2.rect.centery = HEIGHT
			cuadrado3.rect.centery = HEIGHT
			cuadrado4.rect.centery = HEIGHT
			cuadrado5.rect.centery = HEIGHT
			pygame.display.update()
			pygame.mixer.music.stop()
			gameOver=True
			while gameOver:
				for eventos in pygame.event.get():
					if eventos.type == pygame.QUIT:
						exitGame = True
						gameOver = False
					if eventos.type == pygame.KEYDOWN:
						if eventos.key == pygame.K_s:
							pygame.mixer.music.play()
							jugador.rect.centerx = WIDTH/2
							puntos=[0,3,0]
							gameOver=False
							exitGame=False
						elif eventos.key == pygame.K_n:
							pygame.mixer.music.stop()
							gameOver=False
							exitGame = True
 
if __name__ == '__main__':
	pygame.init()
	main()

import math
import random

from pygame.locals import *
import pygame
from pygame import mixer

pygame.init()

#Pantalla
WIDTH = 346
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("images/grass-346-640.jpg")
pygame.display.set_caption("Wolf attack!!!")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#Personajes
bunny = pygame.image.load("images/bunny-72-72.png")
bunnyX = 141
bunnyY = 470
bunnyX_change = 0
BUNNY_SIZE = 72

bullet = pygame.image.load("images/bullet.png")
bltx = 0
blty = 400
bltx_change = 0
blty_change = 10
bullet_state = "ready" #Dos estados: ready para indicar que está listo para disparar y fire para indicar que se ha disparado
BULLET_SIZE = 32

wolf = []
wolfX = []
wolfY = []
wolfX_change = []
wolfY_change = []
WOLF_SIZE = 64
wolfs = 6

for i in range(wolfs):
  wolf.append(pygame.image.load("images/wolf-64-64.png"))
  wolfX.append(random.randint(0, 282))
  wolfY.append(random.randint(0, 200))
  wolfX_change.append(1)
  wolfY_change.append(10)

#Multimedia
mixer.music.load("sounds/background.wav")
mixer.music.play(-1)

#Puntaje
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 23)
tx = 10
ty = 10

def player(x, y):
  screen.blit(bunny, (x, y))

def bunny_movement():
  global bunnyX_change
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      bunnyX_change = -2

    if event.key == pygame.K_RIGHT:
      bunnyX_change = 2

    if event.key == pygame.K_SPACE:
      shot()

  #Para evitar que el conejo se mueva hacia arriba
  if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      bunnyX_change = 0

def enemy(x, y, i):
  screen.blit(wolf[i], (x, y))

def fire_bullet(x, y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(bullet, (x, y))

def shot():
  global bltx
  if bullet_state is "ready":
    bulletSound = mixer.Sound("sounds/laser.wav")
    bulletSound.play()
    #Para hacer que la bala aparezca desde donde está parado el conejo
    bltx = bunnyX
    fire_bullet(bltx, blty)

def show_score(x, y):
  score = font.render("Score: " + str(score_value), True, (255, 255, 255))
  screen.blit(score, (x, y))


def isCollision(wolfX, wolfY, bltx, blty):
  distance = math.sqrt(math.pow(wolfX - bltx, 2) +  + math.pow(wolfY - blty, 2))
  if distance < 27:
    return True
  else:
    return False

def defeat(i):
  global blty, score_value
  #Si choca contra un lobo
  collision = isCollision(wolfX[i], wolfY[i], bltx, blty)
  if collision:
    explosionSound = mixer.Sound("sounds/explosion.wav")
    explosionSound.play()

    blty = 400
    bullet_state = "ready"
    score_value += 1
    wolfX[i] = random.randint(0, 282)
    wolfY[i] = random.randint(0, 200)

running = True
while running:
  screen.fill((0, 0, 0))
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    bunny_movement()

  bunnyX += bunnyX_change
  #Para evitar que se salga de la pantalla
  if bunnyX <= 0:
    bunnyX = 0
  elif bunnyX >= 274:
    bunnyX = 274

  #Movimiento de los lobos
  for i in range(wolfs):
    wolfX[i] += wolfX_change[i]

    if wolfX[i] <= 0:
      wolfX_change[i] = 1
      wolfY[i] += wolfY_change[i]
    elif wolfX[i] >= 282:
      wolfX_change[i] = -1
      wolfY[i] += wolfY_change[i]

    enemy(wolfX[i], wolfY[i], i)

    defeat(i)


  #Movimiento de la bala
  if blty <= 0:
    blty = 400
    bullet_state = "ready"

  if bullet_state is "fire":
    fire_bullet(bltx, blty)
    blty -= blty_change

  #Muestra de datos en pantalla
  player(bunnyX, bunnyY)
  show_score(tx, ty)
  pygame.display.update()

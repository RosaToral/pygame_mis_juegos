import math
import random

from pygame.locals import *
import pygame
from pygame import mixer

class Bunny:
  bunnyX = 0
  bunnyY = 0
  bunnyX_change = 0

class Bullet:
  bltx = 0
  blty = 0
  bltx_change = 0
  blty_change = 0
  bullet_state = "ready" #Dos estados: ready para indicar que está listo para disparar y fire para indicar que se ha disparado

class Wolf:
  wolfX = 0
  wolfY = 0
  wolfX_change = 0
  wolfY_change = 0

class wolfAttack:
  def __init__(self):
    self.WIDTH = 346
    self.HEIGHT = 550
    self.BUNNY_SIZE = 72
    self.BULLET_SIZE = 32
    self.WOLF_SIZE = 64
    self.N_WOLFS = 6
    self._running = True

    self.bunny = Bunny()
    self.bullet = Bullet()

    self.bunny.bunnyX = 141
    self.bunny.bunnyY = 470

    self.bullet.blty = 400
    self.bullet.blty_change = 10

    self.wolfs = []
    for i in range(self.N_WOLFS):
      self.wolfs.append(Wolf())
      self.wolfs[i].wolfX = random.randint(0, 282)
      self.wolfs[i].wolfY = random.randint(0, 200)
      self.wolfs[i].wolfX_change = 1
      self.wolfs[i].wolfY_change = 10


  def on_init(self):
    pygame.init()
    pygame.display.set_caption("Wolf attack!!!")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    #Multimedia
    #mixer.music.load("sounds/background.wav")
    #mixer.music.play(-1)
    
    self.bunny_img = pygame.image.load("images/bunny-72-72.png").convert()
    self.bullet_img = pygame.image.load("images/bullet.png").convert()
    self.background = pygame.image.load("images/grass-346-640.jpg").convert()
    #self.wolfs_img = []
    #for i in range(self.N_WOLFS):
    #  self.wolfs_img.append(pygame.image.load("images/wolf-64-64.png").convert())

    #Puntaje
    self.score_value = 0
    self.font = pygame.font.Font('freesansbold.ttf', 23)
    self.tx = 10
    self.ty = 10

  def on_render(self):
    self.screen.fill((90,255,255))
    self.screen.blit(self.background, (0, 0))

    self.screen.blit(self.bunny_img, (self.bunny.bunnyX, self.bunny.bunnyY))

    #for i in range(self.N_WOLFS):
    #  self.screen.blit(self.wolfs_img[i], (self.wolfs[i].wolfX, self.wolfs[i].wolfY))

  def on_cleanup(self):
    pygame.quit()
  
  def on_execute(self):
    if self.on_init() == False:
      self._running == False

    while self._running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self._running = False

      self.on_render()

    self.on_cleanup()
  

if __name__ == '__main__':
  game = wolfAttack()
  game.on_execute()
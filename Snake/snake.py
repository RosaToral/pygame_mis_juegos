#1.- Crear una ventana
#2.- Carga de imagenes
#3.- Entradas del teclado
#4.- Haciendo la serpiente
#5.- Game play

from pygame.locals import *
import pygame
import time
from random import randint

#3.- Se crea una nueva clase que tome las pulsaciones del teclado
#3.- y las transforme a posiciones en la pantalla
class Player:
  x = 0 #3.- Posicion horizontal
  y = 0 #3.- Posicion vertical
  d = 0 #4.- Cambia la direccion de la serpiente
  positions = [] #4.- Guarda la última posicion en la que estuvo la imagen
  length = 5 #4.- Tamaño de la serpiente

#5.- Se crea una nueva clase para poder manejar la manzana como con la serpiente
class Apple:
  x = 0 #5.- Posicion horizontal
  y = 0 #5.- Posicion vertical

class Snake:
  def __init__(self):
    #5.- Constantes para manejar la posicion de la manzana, de la serpiente y el tamaño de la ventana
    self._MOVEMENT = 24
    self._WIDTH = 26
    self._HEIGHT = 20

    self._running = True #1.- Variable para saber si el juego esta siendo ejecutado
    
    self.player = Player()
    self.apple = Apple()

    #5.- Se le asigna a la manzana una posicion aleatoria al principio
    self.apple.x = randint(0, self._WIDTH-1)*self._MOVEMENT
    self.apple.y = randint(0, self._HEIGHT-1)*self._MOVEMENT

  def on_init(self):
    pygame.init() #1.- Inicializa pygame

    #1.- Crea una ventana ((ancho, alto), utilizar aceleracion del hardware)
    self._display_surf = pygame.display.set_mode((self._WIDTH*self._MOVEMENT, self._HEIGHT*self._MOVEMENT), pygame.HWSURFACE)
    pygame.display.set_caption("Snake by Ross") #1.- Titulo de la ventana

    #2.- Cargar una imagen.
    #2.- Debe ser cargada y guardada en una variable
    self._snake_i = pygame.image.load("android/c1-24.png").convert()
    self._apple_i = pygame.image.load("android/app-24.png").convert()

  def on_render(self):
    #1.- Color de la pantalla (rojo, verde, azul)
    self._display_surf.fill((90,255,255))

    #4.- Pinta la imagen en ls posiciones que se guardaron para dibujar a la serpiente
    for p in self.player.positions:
      #2.- Dibujar la imagen en la ventana (variable que guarda la imagen, (horizontal, vertical))
      self._display_surf.blit(self._snake_i, (p[0], p[1]))
    
    self._display_surf.blit(self._apple_i, (self.apple.x, self.apple.y))
    
    pygame.display.flip() #1.- Actualiza la pantalla

  def moving(self):
    #3.- Se pueden atrapar las teclas que el usuario presiona
    keys = pygame.key.get_pressed()


    #4.- Solo se cambia la direccion de la serpiente, por lo que
    #4.- para que se pueda cambiar, lo que se va a hacer es que se movera
    #4.- de forma continua , es decir que se va a aumentar la variable x y y
    #4.- sin que dependa de un evento y cuando el usuario presione una tecla,
    #4.- se va a cambiar la direccion
    #4.- Aqui se detecta que tecla se presiono
    if keys[K_RIGHT]:
      self.player.d = 0
    if keys[K_LEFT]:
      self.player.d = 1
    if keys[K_UP]:
      self.player.d = 2
    if keys[K_DOWN]:
      self.player.d = 3

    #4.- Aqui se cambia la direccion, haciendo que se mueva constantemente
    #3.- Se cambia el valor en x y y del player cada vez que se presione una tecla
    if self.player.d == 0:
      self.player.x += self._MOVEMENT
    elif self.player.d == 1:
      self.player.x -= self._MOVEMENT
    elif self.player.d == 2:
      self.player.y -= self._MOVEMENT
    elif self.player.d == 3:
      self.player.y += self._MOVEMENT

    #4.- Si ya se alcanzo el limite de posiciones guardadas se elimina la de la primera posicion porque ya no sirve
    if len(self.player.positions) >= self.player.length:
      self.player.positions.pop(0)
    
    #4.- Agrega la ultima posicion de la imagen
    self.player.positions.append((self.player.x, self.player.y))

  def isCollision(self, x1, y1, x2, y2, bsize):
    #5.- Se detecta si hay una colision.
    #5.- Puede ser una colision entre la manzana y la serpiente, con la serpiente misma o con las paredes
    if x1 >= x2 and x1 < x2 + bsize:
      if y1 >= y2 and y1 < y2 + bsize:
        return True

    return False

  def collisions(self):
    #5.- Si hay una colision entre la manzana y la serpiente, se cambia la posicion de la manzana
    #5.- y se agrega una posicion mas a la serpiente (lenght) para guardar la que se acaba de comer
    if self.isCollision(self.player.x, self.player.y, self.apple.x, self.apple.y, self._MOVEMENT):
      self.apple.x = randint(0, self._WIDTH-1)*self._MOVEMENT
      self.apple.y = randint(0, self._HEIGHT-1)*self._MOVEMENT
      self.player.length += 1

    #5.- Si hay una colision de la serpiente consigo misma, se termina el juego y se muestra un mensaje de "Game over"
    if len(self.player.positions) > self.player.length-1:
      for i in range (0, self.player.length-1):
        if self.isCollision(self.player.x, self.player.y, self.player.positions[i][0], self.player.positions[i][1], 20):
          print("Game over")
          exit()

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    #1.- Si el juego no se ha inicializado, se sale de la ejecucion
    if self.on_init() == False:
      self._running == False

    #1.- Este ciclo es para mantener corriendo el programa
    while self._running:
      #1.- Este ciclo sirve para detectar cuando el usuario detiene la aplicacion
      #1.- Cada evento que vaya recibiendo (teclado, mause)
      for event in pygame.event.get():
        #1.- Si el siguiente evento que recibe es el de clic sobre la x 
        #1.- para cerrar la ventana, cambia la variable de estado a False
        if event.type == pygame.QUIT:
          self._running = False

      #3.- Funcion que mueve y pinta la imagen de la serpiente
      self.moving()

      #5.- Esta funcíon se encarga de manejar las colisiones
      self.collisions()

      #1.- Renderiza la ventana cada vez si no se ha cambiado la variable de estado a False.
      self.on_render()
      
      #4.- Para evitar que la serpiente se mueva muy rapido
      time.sleep(0.18)

    #1.- Si se cambia a False, se sale del ciclo y on_cleanup cierra la app
    self.on_cleanup()

if __name__ == "__main__":
  game = Snake()
  game.on_execute()
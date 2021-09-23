#1.- Crear una ventana
#2.- Carga de imagenes
#3.- Entradas del teclado
from pygame.locals import *
import pygame

#3.- Se crea una nueva clase que tome las pulsaciones del teclado
#3.- y las transforme a posiciones en la pantalla
class Player:
  x = 0
  y = 0
    

class Prueba:
  """docstring for Snake"""
  def __init__(self):
    self._running = True #1.- Variable para saber si el juego esta siendo ejecutado
    self.player = Player()


  def on_init(self):
    pygame.init() #1.- Inicializa pygame

    #1.- Crea una ventana ((ancho, alto), utilizar aceleracion del hardware)
    self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE)
    pygame.display.set_caption("Snake by Ross") #1.- Titulo de la ventana

    #2.- Cargar una imagen.
    #2.- Debe ser cargada y guardada en una variable
    self._bunny = pygame.image.load("android/bunny-72-72.png").convert()


  def on_render(self):
    #1.- Color de la pantalla (rojo, verde, azul)
    self._display_surf.fill((0,0,0))

    #2.- Dibujar la imagen en la ventana (variable que guarda la imagen, (horizontal, vertical))
    self._display_surf.blit(self._bunny, (self.player.x, self.player.y))
    pygame.display.flip() #1.- Actualiza la pantalla


  def on_cleanup(self):
    pygame.quit()

  def moving(self):
    #3.- Se pueden atrapar las teclas que el usuario presiona
    keys = pygame.key.get_pressed()

    #3.- Se cambia el valor en x y y del player cada vez que se presione una tecla
    #3.- Se puede tomar cualquier tecla del teclado por K_nombre
    if keys[K_RIGHT]:
      self.player.x += 1
    if keys[K_LEFT]:
      self.player.x -= 1
    if keys[K_UP]:
      self.player.y -= 1
    if keys[K_DOWN]:
      self.player.y += 1

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

      self.moving() #3.- La parte para mover la imagen esta aqui

      #1.- Renderiza la ventana cada vez si no se ha cambiado la variable de estado a False.
      self.on_render()

    #1.- Si se cambia a False, se sale del ciclo y on_cleanup cierra la app
    self.on_cleanup()

if __name__ == "__main__":
  game = Prueba()
  game.on_execute()
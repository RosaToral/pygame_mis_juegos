import pygame

pygame.init()

screen = pygame.display.set_mode((346, 640))
background = pygame.image.load("images/grass-346-640.jpg")
bunny = pygame.image.load("images/bunny-72-72.png")
wolf = pygame.image.load("images/wolf-64-64.png")

running = True

while running:
  screen.fill((0, 0, 0))
  screen.blit(background, (0, 0))
  screen.blit(bunny, (123, 480))
  screen.blit(wolf, (90, 100))
  screen.blit(wolf, (180, 150))
  screen.blit(wolf, (230, 320))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    pygame.display.update()

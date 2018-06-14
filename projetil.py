import pygame
import math

# Definicoes da tela
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projetil')
resistenciaDoAr = 0.999
elasticidade = 0.75

# Tamanho eh a velocidade da particula
def somaVetores((angulo1, tamanho1), (angulo2, tamanho2)):
  x = math.sin(angulo1) * tamanho1 + math.sin(angulo2) * tamanho2
  y = math.cos(angulo1) * tamanho1 + math.cos(angulo2) * tamanho2

  angulo = math.atan2(x, y)
  tamanho = math.hypot(x,y)

  return (angulo, tamanho)

class Particula:
  def __init__(self, (x,y), raio, angulo):
    self.x = x
    self.y = y
    self.raio = raio
    self.cor = (0,0,0)
    self.linha = 1
    self.velocidade = 0.01
    self.angulo = angulo

  def mover(self, gravidade = (0, 0.002)):
    (self.angulo, self.velocidade) = somaVetores((self.angulo, self.velocidade), gravidade)
    self.x += math.sin(self.angulo) * self.velocidade
    self.y += math.cos(self.angulo) * self.velocidade
    #self.velocidade *= resistenciaDoAr
   
  def display(self):
    pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), self.raio, self.linha)



p1 = Particula((15, 500 - 15), 15, 3 * math.pi / 4)
p1.velocidade = 3.5


p2 = Particula((500 - 15, 15), 15, 0)
p2.velocidade = 0

g = 0.010


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  p2.mover((0,g))
  p2.display()
  p1.mover((0,g))
  p1.display()
  pygame.display.flip()  

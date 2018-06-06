import pygame
import random
import math

# Definicoes da tela
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gravidade')
#gravidade = (0 , 0.002)
resistenciaDoAr = 0.999
elasticidade = 0.75

def somaVetores((angulo1, tamanho1), (angulo2, tamanho2)):
  x = math.sin(angulo1) * tamanho1 + math.sin(angulo2) * tamanho2
  y = math.cos(angulo1) * tamanho1 + math.cos(angulo2) * tamanho2

  angulo = math.atan2(x, y)
  tamanho = math.hypot(x,y)

  return (angulo, tamanho)

class Particula:
  def __init__(self, (x,y), tamanho):
    self.x = x
    self.y = y
    self.tamanho = tamanho
    self.cor = (0,0,0)
    self.linha = 1
    self.velocidade = 0.01
    self.angulo = 0

  def mover(self, gravidade = (0, 0.002)):
    (self.angulo, self.velocidade) = somaVetores((self.angulo, self.velocidade), gravidade)
    self.x += math.sin(self.angulo) * self.velocidade
    self.y += math.cos(self.angulo) * self.velocidade
    self.velocidade *= resistenciaDoAr
  
  def refletir(self):
    if self.x > width - self.tamanho:
      self.x = 2 * (width - self.tamanho) - self.x
      self.angulo = -self.angulo
      self.velocidade *= elasticidade
    elif self.x < self.tamanho:
      self.x = 2 * self.tamanho - self.x
      self.angulo = - self.angulo
      self.velocidade *= elasticidade

    if self.y > height - self.tamanho:
      self.y = 2 * (height - self.tamanho) - self.y
      self.angulo = math.pi - self.angulo
      self.velocidade *= elasticidade
    elif self.y < self.tamanho:
      self.y = 2 * self.tamanho - self.y
      self.angulo = math.pi - self.angulo
      self.velocidade *= elasticidade

  
  def display(self):
    pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), self.tamanho, self.linha)


# Definicoes das particulas
numero_de_particulas = 10
lista_de_particulas = []
min = 10 # Tamanho minimo da particula
max = 20 # Tamanho maximo da particula

for n in range(numero_de_particulas):
  tamanho = random.randint(min,max)
  x = random.randint(tamanho, width - tamanho)
  #y = random.randint(tamanho, height - tamanho)
  y = 20
  particula = Particula((x,y), tamanho)
  particula.velocidade = random.random()
  particula.angulo = random.uniform(0, math.pi * 2)
  lista_de_particulas.append(particula)

p1 = Particula((40,40), 15)
p1.velocidade = 1.5
p1.angulo = 0

p2 = Particula((100,40), 15)
p2.velocidade = 1.5
p2.angulo = 0



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  '''
  for particula in lista_de_particulas:
    particula.mover()
    particula.refletir()
    particula.display()
  '''
  p2.mover((0,0.002))
  p2.refletir()
  p2.display()
  p1.mover((0,0.0002))
  p1.refletir()
  p1.display()
  pygame.display.flip()  

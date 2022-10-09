import pygame
from pygame.locals import *
from sys import exit
from random import randint

class Boost_velocidade:
    def __init__(self):
        x_vel = randint(largura_tela, altura_tela)
        y_vel = randint(largura_tela, altura_tela)
        pygame.draw.rect(tela, (250, 250, 250), (x_vel, y_vel, 12, 12))





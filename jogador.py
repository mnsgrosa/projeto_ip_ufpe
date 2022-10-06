import pygame
from pygame.math import Vector2

class Jogador:
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self._pos = Vector2(w//2, h//2)
        self._vida = 10
        self._vel = 20
        self._dinheiro = 0
        self._arma1 = True
        self._arma2 = False
    
    def movimentacao(self, tecla):
        if tecla == pygame.
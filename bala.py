import pygame
import math
import random

class Bala(pygame.sprite.Sprite):
    def __init__(self, alvo, jogador_x, jogador_y):
        pygame.sprite.Sprite.__init__(self)
        angle = math.atan2(alvo.y - jogador_y, alvo.x - jogador_x)
        self.dx = math.cos(angle) * 80
        self.dy = math.sin(angle) * 80
        self.x = jogador_x
        self.y = jogador_y
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (jogador_x, jogador_y))


    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
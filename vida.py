from pygame.math import Vector2
from pygame.transform import scale
import pygame
import random


class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.existe_sprite = False
        self.pos = Vector2(random.randint(0, self.largura_tela - 12), random.randint(0, self.altura_tela - 12))
        self.image = pygame.image.load('sprites/sprite_milho.png')
        self.image = scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 2000

    def spawn_vida(self, status):
        if status:
            self.existe_sprite = False
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 600:
            self.tempo_spawn += 1
            self.rect.x = 2000
            self.rect.y = 2000
        elif not self.existe_sprite and self.tempo_spawn >= 600:
            self.pos = Vector2(random.randint(0, self.largura_tela-50), random.randint(0, self.altura_tela-50))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            self.existe_sprite = True

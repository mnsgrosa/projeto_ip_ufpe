import pygame
from pygame.math import Vector2
from pygame.transform import scale
import random


class Velocidade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.existe_sprite = False
        self.pos = Vector2(random.randint(0, self.largura_tela - 50), random.randint(0, self.altura_tela - 50))
        self.image = pygame.image.load('sprites/sprite_cafe.png')
        self.image = scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 2000
        self.last = pygame.time.get_ticks()
        self.cooldown = 0
        duracao_boost = False
        boost_ativo = False

    def spawn_velocidade(self, status):
        if status:
            self.existe_sprite = False
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 400:
            self.tempo_spawn += 1
        elif not self.existe_sprite and self.tempo_spawn >= 400:
            self.pos = Vector2(random.randint(0, self.largura_tela - 50), random.randint(0, self.altura_tela - 50))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            self.existe_sprite = True

    def duracao_velocidade(self):
        if pygame.time.get_ticks() < self.duracao_boost:
            self.boost_ativo = True

        else:
            self.boost_ativo = False
            self.duracao_boost = pygame.time.get_ticks()

    # funcao que de cooldown do boost
    def respawn(self, status):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.spawn_velocidade(status)

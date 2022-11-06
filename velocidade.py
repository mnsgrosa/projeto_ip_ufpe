import pygame
from pygame.math import Vector2
from pygame.transform import scale
import random


class Velocidade(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.init()
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.duracao_boost = 0
        self.existe_sprite = False
        self.boost_ativo = False
        self.som = pygame.mixer.Sound('sons/som_velocidade.wav')
        self.som.set_volume(0.09)
        self.image = scale(pygame.image.load('sprites/sprite_cafe.png'), (50, 50))
        self.rect = self.image.get_rect(topleft=(0, 2000))
        self.vel = self.largura_tela // 40

    def spawn_velocidade(self, coleta):
        if coleta:
            self.rect.x, self.rect.y = 0, 2000
            self.existe_sprite = False
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and not self.boost_ativo and self.tempo_spawn < 210:
            self.tempo_spawn += 1
        elif not self.existe_sprite and not self.boost_ativo and self.tempo_spawn >= 210:
            self.rect.x, self.rect.y = random.randint(0, self.largura_tela - 50), random.randint(0, self.altura_tela - 50)
            self.existe_sprite = True

    def boost(self, coleta):
        if coleta:
            self.som.play()
            self.boost_ativo = True
        if self.boost_ativo and self.duracao_boost < 180:
            self.duracao_boost += 1
            self.vel = self.largura_tela // 20
        elif self.boost_ativo and self.duracao_boost >= 180:
            self.duracao_boost = 0
            self.boost_ativo = False
            self.vel = self.largura_tela // 40

    def update_cafe(self, coleta):
        self.spawn_velocidade(coleta)
        self.boost(coleta)

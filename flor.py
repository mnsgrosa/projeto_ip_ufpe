import pygame
from pygame.transform import scale
from random import randint


class Flor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.existe_sprite = False
        self.image = pygame.image.load('sprites/sprite_flor.png')
        self.image = scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = randint(0, self.largura_tela - 50), randint(0, self.altura_tela - 70)

    def spawn_flor(self, dano):
        if dano:
            self.rect.x, self.rect.y = 2000, 2000
            self.existe_sprite = False
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 10:
            self.tempo_spawn += 1
        elif not self.existe_sprite and self.tempo_spawn >= 10:
            self.rect.x, self.rect.y = randint(0, self.largura_tela - 50), randint(0, self.altura_tela - 70)
            self.existe_sprite = True

import pygame
from pygame.transform import scale
from random import randint


class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.existe_sprite = False
        self.image = pygame.image.load('sprites/sprite_milho.png')
        self.image = scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 2000, 2000

    def spawn_vida(self, coleta_vida):
        if coleta_vida:
            self.rect.x, self.rect.y = 2000, 2000
            self.existe_sprite = False
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 390:
            self.tempo_spawn += 1
        elif not self.existe_sprite and self.tempo_spawn >= 390:
            self.rect.x, self.rect.y = randint(0, self.largura_tela - 50), randint(0, self.altura_tela - 50)
            self.existe_sprite = True


class Barra_vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coracao_0 = pygame.image.load('sprites/coracao_0.png')
        self.coracao_1 = pygame.image.load('sprites/coracao_1.png')
        self.coracao_2 = pygame.image.load('sprites/coracao_2.png')
        self.coracao_3 = pygame.image.load('sprites/coracao_3.png')
        self.coracao_0, self.coracao_1 = scale(self.coracao_0, (150, 50)), scale(self.coracao_1, (150, 50))
        self.coracao_2, self.coracao_3 = scale(self.coracao_2, (150, 50)), scale(self.coracao_3, (150, 50))
        self.image = self.coracao_3
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 20, 10

    def update_barra(self, vida):
        if vida == 3:
            self.image = self.coracao_3
        elif vida == 2:
            self.image = self.coracao_2
        elif vida == 1:
            self.image = self.coracao_1
        elif vida == 0:
            self.image = self.coracao_0

import pygame
import random
largura_tela, altura_tela = pygame.display.get_surface().get_size()
tela = pygame.display.get_surface()

class Velocidade:
    def __init__(self):

        self.tempo_spawn = 0
        self.existe_sprite = False
    def spawn_velocidade(self):
        if self.existe_sprite:

            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 900:

            self.tempo_spawn += 1
        elif not self.existe_sprite and self.tempo_spawn >= 900:

            posicao_velocidade = (random.randint(0, (largura_tela-12)), random.randint(0, (altura_tela-12)))
            pygame.draw.rect(tela, (255, 255, 0), (posicao_velocidade[0], posicao_velocidade[1], 12, 12))
            self.existe_sprite = True


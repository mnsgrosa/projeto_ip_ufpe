import pygame
import random
largura_tela, altura_tela = pygame.display.get_surface().get_size()
tela = pygame.display.get_surface()

class Vida:
    def __init__(self):
        # Inicia o objeto com um contador para controlar o intervalo de spawn
        # O objeto também possui uma variável para checar se o objeto já está spawnado 
        self.tempo_spawn = 0
        self.existe_sprite = False
    def spawn_vida(self):
        if self.existe_sprite:
            # Caso já exista um objeto spawnado, o objeto tem seu contador zerado
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 600:
            # Caso não exista um objeto spawnado, o contador aumentará até o tempo definido
            self.tempo_spawn += 1
        elif not self.existe_sprite and self.tempo_spawn >= 600:
            # Supondo que o jogo rode a 30fps, o contador irá até 600, ou seja, 20 segundos
            # Então o objeto é desenhado aleatoriamente na tela (por enquanto sem sprite)
            # E a variável recebe True até que haja a colisão do jogador com o objeto e variável volte a ser False
            posicao_vida = (random.randint(0, (largura_tela-12)), random.randint(0, (altura_tela-12)))
            pygame.draw.rect(tela, (250, 5, 180), (posicao_vida[0], posicao_vida[1], 12, 12))
            self.existe_sprite = True

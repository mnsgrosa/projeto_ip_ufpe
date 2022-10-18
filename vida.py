from pygame.math import Vector2
import pygame
import random


class Vida:
    def __init__(self):
        # Inicia o objeto com um contador para controlar o intervalo de spawn
        # O objeto também possui uma variável para checar se o objeto já está spawnado 
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.existe_sprite = False
        self.pos = Vector2(random.randint(0, self.largura_tela - 12), random.randint(0, self.altura_tela - 12))
        self.block = pygame.Rect(self.pos.x, self.pos.y, 12, 12)

    def spawn_vida(self, status):
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
            # Matheus: Nao sei fazer spawnar uma segunda vez tem algum erro na minha logica
            status = False
            self.pos = Vector2(random.randint(0, self.largura_tela-12), random.randint(0, self.altura_tela-12))
            self.block.x = self.pos.x
            self.block.y = self.pos.y
            self.existe_sprite = True

    # Se o jogador coletar coloca a caixa pra fora da tela pra nao ser coletada depois que respawnar
    # sera alocado na tela novamente 
    def coletado(self, status):
        if status:
            self.existe_sprite = False
            self.pos.x = 2000
            self.pos.y = 2000

    # So desenha na tela se o sprite existir na tela
    def draw_vida(self):
        if self.existe_sprite:
            pygame.draw.rect(self.tela, (250, 5, 180), self.block)

    # funcao que deve se repetir em outros objetos
    def update_vida(self, status):
        self.spawn_vida(status)
        self.coletado(status)
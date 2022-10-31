import pygame, sys
from pygame.math import Vector2
from jogador import Jogador
from bala import Bala
from vida import Vida
from vida import Barra_vida
from velocidade import Velocidade
from pontos import Pontos
import numpy as np


# Classe que ira conter todos os objetos
class Main:
    def __init__(self):
        self.tela = pygame.display.get_surface()
        self.jogador = Jogador()
        self.item_vida = Vida()
        self.item_vel = Velocidade()
        self.item_ponto = Pontos()
        self.barra_vida = Barra_vida()
        self.next_move = pygame.time.get_ticks() + 100
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto, self.barra_vida)

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)
        self.item_vida.spawn_vida(self.jogador.coleta_vida)
        self.item_vel.spawn_velocidade(self.jogador.coleta_vel)
        self.item_ponto.spawn_ponto(self.jogador.coleta_ponto)
        self.barra_vida.update_barra(self.jogador.vida)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto, self.barra_vida)

    def draw_elementos(self):
        self.sprites.draw(self.tela)

def digitar_texto(texto, cor, tamanho, posicao):
    fonte = pygame.font.SysFont('arial', tamanho, True, False)
    texto_formatado = fonte.render(texto, False, cor)
    screen.blit(texto_formatado, posicao)


if __name__ == '__main__':
    unidade = 20
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 22.5

    clock = pygame.time.Clock()
    clock.tick(30)

    bg = pygame.image.load("sprites/background.png")
    bg = pygame.transform.scale(bg, (unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))

    inimigo_pos = Vector2(np.random.randint(0, (unidade * SCREEN_WIDTH) - 22),
                          np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22))
    inimigo = pygame.Rect(inimigo_pos.x, inimigo_pos.y, 22, 22)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('CINGAÇO')


    grupo_balas = pygame.sprite.Group()

    game = True
    tela_start = True
    running = False

    pygame.init()
    pygame.font.init()

    record = 0
    contador = 0

    while game:
        while tela_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tela_start = False
                    running = False
                    game = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        tela_start = False
                        running = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        tela_start = False
                        running = True

            screen.fill((250, 250, 250))
            digitar_texto(f'RECORDE: {record}', (0, 0, 0), 33, (162, 270))
            digitar_texto('APERTE ESPAÇO PARA JOGAR', (0, 0, 0), 33, (162, 330))
            pygame.display.flip()
            clock.tick(30)

        jogo = Main()

        while running:
            antiga_vida = jogo.jogador.vida

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tela_start = False
                    running = False
                    game = False

            if jogo.jogador.morto:
                if jogo.jogador.ponto > record:
                    record = jogo.jogador.ponto
                tela_start = True
                running = False

            tecla = pygame.key.get_pressed()
            jogo.update([inimigo], jogo.item_vel.rect, jogo.item_vida.rect, jogo.item_ponto.rect, tecla)
            jogo.jogador.vel = jogo.item_vel.vel

            if jogo.jogador.vida < antiga_vida:
                inimigo = pygame.Rect(np.random.randint(0, (unidade * SCREEN_WIDTH) - unidade),
                                      np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22), 22, 22)

            if contador == 30:
                grupo_balas.add(jogo.jogador.atira([inimigo]))
                contador = 0

            contador += 1
            pygame.display.update()
            screen.fill((255, 255, 255))
            screen.blit(bg, (0, 0))
            grupo_balas.update()
            grupo_balas.draw(jogo.tela)
            jogo.draw_elementos()
            pygame.draw.rect(pygame.display.get_surface(), (250, 0, 0), inimigo)
            digitar_texto(f'{jogo.jogador.ponto}', (0, 0, 230), 28, (728, 10))
            pygame.display.flip()
            clock.tick(30)

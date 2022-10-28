import pygame, sys
from pygame.math import Vector2
from jogador import Jogador
from vida import Vida
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
        self.next_move = pygame.time.get_ticks() + 100
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto)

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)
        self.item_vida.spawn_vida(self.jogador.coleta_vida)
        self.item_vel.spawn_velocidade(self.jogador.coleta_vel)
        self.item_ponto.spawn_ponto(self.jogador.coleta_ponto)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto)

    def draw_elementos(self):
        self.sprites.draw(self.tela)


if __name__ == '__main__':
    unidade = 20
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 22.5

    clock = pygame.time.Clock()
    clock.tick(30)

    bg = pygame.image.load("sprites/background.png")
    bg = pygame.transform.scale(bg, (unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))

    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 28, True, False)

    inimigo_pos = Vector2(np.random.randint(0, (unidade * SCREEN_WIDTH) - 22),
                          np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22))
    inimigo = pygame.Rect(inimigo_pos.x, inimigo_pos.y, 22, 22)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('CINGAÇO')

    running = True

    pygame.init()

    jogo = Main()

    while running:
        antiga_vida = jogo.jogador.vida

        texto_vidas = f'Vidas: {jogo.jogador.vida}'
        texto_pontos = f'Pontos: {jogo.jogador.ponto}'
        contador_vidas = fonte.render(texto_vidas, False, (230, 0, 0))
        contador_pontos = fonte.render(texto_pontos, False, (0, 0, 230))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if jogo.jogador.morto:
            running = False

        tecla = pygame.key.get_pressed()
        jogo.update([inimigo], jogo.item_vel.rect, jogo.item_vida.rect, jogo.item_ponto.rect, tecla)
        jogo.jogador.vel = jogo.item_vel.vel

        if jogo.jogador.vida < antiga_vida:
            inimigo = pygame.Rect(np.random.randint(0, (unidade * SCREEN_WIDTH) - unidade),
                                  np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22), 22, 22)

        pygame.display.update()
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))
        jogo.draw_elementos()
        pygame.draw.rect(pygame.display.get_surface(), (250, 0, 0), inimigo)
        screen.blit(contador_vidas, (20, 10))
        screen.blit(contador_pontos, (610, 10))
        pygame.display.flip()
        clock.tick(30)

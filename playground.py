import pygame, sys
from pygame.math import Vector2
from jogador import Jogador
import numpy as np

# Classe que ira conter todos os objetos
class Main:
    def __init__(self):
        self.jogador = Jogador()
        self.next_move = pygame.time.get_ticks() + 100

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        if pygame.time.get_ticks() >= self.next_move: 
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)

    def draw_elementos(self):
        self.jogador.draw_jogador()

if __name__ == '__main__':
    unidade = 20
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 22.5

    clock = pygame.time.Clock()
    clock.tick(60)

    bg = pygame.image.load("background.png")

    inimigo = pygame.Rect(10, 10, 20, 20)
    item_vel = pygame.Rect(40, 10, 20, 20)
    item_vida = pygame.Rect(70, 10, 20, 20)
    item_ponto = pygame.Rect(100, 10, 20, 20)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('playground')

    running = True

    pygame.init()

    jogo = Main()


    while running:
        antiga_pontuacao = jogo.jogador.ponto
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        print(jogo.jogador.ponto, jogo.jogador.vel)

        if jogo.jogador.morto:
                running = False

        tecla = pygame.key.get_pressed()        
        jogo.update([inimigo], [item_vel], [item_vida], [item_ponto], tecla)
        
        if jogo.jogador.ponto != antiga_pontuacao:
            item_ponto = pygame.Rect(np.random.randint(0, (unidade * SCREEN_WIDTH) - unidade), np.random.randint(0, (unidade * SCREEN_HEIGHT) - 20), 20, 20)

        pygame.display.update()
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))
        jogo.draw_elementos()
        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), item_vel)
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), item_vida)
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 255), item_ponto)
        pygame.draw.rect(pygame.display.get_surface(), (0, 123, 122), inimigo)
        pygame.display.flip()
        clock.tick(30)
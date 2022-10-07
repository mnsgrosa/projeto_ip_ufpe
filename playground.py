import pygame, sys
from pygame.math import Vector2
from jogador import Jogador

class Main:
    def __init__(self):
        self.jogador = Jogador()

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)

    def draw_elementos(self):
        self.jogador.draw_jogador()

if __name__ == '__main__':
    unidade = 20
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 22.5

    clock = pygame.time.Clock()
    clock.tick(30)

    inimigo = pygame.Rect(10, 10, 20, 20)
    item_vel = pygame.Rect(40, 40, 20, 20)
    item_vida = pygame.Rect(70, 70, 20, 20)
    item_ponto = pygame.Rect(100, 100, 20, 20)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('playground')

    running = True

    pygame.init()

    jogo = Main()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                jogo.update([inimigo], [item_vel], [item_vida], [item_ponto], event.key)

        pygame.display.update()
        screen.fill((255, 255, 255))
        tecla = pygame.event
        print(jogo.jogador.pos)
        jogo.draw_elementos()
        
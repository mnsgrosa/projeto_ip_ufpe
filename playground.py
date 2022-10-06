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

    inimigo = pygame.Rect(10, 10, 20, 20)
    item_vel = pygame.Rect(40, 40, 20, 20)
    item_vida = pygame.Rect(70, 70, 20, 20)
    item_ponto = pygame.Rect(100, 100, 20, 20)

    screen = pygame.display.set_mode([unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT])
    running = True

    pygame.init()

    jogo = Main()

    pygame.display.set_caption('playground')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tecla = pygame.key.get_pressed()
        jogo.update([inimigo], [item_vel], [item_vida], [item_vel], tecla)
        jogo.draw_elementos()
        screen.fill((255, 255, 255))
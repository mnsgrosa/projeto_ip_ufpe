import pygame
from pygame.math import Vector2
from pygame.transform import scale
from random import randint
from jogador import Jogador
from vida import Vida
from vida import Barra_vida
from velocidade import Velocidade
from pontos import Pontos
from flor import Flor


# Classe que ira conter todos os objetos
class Main:
    def __init__(self):
        self.tela = pygame.display.get_surface()
        self.jogador = Jogador()
        self.item_vida = Vida()
        self.item_vel = Velocidade()
        self.item_ponto = Pontos()
        self.flor = Flor()
        self.barra_vida = Barra_vida()
        self.next_move = pygame.time.get_ticks() + 100
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto, self.flor, self.barra_vida)

    def update(self, items_vel, items_vida, items_ponto, posicoes_flor, tecla):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(items_vel, items_vida, items_ponto, posicoes_flor, tecla)
        self.item_vida.spawn_vida(self.jogador.coleta_vida)
        self.item_vel.update_cafe(self.jogador.coleta_vel)
        self.item_ponto.update_ponto(self.jogador.coleta_ponto)
        self.flor.spawn_flor(self.jogador.dano)
        self.barra_vida.update_barra(self.jogador.vida)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.item_ponto, self.flor, self.barra_vida)

    def draw_elementos(self):
        self.sprites.draw(self.tela)


def atualiza_tela():
    pygame.display.update()
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    jogo.draw_elementos()
    digitar_texto(f'{jogo.jogador.ponto}', (0, 0, 230), 28, (728, 10))

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
    logo = pygame.image.load("sprites/cingaco_logo.png")
    logo = pygame.transform.scale(logo, (500, 500))
    logo_rect = logo.get_rect(center=((unidade * SCREEN_WIDTH) / 2, 50))

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('CINGAÇO')

    game = True
    tela_start = True
    running = False

    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    som_start = pygame.mixer.Sound('sons/som_start.wav')
    som_ganha_vida = pygame.mixer.Sound('sons/som_ganha_vida.wav')
    som_perde_vida = pygame.mixer.Sound('sons/som_perde_vida.wav')
    som_game_over = pygame.mixer.Sound('sons/som_game_over.wav')

    record = 0
    contador = 30

    while game:

        musica_fundo = pygame.mixer.music.load('sons/musica_fundo_tela.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

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

            screen.fill((255, 255, 255))
            screen.blit(bg, (0, 0))
            screen.blit(logo, logo_rect)
            digitar_texto(f'RECORDE: {record}', (0, 0, 0), 33, (162, 270))
            digitar_texto('APERTE ESPAÇO PARA JOGAR', (0, 0, 0), 33, (162, 330))
            pygame.display.flip()
            clock.tick(30)

        jogo = Main()

        som_start.play()
        musica_fundo = pygame.mixer.music.load('sons/musica_fundo_game.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

        while running:

            antiga_vida = jogo.jogador.vida

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tela_start = False
                    running = False
                    game = False

            if jogo.jogador.morto:
                tela_start = True
                running = False

            tecla = pygame.key.get_pressed()
            jogo.update(jogo.item_vel.rect, jogo.item_vida.rect, jogo.item_ponto.rect, jogo.flor.rect, tecla)
            jogo.jogador.vel = jogo.item_vel.vel

            if jogo.jogador.vida < antiga_vida:
                som_perde_vida.play()
            elif jogo.jogador.vida > antiga_vida:
                som_ganha_vida.play()

            contador += 1
            atualiza_tela()
            pygame.display.flip()
            clock.tick(30)

        som_game_over.play()
        if jogo.jogador.ponto > record:
            record = jogo.jogador.ponto

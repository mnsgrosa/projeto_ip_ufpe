import pygame
from pygame.math import Vector2
from random import randint
from jogador import Jogador
from bala import Bala
from vida import Vida
from vida import Barra_vida
from velocidade import Velocidade
from pontos import Pontos
from inimigo import Inimigo


# Classe que ira conter todos os objetos
class Main:
    def __init__(self):
        self.tela = pygame.display.get_surface()
        self.jogador = Jogador()
        self.item_vida = Vida()
        self.item_vel = Velocidade()
        self.item_ponto = Pontos()
        self.barra_vida = Barra_vida()
        self.inimigos = []
        self.next_move = pygame.time.get_ticks() + 100
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.barra_vida)

    def add_inimigo(self):
        if self.inimigos.len() < 10:
            self.inimigos.append(Inimigo())

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla, morte_inimigo, pos_inimigo_morto, bala):
        self.item_ponto.update_ponto(morte_inimigo, pos_inimigo_morto, self.jogador.ponto_coletado)
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)
        self.item_vida.spawn_vida(self.jogador.coleta_vida)
        self.item_vel.update_cafe(self.jogador.coleta_vel)
        self.barra_vida.update_barra(self.jogador.vida)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel, self.barra_vida)
        if self.inimigos > 0:
            for indice, inimigo in enumerate(self.inimigos):
                inimigo.update(self.jogador, bala)
                if inimigo.morto:
                    self.inimigos.pop(indice)

    def draw_elementos(self, bala):
        self.sprites.draw(self.tela)
        for inimigo in inimigos:
            inimigo.draw(self.jogador, bala)

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
    logo_rect = logo.get_rect(center = ((unidade * SCREEN_WIDTH) / 2, 50))

    inimigo_pos = Vector2(randint(0, (unidade * SCREEN_WIDTH) - 22), randint(0, (unidade * SCREEN_HEIGHT) - 22))
    inimigo = pygame.Rect(inimigo_pos.x, inimigo_pos.y, 22, 22)
    morte_inimigo = False
    pos_inimigo_morto = (inimigo_pos.x, inimigo_pos.y)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('CINGAÇO')

    grupo_balas = pygame.sprite.Group()

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
    contador = 0

    while game:
        pygame.display.update()
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))

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

            if jogo.jogador.vida < antiga_vida:
                som_perde_vida.play()
                morte_inimigo = True
                pos_inimigo_morto = (inimigo_pos.x, inimigo_pos.y)
                inimigo_pos = Vector2(randint(0, (unidade * SCREEN_WIDTH) - 22),
                                      randint(0, (unidade * SCREEN_HEIGHT) - 22))
                inimigo = pygame.Rect(inimigo_pos.x, inimigo_pos.y, 22, 22)
            elif jogo.jogador.vida > antiga_vida:
                som_ganha_vida.play()
                morte_inimigo = False
            else:
                morte_inimigo = False

            if contador == 30:
                bala = jogo.jogador.atira(jogo.inimigos)
                grupo_balas.add(bala)
                contador = 0

            tecla = pygame.key.get_pressed()
            jogo.update([inimigo], jogo.item_vel.rect, jogo.item_vida.rect, jogo.item_ponto.lista_ponto, tecla, morte_inimigo, pos_inimigo_morto, bala)
            jogo.jogador.vel = jogo.item_vel.vel

            contador += 1
            grupo_balas.update()
            grupo_balas.draw(jogo.tela)
            jogo.draw_elementos()
            pygame.draw.rect(pygame.display.get_surface(), (250, 0, 0), inimigo)
            digitar_texto(f'{jogo.jogador.ponto}', (0, 0, 230), 28, (728, 10))
            pygame.display.flip()
            clock.tick(30)

        som_game_over.play()
        if jogo.jogador.ponto > record:
            record = jogo.jogador.ponto

import sys
import pygame

class Game():

    state = None
    STATE_QUIT = 0
    STATE_MAINGAME = 1
    STATE_RESET = 2
    STATE_GAMEOVER = 3

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        
        self.size = self.width, self.height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        self.loadEntities()
        self.run()
        
    def loadEntities(self):
        # Criando as coisas da tela:
        self.my_font1 = pygame.font.SysFont('Comic Sans MS', 16)
        self.my_font2 = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0
        self.black = 0, 0, 0
        self.white = 255, 255, 255

        # Importando imagem da "bola":
        self.ball = pygame.image.load("Semana14/koopa_shell.png")
        # Mudando a dimensão da imagem da "bola":
        self.ball = pygame.transform.scale(self.ball, (100, 100))
        # Criando o retângo "físico" ao redor da imagem:
        self.ballrect = self.ball.get_rect()
        # Criando o vetor de velocidade da bola:
        self.ball_speed = [1, 1]

        # Criando o bloco retangular para o jogo:
        self.block_size = (int(self.width/6), 40)
        self.block_rect = pygame.Rect(int(self.width/2 - self.block_size[0]/2), self.height-200, self.block_size[0], self.block_size[1])

        # Setando velocidade do bloco (lembrando que o vetor de velocidade desse é apenas sobre o eixo x, ou seja, é unidimensional):
        self.block_speed = 1

    def run(self):

        # Flags para os botões a serem utilizados:
        self.keyLeft = False
        self.keyRight = False
        self.resetKey = False
        # Flag para manter ou fechar o jogo:
        self.state = self.STATE_MAINGAME

        self.last_time = self.current_time = 0
        
        # Rodando o joga (com cada ação dependendo do estado):
        while self.state != self.STATE_QUIT:
            self.current_time = pygame.time.get_ticks()
            self.dt = self.current_time - self.last_time

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()

            if self.state == self.STATE_MAINGAME:
                self.maingame()
            elif self.state == self.STATE_GAMEOVER:
                self.gameover()
            self.last_time = self.current_time
            
    def maingame(self):
        for event in pygame.event.get(): 
            # Se uma tecla esta pressionada(keydown):
            if event.type == pygame.KEYDOWN:
                # Se esta tecla é a seta para a esquerda:
                if event.key == pygame.K_LEFT:
                    # seta para a esquerda ativada:
                    self.keyLeft = True
                # Se esta tecla é a seta para a direita:
                if event.key == pygame.K_RIGHT:
                    # seta para a direita ativada:
                    self.keyRight = True
            # Senão, se uma tecla está solta(keydown):
            elif event.type == pygame.KEYUP:
                # Se esta tecla é a seta para a esquerda:
                if event.key == pygame.K_LEFT:
                    # seta para a esquerda desativada:
                    self.keyLeft = False
                # Se esta tecla é a seta para a direita:
                if event.key == pygame.K_RIGHT:
                    # seta para a direita desativada:
                    self.keyRight = False
        print('->', self.keyLeft, self.keyRight)
        # Se a seta para esquerda está ativada e a seta para a direita não está ativada:
        if self.keyLeft and (not self.keyRight):
            self.block_rect[0] -= self.block_speed
        # Se a seta para esquerda não está ativada e a seta para a direita está ativada:
        if (not self.keyLeft) and self.keyRight:
            self.block_rect[0] += self.block_speed 
        # Atualiza a posição do objeto ballrect:
        self.ballrect = self.ballrect.move(self.ball_speed)

        # Se o objeto ballrect encostar na 'parede' da esquerda ou na parede da 'direita':
        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.ball_speed[0] = -self.ball_speed[0]
        # Se o objeto ballrect encostar no 'teto' ou no 'chão':
        if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
            self.ball_speed[1] = -self.ball_speed[1]

        # Se o objeto ballrect encostar no 'chão':
        if self.ballrect.bottom > self.block_rect.top:
            # Se o objeto ballrect colidir com o objeto block_rect:
            if self.ballrect.colliderect(self.block_rect):
                # Inverte a direção do vetor de velocidade:
                self.ball_speed[1] = -self.ball_speed[1]
                # Soma 1 no contador da multiplicação:
                self.score += 1
            else:
                # Se não encerra o jogo
                self.state = self.STATE_GAMEOVER

        # Cria uma superfície de texto:
        self.text_surface = self.my_font1.render('Score: ' + str(self.score), False, (0, 0, 200))

        # Atualizando objetos e imagens:
        self.screen.fill(self.white)
        self.screen.blit(self.ball, self.ballrect)
        self.screen.blit(self.text_surface, (750, 50))
        pygame.draw.rect(self.screen, (255,0,0), self.block_rect)
        pygame.display.flip()

    def gameover(self):
        # Atualizando a tela para a tela de gameover:
        self.text_surface = self.my_font2.render('Game-Over', False, (0, 0, 200))
        self.ball_speed = [0, 0]
        # self.block_speed = 0
        self.screen.blit(self.text_surface, (500, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.loadEntities()
                # self.block_speed = 0
                self.state = self.STATE_MAINGAME


    
if __name__ == "__main__":
    game = Game()
    game.run()
import sys
import pygame

pygame.init()
pygame.font.init()

my_font1 = pygame.font.SysFont('Comic Sans MS', 16)
my_font2 = pygame.font.SysFont('Comic Sans MS', 30)
score = 0

size = width, height = 1000, 800
ball_speed = [1, 1]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

# importando imagem da "bola":
ball = pygame.image.load("Semana14/koopa_shell.png")
# Mudando a dimensão da imagem da "bola":
ball = pygame.transform.scale(ball, (100, 100))
# Criando o retângo "físico" ao redor da imagem:
ballrect = ball.get_rect()

# Criando o bloco retangular para o jogo:
block_size = (int(width/6), 40)
block_rect = pygame.Rect(int(width/2 - block_size[0]/2), height-200, block_size[0],block_size[1])

# Setando velocidade do bloco (lembrando que o vetor de velocidade desse é apenas sobre o eixo x, ou seja, é unidimensional):
block_speed = 1

# Flags para os botões a serem utilizados:
keyLeft = False
keyRight = False

# Flag para manter ou fechar o jogo:
Run = True

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Senão, se uma tecla esta pressionada(keydown):
        elif event.type == pygame.KEYDOWN:
            # Se esta tecla é a seta para a esquerda:
            if event.key == pygame.K_LEFT:
                # seta para a esquerda ativada:
                keyLeft = True
            # Se esta tecla é a seta para a direita:
            if event.key == pygame.K_RIGHT:
                # seta para a direita ativada:
                keyRight = True
        # Senão, se uma tecla está solta(keydown):
        elif event.type == pygame.KEYUP:
            # Se esta tecla é a seta para a esquerda:
            if event.key == pygame.K_LEFT:
                # seta para a esquerda desativada:
                keyLeft = False
            # Se esta tecla é a seta para a direita:
            if event.key == pygame.K_RIGHT:
                # seta para a direita desativada:
                keyRight = False

    # Se a seta para esquerda está ativada e a seta para a direita não está ativada:
    if keyLeft and (not keyRight):
        block_rect[0] -= block_speed
    # Se a seta para esquerda não está ativada e a seta para a direita está ativada:
    if (not keyLeft) and keyRight:
        block_rect[0] += block_speed    

    # Atualiza a posição do objeto ballrect:
    ballrect = ballrect.move(ball_speed)

    # Se o objeto ballrect encostar na 'parede' da esquerda ou na parede da 'direita':
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    # Se o objeto ballrect encostar no 'teto' ou no 'chão':
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    # Se o objeto ballrect encostar no 'chão':
    if ballrect.bottom > block_rect.top:
        # Se o objeto ballrect colidir com o objeto block_rect:
        if ballrect.colliderect(block_rect):
            # Inverte a direção do vetor de velocidade:
            ball_speed[1] = -ball_speed[1]
            # Soma 1 no contador da multiplicação:
            score += 1
        else:
            # Se não encerra o jogo
            Run = False

    # Cria uma superfície de texto:
    text_surface = my_font1.render('Score: ' + str(score), False, (0, 0, 200))

    # Atualizando objetos e imagens:
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(text_surface, (750, 50))
    pygame.draw.rect(screen, (255,0,0), block_rect)
    pygame.display.flip()
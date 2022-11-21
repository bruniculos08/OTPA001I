import sys
import pygame

pygame.init()
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
block_rect.fill('grey')

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

    if keyLeft and (not keyRight):
        block_rect[0] -= block_speed
    if (not keyLeft) and keyRight:
        block_rect[0] += block_speed    

    ballrect = ballrect.move(ball_speed)
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    if ballrect.bottom > block_rect.top:
        if ballrect.colliderect(block_rect):
            ball_speed[1] = -ball_speed[1]
        else:
            Run = False

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, (255,0,0), block_rect)
    pygame.display.flip()
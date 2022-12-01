import sys
import pygame
from pygame import gfxdraw
import random

class Fire:
    STEPS_BETWEEN_COLORS = 15
    COLORS = ['black', 'red', 'orange', 'yellow', 'white']
    PIXEL_SIZE = 5

    def __init__(self, game):
        self.game = game
        self.fire_width = self.game.width // self.PIXEL_SIZE
        self.fire_height = self.game.height // self.PIXEL_SIZE

        self.palette = self.get_palette()
        self.fire_array = self.get_fire_array()

    @staticmethod
    def get_palette():
        palette = [(0,0,0)]
        for i, color in enumerate(Fire.COLORS[:-1]):
            c1, c2 = color, Fire.COLORS[i + 1]
            for step in range(Fire.STEPS_BETWEEN_COLORS):
                c = pygame.Color(c1).lerp(c2, (step + 0.5) / Fire.STEPS_BETWEEN_COLORS)
                palette.append(c)
        return palette

    def draw_palette(self):
        """For debug"""
        size = 50
        for i, color in enumerate(self.palette):
            pygame.draw.rect(self.game.screen, color, (i*size, 850, size-5, size-5))

    def get_fire_array(self):
        fire_array = [[0 for i in range(self.fire_width)] for j in range(self.fire_height)]
        for i in range(self.fire_width):
            fire_array[self.fire_height - 1][i] = len(self.palette) - 1

        return fire_array

    def update(self):
        for x in range(self.fire_width):
            for y in range(1, self.fire_height):
                color_index = self.fire_array[y][x]
                color_index = min(len(self.palette)-1, max(0, color_index - random.randint(-1,3)))
                self.fire_array[y-1][x] = color_index


    def draw(self):
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.palette[color_index]
                    gfxdraw.box(self.game.screen, (x * self.PIXEL_SIZE, y * self.PIXEL_SIZE,
                                        self.PIXEL_SIZE, self.PIXEL_SIZE),
                                        color)


class BaseMovable:
    def __init__(self, game, speed=0.2):
        self.game = game
        self.speed = speed
        self.w = self.game.width/6
        self.h = self.game.height/6
        self.x = self.game.width/2 - self.w/2
        self.y = self.game.height/2 - self.h/2

    def set_speed(self, speed):
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

class Puck(BaseMovable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reset()

    def reset(self):
        self.x = int(self.game.width/2 - self.game.width/6)
        self.y = self.game.height-200
        self.w = self.game.width/6
        self.h = 40

    def move_left(self, dt):
        self.x -= self.speed * dt
        if self.x < 0:
                self.x = 0

    def move_right(self, dt):
        self.x += self.speed * dt
        right_limit = self.game.width - self.w
        if self.x > right_limit:
            self.x = right_limit

    def draw(self):
        pygame.draw.rect(self.game.screen, (255,200,200), self.get_rect())

class Ball(BaseMovable):
    COLLIDE_NONE = 0
    COLLIDE_PUCK = 1
    COLLIDE_BOTTOM = 2

    def __init__(self, image, *args, **kwargs):
        self.image = pygame.image.load(image)
        super().__init__(*args, **kwargs)
        self.reset()

    def reset(self):
        rect = self.image.get_rect()
        self.x = int(self.game.width/2 - rect[2]/2)
        self.y = 300
        self.w = rect[2]
        self.h = rect[3]
        self.direction = [1, 1]
        self.check_middle = True  # Avoid double score

    def draw(self):
        self.game.screen.blit(self.image, self.get_rect())

    def update(self, dt):
        self.x += self.speed * self.direction[0] * dt
        self.y += self.speed * self.direction[1] * dt

        # walls collision update
        rect = self.get_rect()
        if rect.left <= 0:
            self.direction[0] = random.uniform(0.8, 1.2)
        elif rect.right >= self.game.width:
            self.direction[0] = random.uniform(-0.8, -1.2)
        if rect.top <= 0:
            self.direction[1] = 1

        if self.y < self.game.height/2:
            self.check_middle = True

        return rect

    def collide(self, puck):
        puck_rect = puck.get_rect()
        ball_rect = self.get_rect()
        if ball_rect.bottom > puck_rect.top:
            if ball_rect.colliderect(puck_rect):
                if self.check_middle:
                    self.check_middle = False
                    self.direction[1] = -1
                    self.x_dir_update(ball_rect, puck_rect)
                    return self.COLLIDE_PUCK
            else:
                return self.COLLIDE_BOTTOM
        return self.COLLIDE_NONE

    def x_dir_update(self, ball_rect, puck_rect):
        diff = (ball_rect.centerx - puck_rect.centerx)/puck_rect.w #~   # [-0.5, 0.5]
        x_dir = 2 * (diff + random.uniform(-0.1, 0.1)) * random.uniform(1.0, 1.1)
        self.direction[0] = x_dir
        print(x_dir)


class Game:
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    YELLOW = 255, 255, 0
    MAGENTA = 255, 0, 255
    CYAN = 0, 255, 255
    BLACK = 0, 0, 0

    STATE_QUIT = 0
    STATE_MAINGAME = 1
    STATE_LEVELINTERMISSION = 2
    STATE_GAMEOVER = 3

    BLOCKS = {
        1: {'color': BLUE, 'points': 10},
        2: {'color': GREEN, 'points': 25},
        3: {'color': RED, 'points': 50},
        4: {'color': YELLOW, 'points': 100},
    }

    LEVELS = [
        #~ {'ball_speed':0.10, 'puck_speed':0.60, 'targets':[[3,4], [1,2]]},
        #~ {'ball_speed':0.20, 'puck_speed':0.57, 'targets':[[4,4], [2,2]]},
        #~ {'ball_speed':0.35, 'puck_speed':0.55, 'targets':[[4,4,4,4], [4,4], [4,4]]},
        {'ball_speed':0.30, 'puck_speed':0.60, 'targets':[[2,1,2,1,2,1,2,1,1,2,1,2], [1,1,1,1,1,1,1,1,1,1,1,1]]},
        {'ball_speed':0.33, 'puck_speed':0.55, 'targets':[[2,3,2,3,2,3,2,3,2,3,2,3], [2,1,2,1,2,1,2,1,1,2,1,2], [1,1,1,1,1,1,1,1,1,1,1,1]]},
        {'ball_speed':0.35, 'puck_speed':0.50, 'targets':[[1,2,3,4,3,4,4,3,4,3,2,1], [3,2,3,2,3,2,3,2,3,2,3,2], [2,1,2,1,2,1,2,1,1,2,1,2]]},
    ]

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.size = self.width, self.height = 1200, 980
        self.screen = pygame.display.set_mode(self.size)

        self.load_entities()
        self.reset()

    def load_entities(self):
        #~ self.ball = pygame.image.load("res/small_ball2.png")
        self.font_score = pygame.font.SysFont('Comic Sans MS', 16)
        self.font_gameover = pygame.font.SysFont('Comic Sans MS', 30)
        self.hit_sound = pygame.mixer.Sound("res/sound_hit.wav")
        self.coin_sound = pygame.mixer.Sound("res/sound_coin.wav")

        self.background_fire = Fire(self)
        self.ball = Ball('res/small_ball2.png', self)
        self.puck = Puck(self)

    def reset(self, level=0, nextlevel=False):
        self.state = self.STATE_MAINGAME
        self.last_time = self.current_time = pygame.time.get_ticks()
        self.dt = 0

        if level >= len(self.LEVELS):
            level = len(self.LEVELS) - 1
        self.level = level
        level = self.LEVELS[self.level]

        self.puck.reset()
        self.ball.reset()
        self.puck.set_speed(level['puck_speed'])
        self.ball.set_speed(level['ball_speed'])

        if nextlevel == False:
            self.score = 0

        self.targets = list()
        for row_id, row in enumerate(level['targets']):
            w = self.width/len(row)
            h = 40
            for col_id, col in enumerate(row):
                self.targets.append({
                    'rect': pygame.Rect(int(col_id * w) + 2, 100 + row_id * h, int(w)-4, h-4),
                    'block': self.BLOCKS[col],
                    'live': True
                })

    def maingame_update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (not keys[pygame.K_RIGHT]):
            self.puck.move_left(self.dt)
        if (not keys[pygame.K_LEFT]) and keys[pygame.K_RIGHT]:
            self.puck.move_right(self.dt)

        ball_rect = self.ball.update(self.dt)

        # puck/bottom collision update
        ball_collision = self.ball.collide(self.puck)
        if ball_collision == self.ball.COLLIDE_PUCK:
            pygame.mixer.Sound.play(self.hit_sound)
            if self.score > 0:  # every puck hit reduce 1 point
                self.score = self.score - 1
        elif ball_collision == self.ball.COLLIDE_BOTTOM:
            self.state = self.STATE_GAMEOVER

        # targets collision update
        alldead = True
        targethit = False
        for trg in self.targets:
            if trg['live']:
                alldead = False
                if ball_rect.colliderect(trg['rect']):
                    targethit = True
                    trg['live'] = False
                    self.score += trg['block']['points']
                    if ball_rect.centerx > trg['rect'].left and ball_rect.centerx < trg['rect'].right:
                        self.ball.direction[1] = -self.ball.direction[1] # swap Y
                    elif ball_rect.centery > trg['rect'].top and ball_rect.centery < trg['rect'].bottom:
                        self.ball.direction[0] = -self.ball.direction[0] # swap X
                    else:
                        self.ball.direction[1] = -self.ball.direction[1] # swap Y
                        self.ball.direction[0] = -self.ball.direction[0] # swap X

        if targethit:
            pygame.mixer.Sound.play(self.coin_sound)
        if alldead:
            self.state = self.STATE_LEVELINTERMISSION

        self.background_fire.update()


    def maingame_draw(self):
        self.screen.fill(self.BLACK)

        #~ self.background_fire.draw_palette()  # debug only
        self.background_fire.draw()

        self.ball.draw()
        self.puck.draw()

        for trg in self.targets:
            if trg['live']:
                pygame.draw.rect(self.screen, trg['block']['color'], trg['rect'])

        TEXT_HEIGHT = 30
        text_surface = self.font_score.render("Score: " + str(self.score), False, (100, 100, 225))
        self.screen.blit(text_surface, (7*self.width/8 - text_surface.get_width()/2, TEXT_HEIGHT))
        TEXT_HEIGHT += text_surface.get_height()

        text_surface = self.font_score.render("Level: " + str(self.level + 1), False, (100, 100, 225))
        self.screen.blit(text_surface, (7*self.width/8 - text_surface.get_width()/2, TEXT_HEIGHT))

        pygame.display.flip()


    def maingame(self):
        self.maingame_update()
        self.maingame_draw()

    def levelintermission(self):
        self.screen.fill(self.BLACK)

        BASE_HEIGHT = self.height/3

        text_surface = self.font_score.render("Level: " + str(self.level + 1) + " COMPLETED!", False, (0, 225, 225))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))
        BASE_HEIGHT += text_surface.get_height()

        text_surface = self.font_score.render("Score: " + str(self.score), False, (0, 0, 225))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))
        BASE_HEIGHT += text_surface.get_height()


        text_surface = self.font_score.render("Press c to continue or r to restart", False, (225, 225, 125))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))

        pygame.display.flip()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.reset(level=0)
        if keys[pygame.K_c]:
            self.reset(level=self.level+1, nextlevel=True)


    def gameover(self):
        self.screen.fill(self.BLACK)

        BASE_HEIGHT = self.height/3

        text_surface = self.font_score.render("GAME OVER", False, (255, 0, 0))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))
        BASE_HEIGHT += text_surface.get_height()

        text_surface = self.font_score.render("Final Score: " + str(self.score), False, (0, 0, 225))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))
        BASE_HEIGHT += text_surface.get_height()


        text_surface = self.font_score.render("Press r to restart", False, (0, 225, 225))
        self.screen.blit(text_surface, (self.width/2 - text_surface.get_width()/2, BASE_HEIGHT))

        pygame.display.flip()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.reset(level=0)


    def run(self):
        while self.state != self.STATE_QUIT:

            self.current_time = pygame.time.get_ticks()
            self.dt = self.current_time - self.last_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = self.STATE_QUIT

            if self.state == self.STATE_MAINGAME:
                self.maingame()
            if self.state == self.STATE_LEVELINTERMISSION:
                self.levelintermission()
            elif self.state == self.STATE_GAMEOVER:
                self.gameover()

            self.last_time = self.current_time


game = Game()
game.run()

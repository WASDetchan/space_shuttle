import pygame
import os
import random

pygame.init()
width, height = 1100, 700
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load(os.getcwd() + '\\pics\\flappybirdico.jpg')
pygame.display.set_icon(icon)
screen.fill([255, 255, 255])
pygame.display.flip()
run = True
boost = 0
y = 450
birdtexture = pygame.image.load(os.getcwd() + '\\pics\\flappybird.png')
gameovertexture = pygame.image.load(os.getcwd() + '\\pics\\GameOver.png')
#pipetexture = pygame.image.load(os.getcwd() + '\\pics\\pipes72930.png')
screen.blit(birdtexture, [300, y])
pygame.display.flip()
boostfl = -10
spawntime = 0


def isHeightNormal(birdy):
    if birdy > 670 or birdy < 0:
        return False
    else:
        return True


def isQuitPressed():
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return True


def IsSpacePressed():
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            return False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                return True
        else:
            return 'NoEvent'


def IsBirdTouchingPipe(pipey, birdy, pipex):
    print(pipey)
    if 270 < pipex < 330:
        if pipey - 390 < birdy or pipey - 540 > birdy:
            return True
        else:
            return False
    else:
        return False


def startscreen():
    screen.fill([255, 255, 255])
    birdy = 450
    screen.blit(birdtexture, [300, birdy])
    for pipea in pipes:
        pipes.remove(pipea)
        pygame.sprite.Sprite.kill(pipea)
    pygame.display.flip()
    while True:
        if IsSpacePressed() == True:
            return True
        if IsSpacePressed() == False:
            return False


def gameover():
    gameend = True
    screen.blit(gameovertexture, [464, 290])
    pygame.display.flip()
    got = 0
    while gameend:
        pygame.time.delay(10)
        if got == 2000:
            return True
        else:
            got += 10
        pygame.time.delay(10)
        if isQuitPressed():
            pygame.quit()
            return False


def pipespawn():
    pipe = PipeClass(os.getcwd() + '\\pics\\pipes72930.png', random.randint(-230, 0))
    pipes.add(pipe)


class PipeClass(pygame.sprite.Sprite):
    def __init__(self, pipe_file, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pipe_file)
        self.rect = self.image.get_rect()
        self.rect.left = 1200
        self.rect.top = y

    def move(self):
        self.rect = self.rect.move(-2, 0)

    def IsOutOfScreen(self):
        if self.rect.left < -50:
            return True
        else:
            return False


pipes = pygame.sprite.Group()
pipespawn()
if not startscreen():
    run = False
    pygame.quit()
while run:  # основной цикл
    spawntime += 10
    screen.fill([255, 255, 255])
    pygame.time.delay(10)
    boostfl += 0.2
    boost = int(boostfl)
    y += boost
    if spawntime == 3000:
        pipespawn()
        spawntime = 0
    screen.blit(birdtexture, [300, y])

    pygame.display.flip()
    for pipe in pipes:
        pipe.move()
        screen.blit(pipe.image, pipe.rect)
        pygame.display.flip()
        print('aksfj')
        if pipe.IsOutOfScreen():
            pipes.remove(pipe)
            pygame.sprite.Sprite.kill(pipe)
        if IsBirdTouchingPipe(pipe.rect.top, y, pipe.rect.left):
            gameover()
            startscreen()
            run = False
    if not run:
        break
    if not isHeightNormal(y):
        boostfl = -10
        y = 450
        if not gameover():
            run = False
            pygame.quit()
            break
        a = startscreen()
        if not a:
            run = False
            pygame.quit()
            break
